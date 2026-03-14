# Zerocap GTM Synthesis — The Playbook

> Distilled from 35 research files (31 Claude + 4 deep research from GPT/Gemini) + TikTok GTM strategy. March 13, 2026.
> Team: 4 people, bootstrapped. All focus on Zerocap.
> Primary GTM channel: paid influencer marketing on TikTok.
> Product: point your phone camera at any real-world object, AI transforms it into a cute living pet with unique personality traits (6 million trait combinations).

---

## Current State (fill in)

> **This section needs real data from the team.** Fill in before using this synthesis for any decision-making or application.

### What's built

- [ ] Camera-to-pet transformation — working? How many seconds from scan to pet?
- [ ] Pet personality system — how many traits implemented?
- [ ] Care mechanics (hunger, happiness, cleanliness) — live or not?
- [ ] Evolution system — any version shipped?
- [ ] Push notifications — implemented?
- [ ] Share artifact (auto-generated TikTok-ready video) — built?
- [ ] Terrain modification — functional?
- [ ] Analytics (installs, retention, sessions) — set up?

### Traction data (Feb 11 - Mar 12, App Store Connect)

| Metric | Value | Assessment |
|--------|-------|-----------|
| App Store impressions | 12,400 | Growing (+3,070%) |
| Product page views | 250 | Low — 2% tap-through from impressions |
| Total downloads | 49 | 16 first-time downloads |
| Conversion rate (impression → download) | 0.6% | Below average — listing needs work |
| Page view → download | ~20% | Decent — people who see the page do download |
| Sessions per active device | **7.41** | **Strong** — users who try it keep opening it |
| Crashes | **15** | **Critical** — nearly 1 crash per active user |
| Revenue | $0 | Expected at this stage |

**Downloads by source:**
- App Store Search: 43 (87.8%) — almost all organic discovery
- App Referrer: 4 (8.2%)
- Web Referrer: 1 (2%)
- App Store Browse: 1 (2%)

**Downloads by territory:** Korea 21, US 14, Russia 4, Australia 3

**Social media (10 days):** 20K combined impressions across TikTok, YouTube, Instagram

### What the data tells us

**The good:** 7.41 sessions per active device is a real retention signal. Small sample, but people who use the app keep opening it. This is directionally encouraging — the pet care loop may be working.

**The bad:** 20K social media impressions produced essentially **zero measurable installs.** Only 1 web referrer and 4 app referrers total. 87.8% of downloads came from App Store Search — people finding it organically, not from social content. The organic social strategy is not converting to installs.

**The critical:** 15 crashes across ~16 active users means nearly every user hit a crash. This kills retention dead. No amount of marketing fixes a crashing app. Before spending a single dollar on influencers, crashes must be near-zero.

**The App Store funnel:** 12.4K impressions → 250 page views (2% tap-through) → 49 downloads (20% conversion). The 20% page-to-download is decent. The **2% tap-through is the bottleneck** — the icon, title, subtitle, or screenshots aren't compelling enough to make people tap from search results.

### Priority order (changed by data)

The original synthesis had paid influencer marketing as #1. The data changes that. **You cannot scale acquisition into a broken funnel.**

**New priority order:**
1. **Fix crashes** — retention killer, must be near-zero before any marketing spend
2. **Fix App Store listing** — icon, screenshots, App Preview Video. 2% tap-through → target 8%+ with better creative. This 4x improvement turns 250 page views into 1,000 from the same impressions.
3. **Build share artifact** — the social content isn't driving installs because there's no frictionless path from "see a TikTok" to "download the app." Auto-generated shareable video with app name visible.
4. **THEN start paid influencer spend** — only after steps 1-3 are fixed. Otherwise you're paying to send people to a crashing app with a bad listing.

### The gap

What must be built before scaling paid influencer spend:
1. Share artifact (TikTok-ready before/after video) — without this, influencer content has no organic amplification
2. Care mechanics — without these, every user acquired through influencers churns like Lensa
3. Analytics — without retention data, you can't tell Speedrun anything meaningful

---

## The Next 14 Days (Sprint Calendar)

If Speedrun deadline or any accelerator application is imminent, compress the 16-week plan into this sprint. The 16-week calendar below is the extended roadmap — this is what you do RIGHT NOW.

### Days 1-4: Fix the foundation (DO NOT SKIP)
- [ ] **Fix all crashes** — 15 crashes on ~16 users is a dealbreaker. Identify top crashers, fix, ship update. Nothing else matters until this is done.
- [ ] **Redesign App Store listing** — new screenshots showing the transformation moment (before: real object → after: cute pet), App Preview Video (15-30 sec showing camera scan → pet reveal), rewrite subtitle to "Turn Real Objects Into AI Pets"
- [ ] Camera-to-pet in <90 seconds — verify or fix
- [ ] Share artifact auto-generates TikTok-ready video — ship if not built
- [ ] Set up proper analytics (D1/D7 retention, session tracking, share rate)

### Days 5-7: Organic seeding (free, while listing settles)
- [ ] Continue daily TikTok/Shorts organic posting (1-2x/day)
- [ ] Post to r/tamagotchi, r/virtualepets, r/iosapps
- [ ] Set up Discord server (5-8 channels)
- [ ] Send free TestFlight access to 10 nano creators (pet + cute niches) — no payment, just seeding
- [ ] Monitor crash rate on new build — must be <1% before paid spend

### Days 8-11: First paid influencer wave
- [ ] **Only if crashes are fixed and listing is updated**
- [ ] Pay 5-8 nano creators to post ($500-$800 total) — test 3 content angles
- [ ] Monitor which videos get traction (views, engagement, saves)
- [ ] Request Spark Ads authorization codes from top 2-3 performers
- [ ] Launch Spark Ads on winners ($300-$500)
- [ ] Collect D1/D7 retention data from first paid cohort

### Days 12-14: Assess + decide
- [ ] Pull all metrics: installs, retention, share rate, crash rate, App Store conversion rate
- [ ] Compare: did the new listing improve tap-through from 2% → 5%+?
- [ ] Compare: did influencer videos drive measurable installs (vs. 0 from organic social)?
- [ ] Identify best content angle and creator niche
- [ ] Decide: scale influencer spend or fix more product issues first

**Sprint budget: $1,000-$1,500** (creators $500-$800 + Spark Ads $300-$500 + reserve $200)

**Expected sprint outcome:** Crash rate near zero, App Store conversion improved, 200-800 installs from paid influencer wave, first real D7 retention data, validated (or invalidated) content angle. If influencer CPI is <$3, you have a channel. If not, iterate on content before scaling.

---

## Strategic Assessment

### Verdict

Zerocap sits at the intersection of three proven viral mechanics — camera transformation (Lensa: $50M+ revenue, Prisma: 7.5M downloads week one, Ghibli filter: 700M images in one week), virtual pet nostalgia (Tamagotchi: 100M units, Pou: 1.1B downloads, Talking Tom: 26B downloads), and AI companion emotional attachment (Character.AI: 92 minutes daily usage, Replika: 25% free-to-paid conversion). No competitor combines all three. The camera-to-pet mechanic produces content that is inherently shareable — the transformation IS the TikTok video. Paid influencer marketing is the right primary channel because this product demonstrates itself in 3 seconds and pet content gets 64% rewatch rates on TikTok (2x platform average).

### Important: AR is not the priority right now

The research references AR/camera extensively (Peridot, Pokemon GO AR mode, etc.), but **AR is not the current focus.** The camera mechanic is photo-based — point, snap, get a pet — not an AR overlay experience. This simplifies development, reduces device requirements, and keeps the core loop fast. AR can come later as an enhancement, not a launch requirement.

### Five things to obsess over

1. **First pet in under 90 seconds.** Lensa proved the transformation reveal is the emotional trigger that drives sharing. Every second between "open app" and "see your first pet" is friction that kills the viral loop. Camera open on first launch. One tap to scan. Pet appears in under 10 seconds of processing. Name it. Done. If onboarding takes longer than 90 seconds, fix it before anything else.

2. **Make the share artifact TikTok-native.** The before/after transformation video must be auto-generated, vertical, 15-20 seconds, with trending audio options and a subtle watermark. This is the single most important product feature for growth. Every share is a free ad. Lensa's #lensa hashtag hit 434M TikTok views — entirely user-generated. If your share output requires ANY editing before posting, you've lost 80% of potential shares.

3. **Nail the care obligation loop before scaling.** Peridot (Niantic) spent millions on TikTok launch marketing — 124M hashtag views — then dropped to 10.5K downloads/month within 6 months because retention was broken. Aggressive monetization + weak emotional bonds = death. Care mechanics (hunger, happiness, personality quirks) operating on real-world time are what turn a novelty into a daily habit. Without them, you're Lensa — $30M in December, $0 by March.

4. **Paid influencer marketing: start with 10 nano creators, not 100.** Test content angles with $500-$1,000 before scaling to $5K-$10K. The data from those first 10 videos tells you which creator niche, which hook format, and which CTA converts best. Then pour budget into the winning formula. Spark Ads let you boost organic-feeling creator content as paid ads — 142% higher completion rate, 37% lower CPA vs. traditional ads.

5. **Never gate the camera-to-pet transformation.** Peridot gated breeding (core mechanic) behind a paywall. Users revolted. Pou kept everything accessible and hit 1.1B downloads with a single developer and zero marketing budget. The camera scan is the core magic. Gate cosmetics, gate extra pet slots, gate premium evolutions — never gate the thing that makes people say "what app is that?"

### Key risks

- **Lensa crash risk.** Camera transformation apps have a documented pattern: explosive viral growth, then near-zero retention because the novelty wears off. Lensa went from $30.75M revenue in December 2022 to rapid decline by January 2023. The pet care loop is the structural answer — but it must be genuinely sticky, not just "a pet exists after the scan."

- **AI cost at scale.** GPT deep research puts per-pet creation at ~$0.30 (Stability AI Fast 3D at $0.10 + image generation ~$0.20), with daily chat at ~$0.006/DAU via gpt-4o-mini. At 100K MAU (25K DAU), that's ~$4,600/mo for chat + creation costs on top. The hybrid architecture (cloud for 3D generation, on-device for conversation via Apple Foundation Models) is critical -- Neopets runs infrastructure at $100K/month and they're a browser game with no AI inference.

- **TikTok regulatory risk.** TikTok faces potential US restrictions. YouTube Shorts should be the parallel investment — 85-90% of creators report better organic reach on Shorts vs. TikTok, and content gains views for months instead of TikTok's 2-3 day peak.

- **Born/Pengu competitive pressure.** 15M users, $25M raised from Accel and Tencent, opening a New York office for US marketing push. They have capital and distribution. Zerocap's differentiation (pets born from YOUR objects vs. a fixed IP character) is strong but must be communicated instantly.

- **Revenue concentration is extreme.** Appfigures data shows the top 10% of AI companion apps generate 89% of category revenue. Only 33 apps have exceeded $1M lifetime. This is a winner-take-most market -- you either break through or you don't. There's no "modest success" path in this category.

### What's strong

- **The demo IS the pitch.** Point at a shoe, get a living pet shoe with personality. This works in a 10-second video, a 3-second TikTok hook, a Speedrun application, or a coffee shop conversation. No other AI companion app has this level of instant demonstrability.
- **The market timing.** AI companion apps hit $221M lifetime consumer spend by July 2025 (Appfigures), with revenue per download doubling from $0.52 to $1.18 in one year. 72% of US teens have tried an AI companion, the Ghibli filter proved camera-to-cute transformation demand at 700M images in one week. Tamagotchi is entering its **30th anniversary year** (1996-2026) with physical unit sales that doubled 2022-2023. The nostalgia + AI + camera intersection is peaking right now.
- **Pet content dominance on social.** Pet content gets 5%+ engagement on TikTok (2x platform average), 64% rewatch rate, and Instagram's highest engagement rate by category (2.00% vs. 0.50% average). The output of using Zerocap IS pet content.
- **No direct competitor.** The competitive landscape map shows no app combining camera input + AI pet generation + personality system + terrain modification + cross-platform persistence. Born/Pengu has a fixed character. Peridot is dead. Replika is chat-only. Character.AI is text-only. Zerocap owns an empty intersection.
- **Proven revenue benchmarks in adjacent products.** Finch (self-care pet) does ~$1.75M/month revenue with ~650K monthly installs at $9.99/mo. Neopets runs on 7% premium conversion with ~$100K/mo infrastructure. Born/Pengu raised $15M Series A on 15M users. The "pet you care about" model monetizes when trust is high.

---

## Core Thesis: Why Zerocap Can Win

### The whitespace

Every photo transformation app (Lensa, Prisma, Remini, Ghibli filter) follows the same pattern: input photo, get delightful output, share, go viral, then crash because there's no reason to come back. The output is static — an image you post once.

Every virtual pet app (Tamagotchi, Pou, Peridot) follows a different pattern: generic pet, care for it daily, retention through obligation, but no viral acquisition mechanic because a generic pet isn't inherently shareable.

Zerocap is the first product to fuse both loops:

```
Photo transformation viral loop (acquisition)
    +
Virtual pet care loop (retention)
    =
Sustainable viral growth
```

The camera transformation drives acquisition (every share is a TikTok-ready before/after video). The pet care mechanics drive retention (your pet has needs, evolves, develops personality). No app has combined these before.

### Why now

| Signal | Data | Implication |
|--------|------|-------------|
| AI companion market | $221M lifetime consumer spend by Jul 2025 (Appfigures), revenue/download doubled from $0.52 to $1.18 in one year, 31% CAGR | Category is exploding AND monetizing better |
| Tamagotchi nostalgia | 100M physical units, sales doubled 2022-2023, 68% of Gen Z respond positively to nostalgia brands, **2026 is 30th anniversary** | "AI Tamagotchi" positioning has built-in emotional resonance — anniversary timing is a marketing hook |
| Camera transformation virality | Ghibli filter: 700M images/week. Lensa: 19.3M downloads/month. Remini: 120M downloads in 2024 | "Photo in, cute thing out" is the most proven viral mechanic in mobile |
| Pet content engagement | 64% rewatch rate on TikTok, 5%+ engagement (2x platform avg), Instagram's #1 engagement category | The product's output is the internet's favorite content category |
| Gen Z AI adoption | 72% have tried AI companions, 52% use regularly | Target demo is already primed for AI-powered experiences |
| On-device AI readiness | Apple Foundation Models enable $0 on-device conversation | Hybrid architecture makes unit economics work at scale |

### The 10-second demo

Point your phone at a coffee mug. AI transforms it into a cute, living creature with a unique personality — maybe it's an introvert who loves jazz and gets "thirsty" faster because it was born from a mug. Name it. Feed it. Watch it evolve. Share the before/after transformation on TikTok. Your friends download the app to try it with their own objects.

That demo works in a Speedrun application video, a TikTok ad, an investor pitch, and a text message. The product sells itself.

---

## GTM Channels Ranked by Expected Impact

| Rank | Channel | Expected CPI | Why It's Here | Budget Priority |
|------|---------|-------------|---------------|-----------------|
| **#1** | **Paid TikTok influencers + Spark Ads** | $2-$5 | Pet content gets 64% rewatch + 5% engagement. Spark Ads boost organic creator posts as paid ads (142% higher completion, 37% lower CPA). The transformation reveal IS native content. | 50-60% of budget |
| **#2** | **TikTok/YouTube Shorts organic** | $0 | 83% of viral TikTok videos come from accounts with <10K followers. YouTube Shorts gives 85-90% better organic reach. Cross-post everything. | Time investment only |
| **#3** | **Instagram Reels creators** | $3-$7 | DM shares are Instagram's #1 signal. "Send this to a friend" content format. Pet content = highest engagement category (2.00%). | 15-20% of budget |
| **#4** | **App Store Optimization** | $0 | Category: Games > Simulation (primary) + Entertainment (secondary). "AI pet," "virtual pet creator," "AI Tamagotchi" keywords. App Preview Video auto-plays in search. | Time investment only |
| **#5** | **Reddit organic + r/tamagotchi seeding** | $0 | r/tamagotchi (100K+ members), r/virtualepets, r/iosapps. Formula Bot got 100K visitors from one r/InternetIsBeautiful post. | Time investment only |
| **#6** | **Product Hunt launch** | $0 | AI + cute categories perform well. Tuesday launch. 200-500 downloads expected. | Time investment only |
| **#7** | **Discord community** | $0 | Build server around pet sharing/collection culture. 50+ relevant servers to seed. Long-term retention channel. | Time investment only |
| **#8** | **Apple Search Ads** | $3-$5 | Brand defense + competitor conquesting. "AI pet app," "virtual pet" keywords. Low volume but high intent. | 10-15% of budget |
| **#9** | **Brand partnerships** | Revenue positive | Food brands (Dole, Chobani: "scan your snack"), fashion (scan your shoes), IP collabs. Phase 3+. | $0 upfront |
| **#10** | **Cross-platform (Spacezero)** | $0 | Pets created in Zerocap persist in Spacezero's browser voxel world. Unique retention mechanic. Phase 4. | Engineering time |

---

## Influencer Marketing Deep Dive (PRIMARY CHANNEL)

### Why influencer marketing, not Show HN

The Spacezero GTM was built around Show HN because browser games convert at near-100% click-to-play with zero friction. Zerocap is an iOS app. The funnel is fundamentally different:

| | Browser Game (Spacezero) | iOS App (Zerocap) |
|---|---|---|
| Click to play | 2 seconds, zero friction | App Store → download → install → onboard |
| Conversion from impression | 60-80% | 3-5% (app store conversion) |
| Best channel | Show HN (technical audience, instant play) | TikTok influencers (visual product, mass audience) |
| Content type | Engineering demo, playable link | Before/after transformation, cute pet content |
| Target demo | HN technical audience, Minecraft builders | Gen Z female 16-24, millennial 25-32 |

Show HN and Product Hunt are supporting channels for Zerocap, not primary. The primary channel must produce visual content showing the transformation to a mass consumer audience. That's paid influencer marketing on TikTok.

### Platform strategy

| Platform | Role | Creator Volume | Content Lifespan |
|----------|------|---------------|-------------------|
| **TikTok** | Primary discovery | Highest supply of nano/micro creators | 2-3 day peak, then dies |
| **YouTube Shorts** | Long-tail discovery | Fewer creators but better organic reach | Content gains views for months |
| **Instagram Reels** | DM sharing + conversion | Strong in lifestyle/aesthetic niches | Medium lifespan, DM-driven |

**Cross-post everything.** Produce once on TikTok, distribute to all three. YouTube Shorts is underinvested — 85-90% of creators report better organic reach vs. TikTok.

### Creator niches ranked by fit

| Rank | Niche | Why | Engagement Rate | Cost (Nano 1K-10K) | Cost (Micro 10K-50K) |
|------|-------|-----|----------------|--------------------|-----------------------|
| 1 | Pet/animal creators | Exact audience overlap. "I turned my dog into an AI pet." | 5%+ | $100-$300 | $200-$800 |
| 2 | Cute/kawaii aesthetic | Audience primed for cute, novel things. "This app turns ANYTHING into the cutest pet." | 4-6% | $100-$400 | $200-$600 |
| 3 | AI/tech "what's new" | Early adopters who download every new AI app. | 3-5% | $150-$500 | $300-$800 |
| 4 | Mom/family | Tamagotchi nostalgia. "I grew up with Tamagotchi, now my kids have THIS." | 3-5% | $100-$400 | $200-$600 |
| 5 | Lifestyle/"things I found" | Discovery audience. "You NEED to download this app." | 3-5% | $100-$400 | $200-$500 |
| 6 | College/Gen Z lifestyle | Highest app adoption rate. Often work for product + small fee ($50-$200). | 4-6% | $50-$200 | $150-$400 |

### Budget allocations by level

#### $500 Budget — Signal Sprint (7-10 days)

| Line Item | Amount | Expected Output |
|-----------|--------|-----------------|
| 2-3 TikTok nano posts ($100-$300 each) | $400-$500 | 2-3 videos, no paid boosting |
| **Total** | **$500** | **Pure signal: which hooks generate "what app is this?" comments** |

No Spark Ads at this tier. Goal is identifying 1-2 hook styles that create organic curiosity, not volume. Track cost per activated user (first scan) and share rate per install.

#### $2K Budget — Proof of Concept

| Line Item | Amount | Expected Output |
|-----------|--------|-----------------|
| 8-10 nano creators (pet + cute niches) | $1,200 | 8-10 videos, 16K-100K total views |
| Spark Ads boost on top 2 performing videos | $500 | 50K-200K additional views |
| Apple Search Ads (brand defense) | $300 | 60-100 installs from high-intent searches |
| **Total** | **$2,000** | **1,000-4,000 installs at $0.50-$2.00 CPI** |

#### $5K Budget — Validated Playbook

| Line Item | Amount | Expected Output |
|-----------|--------|-----------------|
| 15 nano creators across 3 niches | $2,000 | 15 videos, test 3 content angles |
| 5 micro creators (10K-50K, pet + lifestyle) | $1,500 | 5 high-reach videos, 50K-250K views each |
| Spark Ads on top 3-5 performers | $1,000 | 100K-500K additional views |
| Apple Search Ads | $500 | 100-170 installs |
| **Total** | **$5,000** | **3,000-10,000 installs at $0.50-$1.65 CPI** |

#### $10K Budget — Scaling Engine

| Line Item | Amount | Expected Output |
|-----------|--------|-----------------|
| 20 nano creators across 4 niches | $2,500 | 20 videos, broad content testing |
| 10 micro creators (pet + cute + AI + lifestyle) | $3,000 | 10 high-reach videos |
| 2 mid-tier creators (50K-100K, pet niche) | $1,500 | 2 anchor videos, 100K-500K views each |
| Spark Ads on top 5-8 performers | $2,000 | 200K-1M additional views |
| Apple Search Ads | $1,000 | 200-330 installs |
| **Total** | **$10,000** | **8,000-25,000 installs at $0.40-$1.25 CPI** |

### Spark Ads strategy

Spark Ads are TikTok's format for boosting organic creator posts as paid ads. The ad runs FROM the creator's handle, looking like native content with a small "Sponsored" label. This is the highest-ROI paid format available.

**Official docs:**
- [About Spark Ads](https://ads.tiktok.com/help/article/spark-ads)
- [Creation guide](https://ads.tiktok.com/help/article/spark-ads-creation-guide)
- [Creative playbook](https://ads.tiktok.com/business/creativecenter/quicktok/online/Spark-Ads-Creative-Playbook/pc/en)

| Metric | Traditional TikTok Ads | Spark Ads |
|--------|----------------------|-----------|
| Completion rate | Baseline | **142% higher** |
| Engagement rate | Baseline | **+43%** |
| CPA (cost per acquisition) | Baseline | **37% lower** |
| CVR (conversion rate) | Baseline | **+30%** |

**The Spark Ads workflow:**
1. Pay creators to post organic content about Zerocap on their own feeds
2. Wait 24-48 hours to identify which videos get organic traction (views, engagement, saves)
3. Request Spark Ads authorization code from winning creators (they generate a code in TikTok, no extra cost)
4. Boost the winners as paid ads through TikTok Ads Manager
5. Budget split: 30% test budget (many creators), 70% scale budget (boost winners)

**Why this matters:** You're not guessing which content will perform. You're letting the algorithm identify winners organically, then pouring fuel on what's already working. This is why Spark Ads deliver 37% lower CPA — you're only scaling proven content.

**Spark Ads case studies (from GPT deep research):**
| App | Result | Method |
|-----|--------|--------|
| **Jodel** (social app) | **85,644 installs at 2.29 CPI** | 60+ micro-influencers + Spark Ads, scaled to 196K spend |
| **LuckyTrip** (travel app) | **85K downloads, 4M impressions in 3 weeks** | Spark Ads using organic creator posts |
| **Endel** (soundscape app) | **$3 CPI via Spark vs $7 non-Spark** (2.3x efficiency) | Spark Ads on creator content |
| **Dyme** (finance app) | **+70% CTR, +30% ROAS, -20% CPC** | Spark Ads + UGC creators, became lowest CPI platform |

These confirm the "creator post, then boost winners" system works across categories. Jodel is the closest comp to Zerocap's scale ambitions.

### Top 5 content concepts for creators

| # | Concept | Hook | Why It Works |
|---|---------|------|-------------|
| 1 | **"What my [object] turned into"** | "I pointed my phone at my coffee mug and..." | Curiosity + reveal + cute result. The before/after IS the content. TikTok completion bait. |
| 2 | **"Turning everything in my room into pets"** | "POV: every object in your room becomes alive" | Series potential, completionist appeal, satisfying compilation. Multiple videos from one concept. |
| 3 | **"AI Tamagotchi in 2026"** | "Remember Tamagotchi? This is what they look like now" | Nostalgia hook + tech wow factor. 68% of Gen Z respond positively to nostalgia brands. |
| 4 | **"My pet's personality is INSANE"** | "My water bottle pet is somehow an introvert who loves jazz" | The 6M trait combinations create unexpected, funny combos worth sharing. Personality = shareability. |
| 5 | **"My pet collection after 1 week"** | "I've been collecting AI pets, here's my zoo" | Drives ongoing content, shows depth beyond first scan, proves stickiness. |
| 6 | **"If this becomes cute I'll keep it forever"** | Creator skepticism → scan → surprise → naming moment | Skepticism-to-delight arc. High completion rate. |
| 7 | **"Turning my coffee into a pet was a mistake"** | Comedic regret → coffee object → demanding pet | Humor-driven. Food objects = inherently viral. |
| 8 | **"My boyfriend picked the object... I got the pet"** | Relationship dynamic → surprise → naming argument | Relationship content. Tag-a-friend CTA. |
| 9 | **"Rare pet hunt: scanning 5 things for a legendary"** | Gamified quest → rapid scans → ranking | Collection/rarity angle. Series potential. |
| 10 | **"The pet's personality test is... too accurate"** | Trait overlay → creator reacting to accuracy | Identity/personality quiz format. Highest share impulse. |

### Expected CPI benchmarks

| Method | CPI Range | Basis |
|--------|-----------|-------|
| Nano influencer (organic post only) | $1-$5 | Benchmarked against similar AI/consumer app campaigns |
| Nano influencer + Spark Ads boost | $0.50-$3 | Spark Ads reduce CPA by 37% |
| Micro influencer (organic post only) | $2-$8 | Higher reach but lower engagement rate |
| Micro influencer + Spark Ads boost | $1-$5 | Best balance of reach and efficiency |
| Apple Search Ads (brand terms) | $3-$5 | High intent, low volume |
| Blended CPI target | **$1-$3** | Weighted average across all paid channels |

### Finding creators: the toolkit

| Platform | Cost | Best For | Notes |
|----------|------|----------|-------|
| **TikTok Creator Marketplace (TTCM)** | Free | Finding TikTok creators by niche, engagement, demographics | 100% of budget goes to creators, no platform fee. First choice. |
| **Collabstr** | $0 subscription | Browsing and filtering creators across platforms | Pay per booking, no subscription required. Good for nano creators. |
| **Heepsy** | $89/month | Bulk creator discovery and audience analysis | Worth it at $5K+ budgets for finding 20+ creators efficiently. |
| **Manual TikTok search** | Free | Finding authentically relevant creators | Search hashtags: #aipets, #tamagotchi, #cutepets, #aifilter, #virtualpet. Time-intensive but highest quality matches. |
| **Modash** | $299/month | Audience vetting, fake follower detection, overlap analysis | Worth it at $5K+ budgets for data-driven creator selection |

### Creator pipeline daily cadence (from GPT deep research)

For a 4-person team running influencer as primary channel:

| Activity | Daily Target |
|----------|-------------|
| New creator prospects sourced | 25-40 |
| Outreaches sent (DM + email) | 10-15 |
| Deals signed per week | 2-4 |
| Posts live per week | 5-15 (depends on budget) |

**DM template that gets replies (15-25% response rate):**
> "Hey [Name] -- your [specific video reference] was fire. I'm building Zerocap: point camera at any object and it becomes a cute living pet. We're paying creators for 1 native post (15-30s). You'd film your own 'scan to pet reveal' with any object you choose. Budget: $[X-Y]. Want me to send the 1-page brief?"

Key: reference a specific video of theirs. Generic pitches get <5% response.

---

## Retention Strategy

### The Lensa problem (and how Zerocap solves it)

Every camera transformation app crashes after the initial viral wave because the core action is one-time: take photo, get output, share it, done. There's no reason to open the app again.

| App | Peak | Crash | Why |
|-----|------|-------|-----|
| Lensa AI | 19.3M downloads/month | 1.4M next month | One-time avatar generation, no retention loop |
| Prisma | 7.5M downloads/week | Rapid decline | Filter applied, photo shared, done |
| FaceApp | Massive viral spikes | Returns to baseline | Aging/de-aging is a single curiosity |

Zerocap's structural answer: the transformation is the beginning, not the end. After the scan, you have a living pet with needs, personality, and evolution potential. The camera moment drives acquisition; the pet relationship drives retention.

### The care obligation loop

Zerocap's daily retention engine, modeled on Tamagotchi's 30-year-proven mechanic:

| Need | Decay Rate | Return Trigger | Time Investment |
|------|-----------|----------------|-----------------|
| Hunger | Decays over 4-6 real hours | Push notification: "Your pet is hungry" | 10-30 seconds |
| Happiness | Decays over 6-8 real hours | Push notification: "Your pet misses you" | 1-3 minutes (mini-game or interaction) |
| Cleanliness | Decays over 8-12 hours | Visual cue (pet looks dirty/sad) | 10-20 seconds |
| Personality expression | Continuous | Curiosity: "What's my pet doing?" | Variable |

**Critical design principle:** Needs operate on real-world time, not play-time. Your pet gets hungry whether you open the app or not. This is what transforms a toy into a responsibility — and responsibility drives daily returns.

**Object-origin personalization:** A pet born from a coffee mug gets "thirsty" faster. A pet from a running shoe needs more "exercise." This ties the care loop to the creation origin — a mechanic no other virtual pet has.

### Evolution system

Evolution gives users a long-term reason to stay. Without it, the pet is static and boring by week two.

**Proposed evolution model:**
- 4 life stages: baby (day 0-2) → child (day 3-7) → teen (day 8-21) → adult (day 22+)
- Care quality determines evolution path (good care → rare/beautiful forms, neglect → common forms)
- Object origin influences evolution options (pet from a plant → nature-themed evolutions)
- Hidden evolution conditions create a meta-game of discovery

**Why this works:** Tamagotchi's branching evolution tree (100+ adult forms) created dedicated communities of players trying to unlock specific evolutions. The uncertainty of "what will my pet become?" is a powerful D7-D30 retention driver.

### First 90 seconds: onboarding flow

| Second | Action | Principle |
|--------|--------|-----------|
| 0-5 | App opens directly to camera | Zero splash screens, zero tutorials |
| 5-15 | User points at object, taps to scan | One-tap interaction, auto-framing |
| 15-30 | AI processing with engaging animation | Show personality traits generating in real-time |
| 30-50 | Pet appears with dramatic reveal | The "wow" moment — make it cinematic |
| 50-70 | Name your pet + see first personality trait | Emotional investment begins with naming |
| 70-85 | First interaction (feed or play) | Demonstrate the care loop immediately |
| 85-90 | Share prompt with pre-generated video | "Show your friends what you made" — one tap to TikTok/Instagram |

**The rule:** Every second past 90 without the user seeing their first pet is retention lost. Lensa's 10-20 selfie upload requirement worked because the payoff was dramatic enough. Zerocap's payoff (a living pet from a random object) is even more dramatic — don't bury it behind setup.

### Retention targets

| Metric | Conservative | Base | Optimistic | Benchmark Source |
|--------|-------------|------|-----------|------------------|
| D1 retention | 30% | 40% | 50% | Virtual pet avg: 28-32%, AI companion avg: 30-40% |
| D7 retention | 12% | 18% | 28% | Virtual pet good: 15-25%, AI companion good: 25-40% |
| D30 retention | 5% | 10% | 18% | Virtual pet good: 8-15%, critical for unit economics |
| DAU/MAU | 15% | 25% | 35% | 20-30% = "good," 30%+ = investors pay attention |
| Sessions/day | 2 | 3-4 | 5+ | Care cycle drives 3-5 micro-sessions (Tamagotchi model) |
| Avg session length | 2 min | 4 min | 8 min | Short sessions OK if frequent (care loop) |

### AI conversation as retention layer

Personality-driven conversation using Apple Foundation Models (on-device, $0 marginal cost):

- Each pet has personality traits that shape how it "talks" (6M trait combinations = every conversation feels unique)
- Conversation references the pet's object origin ("As a former coffee mug, I have opinions about tea...")
- Memory of past interactions creates deepening relationship over time
- On-device processing means conversations are instant, private, and free at scale
- This is the mechanic that pushes DAU/MAU from "camera app" territory (10-20%) toward "AI companion" territory (30-40%)

---

## Monetization Recommendation

### The golden rule: never gate camera-to-pet

The camera transformation is the viral engine. Every gated scan is a lost share, a lost TikTok video, a lost download from a friend. Peridot gated breeding (core loop) and died. Pou kept everything accessible and hit 1.1B downloads.

### Recommended model: hybrid subscription + cosmetic IAP

| Tier | Price | What's Included |
|------|-------|-----------------|
| **Free** | $0 | 3 lifetime pet creations, basic care mechanics, basic cosmetics, AI conversation (on-device) |
| **Zerocap Plus** | $6.99/month ($49.99/year) | Unlimited pet creations, premium evolutions, advanced personality traits, terrain modification, ad removal |
| **Cosmetic IAP** | $0.99-$9.99 | Hats, outfits, accessories, habitat themes, premium skins. Never gameplay-affecting. |

### Why $6.99/month

| Data Point | Source |
|-----------|--------|
| Replika charges $19.99/mo with 25% conversion — proves emotional attachment supports premium pricing | Replika revenue data |
| Character.AI charges $9.99/mo — accessible for Gen Z core demo | Character.AI pricing |
| My Tamagotchi Forever charges $4.99/mo — casual pet audience price point | Bandai Namco pricing |
| $6.99 sits between "casual pet app" and "AI companion" — matches Zerocap's hybrid positioning | Pricing benchmark analysis |
| 7-day free trial is industry standard — lets users experience the care loop before committing | Subscription best practices |

### Free tier economics

| Metric | Value | Notes |
|--------|-------|-------|
| Cost per free user (monthly) | $0.05-$0.15 | 3 lifetime pet creations = one-time cloud cost (~$0.45 total), on-device conversation = $0 |
| Ad revenue per free user (monthly) | $0.50-$2.00 | Opt-in rewarded video ads (extra food, cosmetic unlocks) |
| Free-to-paid conversion target | 5-8% | Replika achieves 25% (exceptional), Character.AI ~3-5%, industry avg 2-5% |
| Monthly ARPU (blended) | $0.80-$1.50 | At scale with 5-8% conversion, ads on free tier |

### Why hybrid beats subscription-only

- **Subscription** handles recurring AI inference costs and provides predictable revenue
- **Cosmetic IAP** captures impulse purchases and whale spending (Fortnite: $9.1B from cosmetics alone)
- **Ads** serve as free-tier monetization — removable via subscription
- Hybrid models reach $9.69 D90 ARPU vs. $7.31 for IAP-only (industry benchmark)

### What to NEVER monetize

- Camera-to-pet transformation (core viral mechanic)
- Basic pet care (feeding, playing — the retention loop)
- AI conversation (on-device, $0 cost — this is the stickiness layer)
- Sharing/export (every gate on sharing kills a potential viral share)

---

## Accelerator Positioning

### Speedrun (a16z Games)

**Lead with:** Game identity. Zerocap is a companion game where the real world is your content pipeline. Every physical object becomes a unique creature with personality, emotions, and the ability to modify terrain in a persistent voxel world.

**The 10-second demo:** Point camera at shoe → living pet shoe with unique personality → it modifies terrain in Spacezero's voxel world. That's a demo, not a pitch.

**Thesis alignment:**
- a16z Big Ideas 2026: complex infrastructure (dual-contouring engine + multimodal AI pipeline), unstructured multimodal data (photo → voxel asset), AI-native design, novel distribution
- Portfolio comp: Nilo (browser-based AI-native 3D sandbox, $4M Supercell seed) — same thesis, different surface
- Born/Pengu ($15M Series A from Accel + Tencent, 15M users) — validates the AI pet companion category, Zerocap differentiates on camera input

**What not to say:** "AI app that turns photos into cute pets" (sounds like an AI wrapper). Say: "AI companion game with 6M unique creatures generated from the real world."

### YC

**Lead with:** Consumer AI with retention. The camera-to-pet loop drives acquisition (every share is a TikTok video). The care obligation loop drives retention (your pet needs you daily). Unit economics work because conversation is on-device ($0) and creation is cloud ($0.15/pet).

**Traction targets for application:**
- 5K-10K downloads
- D7 retention > 15%
- DAU/MAU > 20%
- Week-over-week growth > 10%

### a16z Big Ideas 2026 alignment

| Big Idea | How Zerocap Maps |
|----------|-----------------|
| Complex infrastructure | Dual-contouring voxel engine + multimodal AI pipeline (image understanding → 3D generation → personality generation) |
| Unstructured multimodal data | Real-world photos → structured 3D assets with personality metadata |
| AI-native design | The game mechanic IS AI — remove AI and the product doesn't exist |
| Novel distribution | Camera-as-character-creator, every creation is a shareable TikTok video, cross-platform iOS → browser |
| Deep personalization | 6M trait combinations, object-origin personality, AI conversation memory |

---

## Execution Calendar

### Phase 1: Pre-Launch Foundation (Weeks 1-3)

| Action | Owner | Outcome |
|--------|-------|---------|
| Ship onboarding flow: camera → pet in <90 seconds | Engineering | Core product ready |
| Build share artifact: auto-generated TikTok-ready before/after video | Engineering | Viral loop enabled |
| Implement care mechanics: hunger, happiness, push notifications | Engineering | D1 retention mechanics live |
| App Store optimization: Games > Simulation, keywords, screenshots, App Preview Video | Marketing | Organic discovery baseline |
| Set up TikTok account (creator account, @zerocap + meme account) | Marketing | Two-account strategy ready |
| Build creator outreach list: 50-100 nano creators in pet/cute/AI niches | Marketing | Outreach pipeline ready |
| Set up analytics: installs, retention (D1/D7/D30), sessions, share rate | Engineering | Measurement infrastructure |
| Create Discord server (5-8 channels, minimal) | Marketing | Community infrastructure |

### Phase 2: Soft Launch + First Influencer Wave (Weeks 4-6)

| Action | Owner | Outcome |
|--------|-------|---------|
| TestFlight to 50 nano creators with free access (product seeding, $0) | Marketing | 10-20 post organically without payment |
| First paid influencer wave: 8-10 nano creators ($1,200) | Marketing | 8-10 videos, test content angles and hooks |
| Begin daily TikTok/YouTube Shorts organic posting (1-2x/day) | Marketing | Account warmup, format testing |
| Reddit seeding: r/tamagotchi, r/virtualepets, r/iosapps | Marketing | Community credibility building |
| Collect D1/D7 retention data from soft launch cohort | Analytics | First retention signal |
| Identify top 2-3 performing creator videos | Analytics | Spark Ads candidates |
| Launch Spark Ads on winning videos ($500) | Marketing | Amplify proven content |

### Phase 3: Launch + Scale (Weeks 7-10)

| Action | Owner | Outcome |
|--------|-------|---------|
| App Store launch (if not already live) | Engineering | Public availability |
| Product Hunt launch (Tuesday) | Marketing | 200-500 downloads, press signal |
| Second influencer wave: 15-20 creators (nano + micro, $2,500-$3,500) | Marketing | Broad content coverage, multiple niches tested |
| Spark Ads scale budget on top performers ($1,000-$2,000) | Marketing | High-efficiency paid growth |
| Apple Search Ads launch (brand + competitor terms, $500-$1,000) | Marketing | High-intent capture |
| Ship evolution system (v1) | Engineering | D7-D30 retention boost |
| Press/blog outreach: 20 tech/app publications | Marketing | Credibility + download spikes |
| Discord community events (pet sharing contests, weekly themes) | Marketing | Community retention |

### Phase 4: Optimize + Expand (Weeks 11-16)

| Action | Owner | Outcome |
|--------|-------|---------|
| Analyze full funnel: which creator niche, hook format, and CTA converts best | Analytics | Playbook crystallized |
| Scale winning influencer formula to $5K-$10K/month | Marketing | Predictable paid growth engine |
| International expansion research (Japan/Korea priority per market analysis) | Strategy | Next growth market identified |
| Brand partnership outreach (food brands, fashion — "scan your snack/shoes") | Partnerships | Revenue-positive marketing |
| Ship cross-platform persistence (Zerocap pets → Spacezero voxel world) | Engineering | Unique retention differentiator |
| Accelerator applications (Speedrun, YC) with traction data | Strategy | Fundraising pipeline |
| Subscription/monetization launch (Zerocap Plus $6.99/mo) | Product | Revenue generation begins |

---

## Budget Breakdown

### $2K Budget — "Prove the loop works"

| Category | Amount | % |
|----------|--------|---|
| Paid influencers (8-10 nano creators) | $1,200 | 60% |
| Spark Ads (boost top 2 performers) | $500 | 25% |
| Apple Search Ads (brand defense) | $300 | 15% |
| **Total** | **$2,000** | **100%** |

**Expected outcome:** 1,000-4,000 installs. Learn which creator niche and content angle converts. Get first D7 retention data from paid cohort. CPI: $0.50-$2.00.

### $5K Budget — "Validate and begin scaling"

| Category | Amount | % |
|----------|--------|---|
| Paid influencers (20 creators: 15 nano + 5 micro) | $3,500 | 70% |
| Spark Ads (boost top 3-5 performers) | $1,000 | 20% |
| Apple Search Ads | $500 | 10% |
| **Total** | **$5,000** | **100%** |

**Expected outcome:** 3,000-10,000 installs. Three content angles tested across three niches. Spark Ads playbook validated. CPI: $0.50-$1.65.

### $10K Budget — "Scale the winning formula"

| Category | Amount | % |
|----------|--------|---|
| Paid influencers (32 creators: 20 nano + 10 micro + 2 mid-tier) | $7,000 | 70% |
| Spark Ads (boost top 5-8 performers) | $2,000 | 20% |
| Apple Search Ads | $1,000 | 10% |
| **Total** | **$10,000** | **100%** |

**Expected outcome:** 8,000-25,000 installs. Full niche coverage. Mid-tier creator content as anchor. Predictable CPI at $0.40-$1.25. Ready to raise or scale further.

---

## Metrics Targets

### Core metrics (12-week targets)

| Metric | Conservative | Base | Optimistic |
|--------|-------------|------|-----------|
| Total downloads | 5,000 | 15,000 | 40,000+ |
| D1 retention | 30% | 40% | 50% |
| D7 retention | 12% | 18% | 28% |
| D30 retention | 5% | 10% | 18% |
| DAU/MAU | 15% | 25% | 35% |
| Share rate (% who share first pet) | 10% | 20% | 35% |
| K-factor (viral coefficient) | 0.15 | 0.30 | 0.50 |
| Blended CPI (paid channels) | $2.00 | $1.25 | $0.50 |
| Sessions per DAU | 2 | 3-4 | 5+ |
| Avg session length | 2 min | 4 min | 8 min |

### Growth milestones

| Milestone | Conservative | Base | Optimistic |
|-----------|-------------|------|-----------|
| 1,000 downloads | Week 5 | Week 3 | Week 2 |
| 5,000 downloads | Week 10 | Week 6 | Week 4 |
| 10,000 downloads | Week 14+ | Week 9 | Week 6 |
| 25,000 downloads | — | Week 14 | Week 9 |
| First viral video (100K+ views) | May not happen | Week 6-8 | Week 3-4 |

### Unit economics targets (at scale)

| Metric | Target | Notes |
|--------|--------|-------|
| Blended CPI | <$2.00 | Must be lower than LTV |
| LTV (12-month, blended) | $3-$8 | At 5-8% conversion, $6.99/mo sub + cosmetic IAP + ads |
| LTV:CAC ratio | >3:1 | Minimum for sustainable paid growth |
| Monthly AI cost per user | $0.10-$0.50 | Hybrid architecture (cloud creation + on-device conversation) |
| Payback period | <60 days | Free-tier ad revenue covers some cost immediately |

---

## Research Files Index

| # | File | One-Line Summary |
|---|------|-----------------|
| 1 | `research/accelerator-positioning.md` | Speedrun/YC/a16z positioning strategy, application narratives, portfolio comps |
| 2 | `research/ai-companion-market-deep-dive.md` | $120M+ market, 31% CAGR, competitor funding landscape, regulatory overview |
| 3 | `research/ai-cost-modeling.md` | $0.15/pet creation cost, hybrid architecture saves 50-70%, scaling economics to 1M users |
| 4 | `research/app-store-ranking-strategy.md` | Games > Simulation primary category, keyword strategy, Apple Search Ads benchmarks |
| 5 | `research/ar-camera-app-virality.md` | Pokemon GO, FaceApp, Lensa case studies; transformation reveal as viral mechanic |
| 6 | `research/brand-partnership-opportunities.md` | Food/fashion/IP partnership frameworks and pitch templates |
| 7 | `research/community-building-playbook.md` | Discord/Reddit/TikTok community strategy, founding member effect, growth tactics |
| 8 | `research/comparable-company-case-studies.md` | Pou (1B downloads), Peridot ($4.1M failure), Born (15M users), Momo (a16z Speedrun) |
| 9 | `research/competitive-landscape-market-map.md` | No competitor combines camera + AI pet + personality + terrain mod + voxel world |
| 10 | `research/creator-brief-templates.md` | Brief anatomy, 5 content concepts with templates, ready-to-send briefs |
| 11 | `research/creator-finding-targeting.md` | Creator niches, manual finding methods, vetting criteria, outreach scripts |
| 12 | `research/cross-platform-strategy.md` | Zerocap (iOS) to Spacezero (browser) companion persistence architecture |
| 13 | `research/deep-research-prompts.md` | Prompts used to generate research across Claude, ChatGPT, and Gemini |
| 14 | `research/discord-gtm-other-servers.md` | Strategy for engaging on 50+ relevant Discord servers for organic growth |
| 15 | `research/discord-own-server-strategy.md` | Server setup, growth from 0 members, engagement mechanics, bot configuration |
| 16 | `research/discord-server-targeting-list.md` | 54 Discord servers with member counts, relevance scores, approach strategies |
| 17 | `research/influencer-campaign-case-studies.md` | 15 campaign case studies (Lensa, Remini, Chai, Duolingo), Spark Ads performance data |
| 18 | `research/influencer-marketplace-comparison.md` | 15 platforms compared; top 3: TTCM (free), Collabstr ($0 sub), Heepsy ($89/mo) |
| 19 | `research/international-market-analysis.md` | US first, then Japan/Korea, then Southeast Asia — market sizing and entry strategy |
| 20 | `research/monetization-strategies.md` | Cosmetics, subscriptions, IAP, ad-supported tiers, pricing psychology deep dive |
| 21 | `research/paid-influencer-marketing.md` | Full paid workflow, pricing by tier ($20-$800/video), CPI benchmarks, FTC compliance |
| 22 | `research/pricing-subscription-benchmarks.md` | $6.99/mo recommended, competitor pricing, 7-day trial, conversion benchmarks |
| 23 | `research/product-hunt-show-hn-launch.md` | Product Hunt Tuesday launch, Show HN technical framing, launch day sequencing |
| 24 | `research/reddit-gtm-strategy.md` | Own subreddit + 30 target subreddits, Reddit ads at $0.50-$2 CPC |
| 25 | `research/retention-engagement-mechanics.md` | Daily loop design, care cycles, evolution systems, first 90 seconds, streak mechanics |
| 26 | `research/spark-ads-whitelisting-strategy.md` | Spark Ads 142% higher engagement, 37% lower CPA, full setup guide, budget splits |
| 27 | `research/target-demographics.md` | Gen Z 16-24 (core), millennial 25-32 (monetization engine), Gen Alpha (growth) |
| 28 | `research/terrain-modification-positioning.md` | "Pet that changes your world" differentiator, Pokopia comparison |
| 29 | `research/traction-metrics-benchmarks.md` | D1/D7/D30 targets by category, DAU/MAU 20-30% good, session benchmarks |
| 30 | `research/user-psychology-emotional-design.md` | Parasocial relationships, Tamagotchi effect, creation bond psychology |
| 31 | `research/viral-loop-design.md` | K-factor 0.30-0.50 target, share artifact design, TikTok-native virality blueprint |

**Deep research reports (GPT + Gemini):**

| # | File | One-Line Summary |
|---|------|-----------------|
| 32 | `research/2026-03-13-gpt-market-deep-research.md` | GPT: $221M AI companion spend, competitor table with funding/users, AI cost modeling, regulatory landscape |
| 33 | `research/2026-03-13-gpt-gtm-deep-research.md` | GPT: Influencer workflow, Jodel/LuckyTrip/Endel case studies, daily pipeline cadence, 10 creator concepts |
| 34 | `research/2026-03-13-gemini-market-deep-research.md` | Gemini: Retention benchmarks, $28B TAM, psychology research citations, international markets |
| 35 | `research/2026-03-13-gemini-gtm-deep-research.md` | Gemini: 14-platform marketplace comparison, Spark Ads workflow, community/Discord GTM, accelerator positioning |

**TikTok GTM files (separate directory):**

| # | File | One-Line Summary |
|---|------|-----------------|
| 36 | `tiktok-gtm/strategy.md` | Master plan for 10M views: two-account strategy, platform priority, content types |
| 37 | `tiktok-gtm/research/zerocap-growth-strategies.md` | Virtual pet case studies, AI pet landscape, photo-to-X virality, $0 growth playbook |

---

## The Bottom Line

Zerocap is the first product to combine the two most proven growth mechanics in consumer mobile: photo transformation virality (Lensa: $50M+ revenue, Ghibli filter: 700M images/week) and virtual pet emotional attachment (Tamagotchi: 100M units, Pou: 1.1B downloads). The camera-to-pet transformation IS a TikTok video — every share is a free ad featuring the internet's highest-engagement content category (pet content: 64% rewatch rate, 5%+ engagement).

The primary GTM channel is paid influencer marketing on TikTok. Start with 10 nano creators at $1,200. Wait for data. Identify which content angle and creator niche converts. Boost winners with Spark Ads (142% higher completion rate, 37% lower CPA). Scale the winning formula. At $10K budget, you're looking at 8,000-25,000 installs at $0.40-$1.25 CPI.

The retention answer is the pet itself. Camera transformation apps crash because the output is static (an image you post once). Zerocap's output is a living pet with needs, personality, and evolution. The care loop (hunger, happiness, personality quirks on real-world time) is what turns a novelty camera app into a daily habit. Never gate the camera scan. Never gate basic care. Monetize through $6.99/mo subscription (unlimited pets, premium evolutions) and cosmetic IAP.

The accelerator story writes itself: point camera at shoe, get living pet shoe with personality, watch it modify terrain in a persistent voxel world. That's a 10-second demo, not a 10-minute pitch. No other AI companion app starts with the user's physical reality, and no other camera app produces a companion you keep.

One sobering reality: Appfigures shows the top 10% of AI companion apps capture 89% of revenue. Only 33 apps have passed $1M lifetime. This is winner-take-most. But Finch proves the "pet you care about" model works at $1.75M/month revenue, and Jodel proves the "micro-influencers + Spark Ads" system works at 85K installs for 2.29 CPI.

You need 10 good creators, one good Spark Ad, and a pet that makes people open the app because it's hungry.
