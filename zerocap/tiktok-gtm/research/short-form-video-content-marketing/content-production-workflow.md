# Content Production Workflow for a 2-Person Team

Efficient workflow to produce 7-14 unique short-form videos per week across TikTok, YouTube Shorts, and Instagram Reels -- with just two people.

---

## 1. Recording iOS Gameplay

### Option A: Built-in iOS Screen Recording (Simplest)

**How:** Control Center → Screen Recording button. Records everything on screen at device resolution.

- **Pros:** Zero setup. Native to iOS. Records at full resolution. Free.
- **Cons:** Records system UI (notifications, status bar). No in-game audio isolation by default. Cannot record face/reactions simultaneously.
- **Best for:** Quick gameplay captures, timelapse base footage, prototype recording.

**Pro tip:** Enable Do Not Disturb before recording to prevent notification popups from ruining footage.

### Option B: ReplayKit (Developer-Integrated Recording)

**How:** Apple's ReplayKit framework can be integrated directly into SpaceZero's codebase. It allows in-app recording with optional microphone audio.

- **Key features:**
  - Records screen + audio without capturing system UI
  - "Rolling clips" feature (iOS 15+): maintains a 15-second buffer of recent gameplay, perfect for capturing "moments" after they happen
  - Can be triggered by in-game button
  - Export directly to Photos or share sheet
- **Pros:** Cleanest footage quality. No system UI captured. In-app share integration possible.
- **Cons:** Requires dev implementation. Does not work while AirPlay or screen mirroring is active. Physical device required (doesn't work in simulator).
- **Best for:** This should be SpaceZero's built-in recording feature long-term. It's the foundation for the UGC flywheel (Roblox's Clip It equivalent).

**Recommendation:** Use built-in iOS Screen Recording NOW for content creation. Build ReplayKit integration into SpaceZero as a product feature for user-generated content.

### Option C: External Capture (for highest quality)

**How:** Connect iPhone to Mac via Lightning/USB-C, use QuickTime Player "New Movie Recording" and select iPhone as source.

- **Pros:** Highest quality capture. Records at device resolution. Can simultaneously record Mac audio.
- **Cons:** Requires Mac + cable. Not portable. Slight latency in preview (doesn't affect recording quality).
- **Best for:** High-quality footage for App Store preview video and polished content pieces.

### Recording Best Practices for Content Batching

- **Record in landscape AND portrait in the same session.** Portrait is native for TikTok/Reels/Shorts. Landscape can be cropped or used for YouTube long-form.
- **Record 30-60 minutes of continuous gameplay per session.** This produces 15-20+ unique short clips after editing.
- **Record at the highest quality setting available.** Downscaling is always possible; upscaling loses quality.
- **Capture "B-roll" gameplay:** Let the game run while building things naturally. Don't only record "perfect" takes. Natural, imperfect building moments are more authentic and perform better on short-form video.

Sources: [Apple Developer: ReplayKit](https://developer.apple.com/documentation/replaykit), [Apple WWDC21: Rolling Clips with ReplayKit](https://developer.apple.com/videos/play/wwdc2021/10101/), [DemoCreator: How to Record iPhone Gameplay](https://democreator.wondershare.com/screen-recorder/record-gameplay-on-iphone.html)

---

## 2. Editing Tools for Short-Form Video

### Tier 1: Primary Editor

**CapCut (Free, iOS + Desktop)**

CapCut is the standard editing tool for short-form video creators in 2026. Here's why it's the right choice for SpaceZero's two-person team:

| Feature | Why It Matters for SpaceZero |
|---------|------------------------------|
| **Auto-captions** | One-tap subtitle generation. Critical for TikTok (many viewers watch with sound off). Saves 15-20 minutes per video vs. manual captioning. |
| **Templates** | Pre-built templates matching trending TikTok formats. Apply a template to raw footage for instant formatted content. |
| **Batch export** | Export multiple clips in different formats simultaneously. Create TikTok + Reels + Shorts versions from one project. |
| **Mobile + desktop sync** | Start editing on iPhone, finish on desktop (or vice versa). Cloud saving preserves projects across devices. |
| **Trending effects** | Access to TikTok-trending effects, transitions, and audio. Keeps content current. |
| **AI features** | Auto-cut long videos into highlights. "Smart trim" identifies the most engaging segments. |
| **1080p export** | Full HD export at no cost. No watermark on free tier. |
| **Direct posting** | Export and share directly to TikTok, YouTube, and Instagram from the app. |

**Cost:** Free for all core features. Pro plan ($9.99/month) adds cloud storage, premium effects, and removes some limits on AI features. The free tier is sufficient for SpaceZero's needs.

### Tier 2: AI Clip Generation (For Volume)

**OpusClip ($19/month starter)**

For turning long recording sessions into multiple short clips automatically:

| Feature | How to Use It |
|---------|---------------|
| **Auto-clip detection** | Upload a 30-60 minute recording session. OpusClip identifies the most engaging 15-60 second segments automatically. |
| **AI scoring** | Each generated clip gets a "virality score" based on pacing, visual engagement, and hook strength. |
| **Auto-captions** | Animated, word-by-word captions overlaid automatically. |
| **Multi-platform export** | Export clips pre-formatted for TikTok, Shorts, and Reels simultaneously. |

**Workflow:** Record 30-60 minutes of gameplay → Upload to OpusClip → Get 10-15 suggested clips → Review and refine top 5-7 in CapCut → Post across platforms.

### Tier 3: Specialty Tools

| Tool | Purpose | Cost | When to Use |
|------|---------|------|-------------|
| **Descript** | Text-based video editing (edit the transcript, the video follows) | Free tier available, Pro $24/month | For voiceover/narration content. Edit by reading text instead of scrubbing timelines. |
| **Submagic** | Premium animated captions (emoji-enhanced, word-by-word highlighted) | $24/month | When you want TikTok-native caption styling that stands out. |
| **ZapCap** | Best caption accuracy (uses OpenAI Whisper, 50+ languages) | Pay-per-video | For content with accents, technical jargon, or non-English audio. |
| **Canva** | Thumbnail/cover image creation | Free tier sufficient | For YouTube Shorts custom thumbnails and Instagram Reel covers. |

**Recommendation for SpaceZero:** Start with CapCut (free) for all editing. Add OpusClip ($19/month) when you have enough gameplay footage to batch-process. That's a $19/month total editing stack.

Sources: [OpusClip: Best YouTube Shorts Editing Apps 2026](https://www.opus.pro/blog/best-youtube-shorts-editing-apps), [Genesys Growth: Descript vs CapCut vs Clipchamp 2026](https://genesysgrowth.com/blog/descript-vs-capcut-vs-clipchamp), [AI Hustle Guy: Opus Clip vs CapCut vs Descript](https://www.aihustleguy.com/blog/descript-vs-capcut-vs-opus-clip-ai-video-editor)

---

## 3. Batch Production Workflow: One Session → One Week of Content

### The "Content Day" System

**Dedicate one full day per week to content production.** This is the most efficient model for a two-person team. Here's the exact workflow:

**Monday: Content Day (6-8 hours total)**

```
MORNING (3 hours): Recording Session
─────────────────────────────────────
09:00-09:30  Plan the 7-10 videos you'll create this week (see Content Ideas doc)
             Write down hooks and key moments for each
09:30-10:30  Recording Block 1: Build timelapses (record 3-4 builds start to finish)
             Use built-in iOS screen recording
             Record in portrait mode
             Let builds play out naturally -- you'll speed them up in editing
10:30-11:00  Recording Block 2: POV/Story clips (record 3-4 scenarios)
             Quick setups, multiple takes OK
11:00-11:30  Recording Block 3: Behind-the-scenes / talking-to-camera content
             Use iPhone front camera
             Natural lighting, casual setting
11:30-12:00  Review footage. Flag the best moments. Delete obvious fails.

AFTERNOON (3-4 hours): Editing Session
─────────────────────────────────────
13:00-13:30  Upload long recordings to OpusClip for AI clip suggestions
13:30-15:00  Edit 5-7 clips in CapCut:
             - Trim to 15-25 seconds
             - Add text overlay hooks
             - Add auto-captions
             - Select background music/sound effects
             - Add end-screen CTA text
15:00-15:30  Export all clips in three formats:
             - TikTok (9:16, with TikTok-specific caption)
             - YouTube Shorts (9:16, with keyword-rich title)
             - Instagram Reels (9:16, with Reels-specific caption)
15:30-16:00  Write captions and hashtags for each platform
             Queue everything in scheduling tool

EVENING (1 hour): Scheduling
─────────────────────────────────────
16:00-17:00  Schedule the week's posts across all platforms
             - 1 post/day × 3 platforms = 21 posts/week
             - Stagger posting times (TikTok first, then Shorts 2-6 hours later,
               then Reels 2-6 hours later)
```

**Tuesday-Sunday: Engage & Monitor (30-60 minutes/day)**
- Reply to every comment within 30 minutes of posting
- Monitor which videos are gaining traction
- If a video hits 10K+ views, create a follow-up within 24 hours (breaks the batch schedule, but worth it)
- Note what's working for next Monday's planning session

### Repurposing One Recording Session into 5-10 Unique Clips

**The "One Build, Five Videos" Method:**

From a single 20-minute build recording, extract:

| Video # | What to Extract | Format | Length |
|---------|----------------|--------|--------|
| 1 | Full build timelapse (compressed) | Satisfying timelapse | 20-25s |
| 2 | The most impressive 5 seconds (zoomed in on a detail) | Visual hook / teaser | 8-12s |
| 3 | Before vs. after (first frame vs. last frame) | Comparison | 10-15s |
| 4 | The build in reverse (finished product "deconstructing") | Reverse reveal | 15-20s |
| 5 | Mid-build "guess what this is" (show the build at 30% completion) | Interactive/engagement bait | 10-15s |
| 6 (bonus) | Real-time segment of the trickiest part of the build | Skill showcase | 15-20s |
| 7 (bonus) | Cinematic fly-through of the finished build | Showcase/spectacle | 15-20s |

**This is how you hit 7+ posts/week from one recording day.** The same raw footage produces different content for different psychological triggers.

Sources: [Buffer: Content Batching Guide](https://buffer.com/resources/content-batching/), [CutBack Video: Batch Filming & Editing](https://cutback.video/blog/batch-filming-editing-the-creator-s-secret-to-posting-consistently), [CapCut: Batch Process Video Editing](https://www.capcut.com/resource/batch-process-video-editing)

---

## 4. Auto-Captioning and Subtitle Tools

### Why Captions Are Non-Negotiable

- TikTok's semantic indexing reads auto-captions to categorize and rank content
- Instagram users frequently browse with sound off
- Captions increase accessibility and watch time
- Animated captions (word-by-word highlight) are the dominant style on TikTok in 2026

### Tool Comparison

| Tool | Accuracy | Style Options | Speed | Cost | Best For |
|------|----------|--------------|-------|------|----------|
| **CapCut auto-captions** | Good (90-95%) | Multiple font/animation styles. TikTok-native styling. | Fast (< 1 min) | Free | Default choice. Good enough for most content. |
| **Submagic** | Very good (95%+) | Premium animated captions, emoji-enhanced, word-by-word highlight | Fast | $24/month | When you want the most eye-catching captions. |
| **ZapCap** | Best (uses OpenAI Whisper) | Clean, professional styles | Fast | Pay-per-video | Accents, technical terms, non-English content. |
| **Descript** | Excellent (95%+) | Professional, clean. Less "TikTok-native" styling. | Medium | Free tier / $24/mo | When editing via transcript (narration-heavy content). |

**Recommendation:** Use CapCut's built-in auto-captions for everything. It's free, fast, and produces TikTok-native caption styling. Only upgrade to Submagic or ZapCap if caption accuracy becomes a visible problem.

---

## 5. Scheduling Tools for Cross-Platform Posting

### Tool Comparison

| Tool | Platforms Supported | Key Feature | Cost | Best For |
|------|-------------------|-------------|------|----------|
| **Buffer** | TikTok, YouTube Shorts, Instagram Reels, + 10 more | Free plan covers 3 channels. Clean scheduling UI. | Free (3 channels) / $6/mo per channel | SpaceZero's starting point. Free tier covers TikTok + YouTube + Instagram. |
| **Repurpose.io** | TikTok, YouTube, Instagram, + 15 more | Auto-repurpose: upload once, auto-format and post to all platforms. Strips TikTok watermarks automatically. Auto-generates captions. | $35/month (14-day free trial, 10 free videos) | When volume increases and manual cross-posting becomes a time sink. |
| **Later** | TikTok, Instagram, YouTube, Facebook, Pinterest, LinkedIn | Visual grid planner. Strong Instagram focus. Auto-schedule Reels and Stories. | Free (limited) / $25/month | If Instagram Reels becomes the primary growth channel. |
| **Metricool** | TikTok, YouTube, Instagram, + more | Combined scheduling + analytics. Shows best posting times. | Free (limited) / $22/month | When you want scheduling + analytics in one tool. |

### Recommended Stack Progression

**Phase 1 (Weeks 1-2): Manual posting**
- Post directly from CapCut/phone to each platform
- This forces you to learn each platform's native UI and posting quirks
- Time cost: ~15 minutes/day

**Phase 2 (Weeks 3-4): Buffer (free tier)**
- Schedule posts in advance across all three platforms
- Plan the week's content in one session
- Time cost: ~1 hour/week (on Content Day)

**Phase 3 (Weeks 5+): Repurpose.io (if budget allows)**
- Upload once → auto-format and distribute to all platforms
- Strips watermarks automatically
- Biggest time saver for cross-platform workflow
- Time cost: ~30 minutes/week

### Cross-Posting Rules

1. **NEVER cross-post with watermarks.** Instagram suppresses TikTok-watermarked content. YouTube suppresses it too. Always download without watermark or use Repurpose.io which strips them automatically.
2. **Stagger posting times.** Post to TikTok first (highest discovery ceiling), then YouTube Shorts 2-6 hours later, then Instagram Reels 2-6 hours later.
3. **Adjust captions per platform.** Same video, different caption:
   - TikTok: Shorter, trending hashtags, CTA in comments
   - YouTube: Keyword-rich title, description with links
   - Instagram: DM-share-bait caption ("Send this to someone who..."), 3-5 hashtags

Sources: [Buffer](https://buffer.com/), [Repurpose.io](https://repurpose.io/), [Planable: Repurpose.io Alternatives](https://planable.io/blog/repurpose-io-alternatives/), [SocialRails: Repurpose.io Pricing 2026](https://socialrails.com/blog/repurpose-io-pricing)

---

## 6. Complete Weekly Content Calendar Template

### For a Two-Person Team Producing 7 Unique Videos/Week

| Day | Activity | Person 1 (Builds/Edits) | Person 2 (Posts/Engages) |
|-----|----------|------------------------|--------------------------|
| **Monday** | Content Day | Record 30-60 min gameplay. Edit 7+ clips. | Write captions, hashtags, schedule posts for the week. |
| **Tuesday** | Post Day 1 | Post TikTok at 7 PM | Post YouTube Short at 9 PM. Reply to comments on TikTok. |
| **Wednesday** | Post Day 2 | Post Instagram Reel (yesterday's TikTok) at 12 PM | Post new TikTok at 7 PM. Reply to all comments. |
| **Thursday** | Post Day 3 | Post YouTube Short at 12 PM | Post new TikTok at 7 PM. Reply to all comments. |
| **Friday** | Post Day 4 | Post Instagram Reel at 6 PM | Post new TikTok at 8 PM. Monitor for viral breakout. |
| **Saturday** | Post Day 5 | Post YouTube Short at 3 PM | Post new TikTok at 7 PM. Weekend engagement surge. |
| **Sunday** | Review + Plan | Analyze week's performance. Note top performers. | Plan next week's 7 videos based on what worked. |

**If a video starts gaining traction (5K+ views in first 2 hours):**
- Create a follow-up video within 24 hours
- Reply to every comment immediately
- Pin a comment with CTA ("Download SpaceZero - link in bio")
- Create a "Part 2" or response video addressing top comments

---

## 7. Total Weekly Time Investment

| Activity | Hours/Week | Who |
|----------|-----------|-----|
| Planning (Content ideas, scripts, hooks) | 1 hour | Both |
| Recording (gameplay, talking head, B-roll) | 2-3 hours | Person 1 |
| Editing (CapCut, captions, formatting) | 3-4 hours | Person 1 |
| Caption writing, hashtags, scheduling | 1-2 hours | Person 2 |
| Daily engagement (comments, replies, DMs) | 3.5 hours (30 min/day) | Person 2 |
| Analytics review + planning | 1 hour | Both |
| **TOTAL** | **11.5-14.5 hours/week** | Split between two people |

This is manageable alongside game development. The key is the batch production model: all recording and editing happens on one day, freeing the rest of the week for dev work with only 30-60 minutes/day for engagement and posting.

---

*Research compiled February 2026.*
