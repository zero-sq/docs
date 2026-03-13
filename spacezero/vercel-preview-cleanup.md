# Vercel Preview Deployment Cleanup

**Date:** 2026-02-17
**Status:** Done
**Completed:** 2026-02-17

## Goal

Disable preview deployments on all Vercel projects except the main SpaceZero app (0.space) to reduce billing costs. Preview deployments spin up on every PR and branch push — there's no reason to pay for previews on internal tools and services that no one reviews visually.

## Method

Using the Vercel project settings, set the **Ignored Build Step** command on each project:

```
if [ "$VERCEL_ENV" = "preview" ]; then exit 0; fi; exit 1
```

This skips preview builds while keeping production deployments intact.

> **Bug fix (2026-02-18):** The original command was missing `exit 1` at the end. Without it, the shell exits with code 0 for production builds too, causing Vercel to skip ALL builds (not just previews). The trailing `exit 1` tells Vercel to proceed with the build for any non-preview environment.

## Projects

| Project | Production URL | Preview | Reason |
|---------|---------------|---------|--------|
| **space-zero** | https://0.space | **Keep ON** | Main product, previews are useful for review |
| space-zero-item-generator | https://space-zero-item-generator.0.space | **Turn off** | Internal tool |
| memepet-agent | https://memepet.0.space | **Turn off** | Agent service |
| space-zero-growth-api | https://space-zero-growth-api.0.space | **Turn off** | API, no visual preview needed |
| space-zero-growth-dashboard | https://space-zero-growth-dashboard.0.space | **Turn off** | Internal dashboard |
| space-zero-sound-generator | https://space-zero-sound-generator.0.space | **Turn off** | Internal tool |
| sz | -- | **Turn off** | No production URL, likely inactive |
| space-zero-item-generator-pet-animation | -- | **Turn off** | No production URL, likely inactive |
| space-zero-texture-generator | https://space-zero-texture-generator.0.space | **Turn off** | Internal tool |
| space-zero-admin | https://space-zero-admin.0.space | **Turn off** | Admin panel |
| space-zero-model-to-media | https://space-zero-model-to-media.0.space | **Turn off** | Internal tool |
| space-zero-glb-compressor | https://space-zero-glb-compressor.0.space | **Turn off** | Internal tool |

## Known limitation: GitHub still shows "Failed" checks

The Ignored Build Step approach saves billing (no build minutes consumed), but GitHub still shows a "Failed" deployment status on every PR/branch push. This is cosmetic — Vercel creates a deployment record, immediately cancels it, and GitHub interprets that as failure.

### Options to fully suppress GitHub checks

**Option A — `vercel.json` (low effort, unreliable)**

Add to each repo's `vercel.json`:
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
Vercel should skip creating the deployment entirely, so no GitHub check appears. However, there's an [open bug](https://github.com/vercel/vercel/issues/11176) (since Feb 2024, unresolved) where this setting gets ignored intermittently. The file must exist in every branch, not just main. No CLI or dashboard equivalent — code change only.

**Option B — Disconnect Git + GitHub Action (guaranteed)**

Disconnect the Vercel-GitHub integration on the 11 projects, then deploy production via a GitHub Action:
```yaml
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install --global vercel@latest
      - run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}
      - run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}
      - run: vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }}
```
No integration = zero GitHub checks. Trade-off: manage `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` secrets across 11 repos.

### Current decision

Staying with Ignored Build Step for now. The "Failed" check is cosmetic noise, billing is saved, and production deploys work. Revisit Option A on one repo if the noise becomes a problem.

## Rollback

To re-enable previews on any project, remove the Ignored Build Step command in that project's Vercel settings (Settings > Git > Ignored Build Step). Or via API:

```bash
curl -X PATCH "https://api.vercel.com/v9/projects/<PROJECT_ID>" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"commandForIgnoringBuildStep": null}'
```
