# Apple Ads (App Store Advertising) Assessment for ZeroCap

**Date:** 2026-03-06
**Updated:** 2026-03-07
**Verdict:** ~~Hold off for now.~~ Running a $600 test-and-scale campaign through March 31 (Speedrun deadline).

---

## How Apple Ads Works

Apple rebranded Search Ads to **Apple Ads** in April 2025. Two tiers:

### Basic
- **You set:** monthly budget + max CPI (cost per install)
- **Apple handles:** keyword selection, targeting, bidding
- Zero control over which keywords you bid on
- CPI model (you pay per install, not per tap)
- Good for: testing if the channel works at all

### Advanced
- **You control:** keywords, audience segments, bids, ad scheduling, custom product pages
- CPT model (cost per tap) — you pay even if they don't install
- 15–25% lower CPIs than Basic when well-optimized
- Good for: scaling once you know what works

### Setup Steps
1. Go to [ads.apple.com](https://ads.apple.com), sign in with your Apple Developer account
2. Pick Basic or Advanced
3. Set your daily/monthly budget and max CPI
4. For Basic: Apple auto-matches your app to relevant searches based on your metadata
5. For Advanced: choose keywords (brand terms, competitor terms, category terms), set bids, define audience (age, gender, location)
6. Your ad shows at the top of App Store search results when someone searches a relevant term

### 2026 Update
Apple is expanding ad placements beyond the single top-of-search slot. Existing campaigns will automatically become eligible for new placements — more inventory, potentially lower costs.

---

## Cost Reality for Games

| Metric | Games Average | All Categories |
|---|---|---|
| CPI | **$12.28** | $1.80 |
| CPT | $1.00–1.20 | $2.25 |
| TTR | 9.7% | 9.7% |
| Conversion Rate | ~66% | 66.2% |

Games have the **highest CPI of any category** because everyone is competing for the same eyeballs. Casual games can do better (mid-to-low CPIs with broad terms), but the category average is brutal.

### Regional Variation
Latin America and Africa/Middle East/India (AMEI) are the most cost-efficient markets for both CPT and CPA — attractive for budget-friendly, volume-based user acquisition.

---

## Why We Should Hold Off

1. **$12 CPI vs. $0 organic.** The existing ZeroCap strategy targets 10K users in 6 weeks with zero spend through short-form video virality. At $12/install, 10K users = $120K. The organic path is dramatically more capital-efficient, and we haven't even tested it yet.

2. **ZeroCap's product IS the ad.** The "point camera at thing → cute AI pet" transformation is inherently shareable content. Apple Ads show a static screenshot in search results — that doesn't capture the magic of the transformation. A 3-second TikTok does.

3. **Search intent mismatch.** People don't search "AI Tamagotchi" or "camera pet app" on the App Store yet — this is a new category. Apple Ads works best for known categories ("puzzle game," "photo editor"). We'd be paying premium CPIs for broad terms like "AI pet" where intent is fuzzy.

4. **Sequence matters.** Apple Ads should come *after* organic traction proves the conversion funnel works. Once we know the App Store page converts at X% from organic traffic, *then* we can confidently pay to send more traffic there. Running ads before that is burning money to learn something we could learn for free.

---

## When It Would Make Sense

After launching the TikTok/YouTube organic push, confirming the App Store listing converts well, and wanting to pour fuel on a working funnel:

1. **Start with Basic** at $500–1K/month to test
2. **Move to Advanced** if CPI comes in under $5 for specific keywords
3. **Target competitor terms** (e.g., Replika, AI companion apps) and **category terms** (e.g., "virtual pet," "AI pet")
4. **Consider cheaper regions** (LATAM, AMEI) for volume-based acquisition if needed

---

## March 2026 Campaign Plan

**Context:** $1.8K in bank now, $5.5K arriving ~Mar 21. Speedrun (a16z SR007) application deadline Mar 31. Doeon set up 4 Apple Ads Advanced campaigns (all paused). Agreed to test with $300 first.

### Budget: $600 total ($300 test + $300 scale)

| Phase | Dates | Daily Budget | Total | Goal |
|---|---|---|---|---|
| **Test** | Mar 7-14 | $40/day | $280 | Get real CPI data per campaign type |
| **Analyze** | Mar 14-21 | $0 | $0 | Kill losers, wait for $5.5K |
| **Scale** | Mar 21-31 | $30/day | $300 | Scale winners before Speedrun deadline |
| **Total** | | | **$580** | |

### Test Phase Campaign Split ($40/day)

| Campaign | Daily Budget | Why |
|---|---|---|
| **CATEGORY** | $15 | Broad terms ("pet game," "virtual pet"). High competition but high intent. |
| **DISCOVERY** | $15 | Let Apple find users. Worth testing. |
| **COMPETITOR** | $10 | Target people searching competing apps. Narrower pool. |
| **BRAND** | **Paused** | Nobody searching "ZeroCap" yet. |

### Decision Points After Test (Mar 14)
- If any campaign has CPI under $5 → scale it in Phase 3
- If all campaigns have CPI over $10 → reduce Phase 3 budget, redirect to creator spend
- If CPI is $5-10 → scale cautiously, monitor daily

### Remaining Budget
- $600 on Apple Ads
- $300-500 on micro-creators (2-3 creators, direct outreach)
- Rest (~$6,200) = operating runway

### Why $600, Not More
At $12 avg game CPI, $600 = ~50 installs. Paid installs don't impress a16z. Organic growth spiking from creator content does. Keep ad spend lean for data, put energy into organic.

---

## Sources

- [Apple Ads Benchmarks 2025 — AppTweak](https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks)
- [Apple Search Ads Costs 2026 — Business of Apps](https://www.businessofapps.com/marketplace/apple-search-ads/research/apple-search-ads-costs/)
- [Apple Ads Basic vs Advanced — SplitMetrics](https://splitmetrics.com/blog/apple-search-ads-basic-vs-advanced-how-to-choose-the-right-one/)
- [Ultimate Guide to Apple Search Ads 2026 — AppTweak](https://www.apptweak.com/en/aso-blog/guide-to-apple-search-ads)
- [Apple Ads Cost Evaluation — SplitMetrics](https://splitmetrics.com/blog/apple-search-ads-cost/)
- [Games CPI Benchmarks — Watsspace](https://watsspace.com/blog/apple-search-ads-cpi-benchmark-by-industry/)
- [Apple Expands App Store Search Ads 2026 — MacRumors](https://www.macrumors.com/2025/12/18/app-store-search-results-more-ads-2026/)
