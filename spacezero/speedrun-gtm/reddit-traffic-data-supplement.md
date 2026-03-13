# Reddit Gaming Traffic: Hard Numbers & Conversion Data

Supplemental research to `reddit-gtm-deep-dive.md`. Focused on specific traffic numbers, upvote-to-visitor ratios, conversion funnels, and paid ad case studies with real spend data. Compiled 2026-03-12.

---

## 1. Upvote-to-Visitor Ratios (The Missing Metric)

Reddit does not publish a universal upvote-to-visitor ratio. But the data points below let us triangulate:

### Known Data Points

| Post | Upvotes | Views/Impressions | Visitors to External Site | Ratio (Upvotes:External Visitors) |
|---|---|---|---|---|
| Laysara: Summit Kingdom on r/gaming | 73,000 | 3.2M views | 11,000+ wishlists (Steam) | ~1:0.15 (upvote to wishlist) |
| Airscape (AMA on r/IAmA) | ~5,000+ (front page) | N/A | ~16,000 app store visitors, 1,779 units sold | ~1:3 (upvote to store visit) |
| Robot game on 500K+ community | 2,500 | N/A | N/A | N/A |
| r/SideProject example | 72 | 11,200 views | N/A | 1:155 (upvote to view) |

### Derived Estimates

- **Views per upvote**: Approximately **40-155x** the upvote count. A post with 1,000 upvotes likely has 40,000-155,000 views (impressions within Reddit).
- **External clicks per upvote**: Much lower. Estimated **0.15-3x** the upvote count for external site visits, depending heavily on:
  - Whether the post contains a direct link vs. link in comments
  - How compelling the call-to-action is
  - Whether the external destination is frictionless (browser game > Steam page > app store)
- **Wishlists per upvote**: ~0.15x for large viral posts (Laysara: 73K upvotes = 11K wishlists). Likely higher ratio on smaller, niche posts with better targeting.

### The Steam Traffic Amplifier Effect

Critical finding from the Laysara case: Reddit traffic triggers Steam's algorithm. After the initial 11K wishlists from Reddit, Steam's Discovery Queue kicked in and drove 2,500 wishlists/day organically, reaching 30K total. **Reddit traffic is a catalyst, not just a channel.**

---

## 2. Subreddit Size vs. Actual Reach

### How Many Members Actually See a Post?

Reddit does not publish per-subreddit reach percentages. But we can infer from platform-wide data:

| Metric | Data |
|---|---|
| Reddit DAU | 121.4M unique daily users (Q4 2025) |
| Reddit MAU | ~1.1-1.36B monthly unique users |
| DAU/MAU ratio | ~7% of monthly users visit daily |
| Time on app per session | ~30 minutes/day (US users) |
| Time on feed | 26% of session time on main feed |
| Time on subreddit pages | 7% of session time browsing subreddits |

**Key insight**: Only ~7% of Reddit users open the app daily (vs. 32% for TikTok, 43% for Instagram). This means a subreddit's "subscriber count" massively overstates its daily active audience.

### Estimated Daily Active Viewers by Subreddit

| Subreddit | Subscribers | Est. Daily Active (~7%) | Est. Who See a Top Post (~20-40% of DAU) |
|---|---|---|---|
| r/gaming | 46M | ~3.2M | 640K-1.3M |
| r/Minecraft | 8.5M | ~595K | 119K-238K |
| r/Minecraftbuilds | ~1M | ~70K | 14K-28K |
| r/IndieGaming | 390K | ~27K | 5.4K-10.8K |
| r/WebGames | 280K (some sources say 131K) | ~9K-19.6K | 1.8K-7.8K |
| r/gamedev | 311K | ~22K | 4.4K-8.8K |
| r/playmygame | 105K | ~7.3K | 1.5K-2.9K |
| r/browsergames | 30K | ~2.1K | 420-840 |

**Note**: These are rough estimates. Posts that hit r/all bypass subreddit-specific reach entirely and can reach millions. The Laysara post hit 3.2M views because it reached r/all, not just r/gaming's subscriber base.

### Comparison to Other Platforms' Organic Reach

| Platform | Organic Post Reach (% of followers) |
|---|---|
| Reddit (top post in subreddit) | ~2-5% of subscribers (estimated) |
| Reddit (r/all viral post) | Millions regardless of sub size |
| Instagram | 3.5% of followers (2025) |
| Facebook | 1.65% of followers |
| X/Twitter | ~3% of followers |

Reddit's organic reach for a regular post is comparable to other platforms. But Reddit's viral ceiling is dramatically higher because r/all amplifies content beyond the original community.

---

## 3. Detailed Case Studies with Traffic Numbers

### Case Study A: Airscape (iOS Game) — Front Page r/IAmA

- **What happened**: Small indie studio featured on Reddit front page via AMA
- **Website traffic**: Site crashed, had to remove link from post. Still got 4,700 website sessions in 2 days.
- **App store traffic**: ~16,000 visitors to app store page
- **Sales**: 1,779 units sold in 2 days. Total revenue: EUR 3,198 (~$3,500)
- **Baseline**: This was 10x normal daily sales
- **Source**: [Game Developer](https://www.gamedeveloper.com/business/how-a-front-page-reddit-post-affected-the-sales-of-an-indie-game-)

### Case Study B: Laysara: Summit Kingdom — r/gaming Video Post

- **Post**: 30-second gameplay clip posted to r/gaming
- **Results in 24 hours**: 3.2M views, 73K upvotes, 11K+ Steam wishlists
- **Sustained effect**: 2,500 wishlists/day for days after. Reached 30K total wishlists.
- **Steam amplification**: Valve rewards external traffic with algorithmic discovery. Discovery Queue became primary traffic source after Reddit spike.
- **Source**: [How To Market A Game](https://howtomarketagame.com/2022/01/10/how-a-two-person-team-earned-11000-wishlists-with-one-reddit-post/)

### Case Study C: Faux-Operative Games — AMA with 36.4K Upvotes

- **Format**: AMA on r/gaming
- **Engagement**: 36,400 upvotes, 2,516 comments, 680 developer replies (39,245 total words)
- **Front page duration**: 12+ hours (average is 4 hours)
- **Ranked alongside**: Bill Nye and Neil DeGrasse Tyson AMAs
- **Failed first attempt**: Bot auto-removed original post after 100 upvotes because it mentioned Kickstarter
- **Source**: [Game Developer](https://www.gamedeveloper.com/business/how-two-indie-devs-got-36-4k-upvotes-on-reddit)

### Case Study D: Chicken Road — Browser Game, 42M Sessions

- **Game**: Minimalist browser-based indie game (pixelated chicken navigating obstacles)
- **Sessions**: 42M total in Q3-Q4 2025 (21M per quarter)
- **Marketing spend**: Zero paid ads
- **Growth drivers**:
  - Initial viral momentum from r/WebGames shares
  - #ChickenRoadChallenge videos: 4.8M views on social media
  - UGC explosion: 1.2M user-generated clips in Q3 alone (37% fail compilations)
  - Aggregator platforms (CrazyGames, Poki) amplified traffic after initial Reddit traction
  - Poki's algorithm pushed it to 15% of their traffic after 500K sessions
- **Key insight**: Reddit was the spark, but aggregator platforms and UGC were the sustained engine
- **Source**: [Digital Edge](https://digitaledge.org/how-a-simple-browser-game-reached-42-million-sessions-in-q3-q4-2025-full-case-study/)

### Case Study E: Part-Time Solo Dev — First 2 Weeks of Wishlists

- **Reddit as traffic source**: Biggest single source of external traffic to Steam page (~190 visits in first 2 weeks)
- **Twitter comparison**: Slightly less traffic from Twitter, but Twitter had higher conversion because followers were genre-aligned and had existing relationship with dev
- **Steam login problem**: 90.35% of visitors from Twitter were NOT logged into Steam, preventing wishlist conversion
- **Total wishlists**: ~150 in first 2 weeks (considered below the 500 threshold for "has potential")
- **Source**: [Game Developer](https://www.gamedeveloper.com/design/shy-of-150-a-part-time-solo-dev-s-first-two-weeks-of-collecting-steam-wishlists-)

---

## 4. Reddit Paid Ads: Detailed Spend Data

### Case Study: $1,000 Reddit Ads Spend (Kolektif Gamedev)

- **Budget**: $1,000
- **Result**: ~$2 per wishlist
- **CPC achieved**: $0.20-$0.30
- **CTR**: 0.6%
- **Previous campaign benchmark**: ~1,000 wishlists for ~$1/wishlist
- **US market CPCs**: $0.30-$0.50 (considered high)
- **Key learning**: Removing mobile was a mistake — 93% of traffic to Steam page came from mobile
- **Source**: [Medium/Kolektif Gamedev](https://medium.com/kolektif-gamedev/how-i-spend-1000-on-reddit-ads-f855662729a5)

### Case Study: $500 Reddit Ads (Squeaky Wheel — Glyphica: Typing Survival)

- **Budget**: $500
- **Duration**: ~14 days (May 27 - June 10)
- **Confirmed wishlists from ads**: 91 out of 386 total wishlists
- **Cost per wishlist**: ~$5.50
- **Desktop-only conversion rate**: 14%
- **Broad vs Niche targeting**: Both converted at similar rates
- **Extrapolation**: $5,000 would net ~1,000 wishlists — not enough alone for Steam's Popular Upcoming list
- **Source**: [Squeaky Wheel](https://www.squeakywheel.ph/blog/how-many-wishlists-can-500-worth-of-reddit-ads-get-you)

### Case Study: $4,365 Reddit Ads (This Grand Life 2)

- **Budget**: $4,365 total
- **Wishlists**: ~4,000
- **Average cost per wishlist**: $1.10 (range: $0.80-$2.50)
- **Best-performing subreddit CTRs**: r/capitalismlab (5.8%), r/tycoon (2.8%)
- **Mobile traffic**: 90% of tracked visits
- **Key insight**: Niche subreddit targeting dramatically outperformed broad targeting

### Case Study: VR Gaming Product

- **eCPM**: $1.52
- **CPC**: $0.37
- **CTR**: 0.63%
- **CPI (cost per install)**: $4.55
- **Targeting**: VR-specific communities

### Case Study: AI Gaming Product

- **Day 1 ROAS**: 100%
- **Day 7 ROAS**: 170%
- **Targeting**: Entertainment, Technology, Gaming, Business & Finance, News & Education interest categories
- **All KPIs met**

### Case Study: SUPERVIVE (Theorycraft Games)

- **Campaign**: Reddit ads during Steam Next Fest with comments open
- **Result**: Overwhelmingly positive engagement, contributed directly to strong demo performance
- **Tactic**: Leaving comments open on promoted posts drives organic discussion

### Minimum Effective Spend Summary

| Budget Tier | What You Get | Recommendation |
|---|---|---|
| $5/day (Reddit minimum) | Algorithm can't optimize, insufficient data | Don't bother |
| $50/day | Minimum for algorithm optimization | Test budget starting point |
| $500-$1,500 | Initial campaign testing | Run 2-3 different creatives, 5-10 subreddit targets |
| $3,000-$12,000 | Pre-launch indie standard | Target $1-2/wishlist, expect 1,500-12,000 wishlists |
| $50/day targeting 5-10 niche subs | 40% lower CPCs than broad targeting | Best ROI approach |

---

## 5. Video vs. Image vs. Text: Performance Comparison

| Format | Relative Engagement | Key Data |
|---|---|---|
| **Video/GIF (native upload)** | Highest | 18% higher engagement than image posts. Autoplay on mobile (73% of Reddit traffic). All top viral gaming posts were video. |
| **Image** | Medium | Works for screenshots, pixel art. 1200px+ recommended. |
| **Text** | Low for reach, high for depth | Best for AMAs, devlogs, postmortems. Lower upvotes but drives deeper engagement. |
| **External link** | Lowest | Suppressed by algorithm. Links in comments perform better than link posts. |

**Reddit-wide data**: Video posts get 18% higher engagement rate (comments + upvotes) than image posts. Top photo/video posts generate 10,000+ more upvotes than link posts. Video ads deliver 48% higher engagement than static image ads.

**Gaming-specific**: The Laysara viral post was a 30-second video clip. The Chicken Road viral spread started with video clips. Every top-performing gaming post identified in research was video/GIF format.

**Optimal video specs for gaming posts**:
- Length: 15-30 seconds
- Format: Native Reddit upload (not YouTube link)
- Content: Gameplay showing the "moment to fun" in first 3-6 seconds
- Resolution: High enough for detail but fast-loading

---

## 6. Conversion Funnel: Reddit Visitor to Player to Signup

### The Full Funnel (Estimated from Aggregated Data)

```
Reddit impressions (view post in feed)
    └── ~2-5% click/upvote the post
         └── ~1-10% click through to external site/store
              └── ~10-25% wishlist/download (if genre-aligned)
                   └── ~15-25% of wishlists convert to purchase at launch
```

### Specific Conversion Benchmarks

| Stage | Rate | Source/Notes |
|---|---|---|
| Post view → Upvote | ~0.6-2.5% | 72 upvotes from 11,200 views (r/SideProject example) |
| Post view → External click | ~0.3-0.5% | Derived from CTR data across campaigns |
| Steam page visit → Wishlist | 10-25% | <10% = targeting is off. 20-25% = high-performing, genre-aligned campaign. |
| Wishlist → Purchase (at launch) | 15-25% | Lower tiers: 15% median. Higher tiers (100K+ wishlists): 25% median. |
| Reddit visit → Play (browser game) | ~30-50% (estimated) | Browser games have near-zero friction. No download, no account required. This is why r/WebGames is high-value. |
| Reddit visit → Signup/Account creation | ~2-5% (estimated) | Standard web conversion rates. Higher if game hooks first, asks for signup after. |

### Browser Game Advantage

For Zerocap specifically, the conversion funnel is dramatically shorter than for Steam games:

**Steam game funnel** (4+ friction points):
Reddit → Click link → Open Steam → Login → Wishlist → Wait for launch → Purchase → Download → Play

**Browser game funnel** (1 friction point):
Reddit → Click link → Playing immediately

This is why r/WebGames posts drive disproportionate engagement — the user can go from seeing the post to playing the game in under 10 seconds.

---

## 7. Platform-Wide Reddit Statistics (Context)

| Metric | Value | Date |
|---|---|---|
| Monthly visits | 1.9B-2.2B | 2024-2025 |
| Daily active users | 121.4M unique | Q4 2025 |
| YoY DAU growth | 19% | Q4 2024 → Q4 2025 |
| Monthly gaming content views | 4.5B | 2024 |
| External clicks sent by Reddit | 1.2B to websites/apps | 2025 |
| Mobile traffic share | 73% | 2025 |
| Average US session length | 30 minutes/day | 2025 |
| Active subreddits | 138,000 | 2025 |
| r/gaming subscribers | 46M | 2025 |
| r/Minecraft subscribers | 8.5M | 2025 |
| r/IndieGaming subscribers | 390K | 2025 |
| r/WebGames subscribers | 131K-280K (conflicting sources) | 2025 |

### Reddit vs. Competitors (Cost Efficiency for Ads)

| Metric | Reddit | Meta | Google Search |
|---|---|---|---|
| eCPM | $2.29 (Q4 2024) | $11.73 | N/A |
| CPC | $0.59 avg | $1.33 | $4-5 |
| CTR | ~0.5% | ~0.5% | Higher (intent-based) |
| Cost advantage | Baseline | 2.3x more expensive | 7-8x more expensive |

Reddit is 5.1x cheaper per thousand impressions than Meta as of Q4 2024.

---

## Sources

- [How a Front Page Reddit Post Affected Sales of an Indie Game (Game Developer)](https://www.gamedeveloper.com/business/how-a-front-page-reddit-post-affected-the-sales-of-an-indie-game-)
- [How Two Indie Devs Got 36.4K Upvotes (Game Developer)](https://www.gamedeveloper.com/business/how-two-indie-devs-got-36-4k-upvotes-on-reddit)
- [How a Two-Person Team Earned 11,000 Wishlists (How To Market A Game)](https://howtomarketagame.com/2022/01/10/how-a-two-person-team-earned-11000-wishlists-with-one-reddit-post/)
- [What Is a Normal Click-Through Rate on Steam? (How To Market A Game)](https://howtomarketagame.com/2022/09/14/what-is-a-normal-click-through-rate-or-wishlist-rate-on-steam/)
- [Shy of 150: Solo Dev's First Two Weeks of Wishlists (Game Developer)](https://www.gamedeveloper.com/design/shy-of-150-a-part-time-solo-dev-s-first-two-weeks-of-collecting-steam-wishlists-)
- [How a Simple Browser Game Reached 42M Sessions (Digital Edge)](https://digitaledge.org/how-a-simple-browser-game-reached-42-million-sessions-in-q3-q4-2025-full-case-study/)
- [How I Spent $1000 on Reddit Ads (Kolektif Gamedev/Medium)](https://medium.com/kolektif-gamedev/how-i-spend-1000-on-reddit-ads-f855662729a5)
- [How Many Wishlists Can $500 of Reddit Ads Get You? (Squeaky Wheel)](https://www.squeakywheel.ph/blog/how-many-wishlists-can-500-worth-of-reddit-ads-get-you)
- [Reddit Ads Benchmarks Per Industry 2026 (AdBacklog)](https://adbacklog.com/blog/reddit-ads-benchmarks-per-industry-2026)
- [Reddit Ads Statistics 2026 (Shno)](https://www.shno.co/marketing-statistics/reddit-ads-statistics)
- [Reddit Ads Statistics 2025 (Marketing LTB)](https://marketingltb.com/blog/statistics/reddit-ads-statistics/)
- [Reddit Ads Cost 2026 (Aimers)](https://aimers.io/blog/reddit-ads-cost)
- [Reddit Ads Cost 2026 (Recho)](https://www.recho.co/blog/how-much-do-reddit-ads-cost-in-2026)
- [Reddit Statistics 2026 (SQ Magazine)](https://sqmagazine.co.uk/reddit-statistics/)
- [Reddit Statistics 2025 (Digital Web Solutions)](https://www.digitalwebsolutions.com/blog/reddit-statistics/)
- [Reddit Users Statistics 2026 (DemandSage)](https://www.demandsage.com/reddit-statistics/)
- [Reddit Stats 2026 (Social Champ)](https://www.socialchamp.com/blog/reddit-stats/)
- [Reddit for Gamers (Business of Apps)](https://www.businessofapps.com/insights/reddit-for-gamers-how-to-drive-engagement-and-boost-game-sales/)
- [Paid Social on Reddit vs Meta and Google (FanIQ)](https://www.faniq.live/blog/reddit-paid-social)
- [Post & Comment Insights (Reddit Help)](https://support.reddithelp.com/hc/en-us/articles/35363096996500-Post-Comment-Insights)
- [r/Minecraft Subreddit Stats (SubredditStats)](https://subredditstats.com/r/Minecraft)
- [r/Minecraftbuilds Subreddit Stats (SubredditStats)](https://subredditstats.com/r/Minecraftbuilds)
- [r/WebGames Stats (GummySearch)](https://gummysearch.com/r/WebGames/)
- [Benchmark: Itch.io Traffic (How To Market A Game)](https://howtomarketagame.com/2025/05/12/benchmark-itch-io-traffic/)
- [Game Marketing Budget (Games.gg)](https://games.gg/news/game-marketing-budget/)
- [Reddit Ads Complete Guide 2026 (ALM Corp)](https://almcorp.com/blog/reddit-ads-ultimate-guide-2026/)
