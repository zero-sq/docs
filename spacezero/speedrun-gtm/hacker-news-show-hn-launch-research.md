# Hacker News Show HN Launch Research

Research date: 2026-03-12

## Overview

Deep research on using Hacker News (Show HN) as a launch channel for browser-based games, voxel engines, and technical demos. Covers successful posts, traffic benchmarks, conversion data, and tactical advice.

---

## 1. Browser Games and 3D Demos That Hit HN Front Page

### Notable Show HN Posts (Voxel / 3D / Browser Games)

| Post | Date | Notes |
|------|------|-------|
| **Show HN: I built a multiplayer voxel browser game engine** | Apr 2023 | 12-year project, multiple rewrites. Browser-based voxel MMO at earth.suncapped.com |
| **Show HN: Basic voxel engine in WebGL/JavaScript with full source** | Apr 2015 | Discussed Three.js performance limits, CPU cost of real-time voxel rendering |
| **Show HN: WebGL Voxel Engine** | Nov 2017 | Personal passion project |
| **Show HN: VoxelChain -- An Experimental Voxel Engine** | Aug 2022 | WebGL2 rendering, C89 simulation compiled to WASM with multi-threading |
| **Show HN: Procedural Voxel Rendering in WebGL** | Mar 2016 | Procedural generation focus |
| **Show HN: DotBigBang -- Multiplayer game engine with 120fps and 2 second load time** | Oct 2023 | Voxel-based 3D game engine, fully browser-based, cross-platform |
| **Show HN: Ambient, a multiplayer game engine and platform using WASM/WebGPU/Rust** | Oct 2023 | Modern stack, WASM + WebGPU |
| **Show HN: PixiBall -- WebGPU Browser Multiplayer Soccer Game** | Jun 2025 | WebGPU-based game |
| **Show HN: Play the game I'm developing directly on its website** (Athena Crisis) | Feb 2024 | Replaced landing page video with playable browser demo. Exact same code as actual game. Solo dev Christoph Nakazawa (ex-Meta, created Jest/Metro/Yarn) |
| **Show HN: A Marble Madness-inspired WebGL game built for Netlify** | Nov 2024 | Three.js with custom render pipeline, Rapier physics |
| **Show HN: Real-Time 3D Gaussian Splatting in WebGL** | Sep 2023 | Advanced graphics visualization |
| **Show HN: Rust ray tracer that runs on any GPU -- even in the browser** | Nov 2025 | Photorealistic mesh rendering, deployed via GitHub Pages |
| **Show HN: I built a 3D web-based multiplayer game with Claude Code** | Jan 2026 | AI-assisted game development showcase |
| **Show HN: TerrainVer -- Generate Worms-Style Cartoon Terrain in JavaScript** | Apr 2018 | Terrain generation demo |
| **Airmash -- Multiplayer Missile Warfare HTML5 Game** | Dec 2017 | Listed among top Show HN game posts of all time on bestofshowhn.com |

### What the Top Game Posts on bestofshowhn.com Include
- Retro video game consoles
- Airmash (multiplayer HTML5 game)
- A simulation game created over 6 years
- "Almost Pong" (web game)
- An RTS game engine in C
- Central bank simulator with realistic economic model
- A Unity-like game editor running in WASM
- Marble Madness WebGL game

### Key Reference: Mikola Lysenko's 0fps.net
Widely cited on HN -- articles "Meshing in a Minecraft Game" and "An Analysis of Minecraft-like Engines" include interactive WebGL/Three.js demos of voxel meshing. These are the canonical technical references that HN loves for voxel work.

---

## 2. Traffic from HN Front Page -- Hard Numbers

### Case Studies with Real Data

| Source | Points | Duration on FP | Unique Visitors | Notes |
|--------|--------|-----------------|-----------------|-------|
| Luke Hsiao (2023) | 722 pts, 319 comments | ~48 hours | **97,600 uniques** | Documentation blog post. Highest documented in recent data |
| Harrison Broadbent (May 2024) | 208 pts, 169 comments | ~20 hours | **15K tracked / ~20-24K actual** | 58-68% of HN users block GA |
| Adriaan van Rossum (Reproof) | Top of front page | ~1 day | **30,000 visitors** | Reproduced across multiple analyses |
| Niko Fischer | #1 ranking | ~12 hours | **11,000 uniques** | On ranking day alone |
| marcotm.com | 68 pts, 28 comments | ~1 hour on FP | **3,500-4,000** from FP, **8,000 total** over 4 days | Secondary sources doubled traffic |
| Groove HQ | Front page for a day | ~24 hours | **~18,000 visitors** | 20,000% traffic increase |
| Nebula Graph | Front page | ~13 hours | **11,000 uniques**, 300+ GitHub stars | Open source project |
| HFT Guy (2017) | Front page | Several hours | **~20,000 unique requests per FP post** | Consistent pattern across multiple posts |
| 7,112 user retrospective (dev.to) | Front page | N/A | **7,112 users** | Side project to front page |

### Traffic Benchmarks Summary
- **Bottom of front page, ~1 hour**: 3,000-5,000 visitors
- **Mid-front page, several hours**: 10,000-15,000 visitors
- **Top of front page, 12+ hours**: 20,000-30,000 visitors
- **#1 for extended period (48h+)**: 50,000-100,000 visitors
- **Secondary traffic** (aggregators, newsletters, social): 30-100% additional over 3-7 days
- **Important**: 58-68% of HN users block JavaScript analytics. Real traffic is likely 2-3x what GA reports.

### Traffic Spike Duration
- Peak traffic: first 2-6 hours
- Significant traffic: 12-24 hours
- Long tail: 3-7 days (from aggregators picking up the story, newsletter mentions, social shares)
- For browser games specifically: an interactive demo keeps people on-site longer, which helps with comment engagement (a ranking signal)

---

## 3. Conversion Rates from HN Traffic

### What We Know
- **General HN traffic to sign-up conversion**: Very low. One case study (Aidlab wearable) reported "sadly, no direct conversions, though, just a lot of curiosity"
- **Browser-playable products have a massive advantage**: No friction. Click and you're in the experience. This is categorically different from "download an app" or "sign up for a SaaS"
- **GitHub stars**: Open source projects consistently report 300+ stars from a front page hit
- **Key insight**: HN traffic is high-intent technical users but low-intent buyers. The conversion is to "trying it" (for a browser game, that's instant) rather than to paying

### Browser Games Conversion Advantage
For a browser game with no login wall:
- **Click-to-play conversion**: Near 100% (no barrier)
- **Play-to-return**: Unknown from HN data, but D1 retention would be the metric to watch
- **Play-to-share**: HN users who are impressed will comment, which drives more traffic (flywheel)

### What "Conversion" Means for a Zerocap Launch
1. Visitor lands on page
2. Game loads instantly in browser (critical -- 2-second load time is the standard DotBigBang set)
3. Player experiences the world
4. Player either: bookmarks/returns, joins Discord, wishlists on Steam, tells friends
5. The HN comments thread itself becomes social proof

---

## 4. What Makes a Show HN Post Successful

### Title Format
- **Best format**: `Show HN: [Product Name] -- [What it does in plain language]`
- **Alternative that works**: `Show HN: I built [X] to [outcome]`
- **What fails**: Marketing language, vague titles, salesy pitches
- **For a voxel/browser game**: Lead with the technical achievement, not the game itself
  - Good: `Show HN: A voxel engine with dual contouring that runs in your browser`
  - Good: `Show HN: Infinite procedural voxel worlds in WebGL -- no download needed`
  - Bad: `Show HN: Check out our awesome new game`

### Description / First Comment
- Add a comment immediately with the backstory: how you built it, what's technically interesting, what makes it different
- Tell a story -- stories perform better than feature lists
- Include technical details HN readers care about: rendering approach, mesh generation algorithm, performance numbers (FPS, chunk load time, poly count)
- If open source, link the repo
- Cut unnecessary words -- posts that perform better are direct, not short

### Best Day and Time to Post

| Strategy | Recommendation | Why |
|----------|---------------|-----|
| **Maximize front page probability** | Sunday 7AM-10PM EST | 2.5x more likely to reach front page vs Wednesday 9AM UTC. Less competition on weekends |
| **Maximize total views once on FP** | Weekday morning US time | More users active mid-week, but more competition too |
| **Most active hour** | 5-6 PM (unclear timezone, likely EST/PST) | Highest overall HN activity |
| **Best compromise** | Monday or Tuesday morning US Eastern | Good activity, less competition than Wed-Thu |

**For Show HN specifically**: Show HN posts appear on the dedicated /show page even if they fall off /new, giving them a second chance at discovery. This means timing is slightly less critical than for regular posts.

### How Technical Should the Framing Be?
- **Very technical** -- HN rewards depth over polish
- Lead with the engineering challenge, not the product
- Example framing: "I implemented dual contouring with LOD in WebGL and it runs at 60fps on a MacBook Air" > "Play our cool new voxel game"
- Discuss tradeoffs you made (marching cubes vs dual contouring, chunk management, GPU vs CPU meshing)
- Include performance benchmarks

### Handling Comments
- **Respond to every technical question** -- this is the #1 thing that keeps posts alive
- Comments are a stronger ranking signal than upvotes
- Be honest about limitations ("yeah, the LOD popping is something I'm still working on")
- If someone suggests an improvement, be gracious and engage
- Never be defensive. Never argue. Technical humility plays well
- If someone finds a bug, fix it live and post an update -- HN loves this

### State of Show HN (2025 Analysis from Sturdy Statistics)
- Show HN quality and engagement peaked in 2022, with 2021/2023/2024 still strong
- 2025 saw a significant performance decline -- likely due to AI-generated content flooding the platform
- AI-related Show HN posts actually underperform expectations (oversaturated)
- **Implication**: A genuinely impressive, non-AI technical demo (like a voxel engine) stands out MORE in 2025-2026 because it's real engineering in a sea of AI wrappers

---

## 5. Tactical Playbook for a Zerocap Show HN Launch

### Pre-Launch
1. Ensure the demo loads in under 2 seconds
2. Make it playable with zero signup / zero download
3. Have a compelling first-load experience (don't dump players in an empty world)
4. Prepare a detailed technical write-up or blog post about the engine
5. Have your GitHub repo ready (if open-sourcing any part)

### Launch Day
1. Post on **Sunday or early Monday morning EST** to maximize front page probability
2. Title format: `Show HN: [Name] -- [technical achievement] in your browser`
3. Immediately post a first comment with:
   - Your backstory (how long you've been building, what motivated you)
   - Technical details (rendering approach, algorithms, performance)
   - What's novel about your approach
   - A link to a technical blog post for deep-dive readers
4. Monitor comments every 15-30 minutes for the first 6 hours
5. Respond to every question thoughtfully

### Post-Launch
1. Track actual traffic with server-side analytics (not GA -- HN users block it)
2. Capture emails / Discord joins from the traffic spike
3. Blog about the experience ("What happened when we hit HN front page") -- this itself can go viral
4. Share the HN thread on Twitter/X for secondary amplification

### Realistic Expectations
- If you hit front page: 10,000-30,000 visitors in 24 hours
- If you hit #1: 50,000-100,000 visitors
- If you don't make front page: 200-500 visitors (still worth the post for Show HN page visibility)
- Browser game advantage: near-100% of visitors will actually try it (no download barrier)

---

## Sources
- [Traffic impact of 722 points on Hacker News](https://luke.hsiao.dev/blog/2023-hn-traffic/)
- [Anatomy of a Hacker News traffic spike (Harrison Broadbent)](https://harrisonbroadbent.com/blog/hacker-news-traffic-spike-anatomy/)
- [Hitting the top of Hacker News = 30,000 Visitors (Reproof)](https://www.reproof.app/blog/the-hacker-news-effect)
- [Stats of being on the Hacker News front page (marcotm)](https://marcotm.com/articles/stats-of-being-on-the-hacker-news-front-page/)
- [Analysis of website traffic after HN #1 ranking (Niko Fischer)](https://nikofischer.com/website-traffic-after-hacker-news-ranking)
- [Hitting the HN Front Page (HFT Guy)](https://thehftguy.com/2017/09/26/hitting-hacker-news-front-page-how-much-traffic-do-you-get/)
- [From side project to HN front page: 7,112 user retrospective](https://dev.to/skeptrune/from-side-project-idea-to-hacker-news-front-page-a-7112-user-retrospective-2p3i)
- [How to do a successful HN launch (Lucas Costa)](https://lucasfcosta.com/2023/08/21/hn-launch.html)
- [State of Show HN 2025 (Sturdy Statistics)](https://blog.sturdystatistics.com/posts/show_hn/)
- [How to Reach HN Front Page (Awesome Directories)](https://awesome-directories.com/blog/hacker-news-front-page-guide/)
- [Show HN Guidelines (official)](https://news.ycombinator.com/showhn.html)
- [Best of Show HN -- All Time](https://bestofshowhn.com/)
- [Best of Show HN -- Game Search](https://bestofshowhn.com/search?q=game)
- [How to hack HN (Indie Hackers)](https://www.indiehackers.com/post/how-to-hack-hacker-news-and-consistently-hit-the-front-page-56b4a04e12)
- [Show HN: Athena Crisis -- browser playable game](https://news.ycombinator.com/item?id=39365135)
- [Show HN: DotBigBang -- multiplayer game engine](https://news.ycombinator.com/item?id=37797606)
- [Show HN: Multiplayer voxel browser game engine](https://news.ycombinator.com/item?id=35705063)
- [voxel.js -- Minecraft-like games in the browser](https://voxeljs.com/)
- [Mikola Lysenko -- Smooth Voxel Terrain (0fps.net)](https://0fps.net/2012/07/12/smooth-voxel-terrain-part-2/)
