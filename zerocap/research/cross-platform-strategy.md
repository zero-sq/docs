# Cross-Platform Companion Strategy: Zerocap x Spacezero

Research date: 2026-03-13

---

## Executive Summary

The cross-platform companion — a pet you raise in Zerocap (iOS) that lives and acts in Spacezero (browser) — is Spacezero's single most defensible differentiator. No existing product combines AI-generated companions from mobile camera input with a browser-native voxel sandbox. This document analyzes every relevant precedent, the technical architecture required, UX design principles, launch sequencing, and the retention math that makes multi-surface presence a compounding advantage.

---

## 1. Cross-Platform Companion Systems That Exist Today

### 1.1 Pokemon GO <-> Pokemon HOME <-> Console Games

The most mature cross-platform creature transfer system in gaming.

**How it works:**
- Pokemon HOME is a cloud-based intermediary service that acts as a central hub connecting Pokemon GO (mobile AR), Pokemon Sword/Shield, Brilliant Diamond/Shining Pearl, Legends: Arceus, and Scarlet/Violet (all console).
- Transfers from GO to HOME use the "GO Transporter," which costs GO Transporter Energy (a regenerating resource that creates artificial scarcity and pacing around transfers).
- HOME tracks game-specific data per Pokemon and assigns appropriate movesets when a creature enters a new game environment it has never been in. If a Pokemon enters a new game, it receives its 4 most recent level-up moves for that environment.
- The system maintains four distinct "game environments" with different move lists, stats, and capabilities — meaning a Pokemon's identity is persistent but its expression is context-dependent.

**Key limitations:**
- Transfers from GO to HOME are one-way — you cannot return a Pokemon to GO once transferred.
- Certain special Pokemon (Gigantamax forms, those caught with special PokeBalls) cannot be transferred at all.
- There is a reception queue — you must accept pending transfers before sending more.
- Free tier exists (no Premium Plan required for transfers from GO), lowering the barrier.

**What this means for Zerocap x Spacezero:**
The one-way transfer limitation is notable. Pokemon chose this because the game environments are so mechanically different that round-trip sync would create exploits. Zerocap and Spacezero have a simpler relationship — the companion's personality and visual identity are persistent, while its capabilities are context-specific (camera interaction in Zerocap, terrain modification in Spacezero). This makes bidirectional sync feasible and desirable.

### 1.2 Tamagotchi Ecosystem: Device <-> App <-> Console

Tamagotchi has evolved from isolated handheld devices to a connected ecosystem, though connectivity remains limited.

**Current state:**
- **Tamagotchi Uni** (launched July 2023) — the first Wi-Fi-enabled Tamagotchi in a smartwatch form factor. Connects to an online "Tamaverse" and received DLC over Wi-Fi in 2024 (expansion packs with new characters, items, minigames).
- **Tamagotchi Plaza** (Nintendo Switch, 2025) — the most significant cross-platform moment in Tamagotchi history. The Switch game links with Tamagotchi Uni hardware, and each platform rewards the other: Uni owners get an extra money source, limited-availability items, and additional minigames, while Plaza players get exclusive Tamagotchis not available through any other method.
- **Tamagotchi On App** (mobile, earlier generation) — allowed users to interact with other devices, visit friends, give gifts, and earn Gotchi points. This was a companion app in the traditional sense — extending the device experience to mobile.

**What this means for Zerocap x Spacezero:**
The Tamagotchi Plaza <-> Uni model is the closest analog to the Zerocap <-> Spacezero relationship: a portable device (mobile app) where you raise your pet, connected to a richer game world (console/browser) where that pet unlocks exclusive capabilities. The key lesson is that exclusivity creates motivation for cross-platform adoption — when each platform offers something the other cannot, users are pulled between both.

### 1.3 Neopets: Web <-> Mobile Companion App

Neopets launched a mobile Companion App globally on January 29, 2026 — a truncated version of Neopets.com accessible on iOS and Android.

**How the cross-platform link works:**
- **NeoPass** serves as the unified identity system, synchronizing user progress across all Neopets platforms (classic web, mobile games, community projects).
- Players can sync scores with their main Neopets account and earn Neopoints while playing on mobile.
- Account linking from standalone mobile apps allows players to earn rewards that carry over to the main web site — creating what Neopets calls "an interconnected system where in-game progress yields rewards on the main site."
- The app explicitly functions as a bridge: mobile-earned items, Neopoints, and achievements flow back to the web experience.

**What this means for Zerocap x Spacezero:**
Neopets validates the web-to-mobile bridge pattern directly. The NeoPass approach (unified identity, bidirectional rewards) is exactly the right model. The critical insight is that Neopets treats mobile as a feeder into the main web experience — which mirrors how Zerocap (mobile) feeds companions into Spacezero (browser).

### 1.4 Digimon Vital Bracelet: Wearable <-> Mobile App

The Digimon Vital Bracelet represents a physical-digital companion bridge.

**How it works:**
- The wearable device raises Digimon through real-world activity (steps, heart rate).
- The Vital Bracelet Lab app connects via NFC to transfer Digimon between device and phone.
- The app provides storage (the device holds only 2 Digimon at a time), item management, healing, evolution acceleration, and online battles.
- Weekly battle rankings and monthly raid bosses created social engagement layers beyond the solo pet-raising loop.

**What went wrong:**
The Vital Bracelet Arena App ended service in 2024, shutting down online connectivity entirely. The NFC-only transfer method created friction (no iPads, requiring specific phone hardware). The wearable-to-app pipeline was too narrow — only storage and battles, not a rich second world.

**Lesson for Zerocap x Spacezero:**
The companion needs a meaningful life on both platforms, not just storage on one and gameplay on the other. When the companion's second-platform presence feels like inventory management rather than a living experience, users don't bother crossing over.

### 1.5 Niantic's Peridot: Mobile AR <-> Snap Spectacles (AR Glasses)

Peridot is Niantic's AI-powered virtual pet game (launched May 2023), and it recently expanded to Snap Spectacles as "Peridot Beyond."

**Cross-platform approach:**
- Each Peridot ("Dot") has unique DNA — genetically one-of-a-kind, procedurally generated.
- The Dot uses AR to interact with real-world surfaces, recognizing terrain and objects.
- Peridot Beyond on Spectacles syncs with the mobile game — progress in Beyond earns rewards in mobile, creating bidirectional value.
- Spectacles enable multiplayer AR walks where friends interact with each other's Dots in shared physical space.

**What this means for Zerocap x Spacezero:**
Peridot is the closest existing product to what Zerocap aims to be (AR companion with unique identity), and its expansion to Spectacles mirrors the "companion lives in multiple places" concept. The sync model (progress in one platform earns rewards in the other) is clean and intuitive. However, Peridot's reach is limited by Spectacles' small install base. Zerocap's advantage is that Spacezero is browser-native — zero friction to access the second platform.

### 1.6 Replika: AI Companion Across Devices

Replika (launched 2017) is the longest-running AI companion app, available on iOS, Android, desktop (via web and emulators), and Meta Quest VR.

**Cross-platform model:**
- Cloud-based conversation history and memory — the companion's personality and relationship persist across all devices.
- The same Replika appears visually on every platform, with platform-appropriate rendering (2D on mobile, 3D avatar in VR).
- Proactive check-ins, journaling, and activities all sync through the cloud backend.

**What this means for Zerocap x Spacezero:**
Replika validates that users form strong emotional bonds with AI companions and expect that bond to persist across surfaces. The identity must feel continuous — same personality, same memories, same visual identity. Replika's weakness is that the companion does the same thing everywhere (conversation). Zerocap's opportunity is that the companion does different things on each platform (camera-based generation on mobile, terrain modification in browser), making each platform feel essential rather than redundant.

### 1.7 Fortnite / Genshin Impact: Cross-Progression Gold Standards

While not companion systems, these are the technical benchmarks for cross-platform state sync.

**Fortnite:**
- Epic Games account is the unified identity layer. Match history, Battle Pass level, cosmetic unlocks all tied to this account.
- Switching platforms pulls latest data from Epic's servers automatically — no manual upload/download.
- V-Bucks purchased remain on the purchasing platform, but items bought with them are available everywhere.
- Account linking supports PlayStation, Xbox, Steam, Switch, mobile, and PC.

**Genshin Impact:**
- HoYoverse account email is the identity key. Cloud-based data storage syncs character data, quest progress, inventory, and currency.
- Server-authoritative model — most recent server data wins in conflicts.
- Changes appear across platforms within minutes. Auto-save on all platforms.
- Progress is locked to the server region selected at account creation (cannot transfer between regions).

**What this means for Zerocap x Spacezero:**
Server-authoritative, cloud-synced state is the proven pattern. The companion's state should live on the server, with both Zerocap and Spacezero as clients that read/write to the same source of truth. Genshin's region-lock is a cautionary tale — avoid creating arbitrary boundaries that fragment the experience.

---

## 2. Technical Architecture Considerations

### 2.1 The Companion State Model

The companion needs a unified data model that both platforms can read from and write to.

**Core companion state (synced globally):**
```
Companion {
  id: UUID
  name: String
  source_object: String          // what real-world object it was created from
  creation_timestamp: DateTime
  visual_identity: {
    base_mesh: VoxelData         // the 3D representation
    texture_map: ImageRef        // AI-generated texture
    color_palette: [Color]
    animations: [AnimationRef]
  }
  personality: {
    traits: [Trait]              // derived from source object + AI generation
    mood: Float                  // current emotional state
    affection_level: Float       // bond with player
    memory: [MemoryEntry]        // significant interactions
  }
  stats: {
    age: Duration
    total_interactions: Int
    zerocap_interactions: Int
    spacezero_interactions: Int
  }
}
```

**Platform-specific state (stored separately but linked):**
```
ZerocapState {
  companion_id: UUID
  discovered_objects: [ObjectRef]
  photo_history: [PhotoRef]
  mobile_achievements: [Achievement]
}

SpacezeroState {
  companion_id: UUID
  terrain_modifications: [ModificationLog]
  placed_items: [ItemRef]
  world_achievements: [Achievement]
  current_world_id: UUID
}
```

### 2.2 Sync Architecture: Real-Time vs Async

**Recommended: Async with near-real-time updates (event-driven)**

The Zerocap <-> Spacezero relationship does not require real-time synchronization. The user is on one platform at a time (mobile phone or browser). The architecture should be:

1. **Server-authoritative state** — the companion's canonical state lives in the cloud (Supabase/PostgreSQL + object storage for assets).
2. **Event-driven updates** — when a user performs a meaningful action on either platform (creates a new companion, levels up, modifies terrain), the client writes the event to the server. The other platform pulls updates on next session start.
3. **Optimistic local state** — each client maintains a local cache of the companion state for responsiveness. Write to server, update locally, reconcile on next sync.
4. **Conflict resolution** — last-write-wins for simple scalar values (mood, affection level). Append-only for additive data (memories, terrain modifications, achievements). This avoids the complexity of CRDTs while handling the actual usage pattern (one platform at a time).

**Why not real-time WebSocket sync:**
- Users are not simultaneously on Zerocap and Spacezero (phone + browser at the same time is an edge case, not the primary flow).
- Real-time sync adds infrastructure cost and complexity disproportionate to the benefit.
- The "wow" moment is opening Spacezero and seeing your companion already there with everything you did in Zerocap reflected — not watching it update live.

**Sync timing:**
- On session start: pull latest companion state from server.
- On significant action: push update to server immediately.
- Background sync: periodic heartbeat every 60 seconds during active sessions.
- On session end: final state push.

### 2.3 Account System and Identity

**Recommended approach: Platform-agnostic identity with social login.**

Based on industry best practices and the Fortnite/Genshin model:

1. **Spacezero Account** as the canonical identity — email + password or social login (Google, Apple, Discord).
2. **Zerocap links to Spacezero Account** — on first launch of Zerocap, prompt to "Connect to Spacezero" using the same credentials. If the user doesn't have a Spacezero account, create one transparently.
3. **OAuth 2.0 / OpenID Connect** — industry standard, well-supported by all platforms.
4. **Social login priority:** Apple Sign-In (required for iOS apps), Google (largest identity provider), Discord (gaming community alignment).
5. **Guest mode with upgrade path** — allow users to start Zerocap without an account (reducing onboarding friction), then prompt to create/link an account when they first want to see their companion in Spacezero. This turns the cross-platform bridge into a natural account creation incentive.

**Build vs buy decision:**
For a 4-person team, use a pre-built auth service (Supabase Auth, Firebase Auth, or Clerk). Building custom OAuth flows for each identity provider is not a good use of engineering time at this stage. Supabase Auth is the natural choice given the existing stack.

### 2.4 Asset Pipeline: Camera to Voxel

The most technically challenging piece is converting a Zerocap-generated companion (from a 2D photo) into a voxel representation that works in Spacezero's Hermite dual-contouring engine.

**Pipeline:**
1. **Zerocap captures photo** → AI generates companion design (2D concept art + personality traits).
2. **Server-side 3D generation** → the 2D design is converted to a 3D voxel model compatible with Spacezero's engine. This can be done via:
   - AI-assisted 3D generation (image-to-3D models like TripoSR, InstantMesh, or similar).
   - Voxelization of the generated 3D mesh into Hermite data that the dual-contouring engine can render.
3. **Asset storage** → the voxel model, texture maps, and animation data are stored in cloud object storage (S3/Supabase Storage), referenced by the companion's UUID.
4. **Spacezero loads on demand** → when a player enters a Spacezero world, the companion's voxel data is fetched and rendered. This can be cached locally after first load.

**Key constraint:** The voxel representation must look recognizably like the Zerocap companion. Visual continuity across platforms is the foundation of the "same pet, two worlds" illusion.

---

## 3. UX Design for Cross-Platform Companions

### 3.1 Making Users Understand "My Pet Is in Both Places"

The single most important UX challenge is making the cross-platform link feel intuitive, not confusing.

**Principles:**

1. **Visual continuity is non-negotiable.** The companion must look like the same creature on both platforms. Same colors, same proportions (adapted to voxel style), same distinctive features. If a user created a companion from a red coffee mug, it should be recognizably "mug-shaped and red" in both places.

2. **Name persistence.** The companion's name, chosen by the user, must appear consistently across platforms. This is the simplest and most powerful identity signal.

3. **Personality persistence.** If the companion is playful in Zerocap, it should exhibit playful behavior in Spacezero (bouncing around, approaching objects curiously). Behavioral continuity reinforces the sense of a single living entity.

4. **Cross-platform memory.** The companion should reference experiences from the other platform. In Spacezero: "Luna seems excited — she discovered three new objects in Zerocap today!" In Zerocap: "Luna modified 12 blocks of terrain in Spacezero while you were away!"

5. **Transition moments.** When the companion first appears in Spacezero after being created in Zerocap, there should be a distinct "arrival" animation — the companion materializing, looking around the voxel world with wonder. This moment cements the cross-platform narrative.

### 3.2 Platform-Specific Roles

Each platform should give the companion a distinct purpose that motivates crossing over.

| Dimension | Zerocap (iOS) | Spacezero (Browser) |
|---|---|---|
| **Core action** | Discover and create companions from real-world objects | Deploy companions to modify terrain, generate items, build |
| **Companion role** | Living pet you nurture and bond with | Active agent that shapes your world |
| **Unique value** | Only way to create new companions | Only way to see companions in a shared 3D world |
| **Interaction style** | Intimate, personal, camera-based | Creative, spatial, building-based |
| **Social dimension** | Share companion creation moments (TikTok/Instagram) | Show off your companion's builds to other players |

The key insight: Zerocap is where companions are born. Spacezero is where companions work. Neither platform is complete without the other.

### 3.3 Cross-Platform Nudges

Gentle, contextual prompts that encourage platform switching without being annoying.

**In Zerocap:**
- After creating a companion: "See [Name] in your Spacezero world → [link]"
- After a companion levels up: "[Name] unlocked a new terrain ability! Try it in Spacezero."
- Daily: "[Name] misses their Spacezero world. Visit?" (only if the user hasn't opened Spacezero in 3+ days)

**In Spacezero:**
- When a companion could be more effective: "[Name] could learn new abilities. Take them exploring in Zerocap."
- When a player has no companions: "Your world is waiting for a companion. Create one in Zerocap → [App Store link]"
- When seeing another player's companion: "Cool companion! Create yours in Zerocap."

**Rules for nudges:**
- Maximum one cross-platform nudge per session.
- Never block gameplay with a nudge.
- Always frame as opportunity, not obligation.
- Track nudge-to-conversion rate and kill underperforming ones.

---

## 4. The "Companion as Bridge" Concept

### 4.1 How the Pet Drives Traffic Between Platforms

The companion is not just a feature — it is the connective tissue between two products. Every interaction with the companion creates a reason to visit the other platform.

**Zerocap → Spacezero traffic:**
- "I just created this cool companion from my shoe — I want to see it in 3D in my world."
- "My companion leveled up and unlocked terrain modification — I want to try it."
- "I collected 5 companions — I want to see them all together in my Spacezero world."

**Spacezero → Zerocap traffic:**
- "I want a companion that can do [specific terrain ability] — I need to create one in Zerocap."
- "I saw someone else's companion and it was amazing — I want to make my own."
- "My companion's abilities are maxed out in Spacezero — back to Zerocap to discover new objects and evolve."

**The flywheel:**
```
Create companion (Zerocap)
    → See companion in world (Spacezero)
        → Companion needs more abilities (Spacezero)
            → Discover objects to level up (Zerocap)
                → Companion unlocks new terrain powers (Spacezero)
                    → Build something amazing (Spacezero)
                        → Share build (social media)
                            → New user downloads Zerocap
                                → Cycle repeats
```

### 4.2 Mobile-to-Web User Flow Design

**Flow 1: Zerocap user discovers Spacezero**
1. User creates companion in Zerocap.
2. After 3rd companion creation (proving engagement), show a contextual prompt: "Your companions have a home — a world you can build. Open Spacezero?"
3. Tapping the prompt opens a deep link to Spacezero in the browser (Safari/Chrome).
4. If no Spacezero account exists, auto-create one using the same Apple/Google credentials from Zerocap. Zero friction.
5. The companion appears in the Spacezero world with an arrival animation.
6. A brief tutorial shows how the companion can modify terrain.
7. The user is now a cross-platform user.

**Flow 2: Spacezero user discovers Zerocap**
1. User is playing Spacezero in the browser.
2. They see another player's companion doing something cool, or encounter an empty "companion dock" in their world.
3. A prompt: "Create your companion in Zerocap" with an App Store link (or QR code on desktop).
4. User installs Zerocap, signs in with same account.
5. First companion created in Zerocap appears in their Spacezero world on next session.

**Flow 3: Social media to dual adoption**
1. User sees a TikTok: "I turned my Starbucks cup into a pet and it built a castle in my game."
2. The video links to Zerocap (App Store) first — lowest friction, highest novelty.
3. After creating their first companion, the Spacezero bridge is introduced.
4. Both products acquired from a single TikTok funnel.

### 4.3 Web-to-App Funnel Economics

Research shows the cost to capture a user on the web is 82% less than acquiring through a paid app install campaign, and web-to-app funnels can reduce cost per trial by up to 60%. For Zerocap x Spacezero:

- Spacezero (browser) can serve as a free acquisition channel for Zerocap. Users who discover Spacezero organically (shareable URL, no download) can be funneled to Zerocap for companion creation.
- Zerocap (iOS) serves as a high-intent acquisition channel for Spacezero. Users who are already creating companions have demonstrated engagement and are primed for the richer sandbox experience.
- The bidirectional funnel means each product's marketing spend benefits both products.

---

## 5. What Makes Cross-Platform Feel Magical vs Confusing

### 5.1 The Magic Formula

Cross-platform experiences feel magical when:

1. **The transition is invisible.** You don't "transfer" your companion — it's already there when you arrive. Genshin Impact and Fortnite both achieve this: log in on a new device and everything is just... there. No manual sync, no import/export, no waiting.

2. **The companion remembers.** If you bonded with your companion in Zerocap this morning, it should react to you in Spacezero this evening. Memory that crosses platform boundaries is the single most powerful signal that "this is the same being."

3. **Each platform is best at something different.** The companion should be better to interact with in Zerocap (intimate, personal, camera-powered) and more impactful in Spacezero (building, modifying, creating). If one platform is strictly superior, there is no reason to cross over.

4. **There's a shared narrative.** The companion has a story that spans both platforms — it was born from a coffee mug, it grew up in your pocket, it built its first wall in your Spacezero world, it discovered a new ability when you showed it a flower. The narrative thread ties the platforms together.

5. **Social proof crosses platforms.** When you see another player's companion in Spacezero and it is impressive, the immediate question — "Where did they get that?" — leads you to Zerocap. The companion itself is a walking advertisement for the other platform.

### 5.2 The Confusion Formula

Cross-platform experiences feel confusing when:

1. **State is inconsistent.** The companion looks different, acts different, or has different stats on each platform. This breaks the "same being" illusion immediately.

2. **Transfers require manual work.** Any friction in the cross-platform flow (export/import, codes to enter, waiting periods) makes users feel like they are managing a system rather than living with a companion.

3. **Platform-specific restrictions are arbitrary.** "You can't use this companion in Spacezero because it was created on a Tuesday" — any restriction that doesn't have an obvious, intuitive reason creates frustration. Pokemon HOME's one-way transfer restriction is tolerated because Pokemon has decades of franchise equity. A new product does not have that luxury.

4. **The companion feels like a gimmick on one platform.** If the companion is the core experience in Zerocap but just a decorative avatar in Spacezero, the cross-platform link feels hollow. The companion must be functionally meaningful everywhere it appears.

5. **Notifications are out of sync.** If Zerocap says "Your companion is waiting in Spacezero!" but the companion is not actually there when you open Spacezero (due to sync delay), trust is broken.

---

## 6. Retention Benefits of Multi-Surface Presence

### 6.1 The Data

Cross-platform engagement statistics paint a clear picture:

| Metric | Single-Platform | Cross-Platform | Delta |
|---|---|---|---|
| 30-day retention | Baseline | +25% higher | +25% |
| Daily return rate | Baseline | +31% more likely | +31% |
| Time spent gaming | Baseline | +40% (tri-platform) | +40% |
| Player lifetime value | Baseline | +35% with cross-progression | +35% |
| Revenue impact | Baseline | +20-40% with cross-platform | +20-40% |

**Source context:** 72% of global gamers already play on 2+ platforms. 61% participate in cross-platform play. Games with cross-progression and cloud saves see 45% higher engagement retention within the first 30 days. The cross-platform gaming market is $12.5B in 2025, projected to reach $21.3B by 2030 (19% CAGR).

### 6.2 Why More Touchpoints = More Daily Engagement

The mechanism is simple: each platform represents a different context of use.

- **Zerocap** fits into mobile-native contexts: commute, waiting in line, walking around, meal breaks. The camera interaction is inherently mobile.
- **Spacezero** fits into sit-down contexts: desk at home, laptop, study break. Browser gaming is a focused, lean-forward experience.

By having the companion present in both contexts, the product occupies more moments in the user's day. A user who opens Zerocap on the bus and Spacezero at home has two daily touchpoints instead of one. Research from Google shows that customers who engage on more than one channel have a 30% higher lifetime value.

### 6.3 The Emotional Compounding Effect

Multi-surface presence creates a psychological effect that goes beyond touchpoint math: the companion feels more real when it exists in more places. A Tamagotchi on your phone is a toy. A companion that greets you on your phone in the morning and has built something new in your world by the time you get home starts to feel like a persistent entity. This is the "ambient companion" effect — the feeling that your pet is living its life even when you're not watching.

This emotional resonance directly drives retention. Users are less likely to churn from a product where they have an emotional attachment that spans their daily routine.

---

## 7. Challenges and Pitfalls

### 7.1 Fragmented Experience

**Risk:** Users feel like they're managing two separate apps instead of one connected experience.

**Mitigation:**
- Unified visual language (same color palette, typography principles, UI patterns for companion interactions).
- Companion state is always consistent — no divergent data.
- Cross-platform awareness is built into both products ("Your companion did X in [other platform] today").
- Design system with shared tokens for companion UI elements.

### 7.2 Sync Issues

**Risk:** Data conflicts, stale state, or lost progress create frustration.

**Mitigation:**
- Server-authoritative model — the server is always the source of truth.
- Optimistic UI with graceful reconciliation — show the user what they expect, correct silently if needed.
- Last-write-wins for scalar values, append-only for log data.
- Clear error states: "Couldn't sync with Spacezero. Your changes are saved locally and will sync when you're online."
- Offline-capable local state with queue-based sync on reconnection.

### 7.3 Platform-Specific Expectations

**Risk:** iOS users expect polished native interactions. Browser users expect instant load times. Failing either expectation reflects poorly on the whole product.

**Mitigation:**
- Zerocap must feel like a first-class iOS app (native Swift, not a web wrapper).
- Spacezero must load fast in the browser (the "no download" advantage is nullified if it takes 30 seconds to load).
- Companion interactions should feel native to each platform — touch gestures on iOS, mouse/keyboard in browser.

### 7.4 The "Weakest Link" Problem

**Risk:** If one platform is significantly less polished or less engaging, it drags down perception of the entire ecosystem. Users judge both products as a package once they're linked.

**Mitigation:**
- Don't launch the cross-platform link until both platforms are independently compelling.
- Each platform must have a standalone value proposition that works even without the other.
- The cross-platform companion is an enhancement, not a crutch.

### 7.5 Account Fragmentation

**Risk:** Users create separate accounts on each platform, then can't link their companion.

**Mitigation:**
- Default to social login (Apple Sign-In, Google) which naturally creates the same account on both platforms.
- Account merge capability: if a user accidentally creates separate accounts, allow them to merge (link one to the other, designate a primary).
- Guest-to-account upgrade: if a user starts as a guest on either platform, make the upgrade path clear before they create a companion they can't later sync.

### 7.6 COPPA and Privacy Compliance

Given that Zerocap's demographic includes users under 13 (the virtual pet audience skews young):

**Key requirements (2025 COPPA amendments, effective June 2025, compliance by April 2026):**
- Separate verifiable parental consent required for non-integral data uses (behavioral advertising, profiling, AI training).
- Biometric identifiers now fall under COPPA (fingerprints, voiceprints, facial templates — relevant if Zerocap uses any camera-based biometric features).
- Granular disclosures about third-party data recipients.
- Heightened data security and retention obligations.
- HoYoverse (Genshin Impact) was subject to FTC enforcement action in January 2025 — a cautionary precedent for any game with young users and cross-platform data flows.

**Mitigation:**
- Age gate at account creation. Under-13 users require parental consent for cross-platform data sync.
- Camera data (photos used to create companions) must be processed and discarded — do not store the original photos on the server (store only the generated companion assets).
- Cross-platform data flow must be clearly disclosed in privacy policy.
- Data retention policy: automatically purge companion creation logs older than [X] months.

---

## 8. Launch Sequencing: Simultaneous vs Stagger

### 8.1 The Case for Staggered Launch (Recommended)

**Phase 1: Launch Zerocap standalone** (current state)
- Ship Zerocap as an independent iOS app with its own value proposition (AI pet creation, care, sharing).
- Build an audience, validate the core loop, iterate on AI quality.
- Users create companions without knowing about Spacezero yet.

**Phase 2: Launch Spacezero standalone**
- Ship Spacezero as a browser-based voxel sandbox with its own value proposition (build, create, share).
- Companions do not exist in Spacezero yet — the world is available, but the differentiator is the engine (smooth voxels, browser-native).

**Phase 3: Launch the cross-platform bridge**
- "Your Zerocap companions now live in Spacezero." This becomes a major update moment — a product event that generates press, social media content, and re-engagement.
- Existing Zerocap users discover their companions have been "waiting" in a Spacezero world.
- Existing Spacezero users discover they can create companions in Zerocap.
- The bridge launch is a marketing moment in itself — three launches from two products.

**Why stagger:**
- Staggered launches create multiple press moments. Each launch generates coverage independently, and the bridge launch generates a third wave.
- Each platform can be validated independently before introducing cross-platform complexity.
- The engineering team can focus on one platform at a time.
- If one platform struggles, the other is not dragged down.
- The "bridge reveal" creates a genuine surprise moment for existing users.

Industry data supports this: staggered launches "net yourself as many launches as you have platforms" and "spread the revenue of your game out over a longer period of time."

### 8.2 The Case for Simultaneous Launch

- Simultaneous launches maximize cultural impact — "hitting a cultural tipping point when your game is everywhere."
- Reduces PR/marketing overhead to a single campaign.
- The Crashlands case study showed a simultaneous launch across Steam, App Store, and Google Play resulted in Editor's Choice on the App Store and a Steam feature over launch weekend.

**Why this is not recommended for Zerocap x Spacezero:**
- The two products are genuinely different (iOS native app vs browser game). Simultaneous launch of two distinct products doubles QA, support, and marketing effort.
- A 4-person team cannot manage two product launches simultaneously without quality suffering.
- The cross-platform bridge is more powerful as a "reveal" than as a launch-day feature (where it gets lost in the noise of everything else).

### 8.3 Recommended Sequence

| Phase | Timing | Action | Marketing Moment |
|---|---|---|---|
| 1 | Now | Zerocap iOS launch + TikTok GTM | "AI Tamagotchi — turn anything into a pet" |
| 2 | 4-6 weeks later | Spacezero browser launch | "Minecraft in your browser — smooth voxels, no download" |
| 3 | 2-4 weeks after Phase 2 | Cross-platform bridge | "Your Zerocap pet now lives in Spacezero" |
| 4 | Ongoing | Deepen integration | New companion abilities, cross-platform events |

---

## 9. The Narrative Advantage: "Your Companion Lives Everywhere"

### 9.1 Positioning Statement

> "Raise your companion in the real world. Watch it shape a new one."

This positions the cross-platform link as the core story, not a feature. Alternative framings:

- "Born from your camera. Lives in your world."
- "The first AI companion that crosses between reality and a virtual world."
- "Point your phone at anything. Watch it come alive — in your pocket and in your world."

### 9.2 Why This Positioning Wins

**Against Minecraft:** Minecraft has no companion system. Mobs exist, but they are not created by you, not persistent, and not linked to a mobile app. The companion is something Minecraft fundamentally cannot replicate without building an entirely new product.

**Against Tamagotchi:** Tamagotchi companions do not exist in a sandbox world. The Tamagotchi Plaza connection is a step in this direction, but it's a curated Nintendo Switch game, not an open voxel sandbox. And it requires buying a Tamagotchi Uni device ($60+).

**Against Pokemon GO / Pokopia:** Pokemon spans mobile and console/Switch, but requires purchasing separate games and a HOME subscription for advanced features. Zerocap + Spacezero is free-to-start on both platforms, and the companion creation mechanic (camera → AI pet) is novel.

**Against AI companions (Replika, Character.AI):** These companions exist only as chatbots. They have no spatial presence, no world they inhabit, no agency beyond conversation. A companion that modifies terrain and builds things is categorically different.

### 9.3 The "Living Everywhere" Story Arc

The narrative deepens over time:
1. **Birth:** User points camera at a coffee mug. AI creates a mug-creature companion.
2. **Growth:** Companion develops personality in Zerocap through daily interactions.
3. **Migration:** Companion appears in user's Spacezero world for the first time (the "wow" moment).
4. **Agency:** Companion modifies terrain, builds structures, generates items in Spacezero.
5. **Evolution:** Companion gains new abilities by discovering more objects in Zerocap.
6. **Social:** Other players encounter your companion in shared Spacezero worlds.
7. **Legacy:** Companion's builds persist in the world even when you're offline — evidence that it "lives" there.

This arc is impossible in any single-platform product. The cross-platform nature is not a technical convenience — it is the narrative.

---

## 10. Account and Identity Management

### 10.1 Architecture

```
                    ┌──────────────────┐
                    │  Spacezero Auth   │
                    │  (Supabase Auth)  │
                    │                  │
                    │  ┌────────────┐  │
                    │  │  User ID   │  │
                    │  │  (UUID)    │  │
                    │  └─────┬──────┘  │
                    │        │         │
                    │  ┌─────┴──────┐  │
                    │  │ Linked     │  │
                    │  │ Identities │  │
                    │  │            │  │
                    │  │ • Apple ID │  │
                    │  │ • Google   │  │
                    │  │ • Discord  │  │
                    │  │ • Email    │  │
                    │  └────────────┘  │
                    └────────┬─────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
         ┌──────┴─────┐  ┌──┴─────────┐  │
         │  Zerocap    │  │  Spacezero │  │
         │  iOS App    │  │  Browser   │  │
         │             │  │            │  │
         │  Session    │  │  Session   │  │
         │  Token      │  │  Token     │  │
         └─────────────┘  └────────────┘  │
                                          │
                                   Future platforms
                                   (Android, desktop app)
```

### 10.2 Identity Linking Flow

1. **User creates account on Platform A** (whichever they encounter first). Receives a Spacezero Account UUID.
2. **User opens Platform B.** Signs in with the same social login (Apple/Google). The auth system recognizes the linked identity and associates the same UUID.
3. **If signed in with a different method on Platform B:** prompt to link accounts. "We found companions on another account. Link them?"
4. **Guest upgrade:** guest users on either platform are prompted to create a full account before their first cross-platform action. "Sign in to take [companion name] to Spacezero."

### 10.3 Key Decisions

- **Single identity, not separate accounts.** One user = one UUID = one companion collection. Never create a world where the same person has different identities on each platform.
- **Social login as default, email as fallback.** Social login reduces friction and naturally produces consistent identity across platforms.
- **No platform lock-in.** A user who starts on Zerocap should not feel "trapped" on iOS. If Android ships later, their account and companions must transfer seamlessly.
- **Display name is cross-platform.** Whatever username you choose appears in both Zerocap and Spacezero.

---

## 11. Data and Privacy Considerations

### 11.1 What Data Crosses Platforms

| Data Type | Crosses Platforms? | Storage | Sensitivity |
|---|---|---|---|
| Companion identity (name, visual, personality) | Yes | Server | Low |
| Companion stats (level, interactions) | Yes | Server | Low |
| Original photos (camera captures) | No — processed on-device, only generated assets stored | Device only | High |
| User account (email, social ID) | Yes | Auth server | Medium |
| Zerocap interaction history | Metadata only (counts, timestamps) | Server | Low |
| Spacezero world data | Yes (companion's modifications synced) | Server | Low |
| Location data | No — not collected | N/A | High |
| Device identifiers | Platform-specific, not shared cross-platform | Platform only | Medium |

### 11.2 Privacy-by-Design Principles

1. **Photo data never leaves the device.** The camera capture is processed locally (or via a secure API call), and only the generated companion assets (voxel model, texture, traits) are stored server-side. The original photo is not uploaded or retained.

2. **Minimal cross-platform data sharing.** Only companion state and user identity cross the platform boundary. Zerocap does not know what the user built in Spacezero, and Spacezero does not know what photos the user took in Zerocap. Each platform knows only what it needs.

3. **No behavioral advertising with companion data.** The companion's personality traits, interaction patterns, and cross-platform usage data must not be used for ad targeting. This is both a COPPA requirement (if under-13 users are present) and a trust requirement.

4. **Data portability.** Users should be able to export their companion data (visual model, stats, memories) in a standard format. This builds trust and may become a regulatory requirement (GDPR data portability).

5. **Deletion cascades.** If a user deletes their account, all companion data on both platforms and the server must be purged. No orphaned data.

6. **Transparent data flow.** The privacy policy must clearly explain: "When you create a companion in Zerocap, its visual design and personality are stored on our servers so it can appear in Spacezero. Your original photos are not stored."

### 11.3 COPPA Compliance Checklist

- [ ] Age gate at account creation
- [ ] Parental consent mechanism for under-13 users
- [ ] No persistent identifiers shared with third-party SDKs without consent
- [ ] Camera data (if biometric-adjacent) handled per COPPA 2025 biometric rules
- [ ] Data retention policy documented and enforced
- [ ] Privacy policy specifically addresses cross-platform data flow
- [ ] Ability to delete all data across both platforms from a single request

---

## 12. Competitive Landscape Summary

| Product | Platforms | Companion Type | Cross-Platform Sync | Creation Mechanic | Open World |
|---|---|---|---|---|---|
| **Zerocap x Spacezero** | iOS + Browser | AI-generated from photos | Bidirectional, cloud-synced | Camera → AI pet | Voxel sandbox |
| Pokemon GO + HOME | Mobile + Console | Franchise creatures | One-way (GO → HOME → console) | Catch in AR | No (instanced battles) |
| Tamagotchi Uni + Plaza | Device + Switch | Pre-designed creatures | Bidirectional rewards | Egg hatching | No (curated game) |
| Neopets Web + App | Web + Mobile | Pre-designed creatures | Bidirectional via NeoPass | Adoption | No (minigames/site) |
| Peridot | Mobile + Spectacles | Procedurally generated | Progress syncs between platforms | AR discovery | No (AR overlay) |
| Replika | Mobile + Web + VR | AI chatbot avatar | Cloud-synced conversation | Text/voice | No (chat interface) |
| Digimon Vital Bracelet | Wearable + Mobile | Franchise creatures | NFC transfer | Activity-based evolution | No (battles only) |

**Zerocap x Spacezero's unique position:** The only system where (a) the companion is created by the user from real-world objects, (b) the companion has agency in an open sandbox world, and (c) both platforms are free-to-access with zero-friction entry (iOS app + browser game).

---

## 13. Recommendations

### Immediate (Phase 1 — Zerocap standalone)
1. Design the companion data model with cross-platform sync in mind from day one, even though the bridge isn't live yet. Store companion state in the cloud from the start.
2. Implement Spacezero Account auth in Zerocap now — even if users don't know what "Spacezero" is yet, their account is ready.
3. Build the 2D-to-voxel asset pipeline as a background workstream. This is the highest-risk technical component and needs early prototyping.

### Near-Term (Phase 2 — Spacezero launch)
4. Ship Spacezero with a "companion dock" — an empty space in the world that clearly signals "something goes here." This creates curiosity and primes users for the bridge.
5. Allow Spacezero users to see other players' companions before they have their own. Social proof drives Zerocap adoption.

### Bridge Launch (Phase 3)
6. The bridge launch should be a product event: blog post, TikTok content ("watch what happens when my Zerocap pet enters my Spacezero world"), push notification to all Zerocap users.
7. First-time companion arrival in Spacezero must have a polished, delightful animation. This is the "wow" moment that determines whether the cross-platform story lands.
8. Measure cross-platform adoption rate (% of Zerocap users who open Spacezero within 7 days of bridge launch) and companion activation rate (% of Spacezero users who create a companion in Zerocap).

### Ongoing (Phase 4)
9. Cross-platform events: "Companion Festival" where companions earn special abilities by completing challenges across both platforms within a time window.
10. Companion evolution paths that require both platforms — e.g., discovering 10 objects in Zerocap + building 100 blocks in Spacezero unlocks a new companion form.
11. Shareable companion profiles: a URL (spacezero.com/companion/[name]) that shows the companion's full cross-platform history — where it was born, what it has built, its personality. This becomes both a social feature and a marketing asset.

---

## Sources

### Cross-Platform Companion Systems
- [What Is Pokemon HOME and How Does It Work in 2025](https://tldr.mataroa.blog/blog/what-is-pokemon-home-and-how-does-it-work-in-2025/)
- [Pokemon HOME Explained — Nintendo Life](https://www.nintendolife.com/guides/pokemon-home-explained-how-to-transfer-all-pokemon-to-and-from-pokemon-home)
- [How to Transfer Pokemon from GO to HOME — Pokemon Support](https://support.pokemon.com/hc/en-us/articles/360050219032)
- [How To Connect Tamagotchi Uni to Tamagotchi Plaza — The Gamer](https://www.thegamer.com/tamagotchi-plaza-tamagatchi-uni-connect-guide/)
- [Neopets Companion App — Jellyneo](https://www.jellyneo.net/?go=comments&post=15743)
- [Neopets NeoPass Cross-Platform Gateway — GAM3S.GG](https://gam3s.gg/news/neopets-introduces-neopass-seamless-cross-platform-gateway-to-neopia/)
- [Digimon Vital Bracelet Lab — Fandom](https://digimon.fandom.com/wiki/Digimon_Vital_Bracelet_Lab)
- [Peridot Beyond Multiplayer — Niantic](https://www.nianticspatial.com/blog/peridot-beyond-multiplayer)
- [Replika AI Friend — App Store](https://apps.apple.com/us/app/replika-ai-friend/id1158555867)

### Technical Architecture
- [Cross-Platform Synchronization for Seamless Play — Panel Perspective](https://panelperspective.com/en/articles/implementing-cross-platform-synchronization-for-seamless-play)
- [Cross-Platform Authentication for Games — AccelByte](https://accelbyte.io/blog/cross-platform-authentication-for-games-should-you-build-it-or-plug-it-in)
- [Authentication in Gaming — Descope](https://www.descope.com/blog/post/gaming-auth)
- [Cross-Platform Game Accounts — FusionAuth](https://fusionauth.io/articles/gaming-entertainment/cross-platform-game-accounts)
- [Fortnite Cross-Device Sync — Epic Games](https://www.epicgames.com/help/en-US/account-c-202300000001645/linked-accounts-c-202300000001754/)
- [Genshin Impact Cross-Save Guide — The Gamer](https://www.thegamer.com/genshin-impact-cross-save-guide/)

### Retention and Engagement Data
- [Cross-Platform Gaming Adoption Statistics 2025 — IconEra](https://icon-era.com/blog/cross-platform-gaming-adoption-statistics-2025.285/)
- [Cross-Platform Gaming Statistics 2026 — SQ Magazine](https://sqmagazine.co.uk/cross-platform-gaming-statistics/)
- [Gaming App Sessions Rose in 2025 — Adjust / BusinessWire](https://www.businesswire.com/news/home/20260310424022/en/)
- [AI Companion Apps $120M — TechCrunch](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)

### Launch Strategy
- [Notes from an Indie Cross-Platform Launch — Game Developer](https://www.gamedeveloper.com/business/notes-from-an-indie-cross-platform-launch)
- [Cross-Platform Release Strategy — iXie](https://www.ixiegaming.com/blog/building-a-cross-platform-release-strategy/)
- [Rise of Gaming Companion Apps — Hedgehog Lab](https://hedgehoglab.com/rise-of-gaming-companion-apps/)
- [Rise of Companion Apps in Gaming — Genius Crate](https://www.geniuscrate.com/the-rise-of-companion-apps-in-gaming)

### User Flow and Funnels
- [Web2App Funnel Fundamentals — Paddle](https://www.paddle.com/resources/web2app-funnel-fundamentals)
- [Web-to-App Funnel Examples — RevenueCat](https://www.revenuecat.com/blog/growth/web-to-app-funnel-examples/)
- [Cross-Platform Analytics — Amplitude](https://amplitude.com/guides/cross-platform-analytics)
- [Seamless Cross-Platform Strategies — Branch](https://www.branch.io/resources/blog/5-examples-of-seamless-cross-platform-experiences-to-drive-app-growth/)

### Privacy and Compliance
- [COPPA Compliance 2025 — Promise Legal](https://blog.promise.legal/startup-central/coppa-compliance-in-2025-a-practical-guide-for-tech-edtech-and-kids-apps/)
- [Amended COPPA Rule — Loeb & Loeb](https://www.loeb.com/en/insights/publications/2025/05/childrens-online-privacy-in-2025-the-amended-coppa-rule)
- [COPPA in Gaming — Xsolla](https://xsolla.com/blog/parental-controls-and-coppa-compliance-safeguarding-childrens-privacy-in-the-gaming-industry)

### UX Design
- [Cross-Platform UX: Designing Consistency — Medium](https://medium.com/@harsh.mudgal_27075/cross-platform-ux-designing-consistency-across-devices-42ad853c7e15)
- [Cross-Platform Experience Guide — UXPin](https://www.uxpin.com/studio/blog/cross-platform-experience/)
- [How To Approach Cross-Platform UX Design — Komodo Digital](https://www.komododigital.co.uk/insights/how-to-approach-cross-platform-ux-design/)
