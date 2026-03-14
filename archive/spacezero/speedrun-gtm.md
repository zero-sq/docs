# Speedrun GTM Synthesis — The Final Play

> Distilled from 20 research streams. March 12, 2026.
> Application deadline: March 25, 2026. Budget: $1–2K.
> Target metrics model: see `research/target-metrics-and-scenarios.md`

---

## Strategic Assessment

### Verdict

The plan is built on a strong thesis: browser-first architecture gives Spacezero a 10-20x funnel advantage over mobile/downloadable games. Even with lower raw retention percentages, absolute retained users are dramatically higher because the top of funnel is so much wider. This is the single most important framing for the Speedrun application and it's well-supported by the research.

### Three things to obsess over

1. **Ship auto-save + shareable URLs before anything else.** Without build persistence, D1 retention is effectively 0% for a builder game. Closing the tab = losing the build = never returning. No amount of marketing fixes this. This one feature is worth more than every channel combined.

2. **Nail the Show HN post.** This is the one high-leverage shot — free, massive reach (10K-30K visitors), and browser-native means near-100% click-to-play. But it's binary: 65+ Show HN posts per week, median 2 points, most fail. The game needs to be stable and impressive the moment someone clicks the link. First 30 seconds of gameplay must be polished.

3. **Launch the build competition with 5-10 seed entries from the team.** The competition solves acquisition, retention, content, and community simultaneously. It gives HN visitors a CTA, generates Reddit content organically, creates retention through builder investment, and produces creator content without paying for it. The season format ("Season 1 launched 7 days ago, here's what's happening") is a strong Speedrun narrative.

### Risks

- **Execution bandwidth.** This plan requires shipping retention features + launching HN + launching a competition + sending 300+ outreach emails + daily TikTok + Discord setup — all in 14 days with a 4-person team. The plan reads well but the bottleneck is engineering hours.

- **Show HN is binary.** If it doesn't hit front page, the highest-leverage channel produces nothing. The fallback channels (Reddit organic, creator outreach) take longer to generate numbers.

- **Retention targets assume unbuilt features.** D7 >8-10% requires auto-save, social loops, and progression. If even one isn't ready, you're looking at 2-5% D7 — below target.

### What's strong

- **Browser advantage math** — the funnel comparison table is the most compelling artifact in the whole document
- **Build competition design** — strategically clever, solves multiple problems at once, season format creates an "active growth engine" narrative for the application
- **Traction claim correction** — walking in informed about what Speedrun actually values (Josh Lu: "traction is #1, #2, #3") vs. the wrong framing ("zero traction is fine") is the difference between a strong and weak application
- **Nilo as portfolio comp** — browser-based AI-native 3D sandbox, $4M Supercell seed, already in Speedrun's portfolio. a16z is actively investing in this exact space
- **Pokopia wedge** — 2.2M frustrated buyers right now, timely and specific

---

## Summary

### The core finding

Every breakout indie game we studied (Vampire Survivors, Among Us, Lethal Company, Agar.io, etc. — $800M+ combined revenue) spent **$0 on marketing**. They all ran the same loop:

> Shareable moment → creator records it → viewer wants their own moment → plays → becomes a creator → loop repeats

- **Spacezero's browser-first architecture is the strongest structure for this loop.** Every share is a direct link to playing — no download, no app store, no friction.
- Browser games skip the entire download funnel where **90% of users drop off** (iLogos). Zero friction = click a link, you're playing in 2 seconds. *(Note: the "37% conversion" figure cited in earlier research likely comes from app store word game data, not browser-specific measurement. The real advantage is funnel elimination, not a specific conversion rate.)*
- The "impossible in Minecraft" visual hook (spheres, curves, smooth terrain) is inherently shareable — show it, and the Minecraft audience loses their minds

### Demand already exists

| Signal | Scale | What it proves |
|---|---|---|
| NoCubes mod (smooth terrain in Minecraft) | 900K+ CurseForge downloads | Hundreds of thousands of Minecraft players want exactly this |
| "Minecraft, But The World is Round!" on YouTube | 11.8M views, 281K likes | The round voxel concept is a proven mass-audience hook |
| Hytale early access (Jan 2026) | 420K peak Twitch viewers | "Minecraft alternative" conversation is at peak attention |
| Pokopia co-op backlash (March 2026) | 2.2M units sold, 98% mechanics disabled in co-op | Millions of frustrated sandbox buyers looking for multiplayer that works |

### The browser advantage math

Even with lower raw retention percentages, browser games produce **10-20x more retained users** than mobile because the top-of-funnel is so much wider:

| Metric | Mobile Game | Browser Game (Spacezero) |
|--------|-------------|-------------------------|
| Reach (impressions) | 100,000 | 100,000 |
| Conversion to player | 3-5% (download + install) | 60-80% (click URL → playing) |
| Players | 3,000-5,000 | 60,000-80,000 |
| D1 retention | 30% | 15-20% (lower due to casual intent) |
| D1 users | 900-1,500 | 9,000-16,000 |
| D7 retention | 9% | 8-10% (with persistence + social) |
| D7 users | 270-450 | 4,800-8,000 |

This is the single most important framing for Speedrun: **raw retention % is the wrong comparison. Absolute retained users is what matters.** Browser-native architecture doesn't just eliminate friction — it multiplies the entire funnel by 10-20x.

### What Speedrun wants to see

- **Not eyeballs — players who come back.** Active users with retention data beats social views every time.
- Minimum viable spark for the application (consensus across Claude/ChatGPT/Gemini research):
  - 2K-3K+ plays (Speedrun minimum); 5K+ is base target
  - D7 retention >8-10% (even small-sample)
  - Week-over-week growth: show baseline DAU (days 2-7 avg vs days 8-14 avg) trending up
  - Growing Discord community (100+ members)
- **Traction is explicitly Speedrun's #1 factor.** Josh Lu: "Traction is number one, two, and three." Pre-traction acceptance is rare and requires an elite team (e.g., Sitch: Stanford MBA + Snapchat Sr. Dir. Engineering). Accepted companies with data had strong metrics — Flamme AI (45% D30 retention), Boinkers.io (11.5M monthly players). Real user data with retention is strongly expected, not a bonus.
- **a16z thesis fit:** Dual-contouring engine + Zerocap maps directly to a16z Big Ideas 2026 (complex infrastructure, unstructured multimodal data, AI-native design, novel distribution)
- **Portfolio comp:** Nilo (browser-based AI-native 3D sandbox) is already in Speedrun's portfolio — $4M seed from Supercell. They're actively investing in this space.

### Strategy ranked by expected impact

| Rank | Channel | Timing | Why it's here |
|---|---|---|---|
| **#1** | **Show HN** | Tue/Wed, 8-11AM UTC | Front page = 4K-30K visitors in 24 hours (base: 4K-9K per ChatGPT/Gemini; our estimate: 10K-30K). Zero-friction browser = majority play instantly. D7 retention data ready by application day. **Warning: 65+ Show HN posts/week, median 2 points — most fail. Front page is the exception.** |
| **#2** | **Build competition** | Season 1: March 18 - April 14 | 2 seasons × 1 month × $1K/season. Tagline: "Build what Minecraft can't." Open categories (Best Creation, Architecture, Landscape, People's Choice). 94% of entrants self-promote, each recruiting avg 2.68 friends. Every entry = shareable browser link. Season format creates compound growth — S1 builders return for S2. |
| **#3** | **Reddit organic** | Day 3-7 | r/WebGames, r/IndieGaming, r/playmygame (NOT r/Minecraft — they remove non-MC posts). One post changed everything for Laysara (74K upvotes, 11K wishlists). Competition entries become Reddit posts. |
| **#4** | **Creator outreach** | Day 4-10 | 300-600 emails to nano Minecraft creators (1K-50K followers). The pitch: "Enter our build competition." Funnel: 600 contacts → 60 replies → 15 content pieces. Competition gives a specific CTA. |
| **#5** | **TikTok/Shorts** | Day 1-14 (background) | Weeks 1-2 get 200-1K views — this is account warmup. Competition timelapse builds = content that writes itself. Compounds post-application. |
| **#6** | **Reddit paid ads** | Day 7-14 (if needed) | Cheapest channel: $0.10-$0.50 CPC vs $0.80-$3.50 on Facebook. $500 = 370-1,850 plays. Only if organic needs help. |

### Key tactical notes

- **Show HN title:** Don't put "AI" in it — causes 15% score drop from HN fatigue. Lead with engineering.
- **Build competition:** 2 seasons × 1 month each. Season 1 launches same day as Show HN. "Build what Minecraft can't" is the marketing tagline — but competition categories are open (Best Creation, Best Architecture, Best Landscape, People's Choice) to avoid 50 novelty sphere entries. Let builders showcase Spacezero's advantages naturally (smooth curves, small voxels, organic shapes).
- **Competition prizes:** $1,000/season ($2,000 total). Per season: Grand Prize $500, 3 category winners $100 each, People's Choice $100, 4 honorable mentions $50 each = 9 winners. "$1,000 Build Competition" is the shareable headline. Plus "Founding Builder" badge for all entrants ($0).
- **Reddit posts:** Never say "Minecraft killer." Let commenters make the comparison — that's free marketing. Competition entries become organic Reddit posts from builders seeking votes.
- **TikTok:** 85% watch without sound — captions are mandatory. Dev face on camera. **TikTok organic is declining sharply in 2025-2026 — budget $200 to boost your best video.**
- **Pokopia wedge:** "Stop wasting time on broken Switch co-op — play a sandbox where everyone can build. In your browser. Right now."
- **Signup capture:** Add a lightweight in-flow CTA during HN spike — real postmortem shows 6.4% capture rate.
- **Day 8 feature update:** Ship a visible new feature mid-sprint to create a second acquisition wave and mechanically lift D7/D14 retention before application.
- **Creator enablement kit:** Send pre-cut vertical clips + challenge prompts ("build a perfect sphere in 60 seconds") to increase publish rate from the 2% baseline.
- **Follow-up emails in week 2:** 42% of cold email replies come from follow-ups — critical for unlocking late-arriving creator videos.
- **Competition viral loop:** Builder enters → builds impossible thing → shares link → viewer clicks into game → tries building → enters or keeps playing. K-factor estimated 0.3-0.7. Even 20 entries → 50+ new players minimum.

### The three must-have retention features

D7 >8-10% requires deliberate retention engineering. Without persistence, a browser sandbox game lands at 2-5% D7. With all three of these, 8-10%+ is achievable:

1. **Build persistence + shareable URLs** (CRITICAL — ship before launch)
   - Auto-save to `localStorage` as MVP (2-4 hours). Every build gets a unique URL: `spacezero.com/w/abc123`
   - Without this, D1 ≈ 0% for a builder game. Closing the tab = losing the build = never returning.
   - The URL IS the viral loop — sharing a build shares the game itself. Agar.io hit 5M DAU with zero marketing via pure URL sharing.

2. **Social loop** (HIGH IMPACT — ship in first week)
   - "Someone visited your world" notification. Visitor counter on builds. Build gallery where players browse and react to each other's creations.
   - Multiplayer games retain 2-4x better than single-player (Mistplay). Even async social (visiting others' builds, leaving reactions) significantly moves retention.
   - This is the D7 engine. Pure solo creative play decays rapidly after novelty wears off.

3. **"Just enough" progression** (MEDIUM-HIGH IMPACT — ship in first week)
   - Unlock new creative capabilities as the player builds more: 50 blocks → unlock spheres, 200 blocks → unlock smooth curves.
   - NOT daily login rewards or grinding. Creative sandbox progression = expanding the palette of what you can build.
   - Achievement system: "First sphere," "100-block structure," "Build visited 10 times." Gives direction without constraining.

**The 2-3 day retention sprint build order:** Day 1: auto-save + shareable URLs + analytics. Day 2: email capture + build gallery + visitor counter. Day 3: progression unlocks + web push notifications + polish. This ensures every retention-critical feature ships before nice-to-haves.

### Budget (if needed)

| Bucket | Amount |
|---|---|
| Build competition prizes (2 seasons × $1K) | $2,000 |
| Reddit ads (two creatives, iterative) | $300-600 |
| Micro-creator stipends (6-10 at $50-100 each) | $300-500 |
| Contingency (boost best-performing content) | $0-350 |

### The bottom line

You don't need $2K to find a spark. You need 5 good clips and one good Tuesday.

---

## The Single Biggest Insight

Across $800M+ in combined indie game revenue (Vampire Survivors, Among Us, Lethal Company, R.E.P.O., Schedule I, Content Warning, Agar.io, Slither.io), the total marketing spend was approximately **$0**. The universal pattern:

**Game produces shareable moments → creators record them → viewers want their own moments → they play → they become creators → loop repeats.**

Spacezero's browser-first architecture is the strongest possible structural advantage for this loop. Every share is a direct link to playing. No download, no app store, no friction. Browser games skip the entire install funnel where **90% of ad viewers never complete the download** (iLogos 2026). Click a link, you're playing in 2 seconds.

The "impossible in Minecraft" visual hook (spheres, curves, smooth terrain) is an inherently shareable moment. You don't need to explain it — you show it, and the Minecraft audience loses their minds.

---

## What Speedrun Actually Wants (research-backed)

From Speedrun partner Josh Lu: traction is "#1, #2, AND #3."

**Traction hierarchy (strongest to weakest):**
1. Revenue
2. Active users with retention (D1, D7 data)
3. Signups / waitlist
4. Press coverage
5. Social media views

Revenue isn't required at pre-seed. But **active users with retention data beats social views every time.** This changes the strategy: the goal isn't just eyeballs — it's getting people to **play the game and come back**.

**Minimum viable spark for the application:**
- 10K+ organic plays
- D7 retention data (even if it's small-sample)
- Week-over-week growth showing velocity (5-7% WoW is "good," 10%+ is "exceptional")
- A growing Discord community
- Social media views as a supplementary signal

**Critical comp:** Nilo is in Speedrun's portfolio — a browser-based AI-native 3D sandbox tool. $4M seed from Supercell. They're looking at this space. Spacezero hits the same thesis but as a game.

**a16z thesis alignment (from Gemini):** The dual-contouring engine + Zerocap maps directly to a16z's published Big Ideas 2026 — they're explicitly seeking startups tackling complex infrastructure, unstructured multimodal data (photo → voxel asset), AI-native design systems, and novel distribution models. This is literally their thesis.

**Competitive timing (from Gemini):** <0.5% acceptance rate (60-70 companies from 14,000+ applicants for SR006). Strong traction chart is a meaningful differentiator even though they say metrics are "encouraged but not required."

---

## The Pokopia Marketing Wedge (from Gemini — critical new finding)

Pokopia launched March 5, 2026. Sold 2.2M units in 4 days. BUT it's getting destroyed on co-op:

- **98% of mechanics are disabled** during GameShare between Switch 2 and original Switch
- Guest players can't craft, interact with Pokemon, open storage, access Pokedex, or do story progression
- Player reviews: "0/10 — avoid entirely if you want multiplayer crafting"
- r/NintendoSwitch is full of frustrated posts

**This is a massive marketing wedge nobody identified until Gemini found it.** The hook: "Stop wasting your time on broken Switch co-op — play a sandbox game where everyone can build. In your browser. Right now." Position Spacezero as the antithesis: zero hardware restrictions, zero download, instant multiplayer access.

**Also from Gemini:** Hytale entered early access Jan 13, 2026 and drew 420K Twitch viewers. The "Minecraft alternative" conversation is the most active it's been in years. You're entering at peak attention for this category.

---

## Demand Validation (from ChatGPT)

- **NoCubes mod** (smooth terrain in Minecraft) has **900K+ CurseForge downloads** — direct proof that hundreds of thousands of Minecraft players want exactly what Spacezero offers
- "Minecraft, But The World is Round!" YouTube video: **11.8M views, 281K likes** — the "round voxel world" concept is a proven mass-audience hook

---

## The Revised Strategy (ranked by research data)

### #1: Show HN — THE Big Bet (Day 3-4)

**Why this is #1 now:** Every data point supports it.

- HN front page = **10K–30K visitors in 24 hours** (real numbers 2-3x what analytics show due to JS blocking)
- Browser game = **near 100% click-to-play conversion** — no download, no signup, just click
- AI posts are oversaturated on HN right now. A genuinely impressive non-AI technical demo **stands out more than it would have a year ago**
- Voxel engines and WebGL demos have a strong track record on HN (DotBigBang hit 120fps, Athena Crisis replaced its landing page with a playable game)
- **Timing is disputed:** Our research says Sunday (2.5x vs weekday). Gemini's 1,200-post analysis says Tuesday/Wednesday 8-11AM UTC, and weekends drop to 8% of peak. **Recommendation: go Tuesday or Wednesday** — Gemini's data is more rigorous (larger sample, specific numbers).
- Comments matter more than upvotes for ranking — being responsive to technical questions keeps the post alive
- **Do NOT put "AI" in the title** — Gemini found "AI-Powered" in HN titles causes a 15% score drop due to community fatigue. Lead with the engineering.
- Threads with live demos get **2.5x more replies**

**Title formula:** `Show HN: Spacezero – Browser voxel sandbox with smooth curves and spheres`

Put "Hermite dual-contouring" and "AI-native textures" in the description body, not the title. The title should maximize curiosity and reduce jargon.

**What to have ready:**
- The game must be playable and stable at the URL
- Prepare to answer technical questions about the engine (HN loves this)
- Have analytics tracking visitors, play sessions, retention from day 1
- When someone calls out a bug, **fix it and reply within hours** — this turns critique into public proof of rapid execution (exactly what Speedrun values)

**Realistic outcome:** 10K-50K visitors. If even 37% play (browser conversion rate), that's **3,700-18,500 players in 24 hours**. With D7 retention data from those players, you have the exact "spark" Speedrun wants.

### #2: Build Competition — "The Impossible Build Challenge" (2 Seasons)

**Why this is #2:** 94% of competition entrants self-promote their entries (Outgrow), each recruiting an average of 2.68 friends (InviteReferrals). Every entry is a shareable browser link — viewers land *inside the game* seeing the build. No other voxel builder has this. The competition amplifies every other channel: gives HN visitors a CTA, turns creators into contestants, and generates Reddit content organically.

**Hard data supporting this:**
- MCC runs with $0 prizes → 913K peak concurrent viewers. Recognition > money for builders.
- MrBeast 100-player build competition → 56.1M YouTube views
- Contest landing pages convert at 7.29% (vs 2.35% baseline)
- 62% of participants recruit a friend to enter
- UGC contests boost engagement 6.9x vs brand content
- Competition participants: 60% become repeat users
- Short contests get 29% more entries, but phase-gated seasons combat the engagement valley (DARPA/GE model)

**Positioning:** "Build what Minecraft can't" is the marketing tagline — it goes in Reddit titles, TikTok captions, outreach emails. But competition categories are deliberately open (Best Creation, Best Architecture, Best Landscape, People's Choice) so builders showcase Spacezero's advantages naturally. Smaller voxel size enables detail/precision impossible in MC, not just smooth curves. Open categories produce diverse, stunning entries instead of 50 novelty spheres.

**Format:** 2 seasons × 1 month each. Phase-gated to maintain urgency and create compound growth.

| | Dates | Theme | Prizes |
|---|---|---|---|
| **Season 1** | March 18 - April 14 | Open: "Build something amazing" | $1,000 (9 winners) |
| **Season 2** | April 15 - May 12 | Themed (based on S1 learnings) | $1,000 (9 winners) |

**Prize structure per season ($1,000):**

| Prize | Amount | Winners |
|---|---|---|
| Grand Prize | $500 | 1 |
| Category winners (3x) | $100 each | 3 |
| People's Choice | $100 | 1 |
| Honorable mentions (4x) | $50 each | 4 |
| **Total** | **$1,000** | **9** |

Plus: "Founding Builder" badge (all entrants, permanent), homepage feature (winners), creator program entry. Costs $0.

Hybrid judging: 50% community vote (drives sharing — voters must visit the game), 50% panel (credibility).

**Why seasons, not one long competition:** Research shows engagement follows a U-shaped curve — peaks at start and end, valley in the middle. At 2 months continuous, the valley is 6 weeks long. Seasons create two urgency cycles with two waves of "I won" social posts. Season 1 builders return for Season 2 — that's retention data. Cumulative leaderboard creates the ladder effect.

**The viral loop:** Builder enters → builds something stunning → shares browser link → viewer clicks in → sees build live → tries building → enters or keeps playing. Estimated K-factor: 0.3-0.7.

**For Speedrun (March 25):** "We launched Season 1 of our build competition 7 days ago. X builders have entered. Y voters have played the game to see each build in-browser. Season 2 launches mid-April. Builder retention is [high] because they're invested in their creations." That's an active growth engine, not a finished event.

**Conservative model (20 entries/season):** 19 social posts → 50+ new players from sharing alone + voter traffic. **Base model (50 entries/season):** 3,000 visitors, 1,500 votes (each = play session), 15 content pieces from participants.

### #3: Reddit Organic Blitz (Day 3-7)

**Critical correction from research:** Do NOT post to r/Minecraft or r/Minecraftbuilds. They remove non-Minecraft game posts.

**The right subreddits (ranked by viability):**

| Subreddit | Members | Why it works |
|---|---|---|
| r/WebGames | 280K | They literally expect playable browser game links |
| r/browsergames | 30K | Same — browser games are the whole point |
| r/IndieGaming | 390K | Explicitly designed for indie game showcases |
| r/playmygame | 105K | Built for devs sharing their games |
| r/gaming | 38M | High-reward but strict — needs a stunning 15-sec GIF, zero promo language |
| r/gamedev | 1.5M | Devlog-style post about the engine, not "play my game" |

**Post format:** Short video/GIF (30 seconds or less) uploaded directly to Reddit. NOT a link post. Titles with "I've been working on..." language. 60-80 character titles. Let commenters discover it's playable in browser — don't lead with it.

**The positioning trick:** Never say "Minecraft killer" or "Minecraft alternative." Post as "I've been building a browser voxel game with smooth curves." Let commenters make the Minecraft comparison themselves — that organic comparison in comments is free marketing.

**Timing:** 10 PM – 2 AM EST on weekends for gaming subs.

**Case study benchmark:** Laysara got 74K upvotes and 11K wishlists from ONE Reddit post, which triggered Steam's algorithm for 2,500 wishlists/day. One post can change everything.

### #4: Creator Outreach Sprint (Day 4-10)

**The math (revised up from Gemini):** Our research said 200 emails. Gemini found real indie dev data showing **600 emails** needed for decent coverage. A realistic two-week funnel: 300-600 contacts → 30-60 replies → 8-15 content pieces. Personalized outreach converts at 25-35% vs 10% generic.

**Who to target:**
- Nano Minecraft creators (1K-50K followers) — they respond to DMs, they're hungry for novel content, engagement rates 3-5x higher than big creators
- EYstreem has **13.1M subscribers** — too big for cold outreach. Target smaller creators in his orbit instead
- Faith-based gaming creators (Redeemed Zoomer, FaithForge Gaming, Gaming and God) — shared faith connection genuinely improves response rates

**Best outreach method:** Email first, DM follow-up 3-5 days later. Personalize to their specific content. Keep it short: what the game is, why it's different (smooth curves in a voxel world, runs in browser), and a direct link to play.

**The pitch writes itself:** "Try building a sphere." That's it. The content makes itself because the visual is inherently surprising to anyone in the Minecraft audience.

**Budget:** $0 if they try for free (many will for a genuinely novel game). $200-500 for any paid placements.

### #5: TikTok/Shorts/Reels Series (Day 1-14, background)

**Reality check:** Weeks 1-2 on TikTok typically get 200-1K views. This is a marathon, not a 2-week sprint. BUT:

- Start now to warm the account (7-14 day warmup before algorithm kicks in)
- Consistent daily posting shows Speedrun you have a content engine running
- The compounding starts NOW for post-application growth

**Content formula (from Mortal Rite's 120M views, $0 spend):**
- Developer face on camera + subtitles on every video
- **85% of users watch without sound** (Gemini) — captions are mandatory, not optional
- Progression videos: before/during/after builds
- "Day X of building impossible things in a browser game" challenge format
- Satisfaction content: building a perfect sphere, smooth circular tunnel

**Hook templates (from Gemini):**
- Curiosity loop: "This new browser engine feels illegal to know" + split screen (blocky vs smooth)
- Pain point: "Stop wasting your time on broken Switch co-op" (Pokopia wedge)
- Contrarian: "Everything you know about voxel building is obsolete in 2026"

**Posting cadence:** 1-2x/day. Cross-post to all 3 platforms, stagger by 1-2 hours. Never leave watermarks from other platforms.

**Hashtags:** 3-5 per video max. #minecraft (527B views) is the discovery engine. Add #indiegame #browsergame #gamedev #voxel.

### #6: Reddit Paid Ads (Day 7-14, if needed)

**Only if organic doesn't catch fire.** Don't spend money until you've tried organic first.

| Platform | CTR | CPC | CPM |
|---|---|---|---|
| **Reddit Gaming** | 0.5-1.2% | $0.10-$0.50 | $1-$4 |
| Facebook/Instagram | — | $0.80-$3.50 | $8-$15 |
| Twitter/X | — | $0.60-$2.20 | $6-$12 |

Reddit is the clear winner on cost. Text overlays on video ads boost CTR by 32% (Reddit's own data).

- $500 budget = 1,000-5,000 clicks = 370-1,850 plays (at 37% browser conversion)
- Tight subreddit targeting yields 40% lower CPCs than broad interest targeting
- Target subreddits: r/VoxelGameDev, r/proceduralgeneration, r/SurvivalGaming, r/basebuildinggames (from Gemini — more specific than broad r/gaming)
- Two creatives only: (1) "impossible in Minecraft" side-by-side clip, (2) "click-to-play in browser" ultra-short clip
- **The key metric isn't CPI — it's sessions and shares per dollar**

**ChatGPT's budget allocation (practical):**
- $600-900: Reddit ads (two creatives, iterative)
- $300-700: Micro-creator stipends (6-10 at $50-100 each)
- $0-400: Contingency for boosting best-performing short-form post

---

## The 14-Day Execution Calendar

### Phase 1: Prepare (Day 1-3, March 12-14)

- [ ] Record 5-10 "impossible builds" clips (sphere, curves, smooth terrain, circular tunnel, smooth cave)
- [ ] Ensure game is stable and playable at a public URL
- [ ] Set up analytics: visitors, play sessions, session length, D1/D7 retention
- [ ] Ship retention essentials: auto-save (localStorage), shareable build URLs, Amplitude/PostHog analytics
- [ ] Create Discord server with 5-8 channels max (see Discord Playbook above). Add Carl-bot, MEE6, Statbot.
- [ ] Set up social accounts if not ready (TikTok, YouTube, Instagram, Reddit)
- [ ] Draft Show HN post (title + description)
- [ ] Build cold outreach list: 300-600 nano Minecraft creators with emails (Gemini says 600 needed for decent coverage)
- [ ] Prepare build competition page: rules, categories (Best Creation, Best Architecture, Best Landscape, People's Choice), prize structure ($1,000/season), voting system
- [ ] Seed 5-10 team builds as initial competition entries
- [ ] Start daily TikTok/Shorts series (account warmup)

### Phase 2: Ignite (Day 4-7, March 15-18)

- [ ] **Tuesday March 18 or Wednesday March 19: Launch Show HN post** (8-11AM UTC / 3-6AM EST)
- [ ] **Same day: Launch "The Impossible Build Challenge" Season 1** — open categories, $1,000 prizes, runs through April 14
- [ ] Be ready to answer technical questions in HN comments for 12+ hours
- [ ] Track: visitors, plays, D1 retention from HN traffic
- [ ] Post to r/WebGames + r/IndieGaming (stagger across days) — include competition CTA
- [ ] Send first batch of 150-200 creator outreach emails — pitch: "Enter our build competition"
- [ ] List competition on itch.io jam board (free, organic discovery)
- [ ] Continue daily TikTok/Shorts series
- [ ] If HN hits front page: immediately cross-post to relevant Discords

### Phase 3: Amplify (Day 8-11, March 19-22)

- [ ] Double down on whatever channel showed most traction
- [ ] Post to r/browsergames + r/playmygame + r/gamedev (devlog angle)
- [ ] Post competition progress updates ("Day X: Y entries so far!")
- [ ] Highlight best competition entries on social media — each highlight = shareable browser link
- [ ] Send second batch of 150-200 creator outreach emails
- [ ] DM follow-up to first batch non-responders
- [ ] If creators are posting: engage, share, amplify their content
- [ ] Launch Reddit ads ($300-600) if organic needs a boost
- [ ] Continue daily TikTok/Shorts — use competition timelapse builds
- [ ] Track D7 retention from HN traffic (this is gold for the application)

### Phase 4: Compile & Apply (Day 12-14, March 23-25)

- [ ] Compile all metrics: plays, visitors, signups, retention, social views, WoW growth, competition entries, votes cast
- [ ] Pull Season 1 competition data (7 days in): entries, votes, sharing metrics, builder retention
- [ ] Calculate week-over-week growth rates
- [ ] Screenshot/export analytics dashboards
- [ ] Reserve $300-500 to boost the best-performing channel for a final push
- [ ] **March 25: Submit Speedrun application with metrics + Season 1 competition data** (Season 1 still running — show ongoing growth engine)

---

## Metrics Targets (realistic, research-backed)

| Metric | Conservative | Base | Optimistic |
|---|---|---|---|
| Show HN visitors | 5,000 | 15,000 | 50,000 |
| Reddit organic visitors | 2,000 | 10,000 | 50,000+ |
| Competition entries | 20 | 50 | 150+ |
| Visitors from competition sharing | 500 | 3,000 | 10,000 |
| Votes cast (= play sessions) | 200 | 1,500 | 5,000 |
| Total unique players | 3,500 | 13,000 | 40,000+ |
| Creator content pieces | 5 | 15 | 40+ |
| TikTok/Shorts views | 1,000 | 5,000 | 20,000 |
| Discord members | 50 | 200 | 500+ |
| WoW growth rate | 20% | 50%+ | 100%+ |

**The story for Speedrun:** "We launched our browser voxel game 2 weeks ago with a build competition — Season 1 of 'The Impossible Build Challenge.' [X] people have played it — no download required, just click and play. [Y] builders entered in the first 7 days, sharing their entries and bringing [Z] voters who played the game to see each build in-browser. D7 retention is [R]%. Week 2 was [W]% higher than week 1. Season 1 runs through mid-April. Season 2 launches after." Then show the builds.

---

## Discord Community Playbook

### Why Discord matters for Speedrun

- Joshua Lu (a16z Games) has called Discord "the future" for gaming, and Discord Activities could become "one of the biggest game platforms available" (TechCrunch)
- Several Speedrun portfolio companies build ON Discord — having an active server is a concrete traction signal
- Key metrics investors want: **community size (Discord members, social followers), Steam wishlists, and compelling gameplay footage** (Indie Game Business 2025)
- Target: **100-500 members in 14 days.** 100 is the "critical inflection point" where the server feels alive to newcomers (Hashmeta). Even better: show growth rate ("0 to 400 in 14 days").

### Realistic cold-start growth expectations

| Phase | Expected Members |
|-------|-----------------|
| Week 1 (cold start) | 20-80 |
| Week 2 (with HN/Reddit momentum) | 80-200 |
| Month 1 (organic only) | 100-300 |
| Month 1 (with viral hit) | 500-5,000+ |

For reference: Among Us had 30-50 concurrent players for 2 years before exploding. Lethal Company had zero marketing budget. R.E.P.O. went from server creation to 323K members in months. The pattern: **the game produces clips → clips drive traffic → traffic joins Discord.**

### Server setup (keep it minimal)

**5-8 channels maximum at launch.** Channel bloat is the #1 structural mistake for small servers.

Core structure: `#welcome-rules` (read-only), `#announcements` (read-only), `#general`, `#show-your-builds`, `#bug-reports`, `#suggestions`, `#building-together` (voice). Add channels only when needed.

Bots: Carl-bot (reaction roles — Builder/Explorer/Tester/Artist, 250 free), MEE6 (leveling), Statbot (analytics from day one).

### Growth tactics that matter

1. **In-game Discord CTA** — show after first play session, not during. "Share your creation / Get feedback on Discord." Personalized CTAs convert 42% more (WiserNotify).
2. **Reddit → Discord pipeline** — r/WebGames + r/IndieGaming posts with playable link + Discord invite. HN front page → estimated 50-150 Discord joins (1-3% of players convert).
3. **The build competition IS the Discord growth engine** — every competition entry discussion, vote, and announcement drives server traffic.
4. **Developer presence** — devs must be visibly active in channels. "In the early stages, be very active and interactive — this will encourage more people to interact." You drive conversations until ~200+ members.

### Discord Embedded App SDK — the secret weapon

The Discord Embedded App SDK transforms browser games into **Discord Activities** playable inside voice/text channels and DMs. It works via iframe — perfect for a browser-based game. Players can discover and play Spacezero without ever leaving Discord.

**This could be a massive differentiator for the Speedrun application.** a16z is explicitly bullish on Discord as a gaming platform, and integrating Spacezero as a Discord Activity maps directly to their thesis. GitHub: [discord/embedded-app-sdk](https://github.com/discord/embedded-app-sdk).

### What keeps people vs. what makes them leave

**STAY:** Regular dev interaction, exclusive insider info, meaningful roles, active voice channels, seeing feedback get implemented, weekly events (build challenges, AMAs).

**LEAVE:** Silent server, too many channels, only announcements with no conversation, no developer presence, overly strict moderation.

### Key metrics to track

| Metric | Target | Why |
|--------|--------|-----|
| Total members | 100-500 | Social proof for Speedrun |
| First-week retention | >20% | Minimum viable; <20% = onboarding needs work |
| Communicators ratio | >30% | Healthy engagement benchmark (Discord) |
| Daily active visitors | >50% of members | Shows server provides value |

---

## Research Files Index

| # | Topic | File | Source |
|---|---|---|---|
| 1 | Viral indie game case studies (15 games, $800M+) | `research/indie-game-viral-case-studies.md` | Claude |
| 2 | Reddit GTM deep dive | `research/reddit-gtm-deep-dive.md` | Claude |
| 3 | TikTok/Shorts indie game marketing | `research/tiktok-shorts-indie-game-marketing.md` | Claude |
| 4 | Hacker News Show HN launch research | `research/hacker-news-show-hn-launch-research.md` | Claude |
| 5 | Creator outreach + browser game virality | `research/creator-outreach-browser-virality.md` | Claude |
| 6 | Accelerator traction benchmarks | `research/accelerator-traction-benchmarks.md` | Claude |
| 7 | ChatGPT deep research (62 citations) | `research/2026-03-12-chatgpt-deep-research.md` | ChatGPT |
| 8 | Gemini deep research (62 URLs, Pokopia angle) | `research/2026-03-12-gemini-deep-research.md` | Gemini |
| 9 | ChatGPT target metrics research | `research/2026-03-12-chatgpt-target-metrics.md` | ChatGPT |
| 10 | Gemini target metrics research | `research/2026-03-12-gemini-target-metrics.md` | Gemini |
| 11 | Target metrics & scenario model (synthesis) | `research/target-metrics-and-scenarios.md` | Claude |
| 12 | Show HN traffic benchmarks | `research/show-hn-traffic-benchmarks.md` | Claude |
| 13 | Reddit traffic data supplement | `research/reddit-traffic-data-supplement.md` | Claude |
| 14 | Creator outreach & short-form data | `research/creator-outreach-and-short-form-data.md` | Claude |
| 15 | Browser game metrics & benchmarks | `research/browser-game-metrics-benchmarks.md` | Claude |
| 16 | Speedrun & YC traction deep dive | `research/speedrun-yc-traction-deep-dive.md` | Claude |
| 17 | Speedrun traction claim audit | `research/speedrun-traction-claim-audit.md` | Claude |
| 18 | Build competition strategy (deep research) | `research/build-competition-strategy.md` | Claude |
| 19 | Player retention mechanics — browser D1/D7 | `research/player-retention-mechanics-browser-games.md` | Claude |
| 20 | Discord community growth — 2-week sprint | `research/discord-community-growth-research.md` | Claude |
| 21 | Competition duration research | `research/competition-duration-research.md` | Claude |

---

## The Bottom Line

Show HN on **Tuesday or Wednesday** is your highest-leverage single action. A browser voxel engine with smooth curves is exactly what HN loves — technically impressive, instantly playable, visually surprising. If it hits front page, you could have 10K+ players in 24 hours with D7 retention data by application day.

The build competition ("Build what Minecraft can't") is your #2 — 2 seasons × 1 month × $1K/season. Season 1 launches same day as Show HN, giving every visitor a specific thing to do. Turns builders into marketers (94% self-promote). Every entry is a shareable browser link. Every vote is a play session. Season format creates compound growth — S1 builders return for S2.

The Pokopia co-op backlash is a gift — 2.2M frustrated buyers looking for a sandbox game where multiplayer actually works. Position Spacezero as the antithesis: zero hardware restrictions, zero download, instant access.

900K NoCubes mod downloads prove the demand for smooth voxels. 11.8M views on "Minecraft But Round" prove the audience. You're not creating a market — you're entering one that's begging for what you've built.

Reddit organic is your #3 — competition entries become organic posts. Creator outreach (300-600 emails, pitch = "enter our competition") is your #4. TikTok is background investment that compounds post-application. Paid Reddit ads ($300-600) are the reliable baseline if organic doesn't spike.

You need 5 good clips, one good Tuesday, and a build competition that makes Minecraft builders say "wait, I can build *that*?"
