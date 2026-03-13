# Vercel: Preventing GitHub Checks on Preview Deployments

**Date:** 2026-02-18
**Status:** Research only
**Context:** We have 11 Vercel projects using the "Ignored Build Step" command (`if [ "$VERCEL_ENV" = "preview" ]; then exit 0; fi; exit 1`) which skips the build but still shows a "Failed" deployment status in GitHub. We want to eliminate that status entirely.

---

## Summary

There is **no single, clean, officially supported way** to keep Vercel's GitHub integration connected AND completely suppress GitHub checks on non-production branches while maintaining automatic production deployments on main. This is a widely-reported limitation. The approaches below are ranked from simplest to most reliable.

### Recommendation

**Approach 2 (`git.deploymentEnabled`) is the best first attempt** -- it is documented, per-branch, and *should* prevent the check from being created at all. However, there is a known bug (open since Feb 2024) where this setting is sometimes ignored. If it doesn't work reliably, **Approach 5 (GitHub Actions + CLI)** is the nuclear option that definitively solves the problem.

---

## Approach 1: Vercel Dashboard -- Disable Preview Branch Tracking

**Where:** Project Settings > Environments > Preview > Branch Tracking

**What it does:** Disabling branch tracking in the Preview environment tells Vercel not to automatically create preview deployments when commits are pushed to non-production branches.

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **Unclear.** Community reports are mixed. Some users report it helps when combined with other settings, but it's not confirmed to fully suppress the check on its own. |
| Production deploys still work? | Yes, production branch tracking is a separate setting. |
| Configuration method | Dashboard only. Per-project. |

**Verdict:** Partial solution at best. Worth toggling off, but unlikely to solve the problem alone.

---

## Approach 2: `vercel.json` -- `git.deploymentEnabled` (per-branch)

**Where:** `vercel.json` in the repository root

**What it does:** Tells Vercel not to create a deployment for matching branches. Unlike "Ignored Build Step" (which creates a deployment then cancels it), this is supposed to prevent the deployment from being created at all, which means no GitHub check should be posted.

**Configuration:**

```json
{
  "git": {
    "deploymentEnabled": {
      "main": true,
      "**": false
    }
  }
}
```

Or to disable all non-main branches using a wildcard approach -- note that Vercel does NOT support a whitelist-only model. You must explicitly disable branches. The `**` glob is a catch-all. If a branch matches multiple rules and at least one is `true`, a deployment will occur. So `main` matching both `"main": true` and `"**": false` should still deploy because one rule is `true`.

Alternative (disable everything, deploy main via CLI/hooks):
```json
{
  "git": {
    "deploymentEnabled": false
  }
}
```

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **In theory, yes.** The deployment is never created, so no check should be posted. Vercel's docs say "Vercel for GitHub will not deploy the given project regardless of the GitHub app being installed." |
| Production deploys still work? | Yes, if you set `"main": true` explicitly. Unspecified branches default to `true`, so be careful to explicitly disable others. |
| Configuration method | `vercel.json` file in the repo. Must be present in EVERY branch (the config is read from the branch being pushed, not from main). |

**Known issues:**
- **Bug report (open since Feb 2024, still unresolved Aug 2025):** [vercel/vercel#11176](https://github.com/vercel/vercel/issues/11176) -- multiple users report `deploymentEnabled` being ignored intermittently. A commenter in Aug 2025 notes the `vercel.json` must exist in the specific branch being deployed (not just in main).
- **Branch tracking dependency:** When branch tracking is disabled in the project settings, Vercel may ignore the `vercel.json` setting and deploy anyway. Branch tracking must be ENABLED for this setting to work.

**Verdict:** Best documented approach. Should work if the bug doesn't bite. The "must be in every branch" requirement is annoying but manageable if `vercel.json` exists in your default branch and gets inherited by feature branches.

---

## Approach 3: `vercel.json` -- Legacy `github.silent` and `github.enabled`

**Where:** `vercel.json` in the repository root

### `github.silent: true`
```json
{
  "github": {
    "silent": true
  }
}
```

**What it does:** Prevents Vercel from posting comments on PRs and commits. **DEPRECATED** in favor of dashboard settings (Project Settings > Git > Comment controls).

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **No.** This only suppresses PR comments, not the deployment check/status itself. |
| Production deploys still work? | Yes, but all comments are silenced (production too). |

### `github.enabled: false`
```json
{
  "github": {
    "enabled": false
  }
}
```

**What it does:** Prevents Vercel from deploying the project via the GitHub integration entirely. **DEPRECATED** in favor of `git.deploymentEnabled`.

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **Yes, but for ALL branches including production.** |
| Production deploys still work? | **No.** This disables the integration entirely. You'd need to deploy via CLI or API. |

**Verdict:** `github.silent` doesn't solve the problem (comments != checks). `github.enabled: false` is too aggressive -- it kills production too. Both are deprecated. Use `git.deploymentEnabled` instead.

---

## Approach 4: Vercel API / Webhook Configuration

### Vercel REST API -- `commandForIgnoringBuildStep`

This is what we currently use (via the dashboard). The API equivalent:
```bash
curl -X PATCH "https://api.vercel.com/v9/projects/<PROJECT_ID>" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"commandForIgnoringBuildStep": "if [ \"$VERCEL_ENV\" = \"preview\" ]; then exit 0; fi; exit 1"}'
```

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **No.** This is exactly our current setup. The deployment is created, then cancelled -- but the GitHub check is still posted with a "Failed" status. |

### Vercel REST API -- Project-level `git.deploymentEnabled`

There is a community feature request ([vercel/community#1410](https://github.com/vercel/community/discussions/1410)) to configure `deploymentEnabled` via the API/GUI rather than only through `vercel.json`. This does NOT appear to be supported via the REST API as of Feb 2026.

### Disabling `deployment_status` webhook events

**Where:** Project Settings (announced in [Vercel changelog](https://vercel.com/changelog/optionally-disable-deployment_status-webhook-events-for-github-actions))

**What it does:** Stops Vercel from sending `deployment_status` webhook events to GitHub. This reduces noise in PR activity logs.

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **No.** This only stops `deployment_status` events (which affect GitHub Actions workflows). The Vercel PR comment and the deployment check itself still appear. |
| Production deploys still work? | Yes. |

### GitHub Webhook Filtering (Branch-level)

The Vercel GitHub App installs a webhook on your repo that fires on push/PR events. GitHub webhooks do NOT support branch-level filtering natively -- the webhook fires for ALL branches and Vercel decides what to do. You cannot configure the webhook to only fire for `main`.

**Verdict:** No API-level solution exists that solves this problem. The `commandForIgnoringBuildStep` is our current approach and it's exactly what causes the "Failed" status.

---

## Approach 5: Disconnect Git Integration + Deploy via GitHub Actions / CLI

**Where:** Vercel Dashboard (disconnect) + GitHub Actions workflow + Vercel CLI

**What it does:** Completely removes Vercel's GitHub App integration from the project. Vercel has no presence on the repo whatsoever -- no webhooks, no checks, no comments. You then deploy production manually using the Vercel CLI from a GitHub Action that triggers only on `main`.

### Setup:

1. **Disconnect Git** in Vercel Dashboard: Project Settings > Git > Connected Git Repository > Disconnect. Or via CLI: `vercel git disconnect`

2. **Create GitHub Action** for production deployment:

```yaml
# .github/workflows/vercel-production.yml
name: Vercel Production Deployment
env:
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Vercel CLI
        run: npm install --global vercel@latest
      - name: Pull Vercel Environment Information
        run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}
      - name: Build Project Artifacts
        run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}
      - name: Deploy Project Artifacts to Vercel
        run: vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }}
```

3. **Secrets needed:** `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` (per project)

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | **Yes, 100%.** Vercel has no GitHub integration. There is no webhook, no app, no check. Nothing appears on non-production branches. |
| Production deploys still work? | **Yes**, but only via the GitHub Action (not automatic from Vercel). |
| Configuration method | Dashboard disconnect + GitHub Actions workflow file per project. |

**Trade-offs:**
- You lose Vercel's automatic production deployment (replaced by GitHub Actions)
- You need to manage secrets across 11 projects (or use a matrix workflow)
- You lose PR preview deployments entirely (which is what we want)
- You need to maintain the GitHub Actions workflow
- Deploy hooks still work as an alternative to GitHub Actions

**Optimization for 11 projects:** Use a single reusable workflow or a matrix strategy:

```yaml
strategy:
  matrix:
    include:
      - project: space-zero-item-generator
        project_id: ${{ secrets.VERCEL_PROJECT_ID_ITEM_GEN }}
      - project: memepet-agent
        project_id: ${{ secrets.VERCEL_PROJECT_ID_MEMEPET }}
      # ... etc
```

**Verdict:** The only approach that **guarantees** no GitHub check appears. Requires more setup but is rock-solid. Recommended by Vercel maintainer @leerob in [vercel/vercel#5878](https://github.com/vercel/vercel/discussions/5878).

---

## Approach 6: Deploy Hooks (Lighter Alternative to GitHub Actions)

**Where:** Vercel Dashboard: Project Settings > Git > Deploy Hooks

**What it does:** Create a webhook URL for the `main` branch. Combine with `git.deploymentEnabled: false` to disable ALL automatic deployments, then trigger production deploys via the hook.

```bash
# Trigger production deploy via hook
curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_XXXX/YYYY
```

You can trigger this from a minimal GitHub Action or even a simple post-merge webhook.

| Question | Answer |
|----------|--------|
| Completely suppresses GitHub check? | Depends on whether `git.deploymentEnabled: false` fully suppresses it (see Approach 2 caveats). If you fully disconnect Git, then yes. |
| Production deploys still work? | Yes, via the hook URL. |

**Verdict:** Lighter than full GitHub Actions approach. But deploy hooks are tied to Vercel's git integration, so if you disconnect Git, hooks may not work. Needs testing.

---

## Decision Matrix

| Approach | Suppresses Check? | Production Works? | Effort | Reliability |
|----------|-------------------|-------------------|--------|-------------|
| 1. Dashboard branch tracking off | Maybe | Yes | Low | Low |
| 2. `git.deploymentEnabled` per-branch | Should, but has bugs | Yes | Low | Medium |
| 3. `github.silent` / `github.enabled` | No / Yes but kills prod | No (for enabled:false) | Low | N/A (deprecated) |
| 4. API / webhook settings | No | Yes | Low | N/A |
| **5. Disconnect + GitHub Actions** | **Yes, guaranteed** | **Yes** | **Medium-High** | **High** |
| 6. Deploy hooks + disable auto | Depends | Yes | Medium | Medium |

---

## Recommended Plan

1. **Try Approach 2 first** -- add `vercel.json` with `git.deploymentEnabled` to disable all non-main branches. This is the lowest-effort option. Test on one project first.
2. **If Approach 2 fails** (or is unreliable due to the known bug), go with **Approach 5** -- disconnect Git and deploy via GitHub Actions. This is the definitive solution.
3. For the **main SpaceZero app (0.space)** which keeps preview deployments ON, no changes needed.

---

## Sources

- [Vercel Git Configuration docs](https://vercel.com/docs/project-configuration/git-configuration)
- [Vercel Git Settings docs](https://vercel.com/docs/project-configuration/git-settings)
- [How can I stop Vercel preview deployments from appearing on PRs?](https://github.com/vercel/vercel/discussions/6434)
- [How to disable Preview Deployments](https://github.com/vercel/vercel/discussions/5878) (includes @leerob recommendation)
- [GitHub status check fails if ignore build step is used](https://github.com/vercel/vercel/discussions/8739)
- [deploymentEnabled option in vercel.json is ignored (bug)](https://github.com/vercel/vercel/issues/11176)
- [Vercel custom environments: Disabling preview checks on GitHub](https://community.vercel.com/t/vercel-custom-environments-disabling-preview-checks-on-github/5068)
- [Is there no way to block all automatic deployments from GitHub?](https://community.vercel.com/t/is-there-no-way-to-block-all-automatic-deployments-from-github/6349)
- [Optionally disable deployment_status webhook events](https://vercel.com/changelog/optionally-disable-deployment_status-webhook-events-for-github-actions)
- [How can I use GitHub Actions with Vercel?](https://vercel.com/kb/guide/how-can-i-use-github-actions-with-vercel)
- [Using Vercel without preview deployments](https://www.codejam.info/2021/09/vercel-without-preview-deployments.html)
