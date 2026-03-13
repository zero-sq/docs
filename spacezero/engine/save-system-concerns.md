# Voxel Engine Save System — Technical Concerns

**Date:** 2025-02-25
**From:** Founding Engineer
**Context:** Working on the save system for the voxel engine. The scope of changes is far larger than initially expected — modifications ripple across the entire system, making even local work non-trivial.

---

Chunk data serialization was the biggest initial worry, but it turned out to be just the tip of the iceberg. The following problems all need to be solved together:

## 1. Can we save only LOD 0 chunks?

- LOD chunk loading based on player position has been deprioritized, making the answer unclear.

## 2. What impact does player-position-based LOD chunk loading have?

- Currently, only LOD 0 chunks can be modified due to LOD propagation. But chunks near the player may not be at LOD 0.
- Additionally, when the propagation level difference is 2 or more, meshing breaks.

## 3. Why not allow editing chunks at LOD 1+?

- Editing a chunk requires LOD 0-level source data.
- Source data doesn't exist in memory — it's been optimized away.
- Keeping it in memory contradicts the optimization = performance degrades.
- Using the file system introduces IO bottlenecks and ambiguous save-point criteria for chunks.

## 4. What happens when LOD updates after saving a modified LOD 0 chunk?

- If only source data lives on disk, all source chunks related to that LOD chunk must be loaded for downsampling.
- Source count can reach thousands — massive IO bottleneck.
- Mipmap data also needs to be persisted to disk, not just source data.

## 5. How should mipmap data be stored?

- Mipmaps depend on LOD, so world size and scale also matter.
- After shipping, persistence constraints make updates extremely delicate.
- World size and scale need to be locked down in advance.
- Efficient mipmap storage requires scheduling and a dedicated pipeline.
- Depending on the case, a unified priority scheduler for build/meshing/editing/saving may be necessary.

## 6. Mipmap save scheduling and pipeline

- When a chunk is modified: update the source, then process mipmaps at each relevant LOD level.
- Players may trigger terrain edits very frequently in a short window.
- If every edit triggers heavy save work, it becomes a bottleneck.
- Needs debouncing, deduplication, and priority ordering.
- Currently, a single edit requires ~6 mipmap operations.
- Decision needed: in-memory multi-level downsampling vs. disk-based mipmap patching — profiling required per case.

## 7. World size and scale tuning

- Current settings: size 14, scale 0.5.
- Matching YYC's scale of 0.25 works in theory, but needs thorough case-by-case testing.
- At scale 0.25, the LOD 0 radius halves — which may cause frequent LOD update thrashing.

## 8. LOD propagation logic changes

- Required by issues #2 and #7.
- Depending on the logic, the number of chunks to process may increase — potential performance bottleneck.
- The propagation level difference and maximum chunk count need to be tuned to what the browser can handle.

---

## Additional notes

- The system is complex enough that unforeseen issues are likely to surface.
- AI assistance was attempted but the codebase context is too large — hitting token limits within 3 exchanges. Reviewing AI output also requires deep understanding, and adding the full context to the review scope creates a review spiral.
- **Immediate next step:** align on world size and scale. Ideally this would be tested by walking through the world, but that implementation isn't ready yet. And because of save persistence, data can't be rolled back — so guessing is risky.
