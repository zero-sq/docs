# Target-Metrics Model for 14-Day GTM Sprint

This report builds a channel-by-channel target-metrics model for a 14-day go-to-market sprint ending on **March 25, 2026**, aligned to what entity["organization","Andreessen Horowitz","venture capital firm"] entity["organization","Speedrun","startup accelerator"] emphasizes in applications: a “small spark” of real market validation (users, signups, engagement) and evidence the team can move fast. citeturn21view0turn21view1turn21view3

Product positioning (“Minecraft but with curves, in your browser”) is well-matched to low-friction distribution: letting people click and play immediately compresses the funnel from “interest” to “use” and makes top-of-funnel spikes (especially from entity["organization","Hacker News","tech news site"]) materially more valuable than they often are for download-first games. citeturn1view3turn21view4

Throughout, **“players”** means *unique visitors who start at least one browser play session*, using your stated **37% visitor→player** conversion (kept constant across channels for comparability). **“Signups”** means accounts or emails captured (your choice of mechanism), modeled as a separate conversion backed by real “Show HN” signup capture examples. citeturn1view3

## Channel-by-channel yield estimates grounded in real launches

### Show HN traffic and conversion model

A practical way to think about “Show HN” is *rank band → unique visitors → decay curve → capture rate*. Multiple public postmortems show enormous variance depending on whether you reach the front page and how long you stay there:

* **Low traction / doesn’t break out:** one founder reports ~**500 uniques** from “Show HN” among multiple HN attempts. citeturn8view3  
* **Front-page-ish but not dominant:** a postmortem describing a front-page stint (“~6 hours”) reports **~2,000 unique visitors from HN**. citeturn8view1  
* **Solid front-page exposure:** an analytics post reports **~3,500–4,000 visitors** attributable to front-page exposure, and ~**8,000 over ~4 days** total. citeturn1view0  
* **Strong “Show HN” hit:** a detailed HN traffic curve shows **8,832 unique visitors on day 1**, **2,755 on day 2**, then a steep decay (hundreds/day by day 3–7). citeturn1view3  
* **#1-level breakout:** a #1-on-HN postmortem reports **63,000 unique visitors day 1** to the author’s site (and **15,000 day 1** to a companion interactive site). citeturn8view0  
* A separate HN comment thread’s “#1 spot” data point reports **~22k visitors/day over two days (~30k uniques)** for a #1 story, reinforcing the “tens of thousands” order of magnitude. citeturn4view1  

**Decay curve (why day 2–7 matters for Speedrun):** the clearest, quantified curve shows day 2 at roughly **~31% of day 1**, day 3–4 falling to **single-digit percent of day 1**, and then a long tail. citeturn1view3 This matters because a Speedrun reviewer can mentally discount a “single spike” unless you show week-2 continuation. citeturn21view3turn21view0

**What fraction will actually play?** With a browser game, your stated **37% visitor→player** is plausible as a structural advantage versus download flows; the model below uses it directly (so Show HN visitor volume translates into unusually high “hands-on” usage compared to most HN launches).  

**Signup capture benchmark from the HN spike:** one Show HN postmortem reports capturing **~6.4%** of visitors as email subscribers after adding a lightweight signup bar during the spike. citeturn1view3 That empirically supports using a **4% / 7% / 10%** visitor→signup range (bear/base/bull) if you add an in-flow CTA (“save worlds,” “get updates,” “join playtest,” “get seed access,” etc.).

### entity["company","Reddit","social news platform"] organic posts in gaming communities

The key measurable for Reddit organic is **post views → outbound actions**. Several indie game posts expose how extreme the distribution is:

* A “meh” post with **36 upvotes** produced **50,000 views** and **217 signups** (for a product adjacent to an HTML5 game), demonstrating that *high view volume can occur without high upvotes*. citeturn12view0  
* A game promo breakdown reports **~300K views** and **6,500 upvotes**, yielding **~264 Steam-attributed wishlists** (~0.088% view→wishlist). citeturn14view0  
* Another dev reports a repost that got **2.5k upvotes** and **100,000+ views**, driving **2–3k wishlists** (a dramatically higher conversion than the prior example, illustrating how “idea strength” and audience-target match dominate). citeturn17view0  
* Smaller, community-origin posts can still drive real site traffic: one creator cites **40 upvotes → 200+ visits** (notably, from a community member posting, which likely increased trust/click propensity). citeturn14view3  
* A campaign writeup shows **~100 upvotes** and **13 link clicks**, a reminder that *some subreddits deliver lots of attention but few outbound clicks*. citeturn14view2  

**Upvotes → visitors:** because Reddit’s UI can bury links (and many devs post the link in comments), the underlying clickthrough is highly sensitive to format. The observed “clicks per upvote” spans from **~0.13 clicks/upvote** (13 clicks on ~100 upvotes) to **~5 visits/upvote** (200+ visits from ~40 upvotes). citeturn14view2turn14view3 Your model should therefore treat “upvotes” as a *distribution amplifier* (drives more views), not a stable proxy for outbound traffic.

**Practical reach benchmarks for the model:** Reddit posts in the cited examples span **50k views** (low-mid virality) to **100k–300k views** (solid) and up to multi-million impressions in other post-insight screenshots. citeturn12view0turn14view0turn11search24 For a browser game with a strong “immediately playable” CTA, you should assume your view→visit conversion is likely better than Steam-wishlist CTAs, but still variable.

### Cold creator outreach (nano/micro gaming creators)

Because you’re targeting **300–600** creators with **2 GTM people**, success is determined less by “average influencer marketing stats” and more by (a) deliverability, (b) reply rate, and (c) *publish rate* (the fraction that actually makes content).

**Response rate anchors (email):** broad cold-email studies in 2025 show average reply rates around **~5.8%**, with wording/length affecting outcomes (e.g., 6–8 sentences is cited as a higher-performing band in one benchmark writeup). citeturn18search16turn18search12 While creators aren’t B2B leads, these benchmarks are still useful as “floor/median” anchors for *unfamiliar inbound*. In practice, creator reply rates can be higher with strong personalization and a clear “why you,” but the publish rate is usually the bottleneck.

**View count expectations (why you need volume):** across YouTube, view distribution is heavy-tailed; one analysis reports a very low median across all videos (illustrating that many uploads get little reach), and another older category breakdown puts “Gaming” average views/video around ~3,050. citeturn18search18turn18search11 For your model, it’s safer to treat expected views per creator video as a range (hundreds to tens of thousands), and then weight by “how many publish.”

**Coverage rate (“what % actually make a video?”):** public, game-specific outreach publish-rate benchmarks are rarely disclosed; a realistic modeling approach is to assume publish rate is a fraction of reply rate, and that most replies will be “can’t cover now” unless you lower friction (binary access link, quick briefing, pre-cut clips, and a hook that makes for good content). This is why the scenario model below uses conservative publish-rate bands.

### entity["organization","TikTok","short-form video platform"] + entity["company","YouTube","video platform"] Shorts organic (0–1k founder account)

Your most useful *real-world* anchor for “new account can it break out?” is a cross-channel indie dev case where the team explicitly says they created **new accounts** and got:

* **Instagram: 1M+ views** on a trailer cut, driving **5,000+ wishlists** from a single piece of content. citeturn17view0  
* **YouTube Shorts: 3–4k views** (described as “more modest”) contributing to discovery of the main trailer. citeturn17view0  

Two takeaways for modeling:
1) for new accounts, a **few thousand views per short** is a reasonable base case; citeturn17view0  
2) “viral” is not linear—one hit can be **100k–1M+** views if the hook is strong and the idea fits the platform. citeturn17view0turn18search18  

Given you’re a browser game, your advantage is that every short can have a direct “play now” payoff (no app store friction), but you should still expect **click-out rates to be the limiting step** unless you build strong “search intent” (people googling “Spacezero”) or a creator/community amplification loop.

### Reddit paid ads benchmarks (gaming)

You have unusually strong benchmark coverage here because indie devs and PPC writers often share concrete figures:

* A “video games” benchmark table reports **CPM ~$1–$4**, **CTR ~0.5%–1.0%**, and **CPC ~$0.10–$0.50** as typical ranges (with conversion rate ranges depending on the conversion event). citeturn2view0  
* A case study reports **$1,071 spend → 1.45M impressions → 17.4K clicks**, with **CTR 1.19%** and **CPC $0.06** (exceptionally efficient), showing the upside when creative + targeting match. citeturn2view0  
* Another campaign reports **$100 → 43,973 impressions → 316 clicks**, **CTR 0.719%**, **CPC $0.36**, a more “normal” outcome. citeturn2view0  

For modeling, it’s reasonable to treat Reddit ads as a controllable lever that can reliably buy **~1k–10k additional visitors** within your $1k–$2k overall budget, depending on what share you allocate and your achieved CPC. citeturn2view0

## Fourteen-day scenario model with Bull, Base, Bear by channel and combined

### Conversion constants used across scenarios

The combined model uses:
* **Visitor → player-start:** 37% (your stated browser advantage).  
* **Visitor → signup/account:** modeled as **4% / 7% / 10%** (bear/base/bull), anchored by an observed **~6.4%** email capture during a Show HN spike. citeturn1view3  
* **Deduping between channels:** 10% (bear) / 12% (base) / 15% (bull) reduction to estimate unique visitors across overlapping audiences (HN/Reddit/creator overlap is real but usually not dominant in a 14-day window).

### Per-channel Bull/Base/Bear outputs (visitors → players → signups)

**Show HN (Day 1 launch)**  
These visitor bands are chosen to line up with published Show HN outcomes spanning ~500 uniques (low), ~2k–4k (moderate front-page), ~12k+ week-of (strong), and ~30k–60k+ day-one (breakouts). citeturn8view3turn8view1turn1view0turn1view3turn8view0turn4view1  
* Bear: **1,500 visitors → 555 players → 60 signups**  
* Base: **9,000 visitors → 3,330 players → 630 signups**  
* Bull: **50,000 visitors → 18,500 players → 5,000 signups**

**Reddit organic (multiple posts across gaming subs)**  
These bands reflect the fact that single posts can generate 50k–300k views (and sometimes far more), but click-outs vary widely; modeling as site visitors keeps the goals operational. citeturn12view0turn14view0turn17view0turn14view2turn14view3  
* Bear: **800 visitors → 296 players → 32 signups**  
* Base: **2,500 visitors → 925 players → 175 signups**  
* Bull: **12,000 visitors → 4,440 players → 1,200 signups**

**Creator outreach (300–600 cold emails)**  
Visitor yield is modeled from “videos published × expected click/search lift,” acknowledging that hard publish-rate data is rarely public; the model is intentionally conservative on visitor yield per creator unless you observe otherwise in week 1. citeturn18search16turn18search18turn18search11  
* Bear: **300 visitors → 111 players → 12 signups**  
* Base: **1,500 visitors → 555 players → 105 signups**  
* Bull: **6,000 visitors → 2,220 players → 600 signups**

**Short-form (TikTok + YouTube Shorts)**  
These visitors assume you’re able to translate attention into “play now” clicks/search. The view-side expectations are anchored by a new-account case showing 3–4k views on Shorts and 1M+ on a breakout clip on another short-form platform. citeturn17view0  
* Bear: **150 visitors → 56 players → 6 signups**  
* Base: **600 visitors → 222 players → 42 signups**  
* Bull: **2,500 visitors → 925 players → 250 signups**

**Reddit paid ads (late sprint control knob)**  
These visitor bands align with observed CPC/CTR ranges and small-budget case studies. citeturn2view0  
* Bear: **1,000 visitors → 370 players → 40 signups**  
* Base: **3,500 visitors → 1,295 players → 245 signups**  
* Bull: **10,000 visitors → 3,700 players → 1,000 signups**

### Combined 14-day projection (deduped)

**Bear combined**  
* Total visitors (raw sum): 3,750 → **3,375 unique visitors** (10% dedup)  
* Total players: **~1,249**  
* Total signups: **~150**

**Base combined**  
* Total visitors (raw sum): 17,100 → **~15,048 unique visitors** (12% dedup)  
* Total players: **~5,568**  
* Total signups: **~1,197** (≈1.1k after minor cross-channel dedup)

**Bull combined**  
* Total visitors (raw sum): 80,500 → **~68,425 unique visitors** (15% dedup)  
* Total players: **~25,316**  
* Total signups: **~8,050** (≈7.5k after minor cross-channel dedup)

### Timeline checkpoints (Day 3, Day 7, Day 14)

The shape of these checkpoints is driven by the empirically steep HN decay curve (most of the total happens in the first 48 hours) and the fact that creator/paid channels typically land later. citeturn1view3turn21view4

**Base scenario (recommended planning baseline):**
* **By Day 3:** ~8.8k unique visitors, ~3.3k players, ~600–700 signups (Show HN dominates; Reddit contributes meaningfully if you post Day 2). citeturn1view3turn12view0  
* **By Day 7:** ~11k unique visitors, ~4.1k players, ~800–900 signups (Reddit wave + early creator trickle). citeturn14view0turn14view2  
* **By Day 14:** ~15k unique visitors, ~5.6k players, ~1.1k–1.2k signups (ads + creators + shorts now matter). citeturn2view0turn17view0  

## “Enough for Speedrun” traction thresholds and tiering

Speedrun’s own materials and recent reporting are unusually explicit about selection pressure and what they want to see:

* Speedrun reports reviewing **19,000+ pitches** for SR006 and selecting **under 0.4%**. citeturn21view0  
* A recent entity["organization","TechCrunch","technology news site"] writeup quotes the program team emphasizing that they aim to “pour gasoline on a very small spark” and like to see **“a little bit of market validation or traction.”** It also states that **~10%** of applicants make it to the video-call stage. citeturn21view3  

Given that framing, a *credible traction package* for a browser game should include:
* **Real usage** (players, sessions, repeat play), not only impressions.  
* **At least one leading indicator of retention/engagement** (D1 and/or D7, or repeat sessions), because “they clicked once” reads like “HN spike” otherwise.  
* **Evidence of compounding distribution** (creator reposts, community share loops, or week-2 growth in baseline traffic).

### A practical minimum / Tier system for a browser game application

These tiers are designed around what a reviewer can quickly sanity-check: your click-to-play advantage, your week-2 continuation, and whether you have a believable path to scale. citeturn21view3turn21view0

**Tier 3 (possible interview): clear spark, but still ambiguous)**
* 14-day unique visitors: **5,000+**  
* Players: **1,800+** (implied by 37% play-start)  
* Signups/accounts: **300+**  
* D1 retention (player-level): **≥20%**  
* Social views (total): **≥50k**  
* Creator videos published: **≥2**  
* Discord members: **≥150**  

This tier says: “People are showing up and trying it, and a subset is opting in.” It matches Speedrun’s “spark” language without requiring scale. citeturn21view3turn1view3

**Tier 2 (likely interview): diversified traction + early compounding)**
* 14-day unique visitors: **15,000+**  
* Players: **5,500+**  
* Signups/accounts: **1,000+**  
* D1 retention: **≥25%**, D7 retention: **≥6%**  
* Social views: **200k+**  
* Creator videos: **≥4**  
* Discord members: **≥300**  
* Baseline WoW growth (excluding launch spike): **≥10%**

This tier looks like: “HN spike happened, but the game kept moving after, and we can already see multiple channels contributing.” citeturn1view3turn2view0turn17view0

**Tier 1 (almost certainly interviewed): breakout signal)**
* 14-day unique visitors: **50,000+**  
* Players: **18,500+**  
* Signups/accounts: **3,500+**  
* D1 retention: **≥35%**, D7 retention: **≥10%**  
* Social views: **1,000,000+**  
* Creator videos: **≥8**  
* Discord members: **≥1,000**  
* Baseline WoW growth (excluding spike): **≥20%**

This corresponds to “we found something with wide appeal *and* the beginnings of retention/community,” which is the kind of compounding signal accelerators can confidently amplify. citeturn21view0turn21view3turn17view0turn8view0

### How Speedrun will likely “discount” views vs users

What founders publicly report on Reddit shows that **view→deep-action** conversion is wildly variable:

* 300k Reddit views → ~264 wishlists (~0.088%). citeturn14view0  
* 1M+ short-form views → 5,000+ wishlists (~0.5%). citeturn17view0  

A reviewer will usually treat raw views as “potential demand,” but will look for at least one of:
1) **click-through proof** (unique visitors),
2) **hands-on proof** (players / sessions),
3) **commitment proof** (signups, Discord),
4) **stickiness proof** (retention / repeat play).

For a browser game, you can strengthen this mental model by explicitly reporting: “X views → Y visitors → Z players (37%) → W signups,” so they don’t have to guess your funnel.

## Week-over-week growth modeling and week-two actions

### The core problem: Show HN spikes decay fast

A realistic “Show HN” trajectory is steeply front-loaded. A published curve shows thousands of visitors on day 1, about a third of that on day 2, and then a rapid fall into the hundreds/day range. citeturn1view3 This means your *week-2 growth story* cannot be “we kept getting HN traffic.” It must be “we created new sources of traffic and/or new loops.”

### A workable way to report WoW for Speedrun

Because week 1 contains a one-time spike, report two curves:
1) **Total weekly visitors** (Week 1 vs Week 2)  
2) **Baseline daily visitors excluding launch day** (Days 2–7 average vs Days 8–14 average)

That second curve is the one that can show **+5% / +10% / +20% WoW** even if the spike makes total-week comparisons noisy.

### Numeric growth scenarios (baseline traffic)

Let baseline (Days 2–7) average daily visitors be **B** (after the day-1 spike). In a base plan, you can target B ≈ 500–1,500/day by week 2 via Reddit cadence + creator hits + small paid spend. citeturn2view0turn17view0

If baseline week-1 (Days 2–7) totals **6B**, then baseline week-2 totals are:

* **5% WoW (decent):** 6B → **6.3B**  
* **10% WoW (good):** 6B → **6.6B**  
* **20% WoW (exceptional):** 6B → **7.2B**

To make that real, you need at least one *new* driver in week 2 (paid ads, creator publishes, or a second platform that starts working).

### Week-two actions that realistically sustain/accelerate after HN

Speedrun’s own content highlights they like founders who communicate and execute consistently (“regular company updates like clockwork”), which maps well to a week-2 plan centered on shipping + broadcasting. citeturn21view0 In practice for Spacezero, the highest-leverage week-2 actions are:

1) **Ship a “shareable moment” loop**: a 10–20 second replay clip, a “world seed” link, or a one-click screenshot/GIF export. This turns player sessions into marketing assets and improves creator coverage conversion.  
2) **Re-post with novelty, not repetition**: instead of “play my game,” post “I built Minecraft-with-curves in the browser; here’s a 15-second clip of [impossible-in-blocks structure]” and include a single clear CTA. The Bioneers/Reddit examples show how strongly the “idea” and framing affect conversion. citeturn17view0turn14view0  
3) **Creator enablement kit**: a one-pager + 5 pre-cut vertical clips + 3 “challenge prompts” (“make a perfect sphere base in 60 seconds,” “carve a tunnel with smooth arches,” etc.). This is aimed at increasing publish rate, which is the limiting step in outreach.  
4) **Spend small, late, and iteratively** on Reddit ads: the benchmarks and case studies show you can get meaningful traffic with small budgets, but performance depends on creative and subreddit fit. Your advantage is that the landing experience is instant-play. citeturn2view0turn13search8  
5) **Explicit weekly reporting dashboard**: make it easy for an accelerator reviewer to see week-over-week deltas (the Speedrun team literally recommends founders show the spark; your job is to package it). citeturn21view3  

## Comparable browser-game benchmarks and browser retention reality

### “First-month scale” examples from browser/.io hits

Public early-stage metrics for browser games are uneven (many studios never publish them), but there are still useful anchors:

* entity["company","Miniclip","online game publisher"]’s publisher story for entity["video_game","Agar.io","2015 browser game"] reports that by **late April 2015** the game had **5M+ players/day** (within its first month), and the game later scaled to tens of millions of monthly players. citeturn21view5turn20search5  
* A .io genre roundup cites entity["video_game","Slither.io","2016 browser game"] at roughly **86M visits/month** on the web (illustrating the ceiling for a breakout browser multiplayer). citeturn21view4  
* For entity["video_game","Shell Shockers","browser shooter game"], the developer entity["company","Blue Wizard Digital","game studio"] reports **200M unique players since 2017**, and an industry newsletter analysis cites DAU peaks **~300k–350k** (illustrating that web games can sustain very large daily usage for years). citeturn22search4turn22search7  
* For entity["video_game","Krunker.io","browser fps game"], publicly accessible early “first month” metrics are not consistently published in primary sources; in practice, you may need to rely on your own telemetry as the canonical proof point for the application (and compare conceptually to the DAU/visit magnitudes above). citeturn21view3turn21view4  

### Browser distribution platforms show how fast “plays” can spike

Even without being a global household name, web game platforms can generate huge “play” volumes when they feature or algorithmically surface a game:

* One developer recounts reaching **1M gameplays in a day** and **~17k concurrent users** for a web game on entity["company","Poki","browser game platform"], and sustaining **~200k daily gameplays** after additional releases. citeturn22search3  
* A web-market overview reports Poki at **~30M MAU** and cites entity["company","CrazyGames","browser game platform"] at similar magnitude (with hundreds of millions of games played monthly), which is relevant if you later pursue platform featuring as a growth layer. citeturn22search19  

### Retention benchmarks: what’s usable when “browser-specific” data is limited

Browser-game retention benchmarks are less standardized in public than mobile benchmarks (because mobile UA economics drove more public reporting). Practically, you can still ground targets using widely cited game retention ranges as *reference points*:

* One retention analysis states “good” historical benchmarks were **D1 ~40%, D7 ~20%, D30 ~10%**, with rising expectations in some categories. citeturn20search7  
* A mobile benchmark report cites median D1 around **~22.91%** and D7 around **~4.20%** across genres, illustrating how quickly retention drops for many games. citeturn20search23  

For Spacezero specifically, you should assume *browser friction helps acquisition more than retention* unless you build:
1) a clear early-game loop (first 2–5 minutes),
2) a reason to return (world persistence, goals, social),
3) a lightweight community hook (Discord, weekly build, creator challenges).

So, a defensible target band for an early sandbox prototype in a 14-day sprint is:
* **Bear:** D1 15%, D7 3%  
* **Base:** D1 25%, D7 6%  
* **Bull:** D1 35%, D7 10%  

These sit between median-ish “many games are leaky” outcomes and “great retention” targets cited above, while still being plausible for a creative sandbox if onboarding is tight. citeturn20search7turn20search23

## The target dashboard

| Metric | Bear | Base | Bull | Speedrun Minimum |
|---|---:|---:|---:|---:|
| Unique visitors (14 days, deduped) | 3,375 | 15,048 | 68,425 | 5,000 |
| Players (visitor→player at 37%) | 1,249 | 5,568 | 25,316 | 1,850 |
| Signups / accounts | 150 | 1,150 | 7,500 | 300 |
| D1 retention (players) | 15% | 25% | 35% | 20% |
| D7 retention (players) | 3% | 6% | 10% | 5% |
| Social total views (short-form + creators) | 25,000 | 200,000 | 1,000,000 | 50,000 |
| Creator videos published | 1–2 | 3–5 | 8–15 | 2 |
| WoW baseline visitor growth (excluding Day-1 spike) | 0–5% | 10% | 20% | 5% |
| Discord members | 50 | 300 | 1,000+ | 150 |

This dashboard is calibrated so that the “Speedrun Minimum” column corresponds to a clear “spark” package consistent with Speedrun’s explicit preference for early validation (not just market theory) and the application selectivity described in their own writeup and recent reporting. citeturn21view0turn21view3turn1view3