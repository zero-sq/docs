# Zerocap Shorts Factory

Batch production system for 6-second looping short-form videos. 3 posts/day across YouTube Shorts, Instagram Reels, and TikTok.

## Format

Benchmarked from @bark-loaf's toilet video (~10k views across platforms). Two-image loop using Higgsfield AI transitions.

**The loop:** Game screen (pet) → Camera screen (real object) → Game screen (pet) → ...

Viewers watch 2-3 loops before realizing it's repeating. ~6 seconds per loop.

---

## What you need per video

### 1. Pet image (generated)
- **Tool:** Nano Banana (or equivalent image gen)
- **Style:** Collectible 3D plush creature — tactile toy feel, big expressive eyes, creature-collector energy (see prompt template below)
- **Background:** Transparent or white (will be composited onto game screen template)
- **Derivation:** Pet visually references the source object (colors, shapes, textures become creature features)

### 2. Camera screen image (generated)
- **Tool:** Nano Banana (or equivalent image gen)
- **Style:** Ultra-realistic, first-person phone camera POV
- **Setting:** Natural environment where the object would be found (kitchen counter, desk, bathroom, etc.)
- **Framing:** Slightly overhead angle, as if holding phone to scan
- **Note:** Will be composited onto camera UI template

### 3. Two transitions (AI video)
- **Tool:** Higgsfield (Kling 3.0 or Veo 3.0)
- **Transition A (camera → pet):** Real object morphs/dissolves into the pet on game screen
- **Transition B (pet → camera):** Pet morphs back into the real object view — this closes the loop
- **Duration:** ~3 seconds each = ~6 seconds total

### 4. Text overlays (CapCut)
- **On game screen:** "this was a [object]" (white text, black pill background, center-top)
- **On camera screen:** "yes... a [object]" (same style)

### 5. Social media copy
- **Title/caption** (same across YT/IG/TikTok)
- **Description** with hashtags
- **First comment** (engagement driver)
- **CapCut caption bar:** "I scanned my [object] and this happened"

---

## Templates (reusable across all videos)

### Game screen template
- Dark background with grassy landscape at top
- Pet name + "Lv.1" badge (top-left)
- Play/volume controls (top-left)
- Left sidebar: action icons (fire, controller, record)
- Bottom bar: avatar, username (@zerocap), navigation icons
- **Swap zone:** Center — replace with generated pet image

### Camera screen template
- Full-screen camera viewfinder
- Back arrow + play/volume controls (top-left)
- Left sidebar: lock, people, globe icons
- "Capture Tips" overlay at bottom-center
- Large capture button (bottom-center)
- Bottom bar: avatar, username (@zerocap)
- **Swap zone:** Full background — replace with generated realistic photo

---

## Production pipeline

```
For each object in the list:

1. GENERATE PET IMAGE
   → Nano Banana prompt (from pet-prompt template)
   → Save as: videos/XXX-object-name/pet.png

2. GENERATE CAMERA IMAGE
   → Nano Banana prompt (from camera-prompt template)
   → Save as: videos/XXX-object-name/camera.png

3. COMPOSITE ONTO TEMPLATES
   → Paste pet.png onto game screen template → game-final.png
   → Paste camera.png onto camera screen template → camera-final.png

4. GENERATE TRANSITIONS (Higgsfield)
   → Upload game-final.png + camera-final.png
   → Transition A prompt: camera-final → game-final
   → Transition B prompt: game-final → camera-final
   → Save as: transition-a.mp4, transition-b.mp4

5. EDIT IN CAPCUT
   → Stitch: transition-a.mp4 + transition-b.mp4
   → Add text overlays
   → Add caption bar
   → Export as loop-friendly MP4 (9:16)

6. POST
   → Upload to YT Shorts, IG Reels, TikTok
   → Copy-paste title, description, first comment from video brief
```

---

## Prompt templates

### Pet image generation (Nano Banana)

**Aspect ratio:** 1:1 (square) — pet gets composited onto the game screen template's center swap zone

**Step 1 — Choose the animal/creature base.** Don't default to a generic blob. Pick a real
animal or character archetype whose natural appearance already shares visual DNA with the
object. The object's colors, patterns, and shapes should suggest the animal. Examples:
- Caramel macchiato → raccoon (brown/cream banding = coffee/milk layers)
- Burger → round bird (plump shape, warm browns, sesame bun = head cap)
- Coke Zero → beetle or penguin (black body, red accents)

The best pets feel like the animal was *born* to represent that object.

**Step 2 — Write the prompt.**

The core aesthetic blends three pillars into one style:
- **Plushie** — tactile, collectible, "I want to buy this as a real toy"
- **Animated film** — big glossy expressive eyes, personality, cinematic warmth
- **Creature collector** — distinct creature with elemental typing energy, feels like
  part of a roster you'd want to collect them all

Every pet should hit all three. The creativity is in HOW each pet executes them — what
animal, what materials, what details. The object drives those decisions.

```
A cute collectible 3D plush [ANIMAL/CREATURE TYPE] inspired by a [OBJECT]. Designed to
feel like a real toy you'd find on a shelf — tactile, huggable, premium build quality.

The [ANIMAL]'s body incorporates the [OBJECT]'s materials, textures, and colors into its
design. [MATERIAL/TEXTURE DIRECTION: describe how the object's visual identity shows up
on the creature — this could be through surface materials (craft plushie approach), through
color/pattern mapping on a clean body (collectible toy approach), or through costume and
environmental details, or any creative combination. Let the object guide what feels right.
Every pet should have its own unique approach — don't repeat the same formula].

Big glossy expressive eyes with bright catchlight reflections (not solid dark — should feel
warm and alive), round body, chibi proportions, stubby limbs — the kind of face that makes
kids (and adults) say "I need this." One or two small accent details from
the object's world — [DETAIL CUES]. Color palette is cohesive, derived from the [OBJECT]'s
natural colors. Soft lighting, clean white background. Front 3/4 view.
```

**Guiding principles:**
- The object drives everything — animal choice, materials, palette. Not the template.
- Do NOT repeat the same formula across pets. Each one should feel like its own creative
  decision.
- The best result is one where someone sees the pet and *immediately* knows what object it
  came from, without being told.
- Target emotion: "I want to collect all of these." If it doesn't trigger that, rethink it.

### Camera screen photo (Nano Banana)

**Aspect ratio:** 9:16 (portrait) — fills the camera screen template background for Shorts/Reels/TikTok

```
A realistic first-person smartphone camera photo of a [OBJECT] sitting on [SURFACE/LOCATION].
Shot from a slightly overhead angle as if someone is holding their phone to take a photo.
Natural indoor lighting, slight depth of field. The [OBJECT] is the clear focal point,
centered in frame. Photorealistic, high resolution, mobile phone camera quality with
natural slight lens distortion. No filters.
```

### Transition A: camera → pet (Higgsfield)

```
The real-life [OBJECT] in the center of the frame magically transforms into a cute plushy
creature. The object glows softly, particles swirl around it, and it morphs smoothly into
the 3D pet character. The background shifts from a realistic room to a dark game environment
with grass. Smooth, magical transformation. 3 seconds.
```

### Transition B: pet → camera (Higgsfield)

```
The cute plushy pet creature in the center of a dark game world reverses back into the
real-life [OBJECT]. The creature dissolves with sparkle particles, the game background
fades into a realistic indoor environment, and the original [OBJECT] re-appears on
[SURFACE]. Smooth reverse transformation. 3 seconds.
```

---

## Social media templates

### Title/caption
```
I scanned my [object] and this happened
```

### Description (same for YT/IG/TikTok)
```
What would YOUR [object] turn into? Drop a 0 in the comments if you want to try this game

[object]-specific line — e.g., "my coke zero became the cutest little soda sprite"

#zerocap #aitamagotchi #aipets #scanit #aigenerated #mobilegame #cute #viral
#[object-specific tags]
```

### First comment (posted immediately after upload)
```
Drop a "0" if you want to scan YOUR stuff into pets. Game drops soon
```

### CapCut caption bar
```
I scanned my [object] and this happened
```

---

## Posting schedule

3 videos/day = 30 videos covers 10 days.

| Time slot | Platform priority | Notes |
|-----------|------------------|-------|
| Morning (8-9 AM) | TikTok | Catches before-school scroll |
| Afternoon (3-4 PM) | Instagram Reels | After-school peak |
| Evening (7-8 PM) | YouTube Shorts | Evening wind-down |

All three platforms get the same video within the same day. Stagger by a few hours.

---

## File structure

```
shorts-factory/
  README.md              ← this file (schema + templates)
  object-list.md         ← 30+ objects with brief notes
  videos/
    001-coke-zero/
      brief.md           ← all prompts, copy, and notes for this video
      pet.png            ← generated pet image
      camera.png         ← generated camera image
      game-final.png     ← composited game screen
      camera-final.png   ← composited camera screen
      transition-a.mp4   ← camera → pet
      transition-b.mp4   ← pet → camera
      final.mp4          ← exported from CapCut
    002-rubber-duck/
      ...
    003-sneaker/
      ...
```
