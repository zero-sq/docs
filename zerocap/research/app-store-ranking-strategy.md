# App Store Ranking & Discovery Strategy for Zerocap

**Date:** 2026-03-13
**Product:** Zerocap -- iOS AI companion/tamagotchi app. Point camera at real-world objects, AI transforms them into cute living pets with personality traits (6 million trait combinations).
**Context:** Bootstrapped team, $600 Apple Ads test running, TikTok-first organic GTM already in motion. This doc covers everything needed to maximize App Store discoverability alongside organic channels.

---

## Table of Contents

1. [App Store Category Selection](#1-app-store-category-selection)
2. [Keyword Strategy & Research](#2-keyword-strategy--research)
3. [App Store Listing Optimization](#3-app-store-listing-optimization)
4. [App Store Featuring](#4-app-store-featuring)
5. [Review Generation Strategy](#5-review-generation-strategy)
6. [Apple Search Ads Strategy](#6-apple-search-ads-strategy)
7. [Ranking Algorithm Factors (2025-2026)](#7-ranking-algorithm-factors-2025-2026)
8. [Launch Day ASO Tactics](#8-launch-day-aso-tactics)
9. [Ranking Benchmarks & Expected Organic Installs](#9-ranking-benchmarks--expected-organic-installs)
10. [Competitor Keyword Analysis](#10-competitor-keyword-analysis)

---

## 1. App Store Category Selection

### The Decision: Games > Simulation (Primary) + Entertainment (Secondary)

This is one of the most consequential ASO decisions. The category determines which top charts you appear on, which competitors you sit next to, and how much daily volume you need to crack visible chart positions.

### Category Analysis

| Category | Total Apps | Competition Density | Relevance to Zerocap | Chart Visibility |
|----------|-----------|-------------------|---------------------|-----------------|
| **Games > Simulation** | ~55,300 total games on iOS (2025) | High but fragmented across 20+ subcategories | **Perfect fit** -- virtual pet is simulation | Subcategory charts are less crowded than overall Games |
| **Entertainment** | 87.5% of apps are non-game | Extremely crowded overall | Moderate -- "entertainment" is broad | Hard to stand out; you compete with Netflix, YouTube, TikTok |
| **Lifestyle** | Large but lower engagement | Moderate | Weak -- lifestyle implies utility (health, habits) | Easier to chart but wrong audience |
| **Games > Casual** | Most competitive game subcategory | Very high | Good fit for gameplay mechanics | Hardest subcategory to crack |

### Recommendation: Games > Simulation

**Why Simulation wins:**

1. **Audience intent alignment.** People browsing Games > Simulation are looking for exactly what Zerocap offers: virtual worlds, pet raising, life simulation. Entertainment browsers are looking for video streaming and content consumption apps.

2. **Subcategory charts are your friend.** Games has 20+ subcategories. Simulation is big enough to have a dedicated chart but small enough that an indie app can realistically reach the top 50 with modest daily downloads (hundreds, not tens of thousands).

3. **Competitor positioning.** Every major virtual pet app (Peridot, My Tamagotchi Forever, Pou) lists under Games > Simulation. Appearing in the same category means you show up in "You Might Also Like" recommendations alongside them.

4. **Games category gets featured more aggressively.** Apple has a dedicated "Game of the Day" slot and games-specific editorial content on the Today tab. Entertainment apps compete for the more generic "App of the Day."

5. **Revenue signal advantage.** Games account for 60% of App Store revenue ($52.5B in 2025) despite being only 12.5% of apps. Apple has strong economic incentives to surface games prominently.

**What about the $12.28 average CPI for Games?** This matters for paid acquisition (covered in Section 6) but has zero impact on organic ranking. Category selection should optimize for organic discovery, not ad costs.

### Secondary Category: Entertainment

Use Entertainment as the secondary category to appear in both chart sets. This catches users who browse Entertainment looking for "something fun" without specifically searching for games. You get dual chart exposure at no cost.

### What NOT to Pick

- **Lifestyle**: Wrong audience. Lifestyle users want meditation apps and habit trackers, not AI pets.
- **Photo & Video**: Tempting because of the camera mechanic, but positions you against professional photo editors. Wrong competitive set entirely.
- **Social Networking**: Only makes sense if the app has robust social features at launch (multiplayer, friend feeds). Premature for v1.

Sources:
- [App Store Statistics 2026 -- SQ Magazine](https://sqmagazine.co.uk/app-store-statistics/)
- [App Store Gaming Revenue 2025 -- 9to5Mac](https://9to5mac.com/2026/02/25/app-store-gaming-revenue-hit-52-5b-in-2025-topping-google-play-and-steam-combined-report/)
- [Casual Games Report H1 2025 -- AppMagic](https://appmagic.rocks/research/casual-report-h1-2025)

---

## 2. Keyword Strategy & Research

### How App Store Keyword Ranking Works

Apple indexes keywords from four metadata sources, weighted in this order:

| Source | Weight | Character Limit | Visibility |
|--------|--------|----------------|-----------|
| **App Title** | Highest | 30 characters | Visible to users |
| **App Subtitle** | High | 30 characters | Visible to users |
| **Keyword Field** | Medium | 100 characters | Hidden (only Apple sees it) |
| **Screenshot Captions** | Medium (new in June 2025) | No hard limit | Visible to users |
| **Description** | Low (via Apple AI extraction) | 4,000 characters | Visible to users |

**Critical rule:** Never duplicate keywords across title, subtitle, and keyword field. Each slot should contain unique terms. Apple automatically combines them when ranking.

### Keyword Categories for Zerocap

#### Tier 1: High-Value Core Keywords

These have the best combination of search volume, relevance, and realistic rankability for a new app.

| Keyword | Search Volume Signal | Competition | Notes |
|---------|---------------------|------------|-------|
| virtual pet | High | Medium-High | Core category term. Peridot, Pou, Tamagotchi all target this. |
| AI pet | Medium | Low-Medium | Emerging term, growing fast. Few direct competitors. |
| pet game | High | High | Broad, high volume. Worth targeting but hard to rank initially. |
| tamagotchi | Medium-High | Low | Brand name, but Bandai's app is mediocre -- opportunity to rank. |
| cute pet | Medium | Medium | Strong emotional intent. Good conversion. |
| pet creator | Low-Medium | Low | Descriptive of Zerocap's unique mechanic. Low competition. |

#### Tier 2: Long-Tail Keywords (Lower Competition, Higher Conversion)

These are where a new app can actually win. Less search volume but easier to rank and higher intent.

| Keyword | Why It Works |
|---------|-------------|
| AI tamagotchi | Literally describes the product. Almost no competition. |
| camera pet | Unique to Zerocap's mechanic. Zero competition. |
| pet maker | Describes the creation mechanic. Low competition. |
| virtual pet creator | Specific enough to rank quickly. |
| AI companion pet | Combines two growing categories. |
| cute AI | Broad but captures emerging search behavior. |
| pet personality | Unique to Zerocap's trait system. |
| real world pet | Describes the camera-to-pet mechanic. |
| object to pet | Extremely specific. If anyone searches this, they want Zerocap. |
| raise a pet | High intent for pet simulation seekers. |
| pet simulator | Standard category term. |
| digital pet | Alternative phrasing of "virtual pet." |

#### Tier 3: Adjacent/Competitor Keywords

Target searches where people are looking for apps similar to yours.

| Keyword | Strategy |
|---------|----------|
| peridot | Competitor conquesting. Users disappointed with Peridot may try alternatives. |
| pou | Massive brand. Some traffic will spill over. |
| talking tom | Huge volume. Even ranking #50 for this sends meaningful traffic. |
| pengu | Direct competitor (Born/Friends app). |
| replika | AI companion searchers. Different product but adjacent audience. |
| character ai | High volume AI companion term. |

#### Tier 4: Trending/Seasonal Keywords

These change over time. Monitor and swap in quarterly.

| Keyword | Timing |
|---------|--------|
| AI filter | Evergreen since Ghibli filter trend (2025). |
| photo pet | Emerging from AI photo transformation trends. |
| AI art | Broad but captures creative AI interest. |

### Keyword Field Optimization (100 Characters)

**Rules for the hidden keyword field:**
- Separate keywords with commas, NO spaces after commas
- Use singular forms only (Apple matches plurals automatically)
- Don't repeat any word already in your title or subtitle
- Don't use "app" or "game" (Apple adds these automatically)
- Don't use competitor brand names here (Apple may reject; use Apple Ads for competitor targeting instead)

**Example keyword field for Zerocap:**

```
tamagotchi,creator,maker,camera,object,transform,cute,raise,digital,companion,simulator,personality,trait,adopt,collect,filter,AR,creature
```

That's 98 characters. Every word is unique, not duplicated from title/subtitle, and covers core, long-tail, and adjacent terms.

### Keyword Tools & Methodology

**Recommended tools (budget-conscious):**

| Tool | Cost | Best For |
|------|------|----------|
| **AstroASO** | $9/month | Native macOS app. Keyword data from Apple Search Ads. Daily difficulty scores. Best value for indie devs. |
| **GrowASO** | $49/year | 60,000+ keyword database. Budget-friendly tracking. |
| **AppTweak** | $69/month (starter) | Industry standard. Volume, difficulty, competitor analysis. Worth it once revenue supports it. |
| **MobileAction** | $49/month (starter) | Comprehensive platform. Keyword suggestions, difficulty scores, competitor tracking. |
| **Apple Search Ads (free)** | $0 | Run Discovery campaigns to find what users actually search. The data is invaluable even if you pause the campaigns. |

**Methodology for keyword iteration:**

1. **Pre-launch:** Research using AstroASO or similar. Build initial keyword set. Prioritize long-tail terms where you can realistically rank top 10.
2. **Week 1-2 post-launch:** Check which keywords you're actually ranking for using App Store Connect's Acquisition > Source Type > App Store Search data.
3. **Week 3-4:** Swap out keywords with zero impressions. Double down on any keyword where you're ranking 10-30 (close to top 10, needs a push).
4. **Monthly thereafter:** Rotate 20-30% of keywords per update cycle. Test new terms, drop underperformers. Track keyword-level install attribution if running Apple Ads.
5. **After viral moments:** When a TikTok goes viral, immediately add related long-tail terms people might search (e.g., if a "turn your shoe into a pet" video blows up, add "shoe pet" to keyword field).

### Post-Launch Keyword Iteration Cadence

| Timeframe | Action | Why |
|-----------|--------|-----|
| **Day 1-7** | Monitor impressions per keyword via App Store Connect | See which keywords Apple is actually indexing you for |
| **Day 7-14** | First keyword swap -- remove zero-impression terms, add alternatives | Don't waste character space on terms that aren't working |
| **Day 14-30** | Analyze conversion rate per keyword (if running Apple Ads) | Impressions mean nothing if nobody taps |
| **Monthly** | Full keyword audit: rotate bottom 20%, test 3-5 new terms | ASO is iterative, not set-and-forget |
| **Quarterly** | Major keyword refresh aligned with app updates | New features = new keyword opportunities |

Sources:
- [ASO Keyword Research 2026 -- MobileAction](https://www.mobileaction.co/blog/aso-keyword-research/)
- [App Store Keyword Research Guide 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/app-store-keyword-research-aso)
- [App Store Keywords Optimization -- SplitMetrics](https://splitmetrics.com/blog/app-store-keyword-optimization/)
- [App Store Keywords Optimization -- App Radar](https://appradar.com/academy/app-store-keywords-optimization)
- [ASO Tools 2025 -- AppDrift](https://appdrift.co/blog/15-best-app-store-optimization-tools)

---

## 3. App Store Listing Optimization

### Title & Subtitle Formulas

**Character limits:** 30 characters each for title and subtitle.

**The proven formula:**

```
Title:  [Brand Name] - [Primary Keyword Phrase]
Subtitle: [Action Verb] + [Benefit/Feature Keywords]
```

**Recommended title options for Zerocap:**

| Option | Characters | Keywords Captured |
|--------|-----------|-------------------|
| `Zerocap - AI Pet Creator` | 24 chars | AI, pet, creator |
| `Zerocap - Virtual Pet AI` | 24 chars | virtual, pet, AI |
| `Zerocap: AI Pet Companion` | 26 chars | AI, pet, companion |
| `Zerocap - AI Tamagotchi` | 24 chars | AI, tamagotchi |

**Recommended:** `Zerocap - AI Pet Creator` -- captures the creation mechanic that makes Zerocap unique. "Creator" signals that you MAKE something, not just adopt a pre-made pet.

**Recommended subtitle options:**

| Option | Characters | Keywords Captured |
|--------|-----------|-------------------|
| `Turn Real Objects Into Pets` | 27 chars | real, objects, pets |
| `Camera to Cute Living Pets` | 27 chars | camera, cute, living, pets |
| `Scan Anything, Raise a Pet` | 27 chars | scan, raise, pet |
| `Create Pets From Real Life` | 27 chars | create, pets, real, life |

**Recommended:** `Turn Real Objects Into Pets` -- this is the single-sentence pitch that communicates the unique mechanic and generates curiosity.

**Final recommendation:**
```
Title:    Zerocap - AI Pet Creator
Subtitle: Turn Real Objects Into Pets
```

This combination captures: AI, pet, creator, real, objects, pets -- plus the brand name. The subtitle doubles as a curiosity hook that makes people want to see how it works.

### Screenshot Strategy

**The first 3 screenshots are everything.** 90% of visitors never scroll past the third screenshot. On iOS, users see the first three screenshots in search results before even tapping into your listing.

Users spend approximately 7 seconds viewing screenshots. Follow the **Value-Usage-Trust** framework:

#### Screenshot 1: "The Wow" (Value)
- Show a side-by-side: real-world object on the left, cute AI pet on the right
- Large text overlay: **"Point. Scan. Meet Your Pet."** (or similar 5-7 word hook)
- This must immediately communicate what makes Zerocap different
- Use the most visually impressive/cute pet transformation you have
- Bright, vibrant colors. The pet should look irresistibly cute.

#### Screenshot 2: "The How" (Usage)
- Show the camera interface in action -- phone pointed at an object, AI transformation happening
- Text overlay: **"Any Object Becomes a Living Pet"**
- This answers the viewer's question: "Wait, how does that work?"
- Show the transformation mid-process if possible (object dissolving into pet)

#### Screenshot 3: "The Depth" (Trust)
- Show the personality trait system -- a pet with its unique trait card/profile
- Text overlay: **"6 Million Unique Personalities"**
- This communicates that it's not a one-trick gimmick -- there's depth and collectibility
- Shows social proof through scale (millions of combinations)

#### Screenshots 4-6 (for scrollers):
- **Screenshot 4:** Pet collection gallery -- show 6-8 different pets from different objects
- **Screenshot 5:** Interaction/care mechanics -- feeding, playing, pet responding
- **Screenshot 6:** Sharing/social -- "Share your pets with friends" with a mock social post

#### Design Rules

| Rule | Implementation |
|------|---------------|
| **Match TikTok content style** | Screenshots should look like polished versions of your TikTok videos. Viewers coming from TikTok expect visual consistency. |
| **"Ugly ads" outperform polish** | Raw, authentic-looking screenshots trigger less ad blindness than glossy studio renders. Show actual gameplay. |
| **Mobile-first framing** | Full-screen vertical captures. No phone device frames wrapping the screenshots. |
| **Minimal text** | Maximum 5-7 words per screenshot overlay. Dense text = bounce. |
| **Bright, warm colors** | Pet/cute apps convert better with warm palettes (pinks, oranges, soft blues) vs. cold/dark palettes. |

#### A/B Testing with Product Page Optimization (PPO)
- Apple allows testing up to 3 alternate versions against your original
- Tests run up to 90 days
- Average successful A/B test boosts conversion by 10-25%
- **Priority test:** Try a version where Screenshot 1 is a short transformation animation (if using App Preview Video) vs. a static before/after

### App Preview Video

**This is the single highest-impact visual asset.** Adding a preview video boosts conversion by 20-40% vs. screenshots alone. For a new-category app like Zerocap where people need to SEE the mechanic, video is not optional.

**Specs:**
- 15-30 seconds of real in-app footage (Apple requirement: must be actual in-app captures)
- Vertical format (1080x1920 for iPhone)
- Auto-plays in search results (silent, with captions)

**Storyboard:**

| Seconds | Content | Purpose |
|---------|---------|---------|
| 0-3 | Most impressive pet transformation -- object on screen, magical animation, cute pet appears | Hook. This is TikTok logic: first 3 seconds decide everything. |
| 3-8 | Show 3-4 rapid-fire transformations of different objects (coffee mug, shoe, plant, book) | Communicate "ANY object works" |
| 8-15 | Pet personality reveal -- traits appearing, pet reacting with personality | Show depth beyond the transformation gimmick |
| 15-22 | Pet interaction -- user caring for pet, pet responding | Demonstrate the ongoing engagement loop |
| 22-28 | Collection view -- gallery of many unique pets | Show collectibility and variety |
| 28-30 | App icon + tagline | Brand recall |

**Update the preview video 2-4 times per year.** Data shows top apps that refresh visual assets quarterly rank higher due to freshness signals.

### Description Optimization

The description has low direct keyword weight, but Apple's AI now extracts semantic meaning from it. Write for humans first, keywords second.

**Structure:**

```
[Opening hook -- 1-2 sentences that capture the magic]

[Core value proposition -- what you do and why it's different]

[Feature list -- 5-6 bullet points]

[Social proof or press mentions if available]

[Call to action]
```

**Above the fold (first 3 lines before "more" tap):**
Only ~170 characters show before the user taps "more." These are the only description words most people will read. Make them count.

**Example:**
```
Point your camera at anything. A coffee mug. A shoe. A houseplant.
Watch AI transform it into a cute, living pet with its own unique
personality. 6 million trait combinations. No two pets are alike.
```

### Screenshot Caption Optimization (New in June 2025)

As of June 2025, Apple indexes text from screenshot captions for keyword ranking. This is a new metadata surface that most competitors haven't optimized yet.

**How to use it:** Write natural-language captions for each screenshot that incorporate keywords not already in your title, subtitle, or keyword field. Each caption is additional keyword surface area.

**Example captions:**
- Screenshot 1: "Transform everyday objects into adorable AI creatures"
- Screenshot 2: "Use your camera to create unique virtual pets"
- Screenshot 3: "Discover millions of personality combinations for your digital companion"

These captions add: transform, everyday, adorable, creatures, camera, create, unique, virtual, discover, millions, personality, digital, companion -- all indexed for search.

Sources:
- [Screenshots Guide 2025 -- ASOMobile](https://asomobile.net/en/blog/screenshots-for-app-store-and-google-play-in-2025-a-complete-guide/)
- [Screenshot Optimization -- AppTweak](https://www.apptweak.com/en/aso-blog/how-to-optimize-your-app-screenshots)
- [App Preview Videos -- SplitMetrics](https://splitmetrics.com/blog/create-app-preview-video-app-store-ios/)
- [Visual ASO Guide -- Business of Apps](https://www.businessofapps.com/guide/app-icon-screenshots-preview-video-optimization-guide/)
- [Text Metadata Optimization -- SplitMetrics](https://splitmetrics.com/glossary/metadata-optimization-guide-to-writing-app-title-subtitle-and-description/)
- [App Store Product Page -- Apple Developer](https://developer.apple.com/app-store/product-page/)
- [App Store Algorithm Update 2025 -- Appfigures](https://appfigures.com/resources/guides/app-store-algorithm-update-2025)

---

## 4. App Store Featuring

### How Featuring Works

Apple's editorial team hand-picks apps for featuring placements on the Today tab, category pages, and search results. The main placements:

| Placement | Impact | Frequency |
|-----------|--------|-----------|
| **App of the Day** | Massive -- can drive 10-50x normal daily downloads | 1 app per day globally |
| **Game of the Day** | Same tier as App of the Day, games-specific | 1 game per day globally |
| **Today Tab Story** | High -- prominent editorial placement | Multiple per day |
| **Category Feature** | Moderate -- visible to category browsers | Rotated regularly |
| **"You Might Also Like"** | Steady -- algorithmic, based on user behavior | Ongoing, automatic |

### What Apple Looks For in 2025-2026

Based on Apple's 2025 App Store Awards and editorial patterns, Apple prioritizes:

1. **Design excellence.** Apps that feel native to iOS, follow Human Interface Guidelines, and look premium. This is non-negotiable.

2. **Innovation in user experience.** Apps that do something genuinely new. Zerocap's camera-to-pet mechanic qualifies -- it's a novel interaction pattern.

3. **Apple technology integration.** Apps that use Apple frameworks (ARKit, Core ML, Vision, SwiftUI). If Zerocap uses on-device ML or ARKit for the camera experience, highlight this prominently.

4. **Cultural relevance and timeliness.** Apps that align with current cultural moments, seasonal events, or trending topics.

5. **Accessibility.** VoiceOver support, Dynamic Type, good contrast ratios. Apple specifically calls out accessibility in their featuring criteria.

6. **Privacy-forward approach.** Minimal data collection, on-device processing, transparent privacy labels. Apple rewards apps that align with their privacy narrative.

### The AI Angle: Nuanced

**Apple's stance on AI apps is subtle but important.** Based on the 2025 App Store Awards:

- Apple does NOT feature apps that lead with "AI" as a marketing gimmick
- Apple DOES feature apps where AI makes the experience magical without being the headline
- The iPhone App of the Year 2025 (Tiimo) uses AI but positions itself as "a visual planner" -- the AI is invisible
- Apple's philosophy: "AI should enhance existing workflows rather than create entirely new categories of interaction"

**Zerocap implication:** Don't position as "AI pet app" when pitching for featuring. Position as "a new way to create and care for virtual pets" where the AI is the magic behind the curtain. The camera mechanic and the pet personality should be the story, not the AI model.

### How to Submit a Featuring Nomination

Apple introduced **Featuring Nominations** in App Store Connect starting with iOS 18:

1. Go to **App Store Connect > Your App > Featuring > Nominations**
2. Click **"+"** next to Nominations, then **Create Nomination**
3. Fill out the nomination form:
   - **Reason**: New app launch, major update, or seasonal content
   - **Planned date**: Must be at least 3 weeks in advance (Apple says 2 weeks minimum, but 3+ is safer)
   - **Key differentiators**: What makes this app special, innovative, unique
   - **Apple technology usage**: List every Apple framework you use (ARKit, Core ML, Vision, Metal, SwiftUI, etc.)
   - **Screenshots and assets**: High-quality marketing materials
4. Submit. Apple reviews within ~30 days.
5. If selected, you'll get a notification via the App Store Connect app.

**Bulk submission:** You can also upload a CSV file for multiple nominations (useful for planning seasonal features months ahead).

**Template fields in the CSV:** App Apple ID, nomination type, locale, planned date, description of what's new, and supporting details.

### Maximizing Featuring Chances for Zerocap

| Action | Timing | Why |
|--------|--------|-----|
| **Submit featuring nomination** | 3-4 weeks before launch | Give Apple time to review |
| **Highlight Apple tech** | In nomination | ARKit? Core ML? On-device processing? These are featuring magnets. |
| **Time launch with Apple events** | If possible | Launching near WWDC, iPhone launch, or iOS updates when Apple needs fresh content to showcase |
| **Prepare high-res marketing assets** | Before nomination | Apple needs your assets at specific sizes for Today tab features |
| **Achieve 4.5+ star rating first** | Before expecting featuring | Over half of featured apps have 4.5+ stars. |
| **Show accessibility features** | In nomination | VoiceOver, Dynamic Type, reduced motion support |
| **Build a relationship with Apple** | Ongoing | Attend WWDC, join Apple developer programs, participate in App Store events |
| **Release meaningful updates consistently** | Monthly | Shows Apple you're invested in the app long-term |

### "App of the Day" -- What It Takes

Realistic assessment for an indie app:

- **Possible?** Yes. Apple regularly features indie apps and small studios. "App of the Day" is not reserved for big companies.
- **Likely at launch?** No. Most "App of the Day" picks have an established track record, strong ratings, and design polish. Target this for 3-6 months post-launch after building reviews and shipping 2-3 updates.
- **Best path:** Get a category feature or Today Tab Story first. These are stepping stones. Apple's editorial team notices apps that perform well in smaller features.
- **The magic ingredient:** A compelling human story. "Two indie developers building the next evolution of Tamagotchi" is the kind of narrative Apple's editorial team gravitates toward. Prepare a press-ready founder story.

Sources:
- [Getting Featured -- Apple Developer](https://developer.apple.com/app-store/getting-featured/)
- [Featuring Nominations -- Apple Developer](https://developer.apple.com/help/app-store-connect/manage-featuring-nominations/nominate-your-app-for-featuring/)
- [How to Get Featured 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/how-to-get-your-app-featured-on-the-app-store)
- [How to Get Featured -- RadASO](https://radaso.com/blog/apple-app-store-featuring-how-to-get-into-the-recommended-apps)
- [Apple Snubs AI Apps 2025 -- TechBuzz](https://www.techbuzz.ai/articles/apple-snubs-ai-apps-but-crowns-ai-powered-winners-in-2025)
- [App Store Awards 2025 -- Apple Developer](https://developer.apple.com/app-store/app-store-awards-2025/)

---

## 5. Review Generation Strategy

### Why Reviews Matter for Ranking

- Apps with 4.5+ stars convert at significantly higher rates -- an increase from 3.6 to 4.2 stars correlated with ~60% higher conversion
- Over 50% of featured apps have 4.5+ star ratings
- Apple's algorithm uses review quality, quantity, and recency as ranking signals
- An extra half-star in average rating can increase download conversion by up to 25%

### Apple's Rules

- You can prompt for ratings using `SKStoreReviewController` up to **3 times per 365-day period**
- The system decides when to actually show the prompt (Apple may suppress it if the user has recently been prompted by another app)
- You cannot customize the prompt UI -- it's Apple's standard dialog
- You cannot incentivize reviews (no "rate us for a reward")
- You cannot redirect negative reviews away from the App Store

### When to Prompt for Zerocap

**The golden rule for companion apps: prompt after an emotional high point, never during friction.**

| Trigger | Why It Works | Implementation |
|---------|-------------|----------------|
| **After first pet creation** | User just experienced the core "wow" moment. Highest delight point in the journey. | Prompt 5-10 seconds after the pet appears, before they navigate away. |
| **After naming their pet** | Naming creates emotional ownership. This is a commitment signal. | Prompt after name is confirmed and pet responds to its name. |
| **After 3rd pet creation** | User has demonstrated repeated engagement. They clearly like the app. | Track pet_created count, prompt on 3rd completion. |
| **After 5th session** | Session-based trigger ensures the user has come back multiple times (retention signal). | Combine with a positive moment (not cold on app open). |
| **After sharing a pet** | User just voluntarily promoted the app. They're clearly a fan. | Prompt 3-5 seconds after share completion confirmation. |

### When NOT to Prompt

| Moment | Why It's Bad |
|--------|-------------|
| First launch / onboarding | User hasn't experienced value yet. Intrusive. |
| After a crash or error | Negative emotion = negative review. |
| During camera scanning | Interrupts the core interaction. |
| Mid-animation / transformation | Breaks the magic moment. |
| On app open (cold start) | No context, no delight trigger. |
| After failed pet creation | Frustration moment. |

### Review Quality Strategy

Getting reviews is only half the battle. Getting GOOD reviews is what matters.

**Pre-filter before prompting:**
1. Crash-free for last 2+ sessions
2. Has created at least 1 pet successfully
3. At least 2 sessions in the app
4. No open bug reports or support tickets
5. At least 90 days since last prompt
6. Has not dismissed a previous prompt

**This filtering approach means only happy, engaged users see the review prompt.** Result: higher average rating.

### Responding to Reviews

- **Respond to every review in the first 3 months.** Apple signals this as developer engagement.
- Respond within 24 hours when possible
- For negative reviews: acknowledge the issue, provide a fix timeline, offer to help via email
- For positive reviews: thank them personally, mention specific features they liked
- Reviews with developer responses can be updated by users -- a helpful response can turn a 2-star into a 4-star

### Target Metrics

| Metric | Target | Why |
|--------|--------|-----|
| **Average rating** | 4.5+ stars | Threshold for featuring eligibility and maximum conversion rate |
| **Total reviews** | 50+ in first month | Critical mass for social proof in the listing |
| **Response rate** | 100% (first 3 months) | Signals active development to Apple and users |
| **1-star reviews** | <10% of total | Monitor for product issues, not review strategy |

Sources:
- [Ratings and Reviews -- Apple Developer](https://developer.apple.com/app-store/ratings-and-reviews/)
- [Ultimate Guide to App Store Reviews 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/app-store-reviews)
- [How to Improve App Store Rating -- MobileAction](https://www.mobileaction.co/blog/how-to-improve-app-store-rating/)
- [How to Ask for App Reviews -- Appcues](https://www.appcues.com/blog/mobile-app-review-request-examples)
- [Strategies to Boost App Ratings 2025 -- Apptile](https://apptile.com/blog/strategies-to-boost-app-ratings-and-reviews/)

---

## 6. Apple Search Ads Strategy

### Context

Zerocap is currently running a $600 test-and-scale campaign through March 31 (4 campaigns: CATEGORY, DISCOVERY, COMPETITOR, BRAND). The existing [Apple Ads assessment](../tiktok-gtm/research/apple-ads-assessment.md) has the full breakdown. This section covers the keyword bidding strategy and how to integrate with organic ASO.

### Budget Allocation for a Bootstrapped Team

**The reality: $600 is a data-gathering budget, not a user acquisition budget.** At $12.28 average game CPI, $600 buys ~50 installs. The value is in the data: which keywords convert, what CPI is achievable, which audiences respond.

**Recommended ongoing budget after the March test:**

| Monthly Budget | Strategy | Expected Outcome |
|----------------|----------|-----------------|
| **$0/month** | Pause ads entirely. Focus on organic. | Smart if TikTok organic is working. Revisit when revenue supports it. |
| **$200-300/month** | Maintain Discovery + best-performing exact-match campaign | Learn continuously. ~15-25 installs/month. Data value > install value. |
| **$500-1000/month** | Scale winning keywords, add competitor targeting | Only if CPI comes in under $5 for specific terms. |
| **$2000+/month** | Full-scale UA | Only when product-market fit is confirmed AND revenue can support it. |

### Keyword Bidding Strategy

#### Campaign Structure (4-Campaign Model)

| Campaign | Match Type | Daily Budget | Bid Strategy | Purpose |
|----------|-----------|-------------|-------------|---------|
| **BRAND** | Exact | $5/day (when active) | Aggressive ($1-2 CPT) | Protect brand searches. Low volume but 100% conversion. Activate once brand awareness exists. |
| **CATEGORY** | Exact + Broad | $15/day | Moderate ($0.50-1.00 CPT) | Target category terms: "virtual pet," "pet game," "AI pet." Core performance driver. |
| **DISCOVERY** | Search Match | $10/day | Conservative ($0.30-0.50 CPT) | Let Apple find relevant queries you haven't thought of. Mining for new keywords. |
| **COMPETITOR** | Exact | $10/day | Moderate ($0.50-1.00 CPT) | Target competitor brand terms: "peridot," "tamagotchi," "pengu," "pou." |

#### Match Type Strategy

- **Exact match = performance.** Higher CPI but higher conversion. Most of your budget should flow here once you know winning keywords.
- **Broad match = discovery.** Lower CPI, lower conversion, but finds keywords you wouldn't have guessed. Run with low bids to mine for opportunities.
- **Search Match = exploration.** Apple's algorithm decides what queries to show you for. Great for new apps that don't know their keyword landscape yet.

**Workflow:**
1. Discovery campaign finds new converting keywords
2. Move proven keywords to Category campaign as exact match
3. Add those keywords as negative keywords in Discovery (avoid paying twice)
4. Increase bids on exact match winners
5. Repeat monthly

#### Target Keywords for Apple Ads

**Exact match (bid aggressively):**
- virtual pet
- AI pet
- pet game
- tamagotchi
- pet simulator
- cute pet game
- virtual pet game

**Exact match -- competitor (bid moderately):**
- peridot
- peridot game
- pou game
- talking tom
- pengu app
- my tamagotchi

**Broad match (bid conservatively for discovery):**
- AI companion
- pet creator
- cute AI
- camera game
- pet maker

### Integration with Organic ASO

**The flywheel effect:** Paid installs boost organic ranking, which drives free installs, which further improves ranking.

```
Apple Ads drives installs for "virtual pet"
  → Download velocity for "virtual pet" increases
    → Organic ranking for "virtual pet" improves
      → More free installs from organic search
        → Higher ranking sustained even after reducing ad spend
```

**How to leverage this:**
1. Focus ad spend on keywords where you're organically ranked 10-30 (close to top 10 but need a push)
2. Concentrate spend in 2-3 day bursts rather than spreading thin across weeks (velocity matters more than total volume)
3. Use Apple Ads impression data to validate keyword search volume before committing keyword field space
4. Move high-performing ad keywords into your organic metadata (title, subtitle, keyword field)

### Decision Framework After March Test

| CPI Result | Action |
|-----------|--------|
| **Under $3** | Excellent. Scale this keyword aggressively. Increase daily budget. |
| **$3-5** | Good. Maintain spend. Monitor for improvement as organic ranking rises. |
| **$5-10** | Marginal. Keep for data but don't scale. Focus budget on better-performing terms. |
| **Over $10** | Cut. This keyword isn't worth paid acquisition at this stage. |

Sources:
- [Apple Ads Best Practices -- Apple](https://ads.apple.com/app-store/best-practices/keywords)
- [Manual Bidding Best Practices -- Apple](https://ads.apple.com/app-store/best-practices/manual-bidding)
- [Apple Search Ads Guide 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/guide-to-apple-search-ads)
- [Apple Search Ads Best Practices 2025 -- Adapty](https://adapty.io/blog/apple-ads-best-practices/)
- [Apple Ads Best Practices 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/apple-ads-best-practices)
- [Broad vs Exact Match -- SplitMetrics](https://splitmetrics.com/glossary/broad-and-exact-match-in-apple-search-ads-maximizing-your-advertising-reach/)

---

## 7. Ranking Algorithm Factors (2025-2026)

### The Full Picture

Apple's App Store ranking algorithm has evolved significantly. Here's the current state as of early 2026:

#### Tier 1: Highest Impact Factors

| Factor | Weight | What It Means |
|--------|--------|---------------|
| **Download velocity** | Very High | Installs per time period. A burst of downloads matters more than the same total spread over weeks. |
| **Keyword relevance** | Very High | How well your metadata (title, subtitle, keywords, screenshot captions) match the search query. |
| **User ratings & reviews** | High | Average rating, review count, recency of reviews. Recent reviews weighted more. |
| **Retention & engagement** | High | Day 1/7/30 retention, session length, sessions per day. Apple tracks if people keep the app. |

#### Tier 2: Significant Impact

| Factor | Weight | What It Means |
|--------|--------|---------------|
| **Revenue performance** | Medium-High | In-app purchases and subscription revenue signal value to Apple. |
| **Uninstall rate** | Medium-High | High uninstall rate = algorithm demotion. Inverse correlation with ranking. |
| **Update frequency** | Medium | Regular updates signal active development. 2-4 updates per year minimum. |
| **Screenshot caption keywords** | Medium | New in June 2025. Text in screenshot captions is now indexed for search. |
| **In-app events** | Medium | Apps using 5+ in-app events per year show stronger engagement signals. |
| **Technical performance** | Medium | Crash rate, load times, battery usage. Apple penalizes unstable apps. |

#### Tier 3: Emerging/Contextual Factors

| Factor | Weight | What It Means |
|--------|--------|---------------|
| **Custom Product Pages (CPPs)** | Growing | CPPs now appear in organic search (July 2025). More CPPs = more keyword surface area. |
| **AI-generated tags** | New (iOS 26 beta) | Apple's ML analyzes your app and auto-suggests categories/keywords. Early signal of automated ASO. |
| **Backlinks / web presence** | Low-Medium | Apple Search increasingly considers web signals. Having a good website with structured data helps. |
| **Localization depth** | Low-Medium | Localized metadata in multiple languages increases surface area. |

### What Changed in 2025-2026

The biggest shift: **the algorithm moved from "who has the best keywords" to "who proves real users want the app, enjoy it, and keep it installed."** Retention, engagement, and uninstall behavior now matter more than pure download volume.

**Key algorithm updates:**

1. **June 2025 -- Screenshot Captions Indexed:** Text in screenshot captions now contributes to keyword ranking. This is effectively free extra keyword space.

2. **July 2025 -- CPPs in Organic Search:** Custom Product Pages can now appear in organic search results when assigned specific keywords. You can create up to 70 CPPs per app.

3. **2025 -- In-App Events Integration:** The algorithm now indexes in-app events and evaluates their relevance to search queries. Events appear in search results, product pages, and the Today tab.

4. **iOS 26 Beta -- AI-Generated Tags:** Apple is testing automated metadata generation using ML analysis of app content and user behavior.

### What This Means for Zerocap

1. **Nail retention first.** No amount of ASO hacking compensates for poor retention. If users install Zerocap and delete it after one session, ranking will crater regardless of keywords.

2. **The pet care loop IS the ranking strategy.** Daily notifications, pet mood changes, feeding schedules -- these drive session count and retention, which drive ranking.

3. **Screenshot captions are free real estate.** Write keyword-rich captions for all 6-10 screenshots. Most competitors haven't updated for this June 2025 change yet.

4. **Plan in-app events early.** Monthly events (new pet types, seasonal transformations, holiday themes) serve dual purpose: retain users AND boost App Store visibility.

5. **Create 3-5 CPPs at launch.** One for "virtual pet" searchers, one for "AI companion" searchers, one for "camera game" searchers. Each with tailored screenshots.

Sources:
- [App Store Ranking Factors 2025 -- SplitMetrics](https://splitmetrics.com/blog/apple-app-store-ranking-factors/)
- [App Store Ranking Factors 2026 -- MobileAction](https://www.mobileaction.co/blog/app-store-ranking-factors/)
- [App Store Ranking Factors -- AppTweak](https://www.apptweak.com/en/aso-blog/app-store-ranking-factors)
- [App Store Algorithm Update 2025 -- Appfigures](https://appfigures.com/resources/guides/app-store-algorithm-update-2025)
- [App Ranking Factors 2025 -- ASO World](https://asoworld.com/insight/app-ranking-factors-in-2025-what-to-expect-from-the-ios-app-store-algorithm-updates/)
- [App Store SEO 2026 -- SEO Sherpa](https://seosherpa.com/app-store-seo/)

---

## 8. Launch Day ASO Tactics

### Pre-Launch Checklist (2-4 Weeks Before)

| Task | Priority | Details |
|------|----------|---------|
| **Finalize keyword research** | Critical | Title, subtitle, keyword field, screenshot captions all locked in. |
| **App Preview Video ready** | Critical | 15-30 second vertical video showing camera-to-pet transformation. |
| **Screenshots designed** | Critical | 6 screenshots following the Value-Usage-Trust framework. |
| **Submit featuring nomination** | High | 3+ weeks before launch via App Store Connect. |
| **Set up Apple Search Ads** | High | Campaigns ready to activate on launch day (even if paused initially). |
| **Custom Product Pages created** | High | At least 2-3 CPPs targeting different keyword clusters. |
| **Pre-order page live** | Medium | Apple allows pre-order up to 180 days before release. Captures early interest. |
| **App Store description finalized** | Medium | First 170 characters optimized for "above the fold." |
| **Privacy labels complete** | Critical | Required. Incomplete = rejection. |
| **Localization (if applicable)** | Medium | At minimum, localize title/subtitle/keywords for top 5 markets. |

### Launch Day Playbook

#### Hour 0-6: Activate Everything Simultaneously

1. **Release the app** (or switch from pre-order to available)
2. **Activate Apple Search Ads campaigns** -- drive immediate search installs
3. **Publish TikTok launch video** -- the organic engine starts
4. **Post on Reddit** (r/tamagotchi, r/iosapps, r/virtualepets) -- community seeding
5. **Email/DM all 50+ seeded creators** -- "it's live! Link in bio"
6. **Publish Product Hunt listing** (if Tuesday/Wednesday -- highest engagement days)

#### Why Launch Day Velocity Matters

Apple gives new apps a **temporary visibility boost** in search results during the first days/weeks after launch. This boost happens once per locale and cannot be repeated. Missing this window means missing free visibility you'll never get again.

The boost affects auto-suggestions for keywords in your title. When a user starts typing a keyword that matches your title, Apple may surface your app higher than its "natural" ranking would dictate.

**How to maximize the new app boost:**
- Concentrate all launch marketing (TikTok, Reddit, creator DMs, Product Hunt) on the same day
- This creates a download velocity spike exactly when Apple's algorithm is watching for new app traction
- The velocity spike + new app boost compound into higher organic ranking than either alone

#### Day 1-3: Monitor and React

| Metric | Where to Check | Action if Low |
|--------|---------------|---------------|
| **Impressions** | App Store Connect > Analytics | Check if keywords are indexed. If zero impressions, keyword field may have issues. |
| **Conversion rate** | App Store Connect > Conversion Rate | If below 20%, screenshots/video aren't working. Consider PPO A/B test. |
| **Search rankings** | ASO tool (AstroASO, AppTweak) | If not ranking for target keywords, verify keyword field formatting. |
| **Download velocity** | App Store Connect > Downloads | If below expectations, amplify marketing push on Days 2-3. |
| **Crash rate** | Xcode Organizer / App Store Connect | Any crashes in first 48 hours = emergency fix. Crashes tank both reviews AND algorithm trust. |

#### Day 4-7: First Keyword Swap Opportunity

Apple re-indexes your keywords when you submit a new version. But you can also update keywords without a new binary by changing metadata in App Store Connect. Do a first check:
- Which keywords generated impressions?
- Which keywords generated taps?
- Which keywords generated installs?
- Drop keywords with zero impressions after 7 days
- Add alternatives from your research list

#### Day 7-14: Trigger First Review Prompts

If Day 1 retention is healthy (28%+ for a pet app), users who've been back 3+ times are now eligible for review prompts. Activate the `SKStoreReviewController` trigger for users meeting the criteria in Section 5.

### Launch Day Asset Checklist

Everything ready before pressing "Release":

- [ ] App icon (1024x1024, no text, bright/warm colors, cute creature face)
- [ ] 6-10 screenshots (iPhone 15 Pro Max and 6.5" sizes at minimum)
- [ ] App Preview Video (15-30 seconds, .mov or .mp4)
- [ ] Title: `Zerocap - AI Pet Creator` (or final version)
- [ ] Subtitle: `Turn Real Objects Into Pets` (or final version)
- [ ] Keyword field: 100 characters, comma-separated, no spaces
- [ ] Description: 4,000 chars, first 170 chars optimized
- [ ] Screenshot captions with keywords (new ranking signal)
- [ ] Privacy labels completed
- [ ] Age rating set
- [ ] Category: Games > Simulation (primary), Entertainment (secondary)
- [ ] Featuring nomination submitted (3+ weeks prior)
- [ ] Apple Ads campaigns built and ready to activate
- [ ] 2-3 Custom Product Pages created
- [ ] Support URL and marketing URL live
- [ ] Press kit / marketing assets ready for creator DMs

Sources:
- [App Launch Strategy 2026 -- Moburst](https://www.moburst.com/blog/app-launch-strategy/)
- [ASO Checklist 2026 -- MobileAction](https://www.mobileaction.co/blog/complete-aso-checklist/)
- [ASO Strategy 2026 -- AppTweak](https://www.apptweak.com/en/aso-blog/aso-strategy)
- [How to Boost First App Store Release -- RadASO](https://radaso.com/blog/how-to-boost-an-app-at-the-first-app-store-release-life-hacks-from-radaso)
- [New App Boost -- SplitMetrics](https://splitmetrics.com/blog/apple-app-store-ranking-factors/)

---

## 9. Ranking Benchmarks & Expected Organic Installs

### Downloads Needed to Reach Chart Positions (US App Store, Games Category)

These are estimates based on industry data. Actual thresholds fluctuate daily based on overall market activity.

| Ranking Position | Estimated Daily Downloads Needed (US) | Organic Installs Impact |
|-----------------|--------------------------------------|------------------------|
| **#1 Overall Free** | 50,000-100,000+/day | Massive -- but unrealistic target for launch |
| **#1 Games > Simulation** | 5,000-15,000/day | Very high visibility within subcategory |
| **Top 10 Games > Simulation** | 1,000-5,000/day | Strong subcategory chart visibility. Users browsing charts will see you. |
| **Top 50 Games > Simulation** | 200-1,000/day | Visible when users scroll subcategory charts. 7-12% lift in organic day-over-day. |
| **Top 100 Games > Simulation** | 50-200/day | Barely visible on charts, but signals to algorithm. ~5,000 downloads/day was the older Games overall top 100 threshold. Subcategory is lower. |
| **Top 200 Games > Simulation** | 20-50/day | Chart position contributes minimally. Ranking value comes from keyword positioning. |

### Realistic Targets for Zerocap at Launch

| Phase | Timeline | Daily Download Target | Expected Ranking |
|-------|----------|----------------------|-----------------|
| **Launch week** | Days 1-7 | 100-500/day | Top 100-200 Simulation (with new app boost) |
| **Early traction** | Weeks 2-4 | 200-1,000/day | Top 50-100 Simulation |
| **Organic growth** | Months 2-3 | 500-2,000/day | Top 20-50 Simulation |
| **Viral moment** | If TikTok hits | 2,000-10,000+/day | Top 10 Simulation, possibly Top 100 Overall Games |

### The Organic Install Multiplier

Once you reach a visible chart position, organic installs compound:

| Chart Position | Estimated Organic Lift |
|---------------|----------------------|
| Not charting | Baseline (all installs from search + external traffic) |
| Top 100 subcategory | +5-10% additional organic installs |
| Top 50 subcategory | +10-20% additional organic installs |
| Top 10 subcategory | +30-50% additional organic installs |
| Top 10 overall category | +100-300% additional organic installs |
| Featured (App/Game of the Day) | +500-5000% spike for 1-3 days |

### Keyword Search Ranking Benchmarks

Chart positions (top charts) matter, but **keyword ranking is where most organic installs come from.** Over 65% of App Store downloads begin with a search.

| Keyword Rank | Visibility | Expected Impact |
|-------------|-----------|----------------|
| **#1 for a keyword** | First result shown | Captures 30-50% of taps for that keyword |
| **#2-3** | Visible without scrolling | Captures 15-25% of taps |
| **#4-7** | Below the fold but visible on first scroll | Captures 5-10% of taps |
| **#8-15** | Second screen of results | Captures 2-5% of taps |
| **#16-30** | Deep scroll required | Captures <1% of taps |
| **#30+** | Effectively invisible | Negligible impact |

**Zerocap's priority:** Rank top 5 for 3-5 long-tail keywords (AI pet, pet creator, AI tamagotchi, camera pet) rather than top 50 for broad terms (pet game, virtual pet). Long-tail top-5 positions drive more qualified installs than broad top-50 positions.

### Conversion Rate Benchmarks

| Metric | Games Average | Virtual Pet / Casual | Target for Zerocap |
|--------|-------------|---------------------|-------------------|
| **Impression to tap** | 9.7% | 10-15% | 12%+ |
| **Tap to install** | 25-30% (US) | 30-40% | 35%+ |
| **Overall conversion** | ~3-5% | 3-8% | 5%+ |

Sources:
- [App Store Ranking Factors -- SplitMetrics](https://splitmetrics.com/blog/apple-app-store-ranking-factors/)
- [Downloads Needed for Top Rankings -- PocketGamer](https://www.pocketgamer.biz/sponsored-app-stores-top-ranking-download-requirements/)
- [App Store Conversion Rate by Category 2026 -- Adapty](https://adapty.io/blog/app-store-conversion-rate/)
- [Organic App Growth 2026 -- MobileAction](https://www.mobileaction.co/blog/organic-app-growth-in-2025/)
- [App Downloads by Category 2025 -- AppTweak](https://www.apptweak.com/en/reports/app-downloads-by-category)

---

## 10. Competitor Keyword Analysis

### Direct Competitors: How They Position on the App Store

#### Peridot (Niantic)

| Element | Details |
|---------|---------|
| **Title** | Peridot |
| **Category** | Games > Simulation |
| **Positioning** | "Inventing the future, with genetically unique AI pets" |
| **Key keywords (estimated)** | virtual pet, AR pet, augmented reality, pet game, walking game, breeding, genetics, cute creatures |
| **Strengths** | Niantic brand, AR technology, strong visuals |
| **Weaknesses** | Downloads dropped to 10.5K/month by Q4 2023. Aggressive monetization killed retention. Missing social layer. |
| **Zerocap opportunity** | Users disappointed by Peridot's monetization are searching for alternatives. Target "peridot" as a competitor keyword in Apple Ads. |

#### Friends / Pengu (Born/SLAY GmbH)

| Element | Details |
|---------|---------|
| **Title** | Friends -- Pengu, Bao & Mellow (evolved from "Pengu -- Raise Virtual AI Pets") |
| **Category** | Lifestyle / Social |
| **Positioning** | "Raise AI Companions" -- emphasis on co-parenting, shared experience |
| **Key keywords (estimated)** | AI companion, virtual pet, raise pet, co-parent, social pet, AI friend, pengu, companion app |
| **Strengths** | 15M+ users, $25M raised, strong social mechanic (co-parenting) |
| **Weaknesses** | Fixed IP characters (Pengu is pre-made). No creation mechanic. Limited personalization of the pet itself. |
| **Zerocap opportunity** | Zerocap's "create YOUR pet from YOUR objects" is a fundamentally different value proposition. Target users who want personal creation, not pre-made characters. |

#### My Tamagotchi Forever (Bandai Namco)

| Element | Details |
|---------|---------|
| **Title** | My Tamagotchi Forever |
| **Category** | Games > Simulation |
| **Positioning** | Classic Tamagotchi experience on mobile |
| **Key keywords (estimated)** | tamagotchi, virtual pet, pet game, simulation, nurture, feed, play, mini games, AR, character evolution |
| **Strengths** | Iconic brand recognition. "Tamagotchi" is a high-volume keyword with nostalgic pull. |
| **Weaknesses** | Mixed reviews. Hasn't matched the physical device's cultural impact. Dated design. Aggressive in-app ads. |
| **Zerocap opportunity** | The Tamagotchi mobile execution is mediocre. The brand creates demand, but the app doesn't satisfy it. Zerocap can capture "tamagotchi" searches by positioning as the modern evolution. |

#### Pou (Paul Salameh)

| Element | Details |
|---------|---------|
| **Title** | Pou |
| **Category** | Games > Simulation |
| **Positioning** | Classic virtual pet (feed, clean, play mini-games) |
| **Key keywords (estimated)** | virtual pet, pet game, tamagotchi, feed pet, dress up, mini games, pou |
| **Strengths** | 1.1B+ downloads. Extreme simplicity. Recent TikTok nostalgia resurgence. |
| **Weaknesses** | Very simple/old design. Single developer, limited updates. $1.99 paid on iOS. |
| **Zerocap opportunity** | Pou proves the appetite for simple pet care loops. Zerocap adds the "wow" factor of AI creation that Pou lacks entirely. Target "pou" as a competitor keyword for users wanting a modern upgrade. |

### Keyword Landscape Map

This maps the competitive density of key search terms relevant to Zerocap:

| Keyword | Competition Level | Top Competitors Ranking | Zerocap Rankability |
|---------|------------------|------------------------|-------------------|
| **virtual pet** | High | Pou, Tamagotchi, Peridot, Friends | Hard at launch. Target with Apple Ads. Organic top 20 possible after 2-3 months. |
| **AI pet** | Low-Medium | Friends/Pengu, Emy | **High opportunity.** Few optimized competitors. Top 5 achievable at launch. |
| **pet game** | Very High | Dozens of casual pet games | Don't waste keyword field space. Too competitive for organic. |
| **tamagotchi** | Medium | My Tamagotchi Forever, Tamagotchi Adventure Kingdom | **Moderate opportunity.** Bandai's app is poorly optimized. Top 10 possible with good ASO. |
| **AI companion** | Medium-High | Replika, Character.AI, Friends | Adjacent audience. Worth targeting in keyword field. |
| **pet creator** | Very Low | Almost no competition | **Top opportunity.** Likely #1 achievable at launch. |
| **camera pet** | None | No competition | **Unique to Zerocap.** Own this keyword. Create awareness through TikTok. |
| **AI tamagotchi** | Very Low | Minimal competition | **Top opportunity.** Niche but perfectly describes the product. |
| **pet simulator** | Medium | Pou, Tamagotchi, various casual games | Worth targeting. Top 20 realistic. |
| **cute AI** | Low | Few direct competitors | Good fit. Growing search term. |
| **pet personality** | Very Low | None optimized | **Own this term.** Unique to Zerocap's trait system. |

### Competitor ASO Gaps (Where Zerocap Can Win)

1. **"AI pet" keyword space is under-contested.** Most virtual pet apps don't emphasize AI in their metadata. Friends/Pengu is the only major competitor targeting this term. Zerocap can own "AI pet" quickly.

2. **No one owns "pet creator."** Creation-focused keywords (pet creator, pet maker, create pet) have almost zero ASO competition. Zerocap's core mechanic maps perfectly to these terms.

3. **"Camera" + "pet" combination is empty.** Zerocap has no competitors for camera-related pet keywords. Build awareness through TikTok content, then capture the search volume you create.

4. **"Tamagotchi" is underserved on mobile.** The brand's own app has poor reviews. Users searching "tamagotchi" are looking for the concept, not necessarily the brand. Zerocap's subtitle referencing "transform objects into pets" can capture these nostalgia-driven searches.

5. **Screenshot captions are underutilized by all competitors.** The June 2025 algorithm update means screenshot captions are now indexed, but most competitor apps haven't updated their listings. First mover advantage here.

### Recommended Competitor Monitoring

Track these metrics monthly using AstroASO or AppTweak:

| What to Track | Why |
|--------------|-----|
| Competitor keyword rankings (top 10 keywords per competitor) | See when they add/drop keywords. React quickly. |
| Competitor rating changes | A competitor's rating drop = opportunity for your reviews to shine |
| Competitor update frequency | Tracks if they're actively improving or stagnating |
| New entrants in "AI pet" keyword space | Detect new competitors early |
| Competitor CPP launches | Learn from their Custom Product Page strategies |

Sources:
- [Peridot -- App Store](https://apps.apple.com/us/app/peridot/id6445801028)
- [Friends -- App Store](https://apps.apple.com/us/app/friends-raise-ai-companions/id6462927800)
- [My Tamagotchi Forever -- App Store](https://apps.apple.com/us/app/my-tamagotchi-forever/id1267861706)
- [App Store Keyword Research -- AppTweak](https://www.apptweak.com/en/aso-blog/app-store-keyword-research-aso)
- [Top by Keyword -- ASO.dev](https://aso.dev/aso/top-by-keyword/)
- [Keyword Rankings -- AppTweak](https://www.apptweak.com/en/aso-tools/app-store-keyword-ranking)

---

## Summary: The 5 Most Important Things to Get Right

1. **Category = Games > Simulation.** This puts you next to every virtual pet app and gives you access to subcategory charts where indie apps can actually rank.

2. **Win long-tail keywords first.** "AI pet," "pet creator," "AI tamagotchi," and "camera pet" are low-competition terms you can own immediately. Don't waste energy on "pet game" until you have organic momentum.

3. **App Preview Video is non-negotiable.** 20-40% conversion lift. Your camera-to-pet transformation IS the ad. Show it in motion.

4. **Prompt for reviews after the first pet creation.** This is the peak delight moment. Target 4.5+ stars and 50+ reviews in month one.

5. **Concentrate launch marketing into a single day.** The new app boost is a one-time event. Make Day 1 download velocity as high as possible by firing TikTok, Reddit, creator DMs, and Apple Ads simultaneously.

---

*Research compiled March 2026. App Store policies, algorithm weights, and market data are subject to change. Revisit quarterly.*
