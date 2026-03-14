# Deep Research Prompts — Spacezero Speedrun GTM Sprint

---

## Prompt for Google Gemini Deep Research

```
I need comprehensive research on go-to-market strategies for an indie browser-based voxel sandbox game launching on an extremely tight timeline — 2 weeks, with a budget of $1,000–$2,000. The goal is to generate visible market traction (social media views, website visitors, user signups) to include in an accelerator application due March 25, 2026.

## About the game: Spacezero

Spacezero is a browser-based voxel sandbox game — think Minecraft, but running entirely in the browser with no download required. The core technical differentiator is our Hermite dual-contouring engine, which took 6 months to build. Unlike Minecraft's marching cubes engine that can only produce cubic/blocky shapes, our engine supports:

- Smooth curves, perfect spheres, and circular shapes — literally impossible in Minecraft
- Smooth, organic terrain (not blocky landscapes)
- AI-native unlimited texture variations (no texture packs, no mods needed)
- Photo-to-item pipeline: users snap a photo of any real-world object with our companion iOS app (Zerocap) and it becomes a usable in-game item
- AI companion integration: the companion app modifies terrain and generates content — similar to the Pokémon × Minecraft concept that Nintendo/Niantic just shipped with Pokopia, but browser-native and AI-native

The game runs in the browser — anyone can play by clicking a link. Zero friction. This is a massive GTM advantage over native games that require downloads.

## Our situation

- Team of 4 (startup called Zero, formerly Spacezero). Two co-founders + two founding engineers.
- Two of us (David + Hoon) are focused on Spacezero GTM. The other two handle the companion app (Zerocap) GTM separately.
- We're applying to a16z's Speedrun accelerator program. They want to see "a little spark from the market" — their words. Social media views, visitor counts, and signups all count as traction signals. They value velocity (week-over-week growth) over absolute numbers.
- Budget: $1,000–$2,000 for Spacezero GTM specifically. We can spend $0 if organic strategies work.
- We've been building the engine for 6 months and are now ready to go to market for the first time.

## What I need researched

### 1. Viral indie game launches with small/zero budgets
Research specific case studies of indie games (especially browser games, sandbox games, or Minecraft-adjacent games) that achieved viral traction with little to no marketing budget. I want to know:
- What channels did they use? (Reddit, TikTok, YouTube, Hacker News, Discord, Twitter/X, Product Hunt, etc.)
- What was the content format that went viral? (gameplay clips, dev logs, challenge series, comparison videos, etc.)
- How quickly did traction build? Days? Weeks?
- What were the actual numbers? (views, visits, signups, downloads)
- What made it work — what was the hook?

Specific games to look at: Vampire Survivors, Among Us, Agar.io, Slither.io, Krunker.io (browser FPS), Minecraft itself (early days), Hytale (announcement trailer virality), Palworld, and any recent (2024–2026) indie games that blew up organically.

### 2. Reddit as a GTM channel for games
- Which gaming subreddits are most effective for indie game promotion? (r/Minecraft, r/Minecraftbuilds, r/gaming, r/IndieGaming, r/WebGames, r/browsers, r/gamedev, r/playmygame, etc.)
- What post formats perform best? (video, GIF, image, text with link?)
- What gets posts removed vs. what's allowed? Promotional rules per subreddit.
- Case studies of games that went viral on Reddit — what was the post, what subreddit, how many upvotes, what was the traffic impact?
- Reddit paid ads for games: CPM rates, targeting options for gaming subreddits, conversion rates, best practices, creative formats.
- Timing: best days/times to post for maximum visibility.

### 3. Short-form video strategies for game launches
- TikTok, YouTube Shorts, Instagram Reels strategies specifically for indie game marketing
- What hooks work for gaming content? First 3 seconds matter — what grabs attention?
- "Day X" challenge series format — has this worked for games? Examples?
- Side-by-side comparison content (e.g., "Minecraft vs. our game") — does this perform well or get flagged?
- Hashtag strategies for gaming content on each platform
- Posting frequency and consistency data — how many days of posting before the algorithm picks you up?
- Any data on browser game promotion specifically on short-form video

### 4. Influencer / creator outreach for indie games
- How do indie games with no budget successfully get creators to play their game?
- What's the response rate for cold outreach to nano-creators (1K–50K followers)?
- What platforms do Minecraft creators prefer for outreach? (email, DM, Discord?)
- What makes a pitch to a creator compelling when you have no budget?
- Examples of indie games that grew primarily through creator seeding
- Gifting vs. paid placement vs. affiliate/rev-share models — what works at our stage?
- Specific Minecraft creator communities or networks to tap into

### 5. Hacker News / Show HN for technical products
- How do browser-based games/demos perform on Hacker News?
- What makes a Show HN post successful? Title format, description, timing?
- Examples of games or technical demos that hit the front page — what were the results?
- Typical traffic numbers from an HN front page hit
- How to write the Show HN description for maximum engagement

### 6. The "Minecraft but better" positioning
- Has any game successfully positioned itself as "Minecraft but [X]"? How did it go?
- What messaging resonates with the Minecraft community vs. what triggers defensiveness?
- How did games like Hytale, Veloren, Minetest, or Vintage Story position themselves?
- The "impossible in Minecraft" angle — has anyone used this kind of comparative framing successfully?

### 7. Timing: Pokopia launch and the Minecraft-alternative conversation
- Pokopia (Nintendo/Niantic's Pokémon × Minecraft game) just launched in early March 2026. Research the current conversation around Minecraft alternatives.
- What's trending in the Minecraft/sandbox gaming space right now?
- Are there content trends or conversations we can ride?
- Search volume trends for "Minecraft alternative," "browser Minecraft," "voxel game," etc.

### 8. Accelerator application traction benchmarks
- What level of traction have successful Speedrun (a16z) applicants shown at application time?
- What do pre-seed accelerators (Y Combinator, Speedrun, SPC, Techstars) actually consider "good" traction for a game?
- Examples of gaming companies that got into top accelerators — what were their numbers?
- What metrics matter most: DAU, signups, social views, revenue, or growth rate?

Please be specific with numbers, links, and examples wherever possible. I need actionable intelligence, not general advice.
```

---

## Prompt for ChatGPT Deep Research

> **Remember: Connect the Spacezero GitHub repository before running this.** This grounds the research in our actual codebase and architecture.

```
I need deep, actionable research on go-to-market strategies for Spacezero — a browser-based voxel sandbox game we're launching in the next 2 weeks to build traction for our a16z Speedrun accelerator application (due March 25, 2026).

## Context on Spacezero (connected repo)

You have access to our GitHub repository. Spacezero is a browser-based voxel sandbox game built with a custom Hermite dual-contouring engine. Key technical facts from the codebase:

- Hermite dual-contouring allows smooth curves, spheres, and organic shapes — fundamentally different from Minecraft's cubic marching cubes approach
- Runs entirely in the browser (WebGL/WebGPU) — no download, no install, zero friction
- AI-native: integrates with our companion iOS app Zerocap for AI-generated textures and photo-to-item conversion
- 6 months of engine development

The engine's capability to render smooth, curved surfaces in a voxel world is our primary differentiator and the foundation of our GTM messaging.

## The situation

- 4-person startup (team name: Zero). Two people on Spacezero GTM (David + Hoon), two on Zerocap GTM.
- Applying to a16z Speedrun by March 25. They want "a little spark from the market" — views, visitors, signups, velocity.
- Marketing budget: $1,000–$2,000 for Spacezero.
- First time going to market with this product. Engine is built; now we need eyeballs.
- The products are interconnected: Zerocap (AI companion) feeds into Spacezero (the game world). Think Pokémon × Minecraft (like Pokopia by Nintendo/Niantic, which just launched).

## Research I need — be exhaustive

### Part 1: Channel-by-channel GTM deep dive

For EACH of the following channels, research real-world case studies, conversion data, best practices, and specific tactics for indie game launches. I need numbers, not generalizations.

**Reddit:**
- Organic posting strategies for r/Minecraft (8M members), r/Minecraftbuilds, r/gaming (38M), r/IndieGaming, r/WebGames, r/gamedev, r/playmygame
- Post format effectiveness: video vs GIF vs image vs text. What's the data?
- Subreddit-specific rules on self-promotion — which subs allow it, which don't, and how to work within the rules
- Reddit paid ads: CPM/CPC for gaming subreddits, conversion benchmarks, minimum effective budget, creative best practices
- Case studies: indie games that blew up on Reddit. What was the post? What subreddit? How many upvotes? What happened to their traffic?
- Best posting times for gaming subreddits
- How to handle the "shill" accusation — framing strategies that come across as genuine

**TikTok / YouTube Shorts / Instagram Reels:**
- Indie game marketing on short-form video: what works in 2025–2026?
- Hook formulas for the first 3 seconds of gaming content
- "Day X of [doing something]" challenge format — performance data for games specifically
- Comparison content ("Minecraft vs X") — does this get views or get flagged?
- Hashtag strategies: #indiegame #minecraft #voxel #browsergame #gamedev — which ones actually drive discovery?
- Posting cadence: how many posts before the algorithm starts pushing your content?
- Cross-posting strategy: same content on all 3 platforms or platform-specific edits?
- Any data on browser game promotion via short-form video

**Hacker News (Show HN):**
- Browser game/demo Show HN posts that hit the front page — compile examples with traffic numbers
- Best title format, description structure, and timing (day of week, time of day)
- How technical should the framing be? "Dual-contouring engine" vs "Minecraft but smooth"
- Average traffic from an HN front page hit for a browser-based product
- How to handle the HN comment section (technical questions about the engine, etc.)

**Creator/Influencer outreach:**
- Cold outreach to Minecraft nano-creators (1K–50K): response rates, best platforms for DMs, what makes a pitch work
- How to find and contact Minecraft creators efficiently (tools, directories, methods)
- Creator seeding playbooks from successful indie game launches
- Gifting vs paid placement vs affiliate models — what works at pre-revenue stage?
- Eyestream (Minecraft YouTuber) and similar faith-based or community-driven creators — how to approach authentically
- How many creators should you reach out to for a 2-week sprint? What's a realistic conversion funnel (outreach → response → post)?

**Other channels to evaluate:**
- Product Hunt: does it work for games? Examples?
- Twitter/X gaming community: worth the effort on a 2-week timeline?
- Discord servers: which gaming Discords allow promotion? How to infiltrate authentically?
- Steam Next Fest / itch.io — relevant for a browser game?
- Gaming press / indie game journalists: too slow for 2 weeks, or worth a shot?
- Twitch micro-streamers: approach them to play live?

### Part 2: The "impossible in Minecraft" viral angle

This is our core messaging hook. Research deeply:

- Has any game successfully gone viral with a "things you can't do in Minecraft" angle?
- What visual content formats best showcase "smooth curves in a voxel world"? (Timelapse builds, side-by-side, before/after, etc.)
- Psychological hooks: why does seeing a sphere in a voxel world create such a strong reaction? (Novelty, cognitive dissonance, "wait that's illegal" meme format)
- Minecraft community sentiment: are they receptive to alternatives, or defensive? How to navigate this?
- Specific video concepts that would maximize shareability:
  - "Building a perfect sphere in a voxel game"
  - "What if Minecraft terrain was smooth?"
  - "Digging a perfectly round tunnel"
  - "Things impossible in Minecraft that I can build in my browser"
- Meme formats that could work: "wait, that's illegal," "the good ending," satisfaction videos, etc.

### Part 3: Browser game GTM advantages

Spacezero's biggest GTM edge is zero friction — click a link, you're playing.

- Research how browser games have leveraged this in marketing (Agar.io, Slither.io, Krunker.io, etc.)
- Link-in-bio strategies for social media (direct to game, no app store redirect)
- QR code to instant gameplay — has anyone done this effectively?
- How does "no download required" change conversion math compared to native games?
- Browser game virality loops: in-game sharing, invite mechanics, etc.

### Part 4: Competitive landscape and timing

- Pokopia (Nintendo/Niantic, Pokémon × Minecraft) launched early March 2026. Map the current conversation:
  - What are people saying about Minecraft alternatives right now?
  - What search terms are trending?
  - What content is performing well in this space?
- Current state of the voxel game market: Minecraft, Hytale status, Veloren, Vintage Story, Minetest, others
- "AI-native gaming" — is this a category yet? Who else is positioning here?
- Sandbox + AI companion games — competitive landscape

### Part 5: Two-week sprint execution playbooks

- Find examples of game launches that generated significant traction in 14 days or less
- What's the realistic upper bound of what 2 people can achieve in 2 weeks with $2K?
- Day-by-day sprint templates for indie game launches
- Content production speed: how many clips/posts per day is sustainable for a 2-person team?
- When in the 2 weeks should paid ads start? (after organic signal, or immediately?)

### Part 6: Metrics and what "good" looks like

- What traction numbers have successful a16z Speedrun applicants shown? (any public data, founder interviews, blog posts)
- Pre-seed gaming company traction benchmarks for top accelerators (YC, Speedrun, SPC)
- What's a realistic target for 2 weeks of effort: 10K views? 50K? 100K? How many signups?
- Which metrics tell the best "velocity" story? (Week 1 vs Week 2 growth rate)

Be specific. Include links, numbers, dates, and real examples. I need a research report I can act on immediately, not a strategy deck full of generalities.
```

---

## Prompt for Gemini Deep Research — Target Metrics & Scenario Modeling

```
I need you to build a detailed target-metrics model for a browser game's 14-day go-to-market sprint. This is for a real application to a16z's Speedrun accelerator (deadline: March 25, 2026).

Context:
- Product: Spacezero — browser-based voxel sandbox game. No download required. Uses Hermite dual-contouring engine (smooth curves/spheres — impossible in Minecraft). Think "Minecraft but with curves, in your browser."
- Team: 2 people on GTM (David + Hoon). Total company is 4 people.
- Budget: $1,000–$2,000 for marketing.
- GTM channels (ranked): (1) Show HN, (2) Reddit organic, (3) Creator outreach (300-600 cold emails to nano/micro gaming YouTubers/TikTokers), (4) TikTok/YouTube Shorts, (5) Reddit paid ads.
- Key advantage: Browser = 37% of page viewers convert to players (vs 6% for download games). Zero friction.
- What Speedrun wants: "A little spark from the market." They value velocity (week-over-week growth) over absolute numbers. Views, visitors, signups all count.

What I need you to research and model:

1. **Channel-by-channel yield estimates with real data**
   - Show HN for browser games/tools: median vs top-quartile traffic (visitors, not just pageviews). How many actually play? What's the typical traffic curve (day 1 vs day 2-7)?
   - Reddit organic posts in gaming subreddits: upvote-to-visitor conversion, typical reach for indie game posts that hit front page of a subreddit vs don't.
   - Cold email outreach to gaming creators: response rates, coverage rates (what % actually make a video), typical view counts for nano-influencer (5K-50K subs) gaming content.
   - TikTok/YouTube Shorts organic: typical view range for indie game content from accounts with 0-1K followers. What's the viral threshold?
   - Reddit paid ads for gaming: CPM, CTR, CPC benchmarks for gaming subreddits specifically.

2. **Scenario modeling: Bull / Base / Bear for each channel AND combined**
   - For each channel, give me three scenarios with specific numbers (visitors, players, signups).
   - Then combine into an aggregate 14-day projection: total unique visitors, total players (using 37% browser conversion), total signups, estimated D1/D7 retention.
   - Include a timeline: what numbers we'd realistically have by day 3, day 7, day 14.

3. **"Enough for Speedrun" threshold analysis**
   - Based on what companies that got into Speedrun (and YC) actually had at application time, what's the minimum credible traction package?
   - What numbers would put us in Tier 1 (almost certainly interviewed) vs Tier 2 (likely interviewed) vs Tier 3 (possible)?
   - How do social media views/impressions factor in vs actual users? What's the conversion ratio Speedrun likely applies mentally?

4. **Growth rate modeling**
   - If we launch Show HN on day 1 and get X visitors, what does a realistic WoW growth curve look like?
   - Model three growth scenarios: 5% WoW (decent), 10% WoW (good), 20% WoW (exceptional).
   - What specific actions in week 2 sustain or accelerate growth after the HN spike decays?

5. **Comparable benchmarks — browser games specifically**
   - Agar.io, Slither.io, Krunker.io, Shell Shockers: what were their first-week and first-month numbers?
   - Any Show HN browser game launches with known traffic data?
   - Browser game retention benchmarks specifically (these differ significantly from mobile/PC games).

6. **The target dashboard**
   - Give me a single table with: Metric | Bear | Base | Bull | "Speedrun Minimum"
   - Metrics should include: unique visitors, players (browser sessions), signups/accounts, D1 retention, D7 retention, social media total views, creator videos published, WoW growth rate, Discord members.

I want real numbers from real launches, not theoretical frameworks. Cite specific examples. If data doesn't exist for browser games, use the closest comparable (browser tools, .io games, web apps launched on HN).
```

---

## Prompt for ChatGPT Deep Research — Target Metrics & Scenario Modeling

```
Research task: Build a quantitative target-metrics framework for a browser game launching in a 14-day sprint, targeting a16z Speedrun acceptance.

Background:
- Spacezero is a browser-based voxel sandbox game (no download). Hermite dual-contouring engine enables smooth curves and spheres — something Minecraft's engine literally cannot do. It runs in a browser tab.
- 2-person GTM team, $1-2K budget.
- Channels in order: Show HN → Reddit organic → Creator outreach (300-600 emails) → TikTok/Shorts → Reddit paid ads.
- Browser games convert 37% of page viewers to players (vs 6% for download). This is our biggest advantage.
- a16z Speedrun cares about velocity (WoW growth), not absolute scale. "A little spark" is enough. Deadline: March 25, 2026.

I need a comprehensive, data-backed analysis:

**Part 1: Channel yield benchmarks (with sources)**
Find real data on:
- Show HN traffic for browser-playable demos, games, and creative tools. What's median traffic day 1? Top 10%? How fast does it decay? What % of HN visitors actually engage (click play, spend >30 seconds)?
- Reddit gaming posts: organic reach by subreddit size. What does a front-page post on r/gaming vs r/indiegaming vs r/WebGames actually deliver in unique visitors? What's the upvote-to-click ratio?
- Creator outreach ROI: for nano-influencers (5K-50K subs) in gaming, what's the typical: response rate to cold email, video creation rate, views per video, click-through to game?
- TikTok/Shorts for indie games from zero-follower accounts: what view counts are realistic? What triggers algorithmic boost?
- Reddit ads for gaming: 2024-2026 CPM, CTR, cost-per-click data. Best-performing ad formats.

**Part 2: Three-scenario projection model**
Build bull/base/bear projections for a 14-day sprint using the channels above:
- Day-by-day estimates for: unique visitors, players (37% of visitors), account signups (estimate conversion), cumulative totals
- Per-channel breakdown so we can see which channels drive what
- Week 1 vs Week 2 comparison (can we show WoW growth?)

**Part 3: What "good enough for Speedrun" actually looks like**
- Research what traction Speedrun companies had at application. Find specific examples if possible.
- Map our projected scenarios to Speedrun's evaluation framework.
- What's the minimum viable traction package? What would make us a strong applicant?
- How do they weigh different types of traction (users vs views vs revenue vs community)?

**Part 4: Retention and engagement targets**
- Browser game retention benchmarks: D1, D7, D30 (these are different from mobile — find browser-specific data if it exists, .io game data is closest)
- Session length benchmarks for browser sandbox games
- What retention numbers are realistic for a 14-day-old browser game?
- DAU/MAU expectations

**Part 5: The target table**
Produce a single reference table:
| Metric | Bear (25th %ile) | Base (50th %ile) | Bull (75th+ %ile) | Speedrun Threshold |
For: total visitors, total players, signups, D1 retention, D7 retention, WoW growth rate, social views, creator videos, Discord members, HN comments/upvotes.

**Part 6: Risks and what kills the growth curve**
- What typically goes wrong in indie game launches that kills momentum?
- For browser games specifically, what are the common failure modes?
- What should we monitor daily to catch problems early?

Use real data, real examples, real launches. Cite everything. I don't want theoretical frameworks — I want numbers I can plan against.
```

---

## Notes

- **Gemini prompt** is optimized for broad web research — market data, case studies, benchmarks, trends
- **GPT prompt** is optimized for depth + codebase context — connect the GitHub repo so it can ground recommendations in what we've actually built
- **Metrics prompts** (both) are focused on quantitative projections and scenario modeling — run these after the GTM research is done
- Run both and compare — they'll surface different things
- Feed the best findings back to Claude Code for synthesis and execution planning
