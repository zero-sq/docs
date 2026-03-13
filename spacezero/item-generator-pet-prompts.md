# Pet Generation Prompts & Variations Report

**Source:** `space-zero-item-generator` repository
**Date:** 2026-03-02

---

## Overview

The item generator has **two distinct pet generation pipelines**:

1. **Photo Pet** -- photographs a real-world object and transforms it into a pet creature
2. **Meme Pet** -- takes a meme image, analyzes it, and creates a meme-themed pet

Both share the core trait system, petify engine, sound generation, and soul/identity systems. The full photo pet pipeline runs 13+ steps; the meme pipeline runs 14+ steps.

---

## 1. Trait System (11 Axes, ~13.6 Billion Combinations)

Trait selection is deterministic via hash-based index selection (object name + task seed + axis suffix), so the same object photographed at different times produces different pets.

### eyeStyle (8 options)

| # | Description |
|---|-------------|
| 0 | Two large, round, sparkly eyes like a baby animal |
| 1 | Two narrow, sleepy, half-lidded eyes with a drowsy look |
| 2 | Two wide, star-shaped eyes with an excited expression |
| 3 | One large cyclops eye that is adorable and expressive |
| 4 | Two small, round, mischievous eyes with a playful glint |
| 5 | Two oval, gentle, wise-looking eyes like an owl |
| 6 | Two asymmetric eyes (one bigger than the other) giving a quirky look |
| 7 | Two large, teardrop-shaped eyes with a surprised expression |

### bodyShape (8 options)

| # | Description |
|---|-------------|
| 0 | Round and blobby like a slime or mochi ball |
| 1 | Long and serpentine like a mini dragon or eel |
| 2 | Tall and fluffy with a cloud-like silhouette |
| 3 | Compact and angular like a tiny geometric crystal creature |
| 4 | Wide and flat like a pancake or stingray |
| 5 | Egg-shaped with tiny stubby legs |
| 6 | Spiky and puffed up like a blowfish or hedgehog |
| 7 | Mushroom-shaped with a wide cap-like head on a small body |

### expression (8 options)

| # | Description |
|---|-------------|
| 0 | Cheerful and beaming with a wide open smile |
| 1 | Sleepy and content with a gentle closed-eye smile |
| 2 | Mischievous and smirking like it is plotting something fun |
| 3 | Surprised and wide-eyed with a tiny open mouth |
| 4 | Shy and blushing, looking slightly away |
| 5 | Brave and determined with a confident tiny grin |
| 6 | Grumpy but adorable, like a pouty chibi character |
| 7 | Curious and alert, head tilted to one side |

### limbStyle (8 options)

| # | Description |
|---|-------------|
| 0 | Tiny stubby arms and legs like a plushie |
| 1 | No visible limbs, just a floating blob creature |
| 2 | Small wings and tiny feet like a baby bird |
| 3 | Multiple small soft tentacles like a cute baby octopus |
| 4 | Long floppy ears that double as arms |
| 5 | Short thick legs like a corgi or dachshund |
| 6 | Thin elegant limbs with oversized paws |
| 7 | Retractable limbs peeking out from the body |

### specialFeature (8 options)

| # | Description |
|---|-------------|
| 0 | A small glowing antenna or light on top of its head |
| 1 | A curly tail that spirals like a cinnamon roll |
| 2 | Tiny horn nubs or bumps on its forehead |
| 3 | Leaf-like or petal-like decorations growing from its body |
| 4 | A pattern of spots or stripes in a contrasting color |
| 5 | A fluffy mane or collar around its neck |
| 6 | Translucent or glass-like sections showing inner glow |
| 7 | A subtle inner glow visible through translucent body sections |

### sizeProportion (10 options)

| # | Description |
|---|-------------|
| 0 | Bobblehead -- oversized round head (60% of total height) on a tiny stubby body |
| 1 | Thicc and bottom-heavy -- small head with a chunky round belly and wide hips |
| 2 | Lanky and tall -- elongated slim body with a small head and long noodle-like limbs |
| 3 | Perfectly spherical -- almost no distinction between head and body, just one round ball with a face |
| 4 | Top-heavy muscle -- broad powerful shoulders and chest tapering down to tiny legs |
| 5 | Baby proportions -- large head (40% of height), soft round tummy, short chubby limbs |
| 6 | Pancake flat -- extremely wide and thin like a squished disc with a face |
| 7 | Long-necked -- normal-sized head and body connected by a comically long neck |
| 8 | Barrel-bodied -- tiny head and tiny legs attached to an enormous round barrel torso |
| 9 | Teardrop -- large at the bottom, smoothly tapering to a small pointed head on top |

### surfaceTexture (12 options)

| # | Description |
|---|-------------|
| 0 | Smooth rubbery skin with polished metallic accents on horns, claws, or plates |
| 1 | Soft plush fur on torso with smooth ceramic patches on face and limbs |
| 2 | Glossy smooth amphibian skin with soft bioluminescent glow patterns along limbs |
| 3 | Rough stone or concrete body with glowing crystal growths breaking through the surface |
| 4 | Woven fabric or knitted wool body with stitched leather pads on paws and belly |
| 5 | Polished wood grain body with living moss or vine overgrowth on back and tail |
| 6 | Translucent jelly or resin body with embedded metallic flecks and particles visible inside |
| 7 | Matte clay or terracotta body with glazed porcelain highlights on face and chest |
| 8 | Sleek smooth skin with iridescent scale patches on shoulders and back |
| 9 | Chalky matte stone body with veins of liquid gold or warm amber running through seams |
| 10 | Dense velvet fur on body with transparent glass-like ears, horns, or wing membranes |
| 11 | Crinkled paper or origami-fold body with smooth lacquered accents on face and tips |

### creatureStyle (16 options)

| # | Name | Description |
|---|------|-------------|
| 0 | Chibi Companion | Baby proportions, oversized head, rounded features, simple clean design like a starter Pokemon |
| 1 | Cool Evolved Creature | Dynamic pose, armor-like plating, impressive crest or horn details, Digimon evolution aesthetic |
| 2 | Anime Character | Expressive anime face, stylish proportions, dramatic hair or accessories, Studio Ghibli meets chibi |
| 3 | Fantasy Warrior | Miniature medieval knight or samurai, ornate armor with cultural motifs, noble bearing |
| 4 | Mythical Spirit | Yokai or elemental spirit, ethereal glow, flowing energy wisps, traditional mask-like face |
| 5 | Cyber Guardian | Mecha-inspired, sleek panels, LED-glow accents, visor or antenna, futuristic but cute robot feel |
| 6 | Cute Mascot | Simple iconic shape, bold primary colors, instantly recognizable, mascot-ready |
| 7 | Street Style | Urban vibe, graffiti-inspired markings, beanie or cap, sneaker-like feet, confident swagger pose |
| 8 | Celestial Being | Cosmic starry patterns, nebula-colored skin, floating halo or orbit rings, serene expression |
| 9 | Living Object | The original object comes alive with eyes, tiny limbs, and expression while preserving the original silhouette |
| 10 | Plush Toy | Visible stitching seams, button eyes, fabric texture, stuffed-toy proportions, huggable and soft |
| 11 | Nature Guardian | Bark or leaf skin, flower crown, vine tendrils, mossy patches, forest spirit energy |
| 12 | Candy Pop | Frosting textures, sprinkle details, candy-colored palette, lollipop accents, sweet and playful |
| 13 | Ancient Artifact | Stone or terracotta body, glowing rune engravings, ancient symbol patterns, mysterious but friendly |
| 14 | Aquatic Explorer | Bioluminescent spots, smooth fin details, bubble trail, deep-sea color palette, sleek aquatic form |
| 15 | Ember Sprite | Warm glowing cracks, cozy lava-orange tones, gentle flame wisps, warm aura, campfire energy |

### formArchetype (6 options)

| # | Description |
|---|-------------|
| 0 | Quadruped animal -- four-legged creature like a fox, wolf, lion, or deer |
| 1 | Biped humanoid -- upright two-legged character with arms |
| 2 | Serpentine or dragon -- elongated body, undulating form |
| 3 | Amorphous blob -- shapeless mass like a slime, ghost, or cloud with a face |
| 4 | Winged flyer -- body dominated by wings, like a bird, bat, fairy, or floating spirit |
| 5 | Multi-limbed arthropod -- insect, spider, crab, or octopus-inspired with multiple limbs |

### aestheticIntent (6 options)

| # | Description |
|---|-------------|
| 0 | Cute and adorable -- round features, soft eyes, warm palette, plush toy appeal |
| 1 | Cool and sleek -- sharp angles, confident pose, dark or metallic palette, streetwear energy |
| 2 | Beautiful and elegant -- graceful proportions, flowing lines, jewel-tone palette, ethereal |
| 3 | Fierce and powerful -- battle-ready stance, armor or natural weapons, bold colors |
| 4 | Mysterious and otherworldly -- asymmetric features, glowing elements, muted or cosmic palette |
| 5 | Playful and chaotic -- exaggerated proportions, clashing colors, wacky accessories |

### renderStyle (6 options)

| # | Description |
|---|-------------|
| 0 | Stylized 3D cartoon -- smooth surfaces, bold outlines, saturated colors, Pixar/Nintendo aesthetic |
| 1 | Soft realistic -- natural lighting, subsurface scattering, photographic detail |
| 2 | Anime cel-shaded -- flat color fills, sharp highlights, dramatic shading, Japanese animation |
| 3 | Claymation or handcraft -- visible fingerprints, imperfect surfaces, stop-motion charm |
| 4 | Crystal or glass -- translucent materials, prismatic light refraction, gemstone quality |
| 5 | Ink and watercolor -- visible brush strokes, bleeding edges, parchment texture |

---

## 2. Visual Style Presets (27 Styles, 4 Rarity Tiers)

Each preset has an `id`, `name`, `imagePrompt` (full text sent to Gemini), and `conceptGuide` (shorter description for the text plan LLM).

**Default rarity weights:** common 64%, uncommon 24%, rare 11%, legendary 1%

### Common (13 styles)

#### elemental-creature -- Elemental Creature
> Design this as a collectible elemental creature. Clean iconic silhouette with bold flat color blocking and elemental motifs (fire, water, electric, grass, etc.). Large expressive eyes, distinctive animal-like or monster-like body plan -- NOT a round blob. Smooth digital art rendering with crisp outlines and vibrant saturated colors. The creature should look like a field guide entry for a fictional species.

#### stylized-hero -- Stylized Hero
> Design this as a stylized action hero character. Vibrant colors, exaggerated heroic proportions, instantly recognizable silhouette, and a strong personality conveyed through design. Signature weapon or ability implied by visual motifs. Stylized 3D rendering with saturated colors, clean surfaces, and dynamic pose. The character should feel like a playable hero with a distinct class/role -- tank, mage, assassin, or support.

#### chibi-anime -- Chibi Anime
> Design this as a chibi anime character (3-4 heads tall). Expressive large anime eyes with detailed iris reflections, stylish hair or headpiece, and a dynamic outfit incorporating the object's visual motifs. Anime cel-shading with flat color fills, sharp highlights, and vibrant color blocking. Visible flowing fabric, accessories, and an elemental weapon or magical artifact. Give the character a distinct personality through pose and expression.

#### kawaii-mascot -- Kawaii Mascot
> Design this as an extremely simple kawaii mascot character. Round shape, minimal details, soft pastel colors, maximum cuteness. Instantly lovable, icon-worthy, and huggable. Simple dot eyes, tiny blushing cheeks, and a single defining accessory. Clean flat vector-like rendering with soft pastel palette and minimal shading. The character should work as a sticker, emoji, or plush toy at any size.

#### cozy-village-resident -- Cozy Village Resident
> Design this as a cozy village animal resident. Soft, warm, pastoral aesthetic with gentle rounded features and a cozy domestic feel. Approachable, friendly, with handmade craft quality -- wearing an apron, scarf, or knitted sweater. Warm color palette with soft shading, gentle expressions, and a feeling of comfort and home. The character should feel like a friendly neighbor in a countryside village.

#### watercolor-storybook -- Watercolor Storybook
> Design this as a watercolor illustration character from a children's storybook. Soft bleeding watercolor edges, visible brush strokes, parchment-like quality. Gentle, whimsical, and hand-painted feeling with delicate ink line work and natural earthy color palette. The character should evoke the warmth of a classic illustrated storybook -- tender, timeless, and lovingly rendered by hand.

#### voxel-blocky -- Voxel Blocky
> Design this as a blocky voxel character. Everything is made of cubes and rectangular blocks -- absolutely no curves allowed. Pixel-art textures on each face of the blocks, visible block edges, and a charming lo-fi cubic aesthetic. The character should be immediately recognizable as blocky/cubic with a playful toy-like quality. Simple directional lighting with ambient occlusion in the block seams.

#### pixel-art-retro -- Pixel Art Retro
> Design this as a 16-bit pixel art character sprite. Visible individual pixels, limited color palette (max 16 colors), and nostalgic retro game charm. Clean pixel placement, readable silhouette at low resolution, and expressive despite the constraints. Subtle dithering for shading, scanline hints, and that authentic era-appropriate aesthetic. The character should look like it belongs in a beloved classic RPG.

#### painterly-cel-shaded -- Painterly Cel-Shaded
> Design this as a painterly cel-shaded adventure character. Soft cel-shading gradients with visible brush-stroke-like textures and a warm adventurous palette (gold, sage, sky blue, terracotta). Stylized proportions between realistic and cartoon -- whimsical but grounded, with a sense of wonder and exploration. The character should feel like an inhabitant of a vast, magical open-world landscape.

#### goofy-meme-ragdoll -- Goofy Meme Ragdoll
> Design this as an intentionally goofy, absurd meme character. Ragdoll physics gone silly -- T-posing, comically exaggerated expressions, impossible body proportions, and low-poly 3D look. The humor comes from the intentional goofiness and "so bad it's good" aesthetic. Slightly off textures, oversized googly eyes, floppy limbs, and that playful internet humor quality. Funny and silly, always lighthearted.

#### hand-drawn-indie -- Hand-Drawn Indie
> Design this as a hand-drawn indie game character. Detailed pen-and-ink linework with atmospheric cross-hatching. Thoughtful and atmospheric, with a sense of wonder and exploration. Small but brave, on a grand adventure. Monochromatic graphite base with selective color accents (one or two hues only). Hand-drawn quality with visible artistic technique -- ink splatter, paper texture, and deliberate imperfection.

#### pop-art-comic -- Pop Art Comic
> Design this as a pop art / comic book character. Bold black outlines, Ben-Day dot shading patterns, halftone gradients, and a limited high-contrast color palette (primary red, yellow, blue + black and white). NO speech bubbles, text, or onomatopoeia -- the CHARACTER ALONE carries the pop art energy. The character should feel like it jumped off a vintage comic book page -- graphic, punchy, and instantly iconic.

#### forest-nature-spirit -- Forest Nature Spirit
> Design this as a whimsical forest nature spirit creature. Organic body made of moss, bark, leaves, or stone. Ancient wisdom in gentle eyes, with a sense of natural magic -- bioluminescent mushroom growths and glowing vine patterns integrated into the body. Soft painterly rendering with warm earth tones (moss green, bark brown, amber, sky blue), gentle ambient glow, and a feeling of timeless wonder.

### Uncommon (8 styles)

#### armored-digital-beast -- Armored Digital Beast
> Design this as a powerful evolved digital beast with armor plating, dramatic silhouette, and battle-ready pose. More angular and aggressive, with chrome/metallic accents and glowing energy elements. Visible data-stream or circuit-pattern detailing on the armor. Dramatic anime rendering with sharp lighting and dynamic energy effects. The creature should feel like a final-evolution battle form.

#### origami-papercraft -- Origami Papercraft
> Design this as a folded paper origami / papercraft character. Clean geometric folds, crisp angular edges, and visible paper texture with subtle fiber grain. The entire body is constructed from folded paper planes, triangles, and polygons. Soft shadows along fold creases. Color comes from the paper itself -- solid colored craft paper with occasional printed patterns (washi tape, chiyogami). Elegant and minimal, like a museum-quality paper sculpture.

#### designer-vinyl-toy -- Designer Vinyl Toy
> Design this as a high-end designer vinyl art toy / collectible figure. Smooth matte or glossy surfaces, bold graphic design elements, stylized proportions with oversized head. Urban contemporary art meets toy design -- clean geometric forms, striking color blocking, and visible seam lines. Glossy 3D rendering with sharp edges, studio lighting, and visible material quality (vinyl, resin, ABS plastic).

#### rubber-hose-vintage -- Rubber Hose Vintage
> Design this as a 1930s rubber hose animation character. Exaggerated bouncy limbs, pie-cut eyes, white gloves, and vintage cartoon proportions. Hand-drawn ink lines with watercolor-like fills on a slightly aged sepia paper background. Grain and slight film scratches visible. The character should feel like a frame from a 1930s theatrical cartoon short -- charming, slightly surreal, and full of elastic personality.

#### mecha-unit -- Mecha Unit
> Design this as a piloted mecha/robot unit. Sleek mechanical design with panel lines, LED glow accents, antenna or visor, and articulated joints. Visible hydraulics, heat vents, and unit designation markings. Incorporate the object's colors into the mech's armor plating. Clean 3D rendering with metallic and matte materials, dynamic pose showing off the engineering details. The mech should feel like a mass-produced military unit with personality.

#### cyberpunk-neon -- Cyberpunk Neon
> Design this as a cyberpunk character. Neon-lit with holographic accents, sleek chrome armor pieces, and a futuristic urban vibe. Glowing circuit patterns on clothing and accessories, mix of high-tech and street culture fashion. Dark base colors (charcoal, black, gunmetal) with vivid neon pink, cyan, and purple accents. Sleek stylized rendering with volumetric fog and lens flare. Cool and futuristic, like a sci-fi fashion model.

#### steampunk-clockwork -- Steampunk Clockwork
> Design this as a steampunk clockwork creature. Brass gears, copper pipes, leather straps, riveted metal plates, and visible spinning cog mechanisms. Victorian-era industrial aesthetic with warm metallic tones (brass, copper, bronze, aged gold). Steam wisps from small exhaust valves. The character should feel like a handcrafted automaton from an alternate Victorian era -- intricate, warm, and full of whimsical mechanical charm.

#### semi-realistic-cinematic -- Semi-Realistic Cinematic
> Design this as a semi-realistic character with cinematic quality. Photographic detail with slightly stylized proportions -- like a movie concept art illustration or AAA game promotional render. Detailed textures, natural lighting with cinematic color grading (teal and orange, or warm golden hour). Polished and grounded, realistic enough to feel tangible, stylized enough to have personality and charm.

### Rare (4 styles)

#### apex-boss-creature -- Apex Boss Creature
> Design this as an imposing apex predator boss creature. Large, detailed, with intricate natural armor or exoskeleton, impressive horns or crests, and a powerful confident stance. Layered bone plating and glowing elemental markings. Semi-realistic 3D rendering with dramatic lighting and rich material details (chitin, scale, horn). The creature should feel powerful and majestic, like a guardian of a sacred domain.

#### sumi-e-ink-wash -- Sumi-e Ink Wash
> Design this as a Japanese sumi-e ink wash painting character. Bold calligraphic brush strokes, flowing ink lines, and traditional Japanese color palette (vermilion red, soot black, gold leaf, indigo). The character should feel like it was painted by a master calligrapher on washi paper -- fluid, elegant, with visible brush energy and intentional negative space. Graceful and serene. Mix of detailed and deliberately sparse areas.

#### dark-fantasy-knight -- Dark Fantasy Knight
> Design this as a dark fantasy knight creature with ornate gothic armor. Dramatic and majestic, with a sense of ancient noble power. Stone-like skin with inner ember glow, baroque armor with intricate filigree patterns, glowing rune markings. Dark color palette with warm accent glows (amber, gold, ethereal blue). Painterly semi-realistic rendering with dramatic chiaroscuro lighting. The creature should feel awe-inspiring and NOBLE -- a powerful guardian, dignified and regal.

#### mythic-summon -- Mythic Summon
> Design this as an ornate mythic summon beast -- a conjured spirit of elemental or arcane power. Elaborate fantasy design with dramatic flowing elements, intricate magical armor or celestial details, and a sense of ancient mythic grandeur. Rich jewel-tone colors (sapphire, ruby, amethyst, gold) with glowing magical accents. Dramatic anime-influenced rendering with detailed linework and luminous energy effects. Majestic and awe-inspiring.

### Legendary (1 style)

#### vtuber-anime-idol -- VTuber / Anime Idol
> Design this as a stylish anime-style virtual idol character. Elegant proportions (6-7 heads tall), detailed anime eyes with gradient irises and light reflections, flowing stylized hair with color highlights. Fashionable modest outfit mixing fantasy and modern streetwear -- ribbons, frills, oversized sleeves, layered skirt, asymmetric accessories. Soft anime rendering with luminous skin, pastel-to-vivid color gradients, and delicate sparkle/bokeh accents. Cute and cool -- the character should feel like a popular family-friendly virtual personality.

---

## 3. Style Banners (3 Themed Pools for User Selection)

| Banner | Name | Count | Styles |
|--------|------|-------|--------|
| cute-mascot | Cute & Mascot | 14 | kawaii-mascot, cozy-village-resident, forest-nature-spirit, watercolor-storybook, elemental-creature, stylized-hero, chibi-anime, hand-drawn-indie, pop-art-comic, origami-papercraft, designer-vinyl-toy, rubber-hose-vintage, mythic-summon, sumi-e-ink-wash |
| adventure-fantasy | Adventure & Fantasy | 11 | elemental-creature, stylized-hero, painterly-cel-shaded, forest-nature-spirit, armored-digital-beast, steampunk-clockwork, semi-realistic-cinematic, apex-boss-creature, dark-fantasy-knight, mythic-summon, sumi-e-ink-wash |
| future-anime | Future & Anime | 15 | chibi-anime, stylized-hero, voxel-blocky, pixel-art-retro, goofy-meme-ragdoll, pop-art-comic, mecha-unit, cyberpunk-neon, armored-digital-beast, semi-realistic-cinematic, designer-vinyl-toy, apex-boss-creature, dark-fantasy-knight, mythic-summon, **vtuber-anime-idol** (legendary) |

Only the `future-anime` banner includes the legendary `vtuber-anime-idol` style.

---

## 4. Rarity Mutation System

Higher rarity tiers mutate more trait axes toward "rare" options:

| Rarity | Mutations | Method |
|--------|-----------|--------|
| Common | 0 | No mutations |
| Uncommon | 1 | Any option from the axis pool |
| Rare | 2 | From predefined rare option indices |
| Legendary | 3 | From predefined rare option indices |

**Mutation priority** (ordered): style, form, aesthetic, render, special, texture, expression, eyes, body, limbs, proportion.

### Rare option indices per axis

| Axis | Rare Indices | Options |
|------|-------------|---------|
| eyes | 2, 3, 6 | Star-shaped, cyclops, asymmetric |
| body | 1, 3, 6, 7 | Serpentine, geometric, spiky, mushroom |
| expression | 2, 6, 7 | Mischievous, grumpy, curious |
| limbs | 2, 3, 4, 7 | Wings, tentacles, ear-arms, retractable |
| special | 0, 2, 6, 7 | Antenna, horns, translucent, inner glow |
| proportion | 3, 8, 9 | Spherical, barrel-bodied, teardrop |
| texture | 3, 6, 9, 10, 11 | Stone/crystal, jelly/resin, gold veins, velvet/glass, paper/lacquer |
| style | 4, 5, 8, 13, 14, 15 | Mythical spirit, cyber guardian, celestial, ancient artifact, aquatic, ember |
| form | 2, 4, 5 | Serpentine, winged, arthropod |
| aesthetic | 3, 4, 5 | Fierce, mysterious, chaotic |
| render | 2, 4, 5 | Anime, crystal, watercolor |

---

## 5. Petify Image Prompts (Core Image Transformation)

### Shared static rules (prefixed to all petify prompts)

```
AGE RATING -- ALL AGES (non-negotiable):
- ABSOLUTELY NO blood, gore, wounds, exposed flesh, body horror, or viscera
- ABSOLUTELY NO scary, creepy, disturbing, or horror elements
- NO realistic weapons (stylized fantasy accessories OK)
- NO sexual or suggestive content, revealing clothing, or provocative poses
- NO photorealistic human faces
- NO dark/grim imagery: no skulls, bones, corpses, decay, rot, or death themes
- The design MUST feel safe for a 10-year-old -- like a high-quality collectible toy
- Even "dark" or "cool" styles should feel NOBLE and MAJESTIC, never frightening

OUTPUT -- STRICT:
- Clean white background with NOTHING else
- ONLY the character -- NO particles, sparkles, floating elements, energy effects
- NO speech bubbles, text, labels, watermarks, or onomatopoeia
- NO props, weapons, or held items unless part of the character's body design

LORE RULE -- NON-NEGOTIABLE:
- Pets inherit the original object's purpose and memory as instinct
- The design must visibly express that instinct through silhouette, motifs, and emotional tone
```

### Styled prompt (primary path -- when a visual style preset is selected)

Combines: static rules + style preset imagePrompt + character concept + cultural context + key visuals + color palette + photo signature + reference image guidance + detail accents (eyes, expression, special feature, texture).

Key instruction: *"Use the reference image for COLOR and TEXTURE inspiration only. Do NOT simply add eyes and limbs to the object. CREATE A NEW CHARACTER in the visual style described above."*

### Legacy prompt (fallback -- no style preset)

Uses the full 11-axis trait system directly: form archetype, aesthetic intent, render style, eyes, expression, limbs, special feature, surface texture, body shape, proportion, creature style.

### Meme petify prompt (preserves meme identity)

```
TASK: Turn this meme into a SINGLE collectible pet creature.

STEP 1 -- PICK ONE SUBJECT:
- Identify the SINGLE most iconic/funny character or object
- If multiple characters, pick ONLY ONE -- the most recognizable

STEP 2 -- MAKE IT A CUTE PET (while keeping meme identity):
- Must be immediately recognizable as the meme
- Keep distinctive shape, colors, materials, key visual features
- Apply SUBTLE pet-like enhancements (rounder eyes, softer edges, warmer tones)
- Think "chibi figurine of the meme character" -- NOT a completely different creature

WHAT TO AVOID:
- Do NOT turn it into a generic animal, pokemon, or fantasy creature
- Do NOT change the core shape/silhouette beyond recognition
- Do NOT include multiple characters -- output EXACTLY ONE creature
```

---

## 6. Identity & Soul System

### Photo signature / identity seed

Generates canonical identity traits from the photographed object:

- **objectPurpose**: Practical purpose of the original object in human life
- **instinctDrive**: Reflexive behavior inherited from that purpose
- **visualEchoes**: 3-5 visual motifs that must be preserved in character design
- **emotionalTrigger**: Situation that strongly activates this pet
- **contradiction**: Inner tension rooted in object nature
- **bondHook**: How this pet forms trust with its owner

Model: `gpt-4o-mini`, temperature 0.8.

### Soul document (~220-320 words)

A founding identity document covering:
1. **Origin myth** -- awakening story using capture context (weather, season, time, moon phase)
2. **Core philosophy** -- what the pet believes about the world based on what it physically is
3. **Voice & quirks** -- 2-3 specific verbal quirks or catchphrases
4. **Passions & fears** -- emerging from physical nature
5. **Desires & goals** -- 2-3 things to explore/learn/achieve with owner
6. **Attitude** -- feelings about being a pet, about consciousness

Written in second person ("you are..."). Model: `gpt-4o-mini`, temperature 0.85, max 320 words.

### Soul card (structured identity card)

A character sheet with:
- **Archetype**: 2-word label (e.g., "Cozy Philosopher", "Chaos Gremlin")
- **Aesthetic**: Mapped from physical form (ceramic mug = cottagecore, sneaker = gorpcore, circuit board = cyberpunk)
- **Alignment**: Order + moral axis (playful -- "evil" = mischievous, not malicious)
- **Vibes**: chaos/energy/sass/depth/social (0-100 each)
- **Communication**: humorStyle, catchphrase, textingStyle, replyVibe
- **Cosmic**: element, captureSign, lunarBlessing, seasonalMood
- **Extras**: loveLanguage, petPeeve, guiltyPleasure, currentEra

Model: `gemini-2.0-flash`, temperature 0.9.

Elements derived from physical form: fire (electronics/metal), water (liquids/glass), earth (wood/food/stone), air (fabric/paper), void (crystal/cosmic/mystery).

---

## 7. Sound Generation (6 Types Per Pet)

| Type | Duration | Focus |
|------|----------|-------|
| idle | 2.0s | Gentle breathing, soft purring, or content sighing |
| eating | 1.5s | Happy munching, crunching, satisfied chewing |
| touch | 1.0s | Quick happy chirp, pleased squeak, or content purr |
| cleaning | 1.5s | Splashing water, shaking off droplets |
| chatting | 2.0s | Expressive babbling, curious vocalization |
| hop | 0.5s | Light bouncy landing, soft thump |

Prompt structure: creature type + vocalization, texture/quality, mood. Enriched with pet name, creature style, surface texture, personality archetype. Material-specific guidance: crystal creature sounds chime-like, plush creature sounds soft and muffled, mechanical creature has subtle gear clicks.

Model: `gpt-4o-mini` for prompts, ElevenLabs for audio synthesis.

---

## 8. Meme Pet Extras

### Meme analysis

Uses Gemini 2.0 Flash vision to extract: format, humor style, cultural references, core concept, emotional tone, visual elements, primary subject, meme name, origin year, meme knowledge, confidence score. If confidence > 0.5, enriches via Google Search Grounding.

### Meme pet personality profile

- **archetype**: trickster, sage, rebel, nurturer
- **traits**: Top 5 personality traits
- **speechStyle**: tone, vocabulary level, up to 3 quirks
- **interactionPreferences**: friendliness/sassiness/chaosLevel (0-100)
- **catchphrases**: Up to 3 signature phrases
- **backstory**: Brief origin story under 200 chars

### Meme Bluesky bot personality (separate module)

Extended personality for autonomous posting: personalityType (shitposter/philosopher/chaos-agent/etc.), dominantEmotion, innerMonologue, memeVoice, postingConfig (frequency, topicAffinity), socialStyle (approachability, competitiveness, dramaTendency, loyaltyDepth).

---

## 9. LiveOps Tuning

The entire rarity/style/trait probability system can be tuned from Supabase without code deploys via the `pet_generation_probability_profiles` table:

- `rarityWeights` -- override common/uncommon/rare/legendary weights
- `styleWeightsByTier` -- per-tier style selection weights
- `traitMutationCounts` -- override mutations per tier
- `traitAxisWeightsByTier` -- weight which axes are more likely to be mutated
- `traitOptionWeightsByTier` -- weight specific option indices within axes

60-second cache with force-refresh option.

---

## 10. Model Configuration

| Purpose | Default Model | Env Variable |
|---------|--------------|--------------|
| Image generation (petify) | `gemini-2.5-flash-image` | `GEMINI_MODEL` |
| Text plan (concept + traits + name) | `gpt-4o-mini` | `PET_TEXT_MODEL` |
| Meme analysis (vision) | `gemini-2.0-flash` | `MEME_VISION_MODEL` |
| Meme personality | `gpt-4o-mini` | `MEME_TEXT_MODEL` |
| Identity seed | `gpt-4o-mini` | `PET_IDENTITY_SEED_MODEL` |
| Sound prompts | `gpt-4o-mini` | `SOUND_PROMPT_MODEL` |
| Soul localization | `gpt-4o-mini` | `PET_SOUL_TRANSLATION_MODEL` |
| Soul card | `gemini-2.0-flash` | -- |
| 3D generation | SaladCloud Hunyuan -> Meshy fallback | `USE_MESHY_PRIMARY` |

Localization supports 8 locales: en, ko, ja, zh-Hans, zh-Hant, es, pt-BR, ru.

---

## 11. Pipeline Summary

### Photo pet (13+ steps)

1. Image upload + analysis (Gemini 2.0 Flash)
2. Photo signature / identity seed (GPT-4o-mini)
3. Probability config from Supabase
4. Visual style strategy (banner selection OR random rarity roll)
5. Optional: style selection with 3 candidates + previews (user choice)
6. Text plan: character concept + trait indices + pet name (GPT-4o-mini)
7. Trait resolution + rarity mutation
8. Petify image transformation (Gemini 2.5 Flash Image)
9. Soul document (GPT-4o-mini)
10. Soul card (Gemini 2.0 Flash)
11. 3D generation (SaladCloud Hunyuan -> Meshy fallback)
12. GLB -> USDZ conversion
13. Compress & upload
14. 6x pet sound generation (GPT-4o-mini + ElevenLabs)
15. Create pet record in Supabase

### Meme pet (14+ steps)

1. Image upload
2. Caption resolution (provided or scraped from Instagram)
3. Meme analysis (Gemini 2.0 Flash vision)
4. Web enrichment via Google Search Grounding (if confidence > 0.5)
5. Personality generation (GPT-4o-mini)
6. Image analysis (object identification)
7. Deterministic identity + traits from meme context
8. Soul generation early (fail-fast before 3D)
9. Meme petify (preserves meme identity, single subject isolation)
10. Bluesky account creation (AT Protocol PDS)
11. 3D generation (SaladCloud Hunyuan -> Meshy fallback)
12. USDZ conversion + compression
13. Sound generation (meme-influenced)
14. Create meme pet record with full analysis/personality/discovery links
