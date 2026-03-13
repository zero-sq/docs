# Spark Ads, Whitelisting & Creator-Powered Paid Media Strategy

> **For:** Zerocap (iOS AI companion/tamagotchi app)
> **Last updated:** 2026-03-13
> **Core concept:** Buy a video from a creator, they post it organically on their feed, then you put paid spend behind it so it reaches far more people than organic alone — but it still shows as coming from the creator's account, not the Zerocap brand account.

---

## Table of Contents

1. [TikTok Spark Ads](#1-tiktok-spark-ads)
2. [Instagram Partnership Ads (Whitelisting)](#2-instagram-partnership-ads-whitelisting)
3. [YouTube BrandConnect](#3-youtube-brandconnect)
4. [The Combined Strategy](#4-the-combined-strategy)
5. [Negotiation with Creators for Whitelisting Rights](#5-negotiation-with-creators-for-whitelisting-rights)

---

## 1. TikTok Spark Ads

### How Spark Ads Work Technically

Spark Ads let you take an organic TikTok video — posted by a creator on their own account — and run it as a paid ad. The ad appears in users' feeds as if it's coming from the creator's profile, not from a brand account. Users can click through to the creator's real profile, see their real follower count, and interact with the post (likes, comments, shares all accrue to the original post).

**The technical flow:**

1. Creator posts a video organically on their TikTok account
2. Creator generates an **authorization code** for that specific video
3. Creator shares the authorization code with the brand
4. Brand enters the code in TikTok Ads Manager to link the post
5. Brand sets up a campaign using that post as the ad creative
6. The ad runs from the creator's handle with full ad targeting/optimization

The key distinction from regular in-feed ads: Spark Ads use *real* posts from *real* accounts. The creator's profile picture, username, and the original post (with its organic engagement) are all preserved. A "Sponsored" label and CTA button are added, but the content reads as native creator content — because it literally is.

**What Spark Ads can't do:**
- You cannot edit the video content after the creator posts it
- You cannot change the caption once the ad authorization is generated
- The creator's original audio must be cleared for ad use (important for licensed music)

### Step-by-Step Setup

#### Creator Side (Generating the Authorization Code)

1. **Enable Ad Authorization:** Go to Settings > Creator tools > Ad settings (or tap the three dots on the specific video)
2. **Select the video:** Navigate to the video you want to authorize
3. **Turn on Ad Authorization toggle**
4. **Choose authorization duration:** 7, 30, 60, or 365 days
5. **Generate Code:** Tap "Generate Code" — this creates a unique alphanumeric code for that specific video
6. **Share the code** with the brand (copy/paste via email, DM, etc.)

Each code is tied to one video only. You need separate codes for each video you want to spark. Creators can batch-authorize up to 20 videos at once.

#### Brand Side (Setting Up the Campaign in Ads Manager)

1. **Go to TikTok Ads Manager** > Assets > Creative > Spark Ads
2. **Click "Apply for Authorization"**
3. **Paste the authorization code** from the creator
4. **Click "Search"** — the linked post will appear with a preview
5. **Click "Confirm"** to add it to your Spark Ads library
6. **Create a new campaign:**
   - Campaign objective: **App Installs** (for Zerocap)
   - Select the Spark Ad post as your creative
   - Set targeting, budget, bid strategy, and schedule
7. **Add your CTA:** "Download" or "Install Now" button with App Store deep link
8. **Set up tracking:** Connect AppsFlyer/Adjust for attribution
9. **Launch**

### Cost Structure & Bidding

**Bidding Models for App Install Campaigns:**

| Model | How it works | When to use |
|-------|-------------|-------------|
| **Cost Cap** | You set your target CPI; TikTok optimizes to stay near it | When you have a clear CPI target (recommended for Zerocap) |
| **Maximum Delivery** | TikTok spends your budget to get the most installs possible | When you want volume and are less price-sensitive |
| **Lowest Cost** | No bid cap; TikTok finds the cheapest installs | Good for initial testing to establish baselines |

**Benchmark Costs (2025 data):**

| Metric | Spark Ads | Regular In-Feed Ads |
|--------|-----------|---------------------|
| **CPM** | $3.50–$10 | 40% lower on average |
| **CPC** | $0.10–$0.30 | $0.35–$1.00 |
| **CTR** | 1.73% (2.1x platform avg) | 0.84% (platform average) |
| **CPI (app installs)** | $0.70–$4.50 (varies by vertical) | Typically higher due to lower engagement |

**Minimum budgets:**
- Ad group minimum: $5/day
- Campaign minimum: $50/day
- Recommended minimum for learning phase: 20x your target CPI per day (e.g., $40/day if targeting $2 CPI)

### Performance Data: Spark Ads vs. Regular In-Feed Ads

This is the core pitch for why Spark Ads matter:

| Metric | Spark Ads Advantage |
|--------|-------------------|
| **CTR** | 64% higher than in-feed ads; 2.1x the platform average |
| **Engagement rate** | 142% higher (6.1% vs 2.5% for standard in-feed) |
| **Video completion rate** | 134% higher (78.3% vs 33.5%) |
| **6-second view-through rate** | 157% higher (64.7% vs 25.2%) |
| **Conversion rate** | 3.84% vs 1.12% for non-Spark (with TikTok Shop) |
| **CPA** | 37% lower ($14.62 vs $23.18 average) |
| **CPC** | 52.4% lower when using organic posts with 500+ engagements |

**The trade-off:** Spark Ads have ~40% higher CPM than regular in-feed ads. But the dramatically better engagement and conversion rates more than compensate — you pay more per impression but much less per actual result. This is because the content reads as authentic creator content, not brand advertising.

**Category-specific data relevant to Zerocap:**
- Gaming/tech verticals hit 7.3–7.8% engagement rates on Spark Ads
- Micro-influencer Spark Ads achieve 9.6% engagement rates
- DTC brands achieve lowest CPAs around $9.87 with Spark Ads

### Creative Best Practices for Spark Ads

Since Spark Ads amplify organic content, the content itself needs to perform organically first. Best practices for briefing creators:

**Content structure:**
- **Hook in first 2 seconds** — Spark Ads with strong hooks see 61% better CPC
- **Show the product being used** — product visibility drives 138% uplift in ad recall
- **Show a face** — face + body content lifts purchase intent by 72%
- **Keep it native** — the whole point is authenticity; polished brand content defeats the purpose
- **Storytelling over selling** — focus on the experience ("I've been raising this little AI pet for 3 weeks and it just...") rather than feature lists
- **Trending formats** — 77% of TikTok users say they like brands better when they participate in trends

**What works specifically for app installs:**
- "Day in my life" format showing the app naturally integrated
- Screen recordings with face-cam reaction
- "I found this app and..." discovery narrative
- Before/after or progression content (perfect for a tamagotchi/companion app)
- Duet/stitch format responding to other content

**Content to avoid:**
- Overly scripted reads that feel like ads
- Heavy branding overlays
- Content that looks different from the creator's usual style
- Licensed music (can cause ad rejection; use original sounds or TikTok's commercial music library)

### Authorization Duration & Approach

**Duration options:**
- **7 days** — too short for meaningful testing; avoid
- **30 days** — minimum viable window; good for initial tests
- **60 days** — recommended standard; gives enough time to optimize
- **365 days** — ideal for top performers; negotiate this for winners

**Can you Spark organic posts that aren't sponsored?**

Yes — and this is one of the most powerful tactics. If a creator genuinely posts about Zerocap (either through gifting or because they actually use it), you can ask them for a Spark code for that organic post. This works particularly well because:
- The content is genuinely organic, so it has maximum authenticity
- There's no "paid partnership" label on the original post
- It still shows as coming from the creator
- You just need the authorization code — no formal sponsorship deal required

**How to approach this:**
1. Monitor TikTok for organic mentions of Zerocap
2. Reach out to the creator: "Hey, we loved your video about [Zerocap]. Would you be open to letting us put some ad spend behind it? We'd pay you $X for the authorization code. It stays on your profile and you keep all the engagement."
3. Many creators will agree because (a) it drives more views/followers to their account and (b) they get paid for content they already made

### Targeting Options for App Install Campaigns

When running Spark Ads optimized for app installs:

**Audience targeting:**
- **Demographics:** Age (16–34 primary for Zerocap), gender, location
- **Interest targeting:** Gaming, AI, virtual pets, digital lifestyle, animation, cute content
- **Behavior targeting:** Users who have installed similar apps, app category engagement
- **Custom audiences:** Upload existing user lists for lookalike targeting
- **Lookalike audiences:** Build from your existing install base or high-value users
- **Automatic targeting:** Let TikTok's algorithm find the best audience (recommended for initial testing)

**Best practice:** Start broad and let TikTok's algorithm learn. Don't over-constrain targeting in the first week. Once you have conversion data (50+ installs), the algorithm gets significantly better at finding similar users.

### Budget Recommendations for Testing

#### Tier 1: $500 Test
- **Goal:** Validate the Spark Ads format; get initial CPI data
- **Structure:** 1–2 Spark Ad posts, 1 campaign, 2–3 ad groups with different targeting
- **Duration:** 5–7 days
- **Expected output:** 100–500 installs, baseline CPI, engagement benchmarks
- **What you learn:** Whether Spark Ads work for Zerocap at all; rough CPI range

#### Tier 2: $1,000 Test
- **Goal:** Compare multiple creators and creative angles
- **Structure:** 3–5 Spark Ad posts from different creators, A/B test targeting
- **Duration:** 10–14 days
- **Expected output:** 300–1,000 installs, comparative creator performance
- **What you learn:** Which creator style performs best; optimal audience segments

#### Tier 3: $5,000 Scale Test
- **Goal:** Find winning creative and scale
- **Structure:** 5–10 Spark Ad posts, kill underperformers after 48 hours, scale winners
- **Duration:** 3–4 weeks
- **Expected output:** 1,500–5,000 installs, proven CPI, scalable winners identified
- **What you learn:** Reliable CPI at scale; which content can sustain spend; retention correlation with ad creative

**Budget scaling rules:**
- Increase daily budget by no more than 15–20% every 2–3 days
- Sudden large increases (>30%) reset the algorithm's learning phase
- If CPI drifts above target for 48+ hours, pause and reallocate
- Refresh creative every 7–10 days to combat ad fatigue

---

## 2. Instagram Partnership Ads (Whitelisting)

### How Partnership Ads Work

Instagram's equivalent of Spark Ads is called **Partnership Ads** (formerly "Branded Content Ads"). The mechanism is similar: a creator grants a brand permission to run ads using the creator's content and identity. The ad appears in users' feeds as coming from the creator's account, with a "Sponsored" label.

**Key terminology update:** Meta renamed "Branded Content Ads" to "Partnership Ads" in 2024. The older term "whitelisting" is still widely used in the industry but isn't an official Meta term.

**What content can be promoted as Partnership Ads:**
- Posts with the "Paid partnership" label
- Instagram Collab posts (co-authored)
- Posts with @mentions of the brand
- Posts with people tags or product tags
- New creatives built in Ads Manager using creator's identity (no existing post required)

### Setup Process

#### Method 1: Content-Level Permission (Per Post)

**Creator side:**
1. Create a Reel, Story, or Feed post
2. Tap "Next" before publishing
3. Tap "Partnership label & ads"
4. Search for and add the brand (Spacezero/Zerocap)
5. Toggle on "Allow partner to boost"
6. Publish the post

**Brand side:**
1. The post appears in Meta Ads Manager under the Partnership Ads Hub
2. Create a new campaign > select the partnership ad
3. Set campaign objective to "App Installs"
4. Configure targeting, budget, and optimization
5. Launch

#### Method 2: Account-Level Permission (All Eligible Content)

**Creator side:**
1. Go to Settings > Creator/Business > Partnership ads > Ad partners
2. Search for the brand's Meta Business account
3. Approve the partnership request

**Brand side:**
1. In Ads Manager, go to All Tools > Partnership Ads Hub
2. Click "Add partnership"
3. Search for creator's username > send request
4. Once approved, any eligible content from that creator becomes available to boost

#### Method 3: Ad Code (Simplest)

**Creator side:**
1. Go to the published post > tap three dots
2. Select "Ad Tools" > "Get partnership ad code"
3. Share the code with the brand

**Brand side:**
1. Enter the ad code in Meta Ads Manager
2. The post becomes available as a Partnership Ad creative

### Performance vs. Regular Instagram Ads

Partnership ads significantly outperform standard brand-run ads:

| Metric | Partnership Ads Advantage |
|--------|--------------------------|
| **CTR** | 53% higher than business-as-usual ads |
| **CPA** | 19% lower |
| **CPM** | Up to 40% cheaper |
| **Conversion rate** | 30% lower CPA compared to standard Meta ads |
| **Engagement** | UGC-based ads get 4x higher CTR and 50% lower CPC |
| **Collab posts** | 3.4x higher engagement than non-collab posts |
| **Overall** | 99% probability of outperforming standard ads when combined with BAU |

### Creative Format Options

| Format | Best For | Notes |
|--------|----------|-------|
| **Reels** | App installs, engagement | Lowest CPM; highest engagement; 9:16 vertical; up to 90 seconds |
| **Stories** | App installs, swipe-up | Full-screen; ephemeral feel; strong for direct response |
| **Feed Posts** | Brand awareness, consideration | Static or carousel; longer shelf life but higher CPM |
| **Reels + Stories combo** | Full-funnel | Run the same creator content across placements |

For Zerocap app installs, **Reels are the priority format** — they deliver the lowest CPM while maintaining strong engagement, and the vertical video format mirrors TikTok content.

### Targeting & Optimization for App Installs

**Campaign setup for Zerocap:**
- **Objective:** App Installs (or App Promotion)
- **Optimization:** Optimize for installs (not link clicks)
- **Advantage+ placements:** Let Meta auto-place across Feed, Stories, Reels, Explore
- **Audience:** Start with Advantage+ Audience (Meta's AI targeting) then test manual segments

**Targeting options:**
- Custom Audiences from existing users (for lookalikes)
- Interest targeting: AI, virtual pets, gaming, digital companions, tamagotchi, cute apps
- Behavioral targeting: Recent app installers, mobile gamers
- Lookalike audiences: 1–3% of your best users

### Cost Benchmarks

| Metric | Range |
|--------|-------|
| **CPM** | $6–$12 (Reels at the lower end) |
| **CPC** | $0.40–$1.50 |
| **CPI (app installs)** | $1.50–$5.00 (varies by targeting and creative) |
| **Partnership Ad CPI** | Typically 20–40% lower than standard ads |

---

## 3. YouTube BrandConnect

### How It Works

YouTube BrandConnect is a self-service platform within YouTube/Google Ads that facilitates brand-creator partnerships. The key feature for whitelisting is **Brand Partner Access** — where a creator grants a brand permission to run their YouTube video as a paid ad.

**The flow:**
1. Creator posts a sponsored video (long-form or Short) on their channel
2. Creator links the video to the brand through BrandConnect
3. Brand gains access to run that video as a paid ad across YouTube and Google's ad network
4. The ad shows a "Paid promotion" label and displays the creator's channel identity
5. Brand gets access to full video performance metrics

### Setup & Access Requirements

**Creator eligibility:**
- Must be in the YouTube Partner Program (YPP)
- Minimum 25,000 subscribers (general guideline)
- Must be eligible for AdSense revenue sharing
- Available in 22 countries (including US, UK, Australia)
- Must comply with YouTube Community Guidelines

**Creator setup:**
1. Go to YouTube Studio > Earn tab > BrandConnect tab
2. Set preferences and customize pricing for long-form videos and Shorts
3. When a brand deal is in place, link the video through BrandConnect
4. Grant "Brand Partner Access" to the advertiser

**Brand setup in Google Ads:**
1. Go to Google Ads > Creator Partnerships Hub
2. Search for the creator's video by title or paste the YouTube URL
3. Select the video to attach to your campaign
4. Create campaign as usual (the creator video is your ad creative)

**Important:** The brand is responsible for securing sufficient rights to use the video as an ad — this requires a separate agreement with the creator.

**Campaign types that support BrandConnect partnership ads:**
- Demand Gen campaigns (In-feed + Shorts)
- Video Action Campaigns
- Video View campaigns
- Video Reach campaigns
- App campaigns
- Performance Max campaigns

### Shorts-Specific Features

- Partnership ads run on the Shorts feed with a co-branded format showing both creator and brand identity
- Internal Google data shows partnership ads on the Shorts feed drive **up to 20% higher conversions** than ads with advertiser branding alone
- Short-form content accounted for 22% of YouTube's total ad revenue in 2025 (up from 15%)
- 62% of brands now allocate more Shorts budget than TikTok or Reels

### Performance Data

| Metric | Benchmark |
|--------|-----------|
| **YouTube Shorts Ads CPV** | $0.10–$0.30 |
| **YouTube Shorts Ads CPM** | ~$4 |
| **Conversion lift (partnership vs. brand-only)** | Up to 20% higher on Shorts feed |

YouTube BrandConnect is newer and less mature than TikTok Spark Ads for this use case. The primary advantage is access to YouTube's audience and Google's ad optimization. For Zerocap, YouTube Shorts partnerships are worth testing but TikTok Spark Ads should be the priority channel.

---

## 4. The Combined Strategy

### The Organic-to-Paid Flywheel

The fundamental framework: **post organically first, identify winners, then pour paid spend into the winners.**

```
Commission content from 10–20 creators
          ↓
Each creator posts organically on their account
          ↓
Monitor performance for 24–48 hours
          ↓
Identify top 3–5 performers (see metrics below)
          ↓
Request Spark Ad / Partnership Ad authorization
          ↓
Run paid campaigns behind the winners
          ↓
Kill underperformers, scale winners
          ↓
Reinvest learnings into next creator batch
```

### How to Identify Which Organic Posts Are Worth Boosting

**Metrics to evaluate in the first 24–48 hours:**

| Metric | Signal | Threshold for Boosting |
|--------|--------|----------------------|
| **Completion rate** | People watch to the end = compelling content | >50% average watch time |
| **Share rate** | Shares = strong distribution signal | >1% of views result in shares |
| **Save rate** | Saves = high perceived value | >0.5% save rate |
| **Comment rate** | Comments = engagement; sentiment matters too | >1% comment rate |
| **View velocity** | How fast views accumulate in first 6 hours | Outperforming creator's average |
| **Profile visits** | People clicking to creator profile = curiosity | Above creator's baseline |
| **Organic CTA engagement** | If link in bio or comment pin, are people clicking? | Any measurable clicks = good signal |

**Red flags (don't boost):**
- High views but very low engagement (content went viral but isn't converting interest)
- Negative comment sentiment
- Completion rate below 30%
- Views plateauing quickly after initial push

**Decision framework:**

| Performance | Action |
|-------------|--------|
| Top 10% (clear winner) | Immediately request Spark code; start with $50–$100/day |
| Top 25% (strong performer) | Request code; test with $20–$50/day |
| Middle 50% | Hold; monitor for another 24 hours |
| Bottom 25% | Don't boost; analyze why it underperformed |

### The Test-and-Scale Framework

**Phase 1: Wide Net (Week 1–2)**
- Commission 10–20 micro/nano creators at $100–$500 each
- Total creator spend: $1,000–$5,000
- Each creator posts 1 video organically
- No paid spend yet — just observing organic performance
- Collect Spark Ad authorization codes upfront (include in the deal)

**Phase 2: Identify Winners (Days 3–5)**
- Rank all posts by the metrics above
- Select top 3–5 posts for paid amplification
- Request extended authorization (60–365 days) for the winners
- Begin paid testing at $20–$50/day per creative

**Phase 3: Optimize (Week 2–3)**
- A/B test targeting (broad vs. interest-based vs. lookalike)
- A/B test different CTA copy
- Kill any ad group not hitting CPI targets after 48 hours of spend
- Scale daily budget 15–20% every 2–3 days on winners

**Phase 4: Scale (Week 3+)**
- Pour budget into proven winners: $100–$500/day per creative
- Commission new content from winning creator profiles (same style/angle)
- Expand to Instagram Partnership Ads with the same winning creators
- Build lookalike audiences from installer data

### Budget Split Recommendations: Creator Fee vs. Ad Spend

The general rule: **plan to spend 2–5x the creator fee on paid amplification** for content that performs.

| Budget Level | Creator Fees | Ad Spend | Ratio |
|-------------|-------------|----------|-------|
| **$2,500 test** | $500–$1,000 (5–10 nano creators) | $1,500–$2,000 (boost top 2–3) | 1:2 to 1:3 |
| **$5,000 test** | $1,000–$2,000 (10–15 creators) | $3,000–$4,000 (boost top 3–5) | 1:2 to 1:3 |
| **$10,000 campaign** | $2,000–$3,000 (15–20 creators) | $7,000–$8,000 (scale winners) | 1:3 to 1:4 |
| **$25,000+ scale** | $5,000 (ongoing creator pipeline) | $20,000 (heavy amplification) | 1:4 to 1:5 |

As you scale, the ratio shifts more toward ad spend because you're reusing proven creative (the winning creators keep making content) and spending more on distribution.

**Budget waterfall within ad spend:**
- 20% on testing new creator content
- 50% scaling top performers
- 30% amplifying proven content through whitelisting/Spark Ads

### Attribution Setup for App Install Campaigns

Proper attribution is critical for measuring CPI and ROAS across Spark Ads and partnership ads.

#### AppsFlyer Setup (Recommended for Zerocap)

**TikTok integration:**
1. In AppsFlyer dashboard, add TikTok for Business as a partner (use the `tiktokglobal_int` integration — the legacy `bytedanceglobal_int` was deprecated March 2024)
2. No additional configuration needed for basic attribution — AppsFlyer auto-detects TikTok installs
3. In TikTok Ads Manager: go to Tools > Events > App Event > select AppsFlyer as your MMP
4. Conversion events (install, registration, in-app purchase) flow automatically

**Meta integration:**
1. In AppsFlyer, add Meta Ads as a partner
2. Configure SKAdNetwork interoperability (AppsFlyer shares conversion value mapping with Meta)
3. In Meta Ads Manager, connect the app and verify the AppsFlyer SDK

**YouTube/Google integration:**
1. In AppsFlyer, add Google Ads as a partner
2. Link your Google Ads account
3. App campaign attribution flows through Google's SRN integration

#### SKAdNetwork (SKAN) Considerations for iOS

Since Zerocap is an iOS app, SKAN is critical:

- SKAN operates without IDFA, so it works regardless of ATT consent
- Configure conversion values in AppsFlyer to map meaningful post-install events (e.g., "completed onboarding," "day-3 retention," "made purchase")
- SKAN postback copies should be sent to AppsFlyer (iOS 15+) for verification
- Meta and TikTok both support SKAN interoperability through AppsFlyer

**Attribution windows:**
- TikTok: 7-day click-through, 1-day view-through (default)
- Meta: 7-day click, 1-day view (default); can extend to 28-day click
- YouTube/Google: 30-day click, 1-day view

**Important:** Expect attribution discrepancies between TikTok/Meta self-reported installs and AppsFlyer-attributed installs. AppsFlyer uses last-touch attribution, while platforms self-attribute more generously. Use AppsFlyer as the source of truth.

---

## 5. Negotiation with Creators for Whitelisting Rights

### Include Spark Ad Authorization in the Initial Deal

The most important principle: **negotiate whitelisting rights upfront, not after the fact.** It's cheaper and simpler to include it in the original creator brief than to go back and ask for it later.

**In the initial outreach/brief, include:**

> "As part of this partnership, we'd love to put some paid ad spend behind the video to help it reach more people. This means we'll run it as a Spark Ad (TikTok) / Partnership Ad (Instagram) — the video stays on your profile, you keep all the engagement and followers, we just boost its reach. We'd need the Spark Ad authorization code for [30/60/365] days."

**Structure the deal as a single package:**
- Content creation fee: $X
- Whitelisting/Spark Ad authorization: included (or +Y% premium)
- Usage rights: [duration] days
- Platforms: TikTok, Instagram, YouTube (specify each)

### What Creators Typically Charge for Whitelisting

**Industry standard pricing:**

| Component | Typical Rate |
|-----------|-------------|
| **Whitelisting access fee** | 20–25% of base content fee per 30-day window |
| **Extended usage (90 days)** | 10–25% additional |
| **12-month license** | 50% of original content fee |
| **Exclusivity premium** | 15–30% additional (category exclusivity) |
| **Cross-platform** | Additional 10–15% per extra platform |

**Example pricing for Zerocap:**

| Creator Tier | Base Fee | + 60-day Spark Auth | Total |
|-------------|----------|---------------------|-------|
| Nano (1–10K) | $100–$300 | +$25–$75 | $125–$375 |
| Micro (10–50K) | $300–$800 | +$75–$200 | $375–$1,000 |
| Mid (50–200K) | $800–$2,500 | +$200–$625 | $1,000–$3,125 |
| Macro (200K–1M) | $2,500–$10,000 | +$625–$2,500 | $3,125–$12,500 |

**Cost-saving tactics:**
- Bundle whitelisting into the base fee for nano/micro creators (many don't know they can charge extra)
- Offer performance bonuses instead of higher base fees: "We'll pay an extra $X if the Spark Ad exceeds Y installs"
- Negotiate lifetime authorization for top performers in exchange for ongoing partnership
- Frame it as a benefit: "More views = more followers for you"

### How to Explain Spark Ads to Creators Who Don't Know What It Is

Many creators — especially nano and micro — have never heard of Spark Ads. Here's how to explain it simply:

**Simple explanation (for DMs/email):**

> "A Spark Ad means we put ad budget behind your video so more people see it — but it still shows as your video, on your profile. You keep all the likes, comments, followers, and views. It's like someone boosting your post for you, for free. All we need is an authorization code from TikTok (takes 30 seconds to generate)."

**If they ask "what's in it for me?":**

> "Your video gets seen by potentially hundreds of thousands more people. All the engagement goes to your account — likes, comments, follows, profile visits. You'll likely gain followers from it. And we're paying you for the authorization on top of the content fee."

**If they're hesitant:**

> "You're in full control. You can revoke the authorization at any time. The code expires after [30/60] days automatically. We can't change your video or caption — it stays exactly as you posted it. The only thing that changes is more people see it."

**Step-by-step instructions to include in your brief:**

> **How to generate your Spark Ad code (takes 30 seconds):**
> 1. Open TikTok > go to the video we're partnering on
> 2. Tap the three dots (•••) on the right side
> 3. Scroll to "Ad settings"
> 4. Toggle on "Ad authorization"
> 5. Select "[60] days" for duration
> 6. Tap "Authorize" then "Generate Code"
> 7. Tap "Copy Code" and send it to us
>
> That's it! Your video stays on your profile. You keep all engagement.

### Template Contract Language for Whitelisting/Spark Ad Rights

#### Clause 1: Paid Amplification Authorization

> **Paid Amplification Rights.** Creator grants Brand a non-exclusive, non-transferable license to promote the Deliverables as paid advertisements using the platform-native amplification tools available on each Approved Platform, including but not limited to TikTok Spark Ads, Meta/Instagram Partnership Ads, and YouTube BrandConnect Partnership Ads (collectively, "Paid Amplification"). The Deliverables will be promoted from Creator's account handle(s) and will appear under Creator's profile identity. Brand may add platform-provided advertising elements (e.g., "Sponsored" labels, call-to-action buttons, tracking pixels) but may not alter the underlying content without Creator's prior written approval.

#### Clause 2: Authorization Duration & Renewal

> **Authorization Period.** Creator shall provide all necessary platform authorization codes (e.g., TikTok Spark Ad codes, Instagram Partnership Ad permissions) within [48 hours] of posting each Deliverable. The initial Paid Amplification authorization period shall be [60] days from the date of authorization. Brand may request renewal for additional [30-day] periods at a fee of [$ amount or percentage] per renewal period, subject to Creator's written approval. All authorization rights expire automatically at 23:59 (Creator's local time) on the final day of the authorization period unless renewed in writing.

#### Clause 3: Platform-Specific Obligations

> **Platform Authorization.** Creator agrees to:
> (a) Generate and deliver TikTok Spark Ad authorization codes for all TikTok Deliverables within the timeframe specified above;
> (b) Grant account-level or content-level Partnership Ad permissions via Meta Business Manager for all Instagram Deliverables;
> (c) Link applicable YouTube Deliverables through YouTube BrandConnect and grant Brand Partner Access where available;
> (d) Maintain all authorization permissions in active status for the duration of the Authorization Period and not revoke access without [7 days'] prior written notice to Brand.

#### Clause 4: Content Integrity

> **Content Modifications.** Brand shall not edit, modify, crop, or alter the Deliverables in any way when used for Paid Amplification. All Paid Amplification shall use the original Deliverable as posted by Creator. Creator acknowledges that captions and content should be in final form prior to generating authorization codes, as platform restrictions may prevent post-authorization edits.

#### Clause 5: Data & Reporting

> **Performance Data.** Creator grants Brand access to view performance metrics for the Deliverables during the Authorization Period through platform-provided analytics tools. Brand may use anonymized, aggregated performance data for internal optimization purposes. Brand shall not share Creator's audience demographic data with third parties without Creator's consent.

#### Clause 6: Compensation

> **Whitelisting Fee.** In consideration of the Paid Amplification rights granted herein, Brand shall pay Creator:
> (a) Content Creation Fee: $[amount] for production and posting of [number] Deliverables;
> (b) Paid Amplification Access Fee: $[amount] for the initial [60-day] Authorization Period;
> (c) Renewal Fee: $[amount] per [30-day] renewal period, if exercised;
> (d) Performance Bonus: $[amount] per [1,000 installs / specified milestone] attributed to the Paid Amplification campaign, payable [monthly/quarterly] based on Brand's MMP reporting.

---

## Quick Reference: Platform Comparison

| Feature | TikTok Spark Ads | Instagram Partnership Ads | YouTube BrandConnect |
|---------|-----------------|--------------------------|---------------------|
| **Auth method** | Authorization code per video | Permission via Meta Business or ad code | Video linking via BrandConnect |
| **Setup complexity** | Low (code copy-paste) | Medium (requires Meta Business accounts) | Medium-High (YPP + BrandConnect tab) |
| **Creator minimum** | Any public account | Professional account (creator/business) | 25K+ subscribers, YPP member |
| **Duration options** | 7, 30, 60, 365 days | Ongoing until revoked | Per-video linking |
| **Content formats** | Videos only | Reels, Stories, Feed, Carousels | Long-form, Shorts |
| **App install support** | Native objective | Native objective | Via App campaigns, Demand Gen |
| **Best for Zerocap** | Primary channel | Secondary channel | Testing channel |
| **Typical CPM** | $3.50–$10 | $6–$12 | ~$4 (Shorts) |
| **Performance lift vs. standard** | 142% engagement, 37% lower CPA | 53% higher CTR, 19% lower CPA | 20% higher conversions (Shorts) |

---

## Recommended Rollout Plan for Zerocap

**Month 1: TikTok Spark Ads Pilot ($2,500)**
- Commission 10 nano/micro creators ($100–$250 each = $1,000–$2,500)
- All creators include 60-day Spark Ad authorization in the deal
- Boost top 3 performers with remaining budget
- Establish baseline CPI

**Month 2: Scale TikTok + Add Instagram ($5,000)**
- Scale winning TikTok Spark Ads ($2,000–$3,000)
- Commission 5 new creators who cross-post TikTok + Instagram Reels ($1,000–$1,500)
- Run Instagram Partnership Ads on top Reels content ($500–$1,000)
- Compare CPI across platforms

**Month 3: Full Funnel ($10,000+)**
- Ongoing creator pipeline: 10–15 new creators/month
- 70% of ad spend on proven Spark Ad winners
- 20% on Instagram Partnership Ads
- 10% on YouTube Shorts testing via BrandConnect
- Attribution fully set up in AppsFlyer; optimizing for post-install retention, not just installs
