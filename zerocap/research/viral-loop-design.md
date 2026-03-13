# Viral Loop Design for Zerocap

**Date:** 2026-03-13
**Product:** Zerocap -- iOS AI tamagotchi app. Point your camera at any real-world object, AI transforms it into a cute living pet with unique personality traits (6M trait combinations).
**Core insight:** The "point camera, get pet" transformation moment is inherently shareable. This document analyzes how to engineer that shareability into a systematic viral growth engine.

---

## Table of Contents

1. [The Anatomy of a Viral Loop](#1-the-anatomy-of-a-viral-loop)
2. [The Transformation Moment -- Why Before/After Goes Viral](#2-the-transformation-moment)
3. [Case Studies](#3-case-studies)
4. [K-Factor Benchmarks](#4-k-factor-benchmarks)
5. [Designing the Share Artifact](#5-designing-the-share-artifact)
6. [Platform-Specific Sharing Mechanics](#6-platform-specific-sharing-mechanics)
7. [Referral Program Design](#7-referral-program-design)
8. [Social Proof Mechanics](#8-social-proof-mechanics)
9. [UGC as Distribution](#9-ugc-as-distribution)
10. [TikTok-Native Virality](#10-tiktok-native-virality)
11. ["Scan This" IRL Virality](#11-scan-this-irl-virality)
12. [Anti-Patterns -- What Doesn't Work](#12-anti-patterns)
13. [Zerocap Viral Loop Blueprint](#13-zerocap-viral-loop-blueprint)

---

## 1. The Anatomy of a Viral Loop

A viral loop is a self-reinforcing cycle where product usage creates new user acquisition. Every successful viral app follows the same fundamental structure:

```
[User action] -> [Delightful output] -> [Share trigger] -> [New user sees it] -> [Downloads app] -> [Repeat]
```

The loop has three measurable components:

- **Invitations per user (i):** How many people each user exposes to the product
- **Conversion rate (c):** What percentage of exposed people become users
- **Cycle time (t):** How quickly the loop completes one revolution

**K-factor = i x c.** When K > 1, each user generates more than one new user, creating exponential growth. When K < 1 but > 0, virality still contributes meaningful organic acquisition alongside other channels.

### Three Types of Virality

**1. Inherent virality (strongest).** The product only works or gets better when shared. WhatsApp needs your contacts. Figma needs collaborators. The act of using the product IS the invitation.

**2. Artificial virality (weakest).** Sharing is incentivized but disconnected from core value. "Invite 3 friends to unlock this feature." Users share because they're told to, not because the content demands it.

**3. Content virality (Zerocap's type).** The product creates outputs that are inherently worth sharing. The user's creation becomes the marketing. Lensa avatars, Prisma filters, FaceApp aging photos -- the output IS the content, and every share is an advertisement.

Content virality is the most powerful type for consumer apps because the user never feels like they're "marketing" anything. They're expressing themselves, entertaining friends, or showing off something cool. The app tag/watermark rides along invisibly.

### The Viral Loop Equation for Zerocap

```
1. User points camera at object               (100% -- this is the core product)
2. AI transforms object into a pet             (the "wow" moment)
3. User shares the transformation              (share rate = key lever)
4. Friends/followers see the before/after       (reach per share)
5. A percentage download the app               (conversion rate)
6. New user points camera at their own object   (loop restarts)
```

Each step is a multiplier. The product of all steps determines K-factor. Improving any single step by even 20% has compounding effects on the total.

---

## 2. The Transformation Moment

The single most viral mechanic in consumer apps is the **before/after reveal**. It works because it creates a narrative in a single frame: here's what I started with, here's what I got. The gap between input and output IS the content.

### Why Transformations Go Viral

**Cognitive surprise.** The brain is wired to notice change. A dramatic transformation triggers dopamine -- the same response that makes magic tricks compelling. When someone sees a coffee mug become a cute living creature, the mismatch between expectation and reality demands attention.

**Self-expression.** The transformation is personal -- it came from YOUR object, YOUR environment. Sharing it is identity signaling: "Look at my creative eye" or "Look at how funny my life is." This is why Lensa avatars spread so fast -- each one was unique to the person, making every share a form of self-expression.

**Low cognitive load.** A before/after image tells its own story with zero explanation needed. No context required, no captions necessary. The viewer immediately understands what happened and wants to try it themselves.

**FOMO activation.** When friends share their transformations, non-users feel left out. This is the single biggest driver of download cascades -- not admiration for the output, but the desire to create their own.

### The Transformation Hall of Fame

| App | Input | Output | Peak Virality |
|-----|-------|--------|---------------|
| Lensa AI | 10-20 selfies | 50 artistic avatar portraits | 19.3M downloads in December 2022 |
| Prisma | Any photo | Impressionist/art-style painting | 7.5M downloads in first week, zero marketing |
| FaceApp | Selfie | Aged/gender-swapped face | 30M downloads in July 2019 alone |
| EPIK | Selfies | 90s yearbook photos | 92.3M lifetime downloads, $7M iOS revenue |
| Remini (clay filter) | Selfie | 3D clay-style portrait | 286% download spike, 380K downloads/day |
| ChatGPT Ghibli filter | Any photo | Studio Ghibli-style image | 700M images generated in one week |

**The pattern is clear:** Input must be effortless (a photo you already have or can take in 1 second). Output must be dramatically different, personally relevant, and visually striking enough to share without any additional effort.

### Why Zerocap's Transformation Is Uniquely Powerful

Most transformation apps create a static image you share once and forget. Zerocap's transformation creates a **living companion** that persists:

- **Lensa problem:** Generate avatars, share them, never open the app again. Revenue dropped from $39M (2022) to $18M (2023).
- **Zerocap solution:** The transformation creates something you keep. The pet has personality, it grows, you interact with it. The initial share drives acquisition, but the ongoing relationship drives retention.

This means Zerocap can generate Lensa-level viral moments while avoiding Lensa's cliff. The transformation is the top of the funnel; the pet relationship is the bottom.

---

## 3. Case Studies

### Lensa AI -- The $50M Viral Explosion

**What happened:** Lensa launched in 2018 as an ordinary photo editor. In November 2022, they shipped "Magic Avatars" -- upload 10-20 selfies, pay $3.99-$7.99, get 50 AI-generated artistic portraits. On November 26, tech YouTuber MKBHD (17M subscribers) shared his avatars. Within days, downloads spiked 631%.

**The numbers:**
- October 2022: 219K downloads
- November 2022: 1.6M downloads
- December 2022: 19.3M downloads, $30.75M revenue
- Peak: $8M/day in revenue
- #lensa on TikTok: 434.2M views (entirely organic)

**Why it worked:**
- Every share was also a paid customer (the viral content required buying the feature)
- The outputs were flattering -- people shared because the AI made them look like fantasy heroes and fine art subjects
- Multiple art styles meant users shared several images, multiplying touchpoints
- FOMO was extreme -- seeing friends' avatars created urgency to try it immediately

**Why it crashed:** Zero retention mechanic. One-shot generation, no reason to return. Revenue fell to $1.09M/month by April 2023.

**Zerocap lesson:** The initial transformation drives acquisition. The living pet with personality drives retention. Zerocap can capture the Lensa-style viral moment AND keep users.

Sources:
- [Startup Spells -- How Lensa Generated $50M+](https://startupspells.com/p/lensa-ai-avatars-riding-ai-wave)
- [TechCrunch -- Lensa AI Climbs App Store Charts](https://techcrunch.com/2022/12/01/lensa-ai-climbs-the-app-store-charts-as-its-magic-avatars-go-viral/)
- [Business of Apps -- Lensa AI Statistics](https://www.businessofapps.com/data/lensa-ai-statistics/)

---

### FaceApp -- The Challenge Mechanic

**What happened:** FaceApp launched in 2017 but went mega-viral in July 2019 through the #FaceAppChallenge -- users applied the aging filter to selfies and shared them on Instagram and Twitter.

**The numbers:**
- Climbed from #1,370 to #1 on the US App Store in 5 days
- 30 million worldwide downloads in July 2019

**Why it worked:**
- **The "challenge" format.** By framing the transformation as a challenge (#FaceAppChallenge), sharing became a social obligation. You weren't just using an app -- you were participating in a cultural moment.
- **Watermarking strategy.** Every FaceApp output carried a subtle watermark. This turned every shared image into a branded advertisement, ensuring viewers knew exactly which app to download.
- **Celebrity adoption.** Justin Bieber, Will Smith, David Guetta, and the Jonas Brothers all participated, giving the trend legitimacy and massive reach.
- **Universal curiosity.** "What will I look like old?" is a question everyone has. The appeal was not niche -- it crossed demographics, genders, and age groups.

**Zerocap lesson:** The challenge/trend format is a multiplier. "Turn your [specific object] into a pet" can become a challenge: "Turn your shoe into a pet," "Turn your breakfast into a pet." Each variant is a new trend, each trend is a new viral cycle. And subtle watermarking on every shared pet image is free advertising.

Sources:
- [Glorify -- FaceApp Virality: Influencer Marketing Strategy Done Right](https://glorify.com/learn/faceapp-marketing-growth-strategy)
- [Gulf News -- Viral FaceApp Challenge](https://gulfnews.com/lifestyle/community/viral-faceapp-challenge-your-face-just-60-years-later-celebrities-jump-in-on-the-trend-1.1563094246736)
- [DXB Apps -- What is FaceApp](https://dxbapps.com/blog/faceapp)

---

### BeReal -- Constraint-Driven Sharing

**What happened:** BeReal took a fundamentally different approach to virality -- instead of making content shareable, it made content creation itself a social ritual. A random daily notification gives users 2 minutes to take and share an unfiltered photo.

**The numbers:**
- iPhone App of the Year 2022
- Content shared 2.5x more than comparable posts elsewhere (despite no native sharing tools)
- Growth driven by college ambassador program in US/UK

**Why it worked:**
- **The constraint IS the mechanic.** The 2-minute window creates urgency, FOMO, and a shared ritual. You don't share BeReal content -- you share the *behavior* of using BeReal. "Did you BeReal yet?" became social currency.
- **Anti-algorithm positioning.** By rejecting likes, follower counts, and algorithmic feeds, BeReal made authenticity itself the viral hook. People talked about the concept, not just the content.
- **Word-of-mouth over share buttons.** BeReal's content doesn't have native sharing tools, so users screenshot and share in DMs and group chats. This paradoxically increased sharing because it felt organic, not engineered.

**Zerocap lesson:** Constraints breed creativity and conversation. A "daily object" feature (scan today's object, streak mechanic) could create BeReal-like ritual sharing. Also: content that spreads through DMs and group chats is more trusted and converts better than public posts.

Sources:
- [Contrary Research -- BeReal Business Breakdown](https://research.contrary.com/company/bereal)
- [TheBigMarketing -- BeReal Marketing Strategy](https://thebigmarketing.com/bereal-marketing-strategy/)
- [Minty Digital -- The Rise and Fall of BeReal](https://www.mintydigital.com/blog/the-rise-and-fall-of-bereal/)

---

### Pokemon GO -- AR-Powered IRL Virality

**What happened:** Pokemon GO launched in July 2016 and became the fastest mobile game to reach $1B in revenue. The AR camera feature -- placing Pokemon in real-world settings through the phone screen -- was the key viral mechanic.

**The numbers:**
- 500M+ downloads in first year
- $1B revenue in 7 months
- Fastest app to reach 50M downloads

**Why it worked:**
- **The AR camera turned every player into a content creator.** Screenshots of Pokemon appearing in real-world locations (on your desk, in front of landmarks, photobombing strangers) were inherently funny and shareable.
- **Physical-world visibility.** The game required walking outside, creating visible crowds of players in parks and public spaces. Seeing dozens of people playing the same game in a park is the ultimate social proof -- no ad can replicate it.
- **Existing IP leverage.** Pokemon is universally recognized. The nostalgia alone drove initial downloads; the product kept people sharing.
- **Community events (raids, community days)** turned solo play into social experiences, creating IRL sharing moments that photos couldn't capture.

**Zerocap lesson:** The camera feature IS the sharing moment. When someone points their phone at an object and a pet appears, anyone watching in person asks "What's that app?" This IRL virality is distinct from social media sharing and potentially more powerful because it comes with immediate social proof (seeing someone you know use it).

Sources:
- [The Conversation -- What's Made Pokemon GO Such a Viral Success](https://theconversation.com/whats-made-poke-mon-go-such-a-viral-success-62420)
- [Medium (Whamsicore) -- Why Pokemon Go Went Viral](https://medium.com/@whamsicore/why-pokemon-go-went-viral-and-why-it-may-evolve-into-a-classic-3ded3ea3d153)
- [Bloomidea -- Pokemon Go: 6 Success Factors](https://bloomidea.com/en/blog/pokemon-go-6-success-factors-of-the-app-that-caught-the-world)

---

### EPIK (AI Yearbook) -- The Nostalgia Trigger

**What happened:** EPIK launched an AI Yearbook feature in late 2023 that transformed selfies into 90s-style school yearbook photos. The trend exploded on TikTok and Instagram.

**The numbers:**
- Downloads increased 30x after the AI Yearbook feature launched
- 92.3M lifetime downloads
- $7M in consumer spending on iOS
- Hit #1 trending free app on the App Store

**Why it worked:**
- **Nostalgia is a universal hook.** 90s yearbook photos tap into collective cultural memory -- even Gen Z (who didn't live through it) romanticizes the aesthetic. 68% of Gen Z say nostalgia makes them feel more positively about a brand.
- **Celebrity acceleration.** Keke Palmer, Guy Fieri, Bretman Rock, James Charles, and Pokimane all tried it, each creating a cascade of downloads from their audiences.
- **The output was identity-first.** People shared because the yearbook version of themselves was entertaining and flattering. It was self-expression disguised as a trend.

**Zerocap lesson:** Nostalgia is a force multiplier. "AI Tamagotchi" positioning already taps this. The yearbook trend proves that when you combine AI transformation with a nostalgic frame, the shareability compounds.

Sources:
- [TechCrunch -- AI App EPIK Hits No. 1](https://techcrunch.com/2023/10/06/ai-app-epik-hits-no-1-on-the-app-store-for-its-viral-yearbook-photo-feature/)
- [CNBC -- People Are Posting AI-Generated Yearbook Pictures](https://www.cnbc.com/2023/10/05/how-to-create-ai-yearbook-pictures-with-viral-epik-app.html)
- [Product Hunt -- How to Create the AI Yearbook Trend](https://www.producthunt.com/stories/how-to-do-ai-yearbook-trend-free-high-school-epik-app)

---

### Dawn AI -- The Fast Follower

**What happened:** Dawn AI was one of several apps that rode the AI avatar wave after Lensa's success, but it achieved notable scale through broad platform support and ease of use.

**The numbers:**
- 8.1M downloads across platforms
- 5M+ on Google Play alone
- 6M+ active users

**Why it worked:**
- **Multi-platform sharing.** Dawn AI supports sharing to Instagram, TikTok, Snapchat, Telegram, WhatsApp, and more. Reducing friction to share on the user's platform of choice increased share rate.
- **Prompt-based creativity.** Users could type descriptions of what they wanted, putting creative control in their hands. This meant outputs were unpredictable and entertaining -- worthy of sharing.
- **Timing.** Dawn AI launched when "AI avatar" was already a known concept, reducing the explanation burden. Users already knew what to expect and were looking for the next app to try.

**Zerocap lesson:** Support every sharing platform. Don't force users into one channel. And timing matters -- being in market when the cultural conversation is about AI + pets/cute content is a strategic advantage.

Sources:
- [Dawn AI - App Store](https://apps.apple.com/us/app/dawn-ai-avatar-generator/id1643890882)
- [Speechify -- Dawn AI](https://speechify.com/blog/dawn-ai-avatar-generator/)

---

## 4. K-Factor Benchmarks

K-factor (viral coefficient) measures how many new users each existing user generates through sharing. The formula: **K = invitations per user x conversion rate per invitation.**

### Industry Benchmarks

| Category | K-Factor Range | Notes |
|----------|---------------|-------|
| Social networks (peak) | 5-8+ | Facebook ~7, but this includes network effects, not just sharing |
| Communication tools (peak) | 8+ | Slack ~8.5 (inherent virality -- you need others to use it) |
| Mobile games | 0.4-0.92 | Jelly Splash achieved 0.92. Most games 0.3-0.5 |
| Photo/transformation apps (peak) | 0.8-1.5+ | Lensa/Prisma during viral peaks likely exceeded 1.0 |
| E-commerce apps | 0.2-0.5 | 38.6% of e-commerce apps show measurable K-factor |
| B2B SaaS | 0.05-0.73 | Echosign 0.2, Ladder 0.73 (exceptional) |
| Consumer internet (good) | 0.15-0.25 | Sustainable baseline |
| Consumer internet (great) | ~0.4 | Strong organic growth contribution |
| Consumer internet (outstanding) | ~0.7 | Rare; significantly reduces CAC |

### Key Findings

- **Only 30% of mobile apps exhibit measurable K-factor.** The majority have zero viral mechanics.
- **Median K-factor among apps that have one: 0.45.** This means the average viral app generates roughly one new user for every two existing users.
- **K > 1 is extraordinarily rare and almost never sustained.** Even Lensa's K-factor during its December 2022 peak was temporary. True exponential viral growth happens in bursts, not steady states.
- **Even K = 0.2 is valuable.** At K = 0.2, for every 5 users acquired through paid channels, you get 1 additional user for free. Over time, this 20% bonus compounds significantly.
- **Cycle time matters as much as K-factor.** A K of 0.5 with a 1-day cycle time generates more users than K of 0.8 with a 7-day cycle time over a month.

### Zerocap's K-Factor Estimate

From the existing growth strategy analysis:

```
Share rate:        50% create a pet x 20% share = 10% effective share rate
Reach per share:   ~200 views (conservative TikTok/Instagram)
Download rate:     5% of viewers download
K = 0.10 x 200 x 0.05 = 1.0
```

This is optimistic for a steady state but realistic during peak moments. The levers to pull:

| Lever | Current Estimate | Improvement Target | Impact |
|-------|-----------------|-------------------|--------|
| Share rate | 20% of creators share | 40% (better share UX, prompts) | 2x K |
| Reach per share | 200 views | 500 views (better share artifacts) | 2.5x K |
| Download conversion | 5% | 8% (better deep links, App Store page) | 1.6x K |
| Cycle time | ~3 days | ~1 day (instant share flow) | 3x velocity |

**Target: sustained K of 0.4-0.7 with burst periods approaching 1.0+ during trends/challenges.**

Sources:
- [Saxifrage -- K-Factor Benchmarks](https://www.saxifrage.xyz/post/k-factor-benchmarks)
- [Visible.vc -- K Factor: What is Your SaaS Company's Viral Coefficient](https://visible.vc/blog/k-factor-what-is-your-saas-companys-viral-coefficient/)
- [MetricHQ -- Viral Coefficient](https://www.metrichq.org/marketing/viral-coefficient/)

---

## 5. Designing the Share Artifact

The "share artifact" is the specific piece of content that gets shared -- the thing that crosses from the app into a social feed and acts as an advertisement. Its design is the single highest-leverage decision in the entire viral loop.

### What Gets Shared: Format Hierarchy

**1. Short video (15-30 seconds) -- highest virality ceiling.**
- Works best on TikTok, Instagram Reels, YouTube Shorts
- Can show the full transformation moment (object -> pet) with dramatic reveal
- Native to how people consume content in 2026
- Has sound, motion, surprise -- all algorithmic signals for promotion
- Downsides: harder to create automatically, higher file size, some friction to share

**2. Side-by-side image -- highest share rate.**
- Works everywhere: iMessage, Instagram Stories, WhatsApp, Twitter/X
- Instantly communicates the before/after without any context needed
- Easy to screenshot, save, forward
- Can include app branding/watermark without feeling intrusive
- Downsides: lower algorithmic reach than video, static

**3. Animated GIF/short clip (3-5 seconds) -- best for messaging.**
- Perfect for iMessage and WhatsApp where full videos feel heavy
- Shows the transformation moment in a loop
- Lightweight, plays automatically in most messaging apps
- Downsides: quality limitations, no sound

**4. Link with rich preview -- lowest friction, lowest virality.**
- Generates an Open Graph preview card when pasted into messages/social
- Requires the recipient to click through to see the content
- Lowest share friction (just paste a URL) but highest viewing friction (requires a click)
- Useful as a complement, not the primary artifact

### Design Principles for the Share Artifact

**The artifact must tell the story by itself.** A viewer who has never heard of Zerocap should understand what happened from the shared content alone: "Someone pointed their camera at a shoe and it became a cute pet creature." No explanation needed.

**Brand the output, don't brand the share.** A subtle "Made with Zerocap" watermark or a small logo in the corner works. A giant banner saying "DOWNLOAD ZEROCAP" does not. FaceApp's watermark strategy is the model -- visible enough to identify, subtle enough to not ruin the content.

**Make the output the user's creation, not the app's ad.** The user should feel like they're sharing THEIR pet, not advertising an app. The emotional frame matters: "Look at this cute thing!" vs. "Check out this app!" The former drives shares; the latter kills them.

**Design for the thumbnail.** On TikTok and Instagram, content is chosen by its first frame/thumbnail. The before/after split image has instant visual clarity even at tiny sizes. Design the share artifact so the two states (object vs. pet) are immediately distinguishable in a 1-inch square.

**Include a call to action in the content, not around it.** Rather than a "Download now" button (which social platforms strip), embed curiosity into the content itself. A caption like "She started as a water bottle" or text overlay "what would YOUR objects turn into?" drives the viewer to seek out the app.

### Recommended Share Artifact Stack for Zerocap

| Context | Artifact | Format |
|---------|----------|--------|
| TikTok/Reels/Shorts posting | 15-second video showing real-time transformation with reveal sound effect | MP4, 9:16 aspect ratio |
| Instagram Stories | Split-screen image: real object on left, AI pet on right, with pet name + personality traits | PNG, 9:16, with interactive sticker ("What would yours look like?") |
| iMessage / WhatsApp / DMs | Animated 3-second GIF of the transformation moment looping | GIF or short MP4, auto-play |
| Twitter/X | Side-by-side image with personality trait card | PNG, 16:9, with "Made with Zerocap" watermark |
| In-person / IRL | Deep link QR code on the pet card that opens directly to App Store | Link or QR |

### The "Pet Card" Concept

One powerful artifact design: a collectible-looking **pet card** -- similar to a Pokemon/trading card -- that shows:
- The pet's image (cute, high-quality rendering)
- The pet's name
- 2-3 personality traits ("Introverted jazz lover who's afraid of thunder")
- The original object it came from (small image or label)
- Subtle Zerocap branding

This format is inherently collectible, shareable, and screenshot-worthy. It borrows from the Madden/FIFA player rating card format that Umax used to go viral -- instantly recognizable visual language designed for social sharing.

Sources:
- [Placid -- Design Your Apps for Viral Growth with Social Sharing](https://placid.app/blog/design-your-apps-for-viral-growth-with-social-sharing)
- [Superwall -- Part 2: How to Design a Viral App in 2025](https://superwall.com/blog/part-2-how-to-design-a-viral-app-in-2025/)
- [Smashing Magazine -- Key Ingredients to Make Your App Go Viral](https://www.smashingmagazine.com/2013/08/key-ingredients-to-make-your-app-go-viral/)

---

## 6. Platform-Specific Sharing Mechanics

Each platform has different technical capabilities, user expectations, and content norms. The share flow should adapt to each.

### iMessage (Highest Trust, Highest Conversion)

**Why it matters:** iMessage is where close friends share content. A friend sending "look what this app did to my shoe" in an iMessage carries more weight than any TikTok post. Conversion rates from personal messages are dramatically higher than from feed content.

**Technical approach:**
- Use iOS Share Sheet to enable one-tap sharing to iMessage
- Share a rich link (Universal Link) with Open Graph preview showing the pet image
- The link should deep-link to the App Store if the recipient doesn't have Zerocap, or into the app if they do
- Animated GIF attachments auto-play in iMessage threads -- use the transformation loop
- Consider an iMessage App Extension that lets users send their pet collection directly in the conversation

**Design considerations:**
- Keep file sizes small (iMessage compresses aggressively)
- The preview image in the link must be compelling at small size
- Include a brief text overlay: "My water bottle became this" -- context for the recipient

### Instagram Stories (Broadest Reach Among Friends)

**Why it matters:** Stories reach a user's entire follower base with ephemeral urgency. The "swipe up" / link sticker mechanic enables direct-to-App-Store funneling.

**Technical approach:**
- Use Instagram's Custom URL Scheme (`instagram-stories://share`) to pre-populate a Story with the Zerocap content
- Provide a background image (the side-by-side transformation) via the `com.instagram.sharedSticker.backgroundImage` pasteboard key
- Add a sticker overlay (the pet card) via `com.instagram.sharedSticker.stickerImage` (must be PNG, under 1MB)
- Include the App Store link so users can add a link sticker
- MUST provide an app ID in the Instagram URL or the content won't open

**Design considerations:**
- Design for 9:16 full-screen format
- Use Instagram's native interactive features: poll sticker ("Which pet is cuter?"), question sticker ("What should I scan next?"), quiz sticker
- The sticker (pet card) should have a transparent background so it looks native to Instagram

### TikTok (Discovery Engine)

**Why it matters:** TikTok is where strangers discover content. A single viral TikTok post from a user can drive tens of thousands of downloads.

**Technical approach:**
- Generate a video file (MP4, 9:16) that users can upload directly to TikTok
- Include a "Post to TikTok" button that opens the TikTok app with the video pre-loaded
- Alternatively, use TikTok's Share SDK to post directly from the app
- Add trending-sound-friendly structure: the video should have a natural pause/beat where users can overlay trending audio
- Include on-screen text (Zerocap should render it) so the video works with or without sound

**Design considerations:**
- The first frame must be a hook -- show the mundane object, create anticipation
- The reveal should happen at 3-5 seconds (after the hook, before attention drops)
- End with the pet card or personality traits for a satisfying conclusion
- Subtle watermark: "Zerocap" text in corner, visible but not intrusive
- **Do NOT include a TikTok-style watermark from Zerocap** -- TikTok deprioritizes content with other platforms' watermarks, and the same applies in reverse

### Snapchat (Younger Audience)

**Why it matters:** Snapchat's camera-first interface mirrors Zerocap's interaction model. The audience skews young and engages heavily with AR/camera experiences.

**Technical approach:**
- Use Snapchat's Creative Kit (Snap Kit SDK) to share content
- Create Snapchat Lenses / AR filters: a Zerocap lens that lets users see a pet version of objects through Snapchat's camera
- Share as a photo snap with a sticker (pet card) overlay
- Only one sticker per snap allowed; PNG under 1MB or animated WebP under 1MB

**Design considerations:**
- Snapchat users expect ephemeral, playful content
- The pet card sticker should be draggable/resizable
- Snapchat's audience responds well to AR experiences -- a Zerocap lens could be a standalone viral mechanic

### Twitter/X (Conversation Starter)

**Why it matters:** Twitter drives conversation. A well-designed tweet with a pet transformation image can spark threads, quote tweets, and trend.

**Technical approach:**
- Share a 16:9 or 4:3 image (Twitter crops differently than other platforms)
- Include a thread-friendly caption: the object origin story, the pet's personality, a question to the audience
- Link to the App Store in a follow-up reply (not the main tweet, which suppresses reach)

**Design considerations:**
- Twitter compresses images aggressively -- use high-contrast designs
- The pet card format works well here because it's information-dense and screenshotable
- GIFs auto-play in Twitter feed -- the transformation animation is effective here

Sources:
- [Ishan Chhabra -- Sharing to Instagram Stories: A Definitive Guide](https://www.ishanchhabra.com/thoughts/sharing-to-instagram-stories)
- [Medium (Daniel Crompton) -- Share Content to an Instagram Story from an iOS App](https://medium.com/@danielcrompton5/share-content-to-an-instagram-story-from-an-ios-app-d55b1e10e68a)
- [Branch -- Branch Links in Snapchat Stories iOS](https://help.branch.io/faq/docs/branch-links-in-snapchat-stories-ios)

---

## 7. Referral Program Design

### What Works for Consumer Apps

The best referral programs share four traits: clear incentives, simple sharing mechanics, strong product alignment, and double-sided rewards.

**Key statistics:**
- Double-sided rewards increase sharing rates by 41%
- $10-$20 is the most effective referral reward range (higher amounts above $50 don't increase referrals significantly)
- Tiered referral programs generate 27% more referrals
- Mobile-first referral pages increase shares by 30%
- One-click sharing increases referrals by 26%
- 75% of customers prefer sharing referral codes via messaging apps
- Reminder prompts increase referral completion rates by 47%
- Gamified rewards boost participation by 34%

### Referral Program Design for Zerocap

The reward must be **aligned with the product's core value.** Dropbox's extra storage is the canonical example -- the reward makes the product more useful, not just more affordable. For Zerocap, the rewards should unlock more product, not give discounts.

**Recommended reward structure:**

| Action | Referrer Gets | Invitee Gets |
|--------|--------------|--------------|
| Friend installs app | 1 exclusive pet style/evolution | 1 bonus pet slot |
| Friend creates first pet | 1 rare personality trait unlock | Starter bonus (extra scan) |
| 3 friends install | Exclusive "collector" pet only available through referrals | -- |
| 5 friends install | Legendary pet evolution path | -- |
| 10 friends install | "OG Collector" badge + exclusive pet family | -- |

**Why this works:**
- Rewards are **product-native** -- exclusive pets, styles, and evolutions that enhance the collection
- They create **scarcity** -- "you can ONLY get this pet through referrals" drives sharing motivation
- They're **visible** to other users -- when someone sees a rare pet in your collection, they ask how you got it, creating a secondary viral loop
- The tiered structure creates a **progression mechanic** that keeps referral motivation alive after the first share

### Implementation Details

**Referral codes vs. links:** Links with embedded codes (e.g., `zerocap.app/join/david123`) create less friction than asking someone to remember and type a code. The link should:
- Open the App Store directly if the app isn't installed (via Universal Links / Smart App Banners)
- Deep-link into the app with the referral credit if already installed
- Show a rich preview card (pet image + "David invited you") when pasted in messages

**Timing of the referral prompt:** Never on first launch. The optimal moment is immediately after the first pet creation -- when delight is highest. The prompt should feel like an extension of the experience, not an interruption:

> "Your pet is alive! Want to share it with a friend? They'll get a bonus pet too."

**Avoid the "gate" pattern:** Never make referrals mandatory to access core features. The moment sharing feels forced, users resent it. Referral rewards should be bonuses, not unlocks of things that feel like they should be free.

Sources:
- [Extole -- The 33 Best Referral Program Examples of 2025](https://www.extole.com/blog/the-33-best-referral-program-examples-of-2025-in-every-industry/)
- [Impact.com -- Referral Program Guide 2025](https://impact.com/referral/7-proven-strategies-for-growth/)
- [Tapp -- 15+ Mobile App Referral Program Examples](https://www.tapp.so/blog/mobile-app-referral-program-examples/)
- [Referral Rock -- How Referral Codes Work](https://referralrock.com/blog/referral-code-example/)

---

## 8. Social Proof Mechanics

Social proof is the psychological phenomenon where people copy the actions of others. In app growth, it means showing users what their friends and peers are creating.

### Why Social Proof Drives Downloads

- 4.6x higher purchase intent for products recommended by friends vs. advertising
- Strava users who see friends' activities have 78% higher retention than solo users
- Apps with social proof mechanics achieve 70% higher conversion rates
- 40-60% reduction in acquisition costs through referral-driven growth

### Social Proof Mechanics for Zerocap

**1. "Friends' Pets" Feed.**
Show what friends (connected via contacts or social accounts) have created. Seeing that your friend turned their dog's bowl into a cute pet creates FOMO and curiosity that drives engagement. This is the Strava model applied to pet creation.

**2. "Popular Transformations" Discovery.**
A feed of the most-liked or most-shared transformations globally. This serves two purposes: it shows new users what's possible (inspiration) and it creates aspiration (I want MY transformation to be on this feed).

**3. Notification Triggers.**
- "3 of your friends created pets this week" -- creates FOMO
- "Sarah's pet just evolved!" -- drives engagement through competitive/social impulse
- "Your pet was liked by 12 people" -- validates sharing behavior

**4. Visible Collection Size.**
Show how many pets a user has collected on their profile. When someone sees a friend with 20+ pets and they only have 3, the gap motivates engagement. This is the same mechanic that drives sneaker collecting, Pokemon card trading, and achievement hunting.

**5. "Created With" Attribution.**
When a user shares a pet, include "Created by @username with Zerocap" in the metadata. This makes the creator feel proud (social validation) and signals to viewers that real people -- people they know -- use this app.

### The Activity Feed Model

Sequoia's research on activity feeds identifies a critical loop: **users produce content that others consume, and feedback from consumers (likes, comments, reactions) motivates producers to create more.** For Zerocap:

```
[User creates pet] -> [Pet appears in friends' feeds] -> [Friends react/like] -> [Creator gets validation] -> [Creator makes more pets and shares more]
```

This production-consumption loop is the engine that turns a one-time transformation into an ongoing engagement habit.

Sources:
- [Sequoia -- Engagement Part I: Introduction to Activity Feeds](https://articles.sequoiacap.com/engagement-part-i-introduction-to-activity-feeds)
- [Rajiv Gopinath -- The Role of Social Proof in Consumer Behavior](https://www.rajivgopinath.com/blogs/marketing-hub/the-role-of-social-proof-in-consumer-behavior)
- [StriveCloud -- 10 Ways to Drive Engagement with Gamification](https://www.strivecloud.io/blog/10-ways-to-drive-engagement)

---

## 9. UGC as Distribution

User-generated content is the most cost-effective distribution channel for consumer apps. When users create content about your product, they become unpaid marketers with an audience that trusts them far more than any brand account.

### Why UGC Outperforms Brand Content

- UGC ads on TikTok are 22% more effective than brand-created videos
- UGC outperforms Facebook ads by 32% and regular ads by 46%
- 79% of people say UGC highly impacts their purchasing decisions
- UGC content has a 28% higher engagement rate than brand content

### The UGC Flywheel

```
[Product creates shareable output]
    -> [Users post it on social media]
        -> [Content performs well (authentic, novel)]
            -> [More people see it and download the app]
                -> [New users create their own content]
                    -> [Cycle accelerates]
```

The flywheel spins fastest when:

1. **The product output IS the content.** Users don't need to add anything -- the pet transformation is already interesting enough to post. Zerocap has this naturally.

2. **Creation has high variance.** Every user's output is different (different objects, different pets, different personality traits), so there's always something new to see. Nobody's feed gets saturated with identical content.

3. **The format is platform-native.** If the share artifact looks like organic TikTok/Instagram content rather than an app ad, the algorithm treats it as real content and promotes it.

4. **The app makes creation of UGC effortless.** One tap to share, pre-formatted for each platform, no editing required. Every additional step reduces the share rate.

### Making Zerocap Outputs UGC-Ready

**The transformation video should be editable.** Let users add their own text, choose music, adjust timing. This gives creators ownership over the content, making them more likely to post it and feel proud of it.

**Support "reaction" formats.** Design a split-screen mode where the user's face reaction is recorded alongside the transformation. Reaction videos are TikTok's most-shared format and they add the human element that makes content relatable.

**Enable compilation creation.** A "My Pet Collection" video that auto-generates a slideshow of all pets a user has created is inherently satisfying content. The more pets someone has, the more impressive the compilation.

**Make pets react to each other.** If two users' pets can interact (play, compete, etc.), this creates collaborative UGC opportunities. "My coffee mug pet met my friend's shoe pet and they became best friends" is content that writes itself.

Sources:
- [Adjust -- UGC Marketing for Mobile Apps](https://www.adjust.com/blog/user-generated-content-guide/)
- [Stormy AI -- The UGC Marketing Playbook](https://stormy.ai/blog/ugc-marketing-playbook-scale-mobile-app)
- [Hootsuite -- Complete Guide to User-Generated Content in 2025](https://blog.hootsuite.com/user-generated-content-ugc/)

---

## 10. TikTok-Native Virality

TikTok is the primary discovery engine for consumer apps in 2026. Understanding what makes people record and share their screen unprompted is critical.

### What Makes People Share Unprompted

People don't share apps -- they share **moments**. The moment has to be:

1. **Surprising.** The transformation from a mundane object to a cute pet is inherently surprising. The bigger the gap between input and output, the more shareable.

2. **Simple to explain visually.** "I pointed my camera at X and got Y" can be communicated in under 3 seconds without any words. TikTok's algorithm rewards content that hooks in the first frame.

3. **Repeatable with variation.** The appeal isn't just seeing ONE transformation -- it's wondering "What would MY stuff turn into?" Each viewer can imagine their own version, which drives downloads.

4. **Personality-driven.** The unique personality traits (6M combinations) add a "results" element similar to personality quizzes. "My water bottle is an introverted jazz lover" is inherently funny and shareable because it's absurd and personal.

### TikTok Content Patterns That Drive App Downloads

**The "Wait for it" reveal.** Show the boring object. Build anticipation ("I can't believe what this turned into"). Reveal the pet. The delayed gratification structure aligns with TikTok's algorithmic preference for high completion rates.

**The challenge/series format.** "Turning everything in my kitchen into pets, Day 1." Series content builds audiences and creates habitual viewers. Each episode is a new viral opportunity.

**The "did you hear about this?" format.** Conversational, speaking-to-camera style. "Okay so there's this app where you point your camera at literally ANYTHING and it becomes a cute little pet with its own personality and I can't stop." This works because it mimics how people naturally recommend things to friends.

**The comparison format.** "What I expected vs. what I got" or "My pet collection vs. my friend's." Comparison creates narrative tension and entertainment value.

**The screen recording.** The raw, unedited screen recording of someone using the app -- showing the real-time transformation -- is the most authentic and often most viral format. No editing needed. The product IS the content.

### Designing for TikTok's Algorithm

- **Completion rate is the #1 signal.** Keep share videos under 30 seconds. The higher the percentage of viewers who watch to the end, the more TikTok promotes the content.
- **Rewatch value.** Content people watch twice gets exponentially more reach. The cute pet reveal has natural rewatch value -- "wait, let me see that again."
- **Comment bait.** Content that provokes comments (predictions, debates, requests) gets algorithmic boost. "What should I scan next?" drives comments.
- **Save rate.** Content people save to watch later or show friends is highly valued by the algorithm. A particularly cute or funny transformation is save-worthy.

### The "Viral on Demand" Framework

Blake Anderson (creator of Umax, RizzGPT, Cal AI) describes a method: study content that goes viral in your app's niche, then design the app's screens and outputs to look like that content. Umax's results screen was inspired by Madden/FIFA player rating cards -- a visual format already proven to go viral.

For Zerocap, this means the pet card/results screen should borrow from proven viral visual formats:
- Trading card aesthetic (Pokemon, sports cards)
- Character stat screens (RPG games, Dungeons & Dragons character sheets)
- "Your results" quiz format (personality quizzes, BuzzFeed-style)

The app's UI becomes the content. Users screenshot the results screen and share it as-is.

Sources:
- [Superwall -- Part 2: How to Design a Viral App in 2025](https://superwall.com/blog/part-2-how-to-design-a-viral-app-in-2025/)
- [Superwall -- How Stronger Built a $600K App Using Viral on Demand TikTok Strategy](https://superwall.com/blog/how-stronger-built-a-usd600k-app-using-viral-on-demand-tiktok-strategy)
- [Superscale -- TikTok UGC Strategy: How Apps Go Viral](https://superscale.ai/learn/tiktok-ugc-strategy-how-to-go-viral-for-your-app-in-2025/)

---

## 11. "Scan This" IRL Virality

Camera-based apps have a unique viral channel that purely digital apps don't: **in-person moments.** When someone pulls out their phone, points it at an object, and something magical happens on their screen, everyone nearby asks "What's that?"

### How IRL Moments Create Organic Sharing

**The curiosity gap.** When you see someone pointing their phone at a shoe and then they laugh or gasp at their screen, you HAVE to know what happened. This in-person curiosity is impossible to ignore and creates an immediate "show me" moment.

**The demonstration effect.** Unlike social media sharing (which requires the viewer to download and try it themselves), IRL sharing includes a live demo. You see the transformation happen in real time, on a device right in front of you, with the app already open. The friction to "try it yourself" is nearly zero -- the person just hands you their phone.

**The group multiplier.** One person using Zerocap at a dinner table creates a moment for everyone present. Each person wants to scan their own object. If 5 people are at a table and 1 uses Zerocap, all 5 see it, and 2-3 download it on the spot. This is how Pokemon GO spread in its first weeks -- visible public usage created cascading adoption.

### Engineering IRL Virality

**Design for spectators.** The transformation animation should be visible and dramatic enough that someone glancing at your screen from across a table can tell something interesting is happening. Bold colors, satisfying animations, clear before/after states.

**Sound design matters.** A distinctive, delightful sound when the pet appears creates an auditory cue. People hear the sound, look up, and ask what just happened. Pokemon GO's catch sound and Shazam's listening animation serve the same function.

**"Scan together" mode.** A feature where two people scan the same object and get different pets creates a shared experience and a conversation starter: "We both scanned the same lamp but got totally different pets!" This doubles the viral touchpoint per object.

**QR code sharing for collections.** Each user's pet collection could generate a QR code that others can scan to view it. This creates a physical-world sharing mechanic: put the QR code on a sticker, a phone case, a school notebook. AR-triggered QR experiences get scanned, played with, and shared -- building engagement that sticks.

**NFC/AirDrop pet trading.** Allowing users to "trade" or "show" pets via AirDrop or proximity-based mechanics turns any gathering into a Zerocap social moment. This is how the original Tamagotchi connection worked (infrared sharing between devices) and it was the #1 driver of schoolyard adoption.

### Real-World Precedents

| App | IRL Mechanic | Effect |
|-----|-------------|--------|
| Pokemon GO | Visible crowds in parks playing the game | Bystanders downloaded immediately; "What are they all doing?" |
| Shazam | Holding phone up to identify a song | Everyone at the table wanted to try it |
| Snapchat | Camera-first interface, group selfies | "Get on Snapchat" became a social norm |
| QR-based event apps (POV, Lense) | Scan to join shared photo album | Frictionless group participation |
| Original Tamagotchi | Infrared connection between devices | Schoolyard trading and showing off |

Sources:
- [Bloomidea -- Pokemon Go: 6 Success Factors](https://bloomidea.com/en/blog/pokemon-go-6-success-factors-of-the-app-that-caught-the-world)
- [QR Code Kit -- QR Codes for AR](https://qrcodekit.com/news/qr-codes-for-ar/)
- [Substack (Akshay Pruthi) -- The Tamagotchi Effect](https://pruthiakshay.substack.com/p/the-tamagotchi-effect-how-a-90s-toy)

---

## 12. Anti-Patterns

### What Doesn't Work

**1. Forced contact access before value delivery.**
Apps that request address book access before the user has experienced any value (e.g., TBH requiring contacts before the app was usable). This creates immediate distrust and drives uninstalls. The rule: deliver value first, ask for sharing permissions after the user is delighted.

**2. Spam invitations on behalf of the user.**
Sending messages to a user's contacts without explicit, granular consent. Facebook's People You May Know controversy (ingesting contact lists of millions of users) is the cautionary tale. Even if it works short-term, the trust damage is permanent.

**3. Mandatory sharing to unlock core features.**
"Share with 3 friends to continue" is a dark pattern that generates resentment, not genuine referrals. Users who are forced to share will use workarounds (share and immediately delete) or leave the app entirely. Sharing should unlock BONUS features, never core ones.

**4. Generic share prompts.**
"Share this app with a friend!" on a random screen with no context. This has near-zero conversion because there's no emotional motivation. The prompt must come at a moment of delight and be specific to what just happened.

**5. Overly branded share content.**
If the shared content looks like an advertisement (giant logo, "DOWNLOAD NOW" CTA, corporate copy), it will be ignored or actively avoided. People don't want to look like they're advertising for a brand. The content must feel like the user's creation with subtle branding.

**6. Ignoring platform norms.**
Sharing a vertical video to Twitter (where horizontal works better), or a static image to TikTok (where video is expected), or a long video to iMessage (where lightweight content is preferred). Each platform has its own norms, and violating them reduces engagement.

**7. No deep linking.**
Sharing a generic App Store link means the new user lands on the store page with no context about what their friend created. A deep link that shows the specific pet their friend made, THEN offers to download, converts dramatically better.

**8. Interrupting the creation flow.**
Showing a "Share now?" prompt before the user has finished admiring their pet. Let the user have their moment. Let them name the pet, read the personality traits, tap around the interface. THEN offer to share when they've had time to fall in love with what they made.

**9. One-size-fits-all share mechanics.**
A single "Share" button that dumps a link is leaving value on the table. Different platforms need different artifacts (video for TikTok, image for Instagram Stories, GIF for iMessage). The share flow should auto-detect the destination and adapt.

**10. Measuring shares instead of conversions.**
A high share count with low download conversion means the share artifact is broken -- either the content doesn't communicate value, the link doesn't work, or the App Store page doesn't convert. Optimize the entire funnel, not just the share step.

Sources:
- [Pixel Envy -- I Do Not Care About Impediments to a Creepy Growth Hacking Technique](https://pxlnv.com/blog/growth-hack/)
- [Eleken -- 18 Dark Patterns Examples](https://www.eleken.co/blog-posts/dark-patterns-examples)
- [Aspire Systems -- Dark Patterns Part I](https://blog.aspiresys.pl/technology/dark-patterns-part-i/)

---

## 13. Zerocap Viral Loop Blueprint

Synthesizing all research into a concrete implementation plan.

### The Core Loop

```
TRIGGER:    User points camera at an object
ACTION:     AI transforms it into a living pet with personality
REWARD:     Delight (cute pet, surprising traits, personal connection)
SHARE:      User shares transformation to friends/social
ACQUIRE:    Friends see it, want their own, download app
REPEAT:     New user scans their own objects
```

### Five Viral Channels, Ranked by Priority

**Channel 1: UGC TikTok/Reels Content (Highest reach, lowest cost)**
- Auto-generate share-ready 15-second transformation videos
- Design the pet card/results screen to look like viral content formats (trading card, stat screen)
- Subtle watermark on all shared content
- "What should I scan next?" comment bait at the end of every video

**Channel 2: iMessage/DM Sharing (Highest conversion)**
- One-tap share of animated transformation GIF
- Deep link that shows the friend's specific pet before prompting download
- "Your friend David made a pet from their coffee mug" preview text
- Rich link preview with the pet image

**Channel 3: Instagram Stories (Broadest friend reach)**
- Native Story sharing with interactive stickers (polls, questions)
- Split-screen template: real object + AI pet
- "What would yours look like?" call to action
- Link sticker to App Store

**Channel 4: IRL "Scan This" Moments (Highest trust)**
- Dramatic, visible transformation animation designed for spectators
- Distinctive sound design (the "pet appears" sound)
- "Scan Together" mode for group experiences
- QR code profile sharing for collections

**Channel 5: Referral Program (Sustained motivation)**
- Exclusive pets only available through referrals
- Tiered rewards (1 friend = rare style, 3 = exclusive pet, 10 = legendary)
- Referral links with embedded deep links and rich previews
- Prompt after first pet creation at peak delight

### Implementation Priorities

**Phase 1: MVP Share Flow (Pre-launch)**
- [ ] Auto-generate side-by-side transformation image (before/after)
- [ ] iOS Share Sheet integration (one tap to any platform)
- [ ] Subtle "Made with Zerocap" watermark on all shared content
- [ ] Deep link to App Store with attribution tracking
- [ ] Transformation reveal video generation (15-second MP4)

**Phase 2: Platform Optimization (Launch)**
- [ ] Instagram Stories native sharing (background + sticker)
- [ ] TikTok share SDK integration
- [ ] Rich link previews (Open Graph tags) for iMessage/WhatsApp
- [ ] Pet card design (trading card format with personality traits)
- [ ] Share prompt UX at optimal moment (post-pet-creation, post-naming)

**Phase 3: Social Layer (Post-launch)**
- [ ] Friends' pets feed (requires social graph)
- [ ] Referral program with exclusive pet rewards
- [ ] "Scan Together" mode for group IRL experiences
- [ ] Pet interaction mechanics (pets from different users meeting)
- [ ] Collection showcase (shareable profile with all pets)

**Phase 4: Viral Amplifiers (Growth)**
- [ ] Challenge format templates ("Turn your kitchen into pets" series)
- [ ] Seasonal/themed transformations (Halloween, holiday variants)
- [ ] Compilation video auto-generation (all my pets in a slideshow)
- [ ] Leaderboards/rankings for most creative transformations
- [ ] Pet trading/gifting between users

### Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Share rate (% of pet creators who share) | 30%+ | Core viral lever |
| Shares per sharer | 2+ platforms | Multiplier on reach |
| Click-through rate on shared content | 15%+ | Share artifact quality |
| Install rate from shared content | 5-8% | Funnel efficiency |
| K-factor (calculated weekly) | 0.4+ sustained, 1.0+ burst | Overall viral health |
| Viral cycle time | <24 hours | Speed of loop |
| UGC content creation rate | 5%+ of users post publicly | Organic distribution |
| iMessage share rate | Track separately | Highest-converting channel |

### The North Star

The ultimate measure of viral success is not K-factor or share rate in isolation. It's whether users create content about Zerocap **without being asked.** When people are screen-recording the transformation moment and posting it to TikTok because the content is genuinely entertaining -- not because a prompt told them to -- the viral loop is working.

Every design decision should be evaluated against this question: **Does this make someone more or less likely to pull out their phone and show their friend?**

---

## Appendix: Quick Reference -- Viral Mechanics Cheat Sheet

| Mechanic | Example | Zerocap Application |
|----------|---------|---------------------|
| Before/after reveal | FaceApp aging, Lensa avatars | Object -> pet transformation |
| Watermarked output | FaceApp, TikTok | "Made with Zerocap" on all shared content |
| Challenge format | #FaceAppChallenge | #TurnItIntoAPet challenge |
| Collectible card format | Umax rating card, Pokemon cards | Pet card with traits and stats |
| Nostalgia trigger | EPIK yearbook, Tamagotchi | "AI Tamagotchi" positioning |
| Celebrity/influencer seeding | Lensa (MKBHD), EPIK (Keke Palmer) | Seed 50+ nano creators with free access |
| Scarcity through referrals | Dropbox storage, Clubhouse invites | Referral-exclusive pets |
| Social proof feed | Strava activity, Instagram Explore | Friends' pets feed |
| IRL demonstration | Pokemon GO crowds, Shazam at dinner | Visible transformation animation + sound |
| Compilation/collection | "My pet collection" series | Auto-generated collection showcase |
| Constraint-driven ritual | BeReal daily notification | Daily scan streak / object of the day |
| Platform-adapted artifacts | Native Stories, TikTok video, iMessage GIF | Different format per destination |
