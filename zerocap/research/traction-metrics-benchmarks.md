# Traction Metrics Benchmarks for AI Companion / Virtual Pet Apps

Research date: 2026-03-13
Product context: Zerocap -- an iOS AI tamagotchi app where you point your camera at real objects and AI transforms them into living pets.

---

## Table of Contents

1. [DAU/MAU Ratios](#1-daumau-ratios-stickiness)
2. [Retention Benchmarks by Category](#2-retention-benchmarks-d1-d7-d14-d30-d90)
3. [Session Length and Sessions Per Day](#3-session-length-and-sessions-per-day)
4. [Time to First Value](#4-time-to-first-value)
5. [Download to Active User Conversion](#5-download-to-active-user-conversion)
6. [Organic vs Paid Installs](#6-organic-vs-paid-install-benchmarks)
7. [App Store Rating Benchmarks](#7-app-store-rating-benchmarks)
8. [Viral Coefficient (K-Factor)](#8-viral-coefficient-k-factor)
9. [Revenue Per User](#9-revenue-per-user-benchmarks)
10. [Growth Rate Benchmarks](#10-growth-rate-benchmarks)
11. [What Good Traction Looks Like by Stage](#11-what-good-traction-looks-like-by-stage)
12. [Case Studies: Successful Companion/Pet Apps](#12-case-studies)
13. [Presenting Traction to Accelerators](#13-presenting-traction-to-accelerators)
14. [Vanity Metrics vs Real Metrics](#14-vanity-metrics-vs-real-metrics)
15. [Zerocap-Specific Targets](#15-zerocap-specific-targets)

---

## 1. DAU/MAU Ratios (Stickiness)

DAU/MAU measures what fraction of your monthly users come back on any given day. It is the single best proxy for "stickiness" -- whether your app is a daily habit or an occasional curiosity.

### Benchmarks by Category

| Category | DAU/MAU | Interpretation |
|----------|---------|----------------|
| Social messaging (WhatsApp, iMessage) | 50-70% | Daily utility |
| Social media (Instagram, TikTok) | 40-60% | Daily entertainment habit |
| **AI companion apps (Character.AI)** | **41-45%** | **Emotionally sticky, daily check-in** |
| Gaming (mobile) | 20-40% | Depends on core loop strength |
| Entertainment | 15-25% | Content consumption cadence |
| Lifestyle / utilities | 10-25% | Use-case dependent |
| E-commerce / marketplaces | 10-20% | Purchase cadence limited |

### What the Numbers Mean for Zerocap

| Tier | DAU/MAU | What It Signals |
|------|---------|-----------------|
| Poor | <10% | App is not forming a habit. Users forget it exists |
| Below average | 10-20% | Some interest but no daily pull. Retention will bleed |
| **Good** | **20-30%** | **Users are coming back regularly. Solid for a new app** |
| **Great** | **30-40%** | **Daily habit forming. Investors pay attention** |
| **Exceptional** | **40%+** | **Character.AI territory. You've built an emotional bond** |

**Key reference point**: Character.AI achieved 41-45% DAU/MAU -- the highest among AI-first companies. This is because companion apps create emotional attachment that drives daily check-ins. Zerocap's pet mechanic should target similar emotional gravity.

**Why this matters for Zerocap**: A camera-based pet creation app has a natural tension -- the creation moment is exciting but one-time. The DAU/MAU ratio will reveal whether your pet care / feeding / evolution loop is strong enough to pull users back daily. If DAU/MAU is below 20%, the core loop needs work. If it's above 30%, you've found something.

### Sources
- [a16z State of Consumer AI 2025](https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/)
- [CleverTap DAU vs MAU](https://clevertap.com/blog/dau-vs-mau-app-stickiness-metrics/)
- [Guru Startups DAU/MAU Benchmarks](https://www.gurustartups.com/reports/dau-mau-ratio-benchmarks-for-startups)

---

## 2. Retention Benchmarks (D1, D7, D14, D30, D90)

Retention is the metric investors care about most after revenue. It answers the fundamental question: do people come back?

### Industry-Wide Benchmarks (All Apps)

| Timeframe | Median (All Apps) | Top Quartile | Top 10% |
|-----------|-------------------|--------------|---------|
| D1 | 22-25% | 35% | 40%+ |
| D7 | 5-11% | 15-20% | 25%+ |
| D14 | 3-7% | 10-15% | 18%+ |
| D30 | 3-6% | 8-12% | 15%+ |
| D90 | 1-3% | 5-8% | 10%+ |

### Retention by Category (Most Relevant to Zerocap)

#### Virtual Pet Apps

| Timeframe | Below Average | Average | Good | Great |
|-----------|---------------|---------|------|-------|
| D1 | <25% | 25-35% | 35-45% | 45%+ |
| D7 | <8% | 8-15% | 15-25% | 25%+ |
| D14 | <5% | 5-10% | 10-18% | 18%+ |
| D30 | <3% | 3-8% | 8-15% | 15%+ |
| D90 | <1% | 1-4% | 4-8% | 8%+ |

Virtual pet apps have a structural advantage: the pet creates guilt/obligation loops ("my pet is hungry"). The best pet apps achieve retention closer to social apps than games because the emotional bond persists even when gameplay is thin.

#### AI Companion Apps

| Timeframe | Below Average | Average | Good | Great |
|-----------|---------------|---------|------|-------|
| D1 | <30% | 30-40% | 40-50% | 50%+ |
| D7 | <15% | 15-25% | 25-40% | 40%+ |
| D14 | <10% | 10-18% | 18-30% | 30%+ |
| D30 | <8% | 8-15% | 15-25% | 25%+ |
| D90 | <3% | 3-8% | 8-15% | 15%+ |

**Key reference**: Character.AI reported D7 retention of 40% in 2023. Flamme AI (Speedrun applicant) reported 45% D30 bounded retention and used it as a lead metric in their interview.

#### Casual Games (Mobile)

| Timeframe | Median | Good | Great | Top Decile |
|-----------|--------|------|-------|------------|
| D1 | 25-33% | 40%+ | 50%+ | 60%+ |
| D7 | 8-12% | 20%+ | 30%+ | 40%+ |
| D14 | 5-8% | 12%+ | 20%+ | 28%+ |
| D30 | 3-6% | 10%+ | 15%+ | 20%+ |
| D90 | 1-3% | 5%+ | 8%+ | 12%+ |

#### Camera / AR Apps

| Timeframe | Median | Good | Great |
|-----------|--------|------|-------|
| D1 | 18-25% | 30%+ | 40%+ |
| D7 | 4-8% | 12%+ | 20%+ |
| D30 | 2-5% | 7%+ | 12%+ |
| D90 | 1-2% | 3%+ | 6%+ |

Camera/AR apps typically have the worst retention of any category because the novelty wears off fast. Pokemon GO was the exception (massive IP + social + exercise loop). Peridot (Niantic's AR pet game) struggled -- 800K total downloads lifetime, averaging 39 downloads/day recently. **This is the cautionary tale for Zerocap**: AR novelty alone does not retain. The pet relationship and care loop must carry retention after the camera magic fades.

### The Retention Curve Shape Matters

Investors don't just look at the numbers -- they look at the shape:

- **Cliff curve** (steep drop, then flat near zero): Bad. Users try it and leave
- **Gradual decay** (steady decline): Normal. Most apps look like this
- **Flattening curve** (drops then levels off at a stable %): Good. You've found a core audience
- **Smile curve** (drops, then recovers upward): Exceptional. Strongest possible PMF signal. Almost guarantees funding

### Sources
- [GameAnalytics 2025 Mobile Gaming Benchmarks](https://www.gameanalytics.com/reports/2025-mobile-gaming-benchmarks)
- [Pushwoosh Retention Benchmarks 2025](https://www.pushwoosh.com/blog/increase-user-retention-rate/)
- [Plotline Retention Rates by Industry](https://www.plotline.so/blog/retention-rates-mobile-apps-by-industry)
- [MAF Mobile Game Retention Benchmarks](https://maf.ad/en/blog/mobile-game-retention-benchmarks/)
- [Solsten D1 D7 D30 Retention in Gaming](https://solsten.io/blog/d1-d7-d30-retention-in-gaming)
- [Andrew Chen: Losing 80% of Users is Normal](https://andrewchen.com/new-data-shows-why-losing-80-of-your-mobile-users-is-normal-and-that-the-best-apps-do-much-better/)

---

## 3. Session Length and Sessions Per Day

### Session Length Benchmarks

| Category | Median Session | Good | Exceptional |
|----------|---------------|------|-------------|
| Casual games | 4 min | 7 min | 10+ min |
| Mid-core games | 5 min | 8 min | 12+ min |
| **AI companion apps** | **15-17 min** | **30 min** | **60+ min** |
| Social media | 8-12 min | 20 min | 30+ min |
| Camera / photo apps | 2-4 min | 5 min | 8+ min |

**Key reference**: Character.AI users average 17 minutes per session (vs. ChatGPT's 7 minutes). Power users of companion apps average 2 hours per day total. PolyBUZZ averages 69 min/day; Talkie and CHA average 62 min/day each.

### Sessions Per Day

| Category | Median | Good | Exceptional |
|----------|--------|------|-------------|
| Casual games | 3-4 | 5-6 | 7+ |
| Mid-core games | 4-5 | 6-7 | 8+ |
| AI companion apps | 3-5 | 5-7 | 8+ |
| Social media | 5-8 | 10+ | 15+ |
| Camera / photo | 1-2 | 3 | 5+ |

### What This Means for Zerocap

Zerocap sits at the intersection of camera (short sessions) and companion (long sessions). The creation moment is camera-like (2-4 min to scan and create a pet). But the pet care, feeding, and interaction should drive companion-like session lengths (10-15 min). Target:

- **Creation sessions**: 3-5 min (fast, magical, shareable)
- **Care/interaction sessions**: 8-15 min (feeding, playing, watching evolution)
- **Sessions per day**: 3-5 (morning check, lunch break, evening care)
- **Total daily time**: 15-30 min (healthy engagement without burnout)

### Sources
- [Character.AI Statistics](https://electroiq.com/stats/character-ai-statistics/)
- [GameAnalytics Mobile Gaming Benchmarks 2025](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)
- [Netguru Mobile App Engagement Metrics](https://www.netguru.com/blog/mobile-app-user-engagement-metrics)

---

## 4. Time to First Value

Time to First Value (TTFV) is how quickly a new user experiences the "aha moment." For Zerocap, that moment is: **"I pointed my camera at something and it became a living pet."**

### Benchmarks

| Category | Target TTFV | Why |
|----------|-------------|-----|
| Mobile games | <60 seconds to first meaningful action | Longer = churn before core loop |
| AI apps | <60 seconds to first output | ProductLed: "60 seconds to value or you lose them" |
| Camera/AR apps | <30 seconds to first capture | Camera is the instant-gratification medium |
| Virtual pet apps | <2 minutes to first pet interaction | Must feel bonded quickly |
| Social apps | <3 minutes to first connection | Setup friction is tolerated if social payoff is clear |

### Zerocap TTFV Target

**Goal: First pet alive in under 90 seconds from app open.**

Recommended flow:
1. App opens (0s)
2. Skip or minimal onboarding -- 1-2 screens max (10-15s)
3. Camera activates with clear prompt: "Point at something to create your first pet" (20s)
4. User scans an object (30-50s)
5. AI transformation happens -- object becomes a living pet (60-90s)

**Why 90 seconds**: If the first pet takes longer than 2 minutes, you lose the "magic" window. Every additional step between download and first pet is a retention cliff. The best onboarding for this kind of app is **no onboarding** -- just camera, scan, pet.

### The Activation Rate Connection

TTFV directly drives activation rate (% of downloaders who complete the core action):

| TTFV | Typical Activation Rate |
|------|------------------------|
| <30 seconds | 60-80% |
| 30-60 seconds | 45-65% |
| 1-2 minutes | 30-50% |
| 2-5 minutes | 15-35% |
| 5+ minutes | <15% |

### Sources
- [ProductLed AI Onboarding](https://productled.com/blog/ai-onboarding)
- [Stormy AI: Reducing Time to Magic](https://stormy.ai/blog/app-onboarding-best-practices-retention-strategies)
- [Mistplay Mobile Game Retention Benchmarks](https://business.mistplay.com/resources/mobile-game-retention-benchmarks)

---

## 5. Download to Active User Conversion

### App Store Page to Download (Tap Rate)

| Category | Average | Good | Exceptional |
|----------|---------|------|-------------|
| Games (iOS) | 20-25% | 30%+ | 40%+ |
| Non-games (iOS) | 25-30% | 35%+ | 45%+ |
| Games (Android) | 25-30% | 35%+ | 45%+ |

### Download to First Open

Roughly 15-25% of all app downloads are never opened. Industry data suggests:

| Tier | Open Rate | What It Means |
|------|-----------|---------------|
| Poor | <60% | Notifications off, forgotten |
| Average | 70-80% | Normal |
| Good | 80-90% | Clear value prop at download |
| Exceptional | 90%+ | High intent users |

### First Open to Activated User

"Activated" = completed the core value action (for Zerocap: created first pet).

| Category | Average | Good | Exceptional |
|----------|---------|------|-------------|
| Mobile games | 40-60% | 65%+ | 80%+ |
| Camera/AR apps | 30-50% | 55%+ | 70%+ |
| AI apps | 35-55% | 60%+ | 75%+ |

### Full Funnel: Download to Weekly Active User

About 21% of users use an app only a single time. Across the full funnel:

| Step | Typical Conversion |
|------|-------------------|
| Download to first open | 75-85% |
| First open to activation | 40-60% |
| Activation to D1 return | 25-40% |
| D1 return to weekly active | 50-70% |
| **Full funnel: download to WAU** | **~8-15%** |

**For Zerocap's targets**: If 1,000 people download, expect 80-150 to become weekly active users. This means you need significant top-of-funnel volume to build a meaningful WAU base.

### Sources
- [UXCam Mobile App Conversion Rate](https://uxcam.com/blog/mobile-app-conversion-rate/)
- [SplitMetrics App Store Conversion Rate](https://splitmetrics.com/blog/good-app-store-conversion-rate/)
- [Business of Apps Conversion Rates](https://www.businessofapps.com/data/app-conversion-rates/)

---

## 6. Organic vs Paid Install Benchmarks

### Cost Per Install (CPI) by Platform and Category

| Category | iOS CPI | Android CPI |
|----------|---------|-------------|
| Overall average | $4.70 | $3.70 |
| Hyper-casual games | $2.00-3.00 | $1.50-2.50 |
| Casual games | $3.00-5.00 | $2.00-4.00 |
| Simulation games | $4.00-6.00 | $3.00-5.00 |
| AI/companion apps | $3.50-6.00 | $2.50-4.50 |
| AR apps | $4.00-7.00 | $3.00-5.50 |

### Organic vs Paid User Quality

| Metric | Organic Users | Paid Users |
|--------|--------------|------------|
| D1 retention | 30-45% | 20-30% |
| D7 retention | 15-25% | 8-15% |
| D30 retention | 8-18% | 4-10% |
| LTV | 2-3x higher | Baseline |
| Session frequency | 1.5-2x more | Baseline |

**Organic users retain 2-3x better than paid users.** This is why early-stage apps should obsess over organic acquisition channels before spending on paid.

### Organic Uplift Ratio

Paid installs generate additional organic installs through improved rankings and visibility:

| Paid Install Volume | Organic Uplift |
|--------------------|----------------|
| Low (hundreds/day) | 0.3-0.5 organic per paid |
| Medium (thousands/day) | 0.5-1.0 organic per paid |
| High (tens of thousands/day) | 1.0-2.0 organic per paid |

### What Investors Want to See

At pre-seed / early stage, investors strongly prefer to see **organic-dominant acquisition**:

- **Best signal**: 80%+ organic installs (proves product pulls users in without money)
- **Good signal**: 60-80% organic (some paid to test, but organic drives the bus)
- **Yellow flag**: 40-60% organic (are users coming because the product is good, or because you're buying them?)
- **Red flag**: <40% organic (unsustainable unless unit economics are proven)

### Sources
- [Mapendo CPI 2025 Report](https://mapendo.co/blog/cost-per-install-2025-the-ultimate-report-to-grow-your-app-worldwide)
- [Business of Apps CPI Rates](https://www.businessofapps.com/ads/cpi/research/cost-per-install/)
- [Business of Apps Organic Growth](https://www.businessofapps.com/insights/achieving-organic-app-growth-oem-preloads)

---

## 7. App Store Rating Benchmarks

### What Ratings Mean

| Rating | Impact |
|--------|--------|
| <3.0 stars | Invisible. App Store suppresses visibility |
| 3.0-3.5 stars | Below threshold. Sharply reduced search visibility |
| 3.5-4.0 stars | Acceptable but not competitive |
| **4.0-4.5 stars** | **Good. 90% of featured apps are 4.0+** |
| **4.5-5.0 stars** | **Exceptional. Significantly higher conversion rates** |

### Category Averages

| Category | Average Rating |
|----------|---------------|
| Games (iOS) | 4.2 |
| Photo/video (iOS) | 4.3 |
| Entertainment (iOS) | 4.1 |
| AI companion apps | 3.8-4.5 (high variance) |

### Rating Volume Benchmarks

| Stage | Rating Count | Signal |
|-------|-------------|--------|
| First month | 50-200 | Normal for organic launch |
| 3 months | 200-1,000 | Healthy early traction |
| 6 months | 1,000-5,000 | Growing audience |
| 1 year | 5,000+ | Established product |

### Impact on Conversion

- Apps rated 4.0+ convert 3-4x better than apps rated 3.0-3.5 from App Store page views to downloads
- 82% of consumers read reviews before deciding to download
- A drop from 4.5 to 4.0 can reduce conversion by 10-20%

### Zerocap Target

**Launch with 4.5+ stars.** This is achievable at low volume by ensuring the first 50-100 users have a delightful experience. Use in-app prompts to ask happy users to rate (and route unhappy users to a feedback form instead of the App Store).

### Sources
- [AppTweak ASO Trends Benchmarks 2025](https://www.apptweak.com/en/aso-blog/aso-app-store-trends-benchmarks-report)
- [Apple Developer: Ratings and Reviews](https://developer.apple.com/app-store/ratings-and-reviews/)
- [AppFollow Conversion Benchmark](https://appfollow.io/benchmark)

---

## 8. Viral Coefficient (K-Factor)

K-factor = invites per user (i) x conversion rate per invite (c). It measures how many new users each existing user brings in.

### Benchmarks

| K-Factor | Tier | What It Means |
|----------|------|---------------|
| <0.15 | Poor | Almost no organic sharing |
| 0.15-0.25 | Starter target | Realistic for new startups |
| 0.25-0.50 | Good | Meaningful organic amplification |
| 0.50-0.75 | Great | Each 100 paid users bring 50-75 organic |
| 0.75-1.0 | Exceptional | Approaching viral threshold |
| >1.0 | Viral | Exponential growth. Extremely rare |

### Category Context

| Category | Median K-Factor | % of Apps with Measurable K-Factor |
|----------|----------------|-----------------------------------|
| Gaming | ~0.20 | 22.5% |
| Non-gaming | ~0.30 | 33.6% |
| E-commerce | ~0.35 | 38.6% |
| Social/messaging | ~0.40-0.60 | 50%+ |

**The median K-factor across apps with measurable virality is 0.45** -- meaning for every 100 paid installs, 45 additional organic installs come through sharing.

### Zerocap's Viral Advantage

Camera-based pet creation is inherently shareable. The transformation moment ("I scanned my coffee mug and it became a dragon") is a natural short-form video clip. This gives Zerocap structural advantages for virality:

- **Built-in shareable moment**: Every pet creation is a potential TikTok/Instagram clip
- **Visual surprise**: The AI transformation is visually dramatic and unexpected
- **Social comparison**: "What did YOUR object become?" drives organic conversations

**Zerocap K-factor target**: 0.30-0.50 at launch (based on share prompts after pet creation). If the share-to-create flow is frictionless, 0.50+ is realistic.

### Sources
- [Saxifrage K-Factor Benchmarks](https://www.saxifrage.xyz/post/k-factor-benchmarks)
- [Udonis K-Factor for Apps](https://www.blog.udonis.co/mobile-marketing/mobile-games/k-factor)
- [Adjust K-Factor](https://www.adjust.com/blog/measuring-k-factor/)
- [AppSamurai K-Factor Guide](https://appsamurai.com/blog/what-is-k-factor-for-apps-and-how-to-calculate/)

---

## 9. Revenue Per User Benchmarks

### ARPU by Revenue Model

| Model | Blended ARPU (per user/month) | Notes |
|-------|-------------------------------|-------|
| Ad-supported (free) | $0.50-1.00 | All users see ads |
| Freemium (IAP) | $0.50-3.00 | 3-5% convert to paying |
| Subscription | $3.00-9.00 | Higher commitment, higher LTV |
| Hybrid (ads + IAP) | $1.00-4.00 | Most common for games |

### ARPPU (Revenue Per Paying User)

| Category | Median ARPPU/month | Top Quartile |
|----------|-------------------|--------------|
| Casual games | $5-10 | $15-25 |
| AI companion apps | $8-15 | $20-30 |
| Virtual pet apps | $3-8 | $10-15 |
| Camera/photo apps | $4-8 | $10-20 |

### AI Companion App Revenue Context

The AI companion app market is on track to generate $120M+ in 2025:
- 337 active revenue-generating companion apps worldwide
- Revenue per download: $1.18 (up from $0.52 in 2024)
- Top 10% of apps capture 89% of category revenue
- ~33 apps have exceeded $1M lifetime consumer spending

Key revenue examples:
- **Character.AI**: $32.2M annual revenue (2024)
- **Chai AI**: $30M+ ARR with only 12 employees
- **Replika**: $24M annual revenue with 2M MAU

### Freemium Conversion Benchmarks

| Tier | Free-to-Paid Conversion | Notes |
|------|------------------------|-------|
| Poor | <2% | Value prop not clear |
| Average | 3-5% | Industry standard |
| Good | 5-8% | Strong perceived value |
| Exceptional | 8-15% | Compelling premium features |

### Subscription Pricing Sweet Spots

| Price Point | Typical Use |
|-------------|-------------|
| $2.99/month | Impulse subscribe, low commitment |
| $4.99-6.99/month | Most common for casual/companion apps |
| $9.99/month | Premium tier for power users |
| $19.99-29.99/year | Annual discount drives retention |

### What Investors Want at Pre-Seed

Revenue is **not required** at pre-seed for consumer apps. But any revenue signal is powerful:
- Any non-zero MRR with growth: Strong signal
- $1K MRR growing 15%+ MoM: Very strong
- $5K+ MRR: Uncommon at pre-seed, essentially guarantees investor attention
- 7% of YC companies had >$50K MRR when accepted (exceptional outliers)

### Sources
- [TechCrunch: AI Companion Apps $120M](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)
- [RevenueCat State of Subscription Apps 2025](https://www.revenuecat.com/state-of-subscription-apps-2025/)
- [BusinessDojo ARPU Estimation](https://dojobusiness.com/blogs/news/mobile-app-arpu-estimation)
- [AdPushup App Monetization Stats](https://www.adpushup.com/blog/app-monetization-statistics/)

---

## 10. Growth Rate Benchmarks

### Week-Over-Week (WoW) Growth Targets

| WoW Growth | Tier | Who Says So | Annual Multiple |
|------------|------|-------------|-----------------|
| <1% | Not working | Paul Graham | 1.7x |
| 1-2% | Struggling | -- | 1.7-2.8x |
| 2-4% | Getting somewhere | -- | 2.8-7.7x |
| **5-7%** | **Good** | **Paul Graham / YC benchmark** | **12.6-33.7x** |
| **10%** | **Exceptional** | **Paul Graham / YC benchmark** | **142x** |
| 15-20% | Rocketship | Multiple accelerators compete for you | 1,000x+ |

### Month-Over-Month (MoM) Growth

| Stage | Target MoM Growth |
|-------|-------------------|
| Pre-seed | 15-20%+ |
| Seed | 15%+ |
| Series A | 12%+ |
| Growth stage | 8-10%+ |

### What Accelerators (Speedrun / YC) Specifically Want

**a16z Speedrun:**
> "Traction is number one, two, and three, followed by team, and then TAM." -- Josh Lu, GM of Speedrun

- Revenue traction is best, growth traction and retention are second best
- They pour "gasoline on a very small spark" -- you need a spark, not a bonfire
- Acceptance rate: <0.4% (19,000+ applicants for SR006)
- They like seeing velocity: week-over-week growth even over short periods

**Y Combinator:**
- Primary metric: Revenue for paid products, DAU for free products
- Most important secondary metric for consumer: Retention rate
- 40% of companies funded each batch are just an idea (no product)
- 7% had >$50K MRR when accepted

### The Compounding Math

| Weekly Growth | In 4 Weeks | In 12 Weeks | In 26 Weeks |
|--------------|-----------|------------|------------|
| 5% | 1.22x | 1.80x | 3.56x |
| 7% | 1.31x | 2.25x | 5.81x |
| 10% | 1.46x | 3.14x | 11.92x |
| 15% | 1.75x | 5.35x | 37.86x |

This is why investors focus on growth rate over absolute numbers. 100 users at 15% WoW beats 10,000 users at 1% WoW within 6 months.

### Sources
- [Paul Graham: Startup = Growth](https://www.paulgraham.com/growth.html)
- [a16z Speedrun: What We Look For](https://speedrun.substack.com/p/what-we-look-for-in-applications)
- [Speedrun: The 3 Signals That Get Startups In](https://speedrun.substack.com/p/sr005-apps-reviewed-the-3-signals-that-get-startups-in)
- [M Accelerator: Growth Rates Investors Expect](https://maccelerator.la/en/blog/investors/the-growth-rates-investors-expect-a-deep-dive/)

---

## 11. What Good Traction Looks Like by Stage

### Pre-Launch / Waitlist

| Metric | Decent | Good | Exceptional |
|--------|--------|------|-------------|
| Waitlist signups | 500-1,000 | 1,000-5,000 | 5,000-10,000+ |
| Waitlist growth rate | 5-10%/week | 10-20%/week | 20%+/week |
| Social media following | 500-1,000 | 1,000-5,000 | 5,000+ |
| Video views (sizzle reel) | 10K-50K | 50K-500K | 500K+ |
| Press mentions | 1-2 | 3-5 | 5+ with tier-1 outlets |
| Email open rate | 25-35% | 35-45% | 45%+ |

**Real examples:**
- Dropbox: 5K to 75K waitlist signups from one demo video
- Day.ai: 4,000+ waitlist signups in 72 hours
- Linear: 10,000+ waitlist from building-in-public on Twitter
- Harry's Razors: 100,000 signups in one week via referral tiers

### First Week After Launch

| Metric | Decent | Good | Exceptional |
|--------|--------|------|-------------|
| Downloads | 500-2,000 | 2,000-10,000 | 10,000-50,000+ |
| D1 retention | 20-30% | 30-40% | 40%+ |
| App Store rating | 3.5-4.0 | 4.0-4.5 | 4.5+ |
| Organic % of downloads | 40-60% | 60-80% | 80%+ |
| Social shares of pet creations | 50-200 | 200-1,000 | 1,000+ |
| Session length (avg) | 3-5 min | 5-10 min | 10+ min |

### First Month

| Metric | Decent | Good | Exceptional |
|--------|--------|------|-------------|
| Total downloads | 5,000-15,000 | 15,000-50,000 | 50,000-200,000+ |
| MAU | 2,000-5,000 | 5,000-20,000 | 20,000-100,000 |
| DAU | 300-800 | 800-5,000 | 5,000+ |
| D7 retention | 10-15% | 15-25% | 25%+ |
| D30 retention | 5-8% | 8-15% | 15%+ |
| WoW growth (after launch spike) | 2-5% | 5-10% | 10%+ |
| Pets created | 3K-10K | 10K-50K | 50K+ |
| Share/viral actions | 500-2K | 2K-10K | 10K+ |

### First 3 Months

| Metric | Decent | Good | Exceptional |
|--------|--------|------|-------------|
| Total downloads | 20,000-50,000 | 50,000-200,000 | 200,000-1M+ |
| MAU | 5,000-15,000 | 15,000-50,000 | 50,000-200,000+ |
| DAU/MAU | 15-20% | 20-30% | 30%+ |
| D30 retention | 5-8% | 8-15% | 15%+ |
| D90 retention | 2-4% | 4-8% | 8%+ |
| MoM growth | 10-15% | 15-25% | 25%+ |
| Revenue (if monetized) | $0-1K MRR | $1K-10K MRR | $10K+ MRR |
| K-factor | 0.10-0.20 | 0.20-0.40 | 0.40+ |
| App Store rating | 4.0+ | 4.3+ | 4.5+ |

---

## 12. Case Studies

### Character.AI -- The AI Companion Gold Standard

| Metric | Value | When |
|--------|-------|------|
| DAU/MAU | 41-45% | 2023-2024 |
| Session length | 17 min average; power users 2 hrs/day | 2024 |
| Sessions/week | 5x per week average | 2024 |
| D7 retention | 40% | 2023 |
| MAU peak | 28M | Mid-2024 |
| MAU current | ~20M | 2025 |
| Revenue | $32.2M annual | 2024 |
| Early community growth | 10 --> 75 --> 1,200 --> 7,000 --> 25,000 subreddit (Aug 2022 --> Mar 2023) | 7 months |

**Lesson**: Emotional attachment drives insane stickiness. The 41-45% DAU/MAU is almost social-app-level engagement because users form relationships with their AI characters.

### Replika -- The Companion App Pioneer

| Metric | Value |
|--------|-------|
| MAU | ~2M |
| Revenue | $24-30M annual |
| Session length | 15 min average |
| Business model | Subscription-only |
| Team size | 93 people |
| Total funding | $11M across 4 rounds |

**Lesson**: Smaller user base than Character.AI but sustainable subscription revenue. Proves the companion category can be profitable even without massive scale.

### Neko Atsume -- Organic-Viral Virtual Pet

| Metric | Value |
|--------|-------|
| Total downloads | 33M+ lifetime |
| Key milestone | 5.5M downloads by July 2015 (9 months post-launch) |
| Marketing spend | $0 |
| Growth driver | Word-of-mouth, Reddit communities, social sharing |
| Rating | 4.5+ stars |

**Lesson**: Pure word-of-mouth virality powered by a delightful collection mechanic. Users shared screenshots of their cat collections, creating organic social loops. Zero marketing budget. The shareable visual moment was the growth engine.

### Peridot (Niantic) -- The AR Pet Cautionary Tale

| Metric | Value |
|--------|-------|
| Total downloads | ~800K lifetime |
| Current daily downloads | ~39/day |
| App Store rating | 3.99 |
| Status | Alive but struggling |

**Lesson**: Being Niantic (Pokemon GO creators) with massive distribution was not enough. AR novelty wore off. The pet care loop was not compelling enough to retain users. Expensive breeding mechanics ($5/nest) created friction. **AR is a feature, not a retention strategy.**

### My Cat -- Virtual Pet Games (2024 Market Leader)

| Metric | Value |
|--------|-------|
| Weekly revenue | $50K-61K |
| Weekly downloads | ~30K-43K |
| Weekly active users | ~134K |
| Revenue/WAU | ~$0.40-0.45/week |

**Lesson**: Steady, not explosive. Virtual pet games can generate meaningful revenue with a loyal audience, but the ceiling is lower than AI companions unless you add social or AI elements.

### Vinci Games -- Gaming + YC

| Metric | Value |
|--------|-------|
| Downloads at YC acceptance | 800K+ |
| App Lab rating | 4.9 stars (16K+ reviews) |
| Total players | 1M+ (Steam + Quest) |
| YC batch | S22 |
| Post-YC funding | $5.1M seed |

**Lesson**: Massive traction BEFORE YC. 800K downloads with 4.9 stars is elite product-market fit. This was not an idea-stage acceptance -- this was proven PMF.

### Sources
- [Character.AI Statistics](https://electroiq.com/stats/character-ai-statistics/)
- [TechCrunch: AI Companion Apps $120M](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)
- [ReferralCandy: How Neko Atsume Achieved 5.5M Downloads](https://www.referralcandy.com/blog/neko-atsume-marketing-strategy)
- [Sensor Tower: Virtual Pet Apps Q2 2024](https://sensortower.com/blog/2024-q2-unified-top-5-virtual%20pet-units-us-62f83d1bf5dff39390bc09c4)

---

## 13. Presenting Traction to Accelerators

### What Accelerators Actually Look At

The hierarchy of traction signals, from strongest to weakest:

1. **Revenue with growth** -- Any non-zero MRR growing WoW is the strongest possible signal
2. **Active users with retention data** -- DAU + D7/D30 retention proves people come back
3. **Growth rate** -- WoW growth even with small numbers shows momentum
4. **Signups / waitlist with conversion** -- Waitlist that converts to actual users
5. **Community engagement** -- Discord members, subreddit growth, organic UGC
6. **Press mentions** -- Validation from credible outlets
7. **Social media views** -- Weakest standalone, but powerful amplifier of other signals

### What to Show (The Traction Dashboard)

Build a single-page traction dashboard with these elements:

**Must-have metrics:**
- DAU / MAU (line chart, daily granularity)
- D1, D7, D30 retention (cohort table or curve)
- WoW growth rate (annotated with milestones)
- Total users / downloads

**Strong supplementary metrics:**
- Session length and sessions per day
- Activation rate (download to first pet created)
- K-factor or share rate
- App Store rating + review count
- Organic vs paid split

**Nice to have:**
- Revenue (if any)
- Geographic distribution
- Content creation volume (pets created, photos shared)
- Community metrics (Discord, Reddit, social mentions)

### How to Frame the Numbers

**Do this:**
- "2,300 waitlist signups from a single Product Hunt launch" (specific, impressive)
- "D7 retention of 23% -- 2x the category average" (contextualized)
- "Growing 12% week-over-week for 4 consecutive weeks" (trajectory)
- "45% of users create a second pet within 48 hours" (engagement depth)

**Don't do this:**
- "We have 50,000 impressions on social media" (unactionable)
- "Our waitlist is growing fast" (no numbers)
- "People love the app" (no evidence)
- "We've been featured by 3 blogs" (which blogs? what impact?)

### The a16z Speedrun Narrative Formula

Based on what worked for accepted founders:

> "We launched [X days] ago. Here's what happened:
> - [Specific user number] people [used the product] in [timeframe]
> - [Retention metric]: [X%] came back on Day 7 without being prompted
> - [Growth metric]: Week 2 DAU was [X%] higher than Week 1
> - [Distribution metric]: [X] organic shares generated [Y] new users
> - [Qualitative]: Users are [specific behavior that shows emotional investment]
> - Zero dollars spent on marketing."

**Why this works**: It answers all three signals Speedrun cares about:
1. Traction: Real numbers, real retention
2. Team: You executed this in [X days] with $0
3. TAM: Organic sharing proves this scales beyond your direct efforts

### Specific Tips for Speedrun Applications

Per published Speedrun guidance and founder interviews:
- Lead with retention, not downloads. "45% D30 retention" is more powerful than "100K downloads"
- Show the growth chart. Daily granularity. Up and to the right
- Be specific about hard problems: "What is your earned secret?"
- Don't oversell. They see 19,000+ applications -- they can smell hype
- If you pivoted between application and interview, share it. They value learning velocity
- Company description matters more than most founders expect

### Sources
- [Speedrun: What We Look For](https://speedrun.substack.com/p/what-we-look-for-in-applications)
- [Speedrun: The 3 Signals](https://speedrun.substack.com/p/sr005-apps-reviewed-the-3-signals-that-get-startups-in)
- [SlideModel: Traction Slide](https://slidemodel.com/traction-slide-pitch-deck/)
- [OpenVC: Traction Slide Best Practices](https://www.openvc.app/blog/traction-slide)
- [Qubit Capital: Consumer App Traction Metrics](https://qubit.capital/blog/evaluating-traction-metrics-consumer-apps)

---

## 14. Vanity Metrics vs Real Metrics

### The Vanity Metrics Trap

Vanity metrics sound good but don't reflect real performance. Investors spot them instantly.

| Vanity Metric | Why It's Misleading | Real Alternative |
|---------------|--------------------|--------------------|
| Total downloads | Says nothing about retention | DAU or WAU |
| Registered users | Many never return | Monthly active users |
| Page views / impressions | No indication of value | Session depth, time in app |
| Social media followers | Followers != users | Follower-to-user conversion rate |
| "Millions of views" on TikTok | Views != downloads != active users | View-to-install conversion rate |
| Total pets created | One user can spam | Unique creators per day |
| App Store "trending" | Temporary visibility | Sustained download velocity |
| Press mentions | Vanity unless they drive users | Press-attributed installs |
| Waitlist size (without conversion) | Email != intent | Waitlist-to-activation rate |

### Real Metrics That Matter

| Real Metric | Why It Matters | What Proves |
|-------------|----------------|-------------|
| **D7 / D30 retention** | Do people come back? | Product-market fit |
| **DAU/MAU ratio** | Is this a daily habit? | Stickiness |
| **WoW growth rate** | Is momentum accelerating? | Trajectory |
| **Activation rate** | Do downloaders become users? | Onboarding quality |
| **Session frequency** | How often do they use it? | Habit formation |
| **Organic share rate** | Do users tell friends? | Word-of-mouth potential |
| **Revenue per user** | Can this be a business? | Unit economics |
| **Cohort retention curves** | Does each new cohort retain better? | Product improvement |
| **Net promoter score** | Would users recommend it? | True satisfaction |

### The Quibi Warning

Quibi hit 1.7 million downloads in its first week. It shut down 6 months after launch due to catastrophic retention. Downloads without retention is a death sentence.

### The 40% Test

Sean Ellis's test: Ask users "How would you feel if you could no longer use this product?"
- If 40%+ say "very disappointed" -- you almost certainly have strong traction
- If <40% -- keep iterating before scaling

### What Zerocap Should Track from Day 1

**Primary metrics (report these to investors):**
1. D1, D7, D30 retention
2. DAU and DAU/MAU ratio
3. WoW growth rate (post-launch-spike baseline)
4. Activation rate (download to first pet created)

**Secondary metrics (track internally):**
1. Pets created per user
2. Session length and frequency
3. Share/viral actions per user
4. Camera scan success rate (technical quality)
5. Return rate after first session

**Ignore (or don't lead with):**
1. Total downloads
2. Social media follower counts
3. Press mention counts
4. App Store impressions

### Sources
- [Epirus VC: Vanity vs Actionable Metrics](https://www.epirus.vc/blog/vanity-metrics-vs-actionable-metrics-how-startup-founders-can-focus-on-what-actually-drives-growth)
- [Hustle Fund: Startup Vanity Metrics](https://www.hustlefund.vc/post/angel-squad-startup-vanity-metrics-investors-should-avoid-and-what-to-focus-on-instead)
- [Exit Fund Weekly: Metrics That Fooled Startups](https://exitfundweekly.substack.com/p/5-lessons-from-metrics-that-fooled)

---

## 15. Zerocap-Specific Targets

Based on all benchmarks above, here are concrete targets for Zerocap at each stage.

### Position in the Category Map

Zerocap sits at the intersection of four categories:
- **AI companion** (emotional bond with a pet)
- **Virtual pet** (care, feeding, evolution loops)
- **Camera/AR** (real-world object scanning)
- **Casual game** (collection, progression)

This means Zerocap should aim for:
- AI companion-level session depth and DAU/MAU
- Virtual pet-level retention mechanics
- Camera app-level time to first value
- Casual game-level growth and accessibility

### Launch Targets (First 2 Weeks)

| Metric | Minimum | Target | Stretch |
|--------|---------|--------|---------|
| Downloads | 2,000 | 10,000 | 50,000 |
| Activation (download to first pet) | 40% | 55% | 70% |
| D1 retention | 25% | 35% | 45% |
| D7 retention | 10% | 18% | 28% |
| App Store rating | 4.0 | 4.3 | 4.5+ |
| Avg session length | 5 min | 8 min | 12+ min |
| Pets created per user | 1.5 | 3 | 5+ |
| Share rate (% who share a pet) | 5% | 12% | 20%+ |

### Month 1 Targets

| Metric | Minimum | Target | Stretch |
|--------|---------|--------|---------|
| MAU | 3,000 | 15,000 | 50,000 |
| DAU | 400 | 3,000 | 12,000 |
| DAU/MAU | 15% | 22% | 30%+ |
| D30 retention | 5% | 10% | 18% |
| WoW growth (post-spike) | 3% | 7% | 12%+ |
| K-factor | 0.15 | 0.30 | 0.50 |

### Month 3 Targets (Accelerator Application Ready)

| Metric | Minimum Viable | Strong Application | Standout |
|--------|---------------|-------------------|----------|
| MAU | 10,000 | 30,000 | 100,000+ |
| DAU | 2,000 | 8,000 | 30,000+ |
| DAU/MAU | 20% | 28% | 35%+ |
| D30 retention | 8% | 14% | 22%+ |
| D90 retention | 3% | 6% | 10%+ |
| MoM growth | 12% | 20% | 30%+ |
| App Store rating | 4.0+ | 4.3+ | 4.5+ |
| Revenue (if any) | $0 (OK) | $1K MRR | $5K+ MRR |

### The Spark That Gets Zerocap Into Speedrun

Based on the Speedrun selection criteria and founder interviews:

**Tier 1 (almost certainly interviewed):**
- 10,000+ organic users with D7 retention > 20%
- Viral TikTok/Instagram content of pet creations with 500K+ views converting to actual users
- Any revenue signal with growth

**Tier 2 (likely interviewed):**
- 1,000-10,000 users with clear growth trajectory (10%+ WoW)
- Strong retention data: D7 > 15%, D30 > 8%
- Active community forming around pet sharing
- Multiple short-form videos showing the camera-to-pet transformation going viral

**Tier 3 (possible with great team):**
- Working product with 100-1,000 users and early retention signals
- Sizzle reel of the camera-to-pet experience with social traction
- Clear insight into why AI pets tied to real objects is different from generic virtual pets

### The One-Sentence Story

> "Zerocap users point their phone at everyday objects and watch them transform into living AI pets. Our D7 retention is [X%] because once you've brought your coffee mug to life, you feel responsible for it."

That sentence contains: (1) what the product does, (2) why it's novel, (3) a real metric, (4) the emotional hook that drives retention.

---

## Appendix: Key Source Summary

### Market Data
- [TechCrunch: AI Companion Apps $120M Revenue Track](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)
- [a16z State of Consumer AI 2025](https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/)
- [Sensor Tower State of AI Apps 2025](https://sensortower.com/blog/state-of-ai-apps-report-2025)
- [Sensor Tower Virtual Pet Apps Q2 2024](https://sensortower.com/blog/2024-q2-unified-top-5-virtual%20pet-units-us-62f83d1bf5dff39390bc09c4)

### Retention & Engagement Benchmarks
- [GameAnalytics 2025 Mobile Gaming Benchmarks](https://www.gameanalytics.com/reports/2025-mobile-gaming-benchmarks)
- [Pushwoosh Retention Benchmarks 2025](https://www.pushwoosh.com/blog/increase-user-retention-rate/)
- [Plotline Retention by Industry](https://www.plotline.so/blog/retention-rates-mobile-apps-by-industry)
- [Andrew Chen: Losing 80% of Users](https://andrewchen.com/new-data-shows-why-losing-80-of-your-mobile-users-is-normal-and-that-the-best-apps-do-much-better/)
- [UXCam Mobile App Benchmarks 2025](https://uxcam.com/blog/mobile-app-benchmarks/)
- [Mistplay Mobile Game Retention](https://business.mistplay.com/resources/mobile-game-retention-benchmarks)

### Growth & Accelerator Benchmarks
- [Paul Graham: Startup = Growth](https://www.paulgraham.com/growth.html)
- [a16z Speedrun: What We Look For](https://speedrun.substack.com/p/what-we-look-for-in-applications)
- [Speedrun: The 3 Signals](https://speedrun.substack.com/p/sr005-apps-reviewed-the-3-signals-that-get-startups-in)
- [Tremendous: YC Valuation & Traction Benchmarks](https://tremendous.blog/2024/11/26/benchmarks-for-valuation-and-traction-at-y-combinator/)

### Virality & Distribution
- [Saxifrage K-Factor Benchmarks](https://www.saxifrage.xyz/post/k-factor-benchmarks)
- [ReferralCandy: Neko Atsume Marketing](https://www.referralcandy.com/blog/neko-atsume-marketing-strategy)
- [Mapendo CPI 2025](https://mapendo.co/blog/cost-per-install-2025-the-ultimate-report-to-grow-your-app-worldwide)

### Revenue & Monetization
- [RevenueCat State of Subscription Apps 2025](https://www.revenuecat.com/state-of-subscription-apps-2025/)
- [Character.AI Statistics](https://electroiq.com/stats/character-ai-statistics/)
- [AI Companions Statistics](https://electroiq.com/stats/ai-companions-statistics/)

### Investor & Pitch Resources
- [Qubit Capital: Consumer App Traction Metrics](https://qubit.capital/blog/evaluating-traction-metrics-consumer-apps)
- [OpenVC: Traction Slide Best Practices](https://www.openvc.app/blog/traction-slide)
- [Epirus VC: Vanity vs Actionable Metrics](https://www.epirus.vc/blog/vanity-metrics-vs-actionable-metrics-how-startup-founders-can-focus-on-what-actually-drives-growth)
