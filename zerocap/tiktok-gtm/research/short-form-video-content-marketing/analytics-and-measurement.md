# Analytics and Measurement Framework

What to track, how to track it, and what "good" looks like at the 0-10K follower stage.

---

## 1. Metrics to Track on Each Platform

### TikTok Metrics (In Order of Importance)

| Metric | Why It Matters | Where to Find It | Target (0-10K followers) |
|--------|---------------|-------------------|--------------------------|
| **Completion rate** | THE #1 algorithm signal. 70%+ completion triggers viral distribution in 2026. | TikTok Analytics → Content → Individual video → "Watched full video" | >70% for videos under 25s |
| **Average watch time** | Measures total engagement depth. TikTok measures at 3s, 15s, 30s, 60s checkpoints. | TikTok Analytics → Content → Individual video | >80% of video length |
| **Shares** | Weighted 3x higher than likes by the 2026 algorithm. Most valuable engagement action. | TikTok Analytics → Content → Individual video | >1% share rate (shares/views) |
| **Saves** | Indicates "future intent." Algorithm treats saves as a durable value signal. | TikTok Analytics → Content → Individual video | >2% save rate |
| **Comments** | Drive algorithmic boost, especially comment threads (replies). | TikTok Analytics → Content → Individual video | >3% comment rate |
| **Profile visits** | Measures curiosity conversion (viewer → potential follower/customer). | TikTok Analytics → Overview | Track weekly trend |
| **Follower growth** | Long-term audience building. Small accounts (<5K) achieve 269% YoY growth on avg. | TikTok Analytics → Followers | 100-500 new followers/week |
| **Video views** | Vanity metric but useful for tracking reach trajectory. | TikTok Analytics → Overview | Track weekly trend |

### YouTube Shorts Metrics

| Metric | Why It Matters | Where to Find It | Target (0-10K subs) |
|--------|---------------|-------------------|---------------------|
| **Swipe-away rate** | YouTube's primary negative signal. Lower = better. | YouTube Studio → Analytics → Engagement | <30% |
| **Average view duration** | YouTube cares about platform-level watch time. | YouTube Studio → Analytics → Engagement | >70% of video length for <30s Shorts |
| **Engaged views** | YouTube distinguishes Views (starts/loops) from Engaged Views (meaningful interaction). Only Engaged Views count for YPP. | YouTube Studio → Analytics | Track ratio of Engaged Views to total Views |
| **Subscriber conversion** | Shorts that convert viewers to subscribers signal high channel value. | YouTube Studio → Analytics → Audience | 1-3 new subs per 1K views |
| **CTR (Click-through rate)** | For Shorts that appear in search results, CTR measures thumbnail/title effectiveness. | YouTube Studio → Analytics → Reach | >5% |
| **Non-subscriber views %** | 74% average for Shorts. Higher = broader discovery. | YouTube Studio → Analytics → Audience | >70% |

### Instagram Reels Metrics

| Metric | Why It Matters | Where to Find It | Target (0-10K followers) |
|--------|---------------|-------------------|--------------------------|
| **Sends (DM shares)** | THE #1 Instagram algorithm signal. 3-5x more valuable than likes for reach. | Instagram Insights → Reels → Individual reel | Track total sends and sends/reach ratio |
| **Watch time** | Second most important signal (confirmed by Mosseri). | Instagram Insights → Reels | >50% of video length |
| **Likes per reach** | Third most important signal. Measures broad appeal. | Instagram Insights → Reels | >5% likes/reach ratio |
| **Saves** | Indicates content value. Saves boost Explore page discovery. | Instagram Insights → Reels | >3% save rate |
| **Reach (non-followers)** | Measures unconnected distribution. Where growth happens. | Instagram Insights → Reels | >50% of total reach from non-followers |
| **Follower conversion** | How effectively Reels convert viewers to followers. | Instagram Insights → Account | Track weekly growth rate |

---

## 2. Free and Cheap Analytics Tools

### Native Platform Analytics (Free)

| Platform | Requirements | What You Get |
|----------|-------------|--------------|
| **TikTok Analytics** | Must have published at least 1 video. Creator or Business account. | Views, completion rate, watch time, engagement breakdown, follower demographics, traffic sources, search queries (limited). |
| **YouTube Studio** | YouTube channel required. | Full analytics dashboard: views, watch time, audience retention graphs, traffic sources, subscriber analytics, revenue (when eligible). |
| **Instagram Insights** | Professional or Creator account. | Reach, engagement, follower demographics, content performance, sends/shares data. |

These native tools are sufficient for SpaceZero's 0-10K phase. Start here before paying for anything.

### Free Third-Party Tools

| Tool | What It Does | Cost | Best For |
|------|-------------|------|----------|
| **Countik** | TikTok profile and video analytics. Analyze any account (including competitors). No registration required. | Free | Competitor analysis. Check how Roblox/Minecraft creator accounts are performing. |
| **MaveKite** | Real-time TikTok analytics for profiles, videos, songs, hashtags. | Free | Hashtag research. Check #sandboxgame, #mobilegaming view counts. |
| **Tikstar** | TikTok analytics including product, video, influencer, and hashtag analysis. | Free | Finding nano-influencers in the gaming niche to partner with. |
| **Social Blade** | Cross-platform statistics tracker (TikTok, YouTube, Instagram). | Free (limited) | Tracking competitor growth rates over time. |

### Paid Tools (When You Scale)

| Tool | What It Does | Cost | When to Upgrade |
|------|-------------|------|-----------------|
| **Metricool** | Combined scheduling + analytics across all platforms. Shows best posting times. | $22/month | When you need scheduling + analytics in one place. |
| **Sprout Social** | Enterprise-grade social analytics, reporting, competitor benchmarking. | $249/month | Not relevant at current stage. |
| **Brand24** | TikTok mention monitoring, sentiment analysis, reach tracking. | $119/month | When SpaceZero starts getting mentioned by other creators. |

**Recommendation for SpaceZero:** Use only native platform analytics for the first 6 weeks. They provide everything you need. Countik and MaveKite (both free) are useful for competitor research only.

Sources: [Sprout Social: TikTok Analytics Tools 2026](https://sproutsocial.com/insights/tiktok-analytics-tools/), [Social Media Curve: Best TikTok Analytics Tools 2026](https://socialmediacurve.com/tiktok-analytics-tools/), [Countik](https://countik.com/tiktok-analytics), [MaveKite](https://mavekite.com/)

---

## 3. Attribution: Tracking Social Media → App Store Installs

This is the hardest part of the measurement stack. Apple's privacy framework (ATT/App Tracking Transparency) makes cross-platform attribution notoriously difficult. Here's what's actually possible:

### Method 1: Apple's Built-In Campaign Tracking (Free)

Apple App Store links support campaign tracking parameters:

```
https://apps.apple.com/app/spacezero/id[YOUR_APP_ID]?pt=[PROVIDER_ID]&ct=[CAMPAIGN_NAME]
```

- `pt` = Provider Tracking (your developer ID)
- `ct` = Campaign Tracking (name your campaign, e.g., "tiktok-bio-feb2026")

**How to use:**
1. Create separate links for each traffic source:
   - TikTok bio link: `?ct=tiktok-bio`
   - YouTube description: `?ct=youtube-desc`
   - Instagram bio: `?ct=instagram-bio`
2. Track installs per campaign in App Store Connect → Analytics → Sources

**Limitations:** Only works for link clicks, not search installs. If someone watches your TikTok and then searches "SpaceZero" on the App Store, Apple attributes that as an "App Store Search" install, not a TikTok install.

### Method 2: UTM-Tagged Links (Free)

Use UTM parameters on your Linktree/bio link page:

```
https://yoursite.com/download?utm_source=tiktok&utm_medium=bio&utm_campaign=feb2026
```

Track clicks in Google Analytics (if you have a landing page between social media and App Store).

**Important TikTok caveat:** TikTok wraps outbound clicks in its own redirect domain (vm.tiktok.com). This can strip or mangle UTM parameters. Test your links before deploying.

### Method 3: Mobile Measurement Partner (MMP)

For more robust attribution tracking:

| MMP | Free Tier | Best For |
|-----|-----------|----------|
| **Tenjin** | Yes (free tier with basic attribution) | Indie developers, startups. Specifically popular with mobile game makers. |
| **AppsFlyer (Zero Plan)** | Limited free tier | Industry standard. Supports TikTok integration natively. Tracks organic vs. non-organic installs. |
| **Singular** | Usage-based pricing | No additional TikTok configuration needed. |
| **Adjust** | No free tier | Enterprise-level. Overkill for current stage. |

**Recommendation for SpaceZero:** Start with Apple's built-in campaign tracking (free, no SDK required). Use separate `ct` parameters for each social platform. If you need deeper attribution, add Tenjin (free tier) as your MMP.

**Important note:** Google shut down Firebase Dynamic Links in August 2025. Do NOT use Firebase for deep linking. Use Apple's native Universal Links or a service like URLgenius instead.

### Method 4: Proxy Metrics (The Practical Approach)

Given attribution limitations, the most practical approach is tracking proxy metrics that strongly correlate with social media-driven installs:

| Proxy Metric | What It Tells You | How to Track |
|-------------|-------------------|--------------|
| **App Store search volume for "SpaceZero"** | Direct measure of TikTok → awareness conversion | App Store Connect → Analytics → Search Terms |
| **Download spikes correlated with viral videos** | Temporal correlation between TikTok views and installs | Compare TikTok Analytics timestamps with App Store Connect download data |
| **"How did you find us?" in-app survey** | Self-reported attribution (surprisingly accurate) | Add a simple onboarding question: "Where did you hear about SpaceZero?" with options: TikTok, YouTube, Instagram, Friend, App Store Search, Other |
| **Bio link click-through rate** | Measures intent conversion from social to App Store | Track via link shortener (Bitly free tier) or Linktree analytics |

**The in-app survey is the highest-ROI attribution method for SpaceZero's stage.** It costs nothing to implement, gives you direct data, and doesn't depend on any third-party tracking infrastructure.

Sources: [URLgenius: TikTok App Links](https://app.urlgeni.us/blog/tiktok-ad-link-open-mobile-app), [URLgenius: App Install Attribution Tags](https://app.urlgeni.us/blog/how-to-append-campaign-attribution-tags-for-google-analytics-to-app-deep-links), [TokPortal: TikTok Link UTM Tracking](https://www.tokportal.com/post/tiktok-link-in-bio-setup-utm-tracking-best-practices), [SplitMetrics: Best MMPs 2025](https://splitmetrics.com/blog/best-mobile-measurement-partners-2022/)

---

## 4. What "Good" Looks Like at the 0-10K Follower Stage

### TikTok Benchmarks (0-10K Followers)

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| **Engagement rate (by views)** | <2% | 4.2% (platform avg for <5K accounts) | 5-7% | >7.5% (gaming creator sweet spot) |
| **Completion rate** | <50% | 50-65% | 65-75% | >75% |
| **Follower growth rate** | Flat | 5-10%/week | 15-25%/week | >25%/week (269% YoY avg for smallest accounts) |
| **Views per video** | <500 | 500-2K | 2K-10K | >10K (breakout territory) |
| **Profile visit rate** | <1% | 1-2% | 2-4% | >4% |
| **Shares per video** | 0-2 | 3-10 | 10-50 | >50 |

**What to expect in Weeks 1-2:** Most videos will get 200-1K views. This is normal. The algorithm is testing your account. Don't panic. Focus on completion rate above all else. If your completion rates are above 70%, the views will come.

**What to expect in Weeks 3-4:** If you've posted consistently, you should see at least 1-2 videos break out of the 200-1K range and hit 5K-50K views. These breakouts tell you what content type the algorithm is amplifying for your account.

**What to expect in Weeks 5-6:** If the strategy is working, you'll have a clear "winning format" that consistently outperforms. Double down on that format. You should be at 2K-10K followers with some videos regularly hitting 10K+ views.

### YouTube Shorts Benchmarks (0-10K Subscribers)

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| **Engagement rate** | <3% | 4-5% | 5.91% (Shorts avg) | >7% |
| **Intro retention (first 3s)** | <50% | 50-65% | 70%+ | >80% |
| **Completion rate (<30s Shorts)** | <40% | 40-55% | 60%+ | >70% |
| **Subscriber conversion** | 0 subs/1K views | 0.5 subs/1K | 1-3 subs/1K | >3 subs/1K |
| **Non-subscriber view %** | <60% | 70-74% | 74%+ | >80% |

**YouTube Shorts growth timeline:** Slower than TikTok in the first 2 weeks, but more consistent. Expect each Short to accumulate views over weeks/months, not just the first 48 hours. By Week 6, your best-performing Shorts from Week 1 may still be gaining views.

### Instagram Reels Benchmarks (0-10K Followers)

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| **Engagement rate** | <2% | 3-4% | 5%+ | >7% |
| **Sends per reach** | 0 | 0.5-1% | 1-3% | >3% |
| **Watch time** | <30% of video | 30-50% | 50-70% | >70% |
| **Non-follower reach %** | <30% | 30-50% | 50-70% | >70% |
| **Follower conversion** | Flat | 1-3%/week growth | 5-10%/week | >10%/week |

**Instagram Reels growth timeline:** Typically the slowest to gain traction of the three platforms, but Instagram users tend to be higher-intent (older demographic, more likely to actually install an app). Quality of installs from Instagram may be higher than from TikTok.

---

## 5. Weekly Analytics Review Template

### Every Sunday, review these numbers:

```
WEEKLY ANALYTICS REVIEW
Date: ________

TIKTOK
├─ Total views this week: ________
├─ Best-performing video: ________ (views: ____, completion: ____%)
├─ Avg completion rate: ________%
├─ New followers: ________
├─ Total followers: ________
├─ Top comment/question to address: ________
└─ Action: What format to double down on? ________

YOUTUBE SHORTS
├─ Total views this week: ________
├─ Best-performing Short: ________ (views: ____, retention: ____%)
├─ New subscribers: ________
├─ Total subscribers: ________
└─ Action: ________

INSTAGRAM REELS
├─ Total reach this week: ________
├─ Best-performing Reel: ________ (reach: ____, sends: ____)
├─ New followers: ________
├─ Total followers: ________
└─ Action: ________

APP STORE (if launched)
├─ Downloads this week: ________
├─ Top search terms: ________
├─ Page conversion rate: ________%
├─ Downloads correlated with viral content? Y/N
└─ Action: ________

THIS WEEK'S WINNER: Which video performed best across all platforms?
NEXT WEEK'S PLAN: What 7 videos will we create based on this data?
```

---

## 6. Setting Up Analytics From Day 1

### Before posting your first video, do these:

**TikTok:**
- [ ] Switch to Creator Account (Settings → Manage Account → Switch to Creator Account)
- [ ] This unlocks TikTok Analytics automatically
- [ ] No cost

**YouTube:**
- [ ] Create a YouTube channel (or use existing Google account)
- [ ] YouTube Studio analytics are available immediately
- [ ] Enable "Advanced Mode" in YouTube Studio for granular data
- [ ] No cost

**Instagram:**
- [ ] Switch to Professional Account (Settings → Account → Switch to Professional Account → Creator)
- [ ] This unlocks Instagram Insights
- [ ] No cost

**App Store Connect (when app is published):**
- [ ] Enable App Analytics in App Store Connect
- [ ] Set up campaign tracking links with `ct` parameters for each social platform
- [ ] No cost

**Attribution (simple setup):**
- [ ] Create separate short links for each platform using Bitly (free tier)
  - `bit.ly/spacezero-tiktok`
  - `bit.ly/spacezero-youtube`
  - `bit.ly/spacezero-instagram`
- [ ] Put the platform-specific link in each bio
- [ ] Track click-through rates weekly in Bitly dashboard
- [ ] No cost

**Total cost for complete analytics setup: $0.**

Sources: [Social Insider: TikTok Metrics](https://www.socialinsider.io/blog/tiktok-metrics/), [Planable: TikTok Metrics](https://planable.io/blog/tiktok-metrics/), [Dash Social: TikTok Benchmarks 2025](https://www.dashsocial.com/social-media-benchmarks/tiktok), [Social Insider: Social Media Benchmarks 2025](https://www.socialinsider.io/social-media-benchmarks), [Enrich Labs: Social Media Benchmarks 2026](https://www.enrichlabs.ai/blog/social-media-benchmarks-2025)

---

*Research compiled February 2026. Benchmark data is based on cross-platform studies and platform-reported statistics.*
