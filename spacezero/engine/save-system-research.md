# Voxel Engine Save System — Research & Recommendations

**Date:** 2025-02-25
**Context:** Response to founding engineer's 8-point technical concern list regarding the voxel engine save/persistence system.

---

## Executive Summary

The core tension — LOD 0 source data is needed for edits but optimized out of memory — is a well-known problem in voxel engines. The established solution is: **save only LOD 0 source to disk, regenerate mipmaps lazily, and use dirty-flagging with debounced writes.** The browser constraint (no raw filesystem) is now largely solved by OPFS. The LOD seam/meshing issue at level difference 2+ has a canonical solution: the Transvoxel algorithm.

The hardest open decision is **world size and scale** — because it's irreversible after persistence ships. This should be locked down first.

---

## 1. Can we save only LOD 0 chunks?

**Answer: Yes. This is the standard approach.**

Production voxel engines (Minecraft, Voxel Plugin for UE, Godot Voxel Tools) all persist only the highest-resolution source data. Lower LOD levels are derived data — they're regenerated from source on load or on demand.

**Why this works:**
- LOD 1+ data is a deterministic function of LOD 0 source. Saving it is redundant.
- Mipmap regeneration cost is paid once at load time, not continuously.
- Disk footprint stays minimal — only source truth is stored.

**Recommendation:** Save LOD 0 only. Regenerate mipmap hierarchy on load. Cache mipmaps in memory once computed.

---

## 2. Player-position-based LOD chunk loading impact

**The problem:** If chunks near the player aren't at LOD 0, the player can't edit them. And LOD propagation with a level difference of 2+ breaks meshing.

**Industry standard: enforce a maximum LOD difference of 1 between adjacent chunks.** This is a hard constraint in nearly every LOD voxel system. The Transvoxel algorithm (Eric Lengyel, 2009) — the canonical solution for LOD seam artifacts — is specifically designed for boundaries where the resolution differs by exactly 2x (one LOD level). It does not handle 4x or higher differences.

**Practical implication:**
- The LOD propagation logic *must* enforce max difference of 1 between neighbors.
- Chunks near the player should always be forced to LOD 0 within edit radius.
- This means player-position-based LOD loading isn't just a "nice to have" — it's a prerequisite for both editing and correct meshing.

**Recommendation:** Prioritize implementing player-position-based LOD loading. The edit system and the meshing system both depend on it. Force LOD 0 within a configurable edit radius around the player.

---

## 3. Why not allow editing LOD 1+ chunks?

**Answer: Don't. The engineer's analysis is correct.**

Editing requires LOD 0 source data. If it's not in memory:
- **Load from disk on demand** — this is the only viable path, but it introduces IO latency.
- **Keep everything in memory** — defeats the purpose of LOD optimization.
- **Edit at lower resolution** — produces artifacts and data inconsistency when LOD 0 source is later loaded.

**What other engines do:** They load the full-resolution chunk into memory before allowing edits. Minecraft loads 16x16x256 columns fully. Voxel Plugin for UE loads LOD 0 data into an edit buffer on demand.

**Recommendation:** When the player approaches edit range, preload LOD 0 source data for nearby chunks asynchronously. This amortizes the IO cost over time rather than hitting it at the moment of edit. Think of it as "LOD 0 prefetching within edit radius."

---

## 4. LOD update after saving a modified LOD 0 chunk

**The problem:** If LOD updates and the mipmap needs regeneration, thousands of source chunks may need to be read from disk.

**Solution: Incremental mipmap updates, not full regeneration.**

When a single LOD 0 chunk is modified, you don't need to reload all sources for the parent mipmap. You only need to update the *contribution of that one chunk* to each ancestor in the mipmap hierarchy.

**Technique — bottom-up incremental update:**
1. Modify LOD 0 chunk.
2. Downsample the modified chunk's data into LOD 1 (replacing only its quadrant/octant in the parent).
3. Propagate up: LOD 1 → LOD 2 → ... etc.
4. Each step only touches one octant of the parent, not all 8.

This is exactly how 2D mipmap updates work in GPU texture streaming. The same principle applies to 3D voxel mipmaps.

**IO cost:** Only the modified chunk + its direct ancestor chain. For a tree of depth N, that's N reads/writes, not thousands.

**Recommendation:** Implement incremental mipmap propagation. Never do full mipmap regeneration on edit — only on initial world load.

---

## 5. How should mipmap data be stored?

**Store mipmaps as a cache, not as source of truth.**

- **Source of truth:** LOD 0 chunk files on disk.
- **Mipmap cache:** Separate files per LOD level, treated as disposable/regeneratable.
- **On load:** Check if cached mipmap exists and matches current world version. If yes, use it. If no, regenerate from source.

**World size and scale dependency:**
The mipmap hierarchy structure (depth, branching factor) depends on world size and scale. Changing these after data is persisted means all cached mipmaps are invalidated and must be regenerated.

**This is why world size and scale must be locked down before shipping persistence.**

**Storage format recommendation:**
- One file per chunk per LOD level, named by chunk coordinates + LOD level.
- Use RLE compression — voxel data compresses extremely well with RLE (2x–30x ratios reported in practice).
- Keep a manifest/version file that records world size, scale, and mipmap structure. If any parameter changes, invalidate the cache.

---

## 6. Mipmap save scheduling and pipeline

**The established pattern: dirty-flagging + debounced write-behind.**

### Dirty flagging
When a chunk is edited, mark it dirty. Don't immediately trigger mipmap propagation or disk writes.

### Debouncing
Accumulate edits for a configurable window (e.g., 200–500ms of no new edits, or a maximum batch window of 1–2 seconds). Then process all dirty chunks in one batch.

### Batch mipmap propagation
When the debounce fires:
1. Collect all dirty LOD 0 chunks.
2. For each, do incremental mipmap update (see #4).
3. Deduplicate: if two dirty chunks share a parent in the mipmap tree, the parent only needs to be updated once.
4. Write modified chunks + updated mipmaps to disk.

### Priority scheduling
Use a priority queue:
1. **Highest priority:** Chunks visible to the player that need re-meshing (visual correctness).
2. **Medium priority:** Mipmap propagation for visible LOD levels.
3. **Lowest priority:** Disk persistence (can lag behind in-memory state).

**The ~6 mipmap operations per edit** should be fine with debouncing. If the player makes 20 edits in 500ms, you process them as one batch, not 120 mipmap operations.

### In-memory vs. disk-based mipmap update
- **If the parent mipmap is in memory:** Update in place. Fast.
- **If the parent mipmap is only on disk:** Read → patch → write. Slower, but infrequent if you keep recently-accessed mipmaps cached.
- **Rule of thumb:** Keep mipmaps for visible LOD levels in memory. Only go to disk for LOD levels that are off-screen.

---

## 7. World size and scale tuning

**This is the most critical decision because it's irreversible after persistence ships.**

### Current: size 14, scale 0.5. Proposed: scale 0.25 (matching YYC).

**Halving the scale (0.5 → 0.25) means:**
- Voxels are half the size → double the resolution → 8x the voxel count per volume.
- LOD 0 radius halves → LOD transitions happen closer to the player.
- More frequent LOD updates as the player moves.
- Higher memory pressure for LOD 0 data.

### LOD update thrashing mitigation — Hysteresis

The standard solution for frequent LOD updates is **hysteresis** (also called distance threshold or deadband):

- Don't update LOD when the player crosses a boundary. Instead, use two thresholds: an *upgrade* threshold (closer) and a *downgrade* threshold (farther).
- Example: Upgrade to LOD 0 at distance 50. Downgrade to LOD 1 at distance 60. The 10-unit gap prevents thrashing.
- Voxel Plugin for UE calls this the "Invoker Distance Threshold" — the LOD octree only rebuilds when the player moves more than this threshold distance.

### Practical recommendation
- **Test with scale 0.25** but implement hysteresis before evaluating. Without hysteresis, any smaller scale will appear to cause thrashing.
- The LOD 0 radius at 0.25 scale may be acceptable if the edit radius is smaller than the LOD 0 radius (which it should be).
- Consider making the LOD 0 radius configurable independently of scale — decouple visual LOD from edit-range LOD.

### Lock-in risk
- Ship with the final scale. Don't plan to change it later.
- If unsure, **start with the smaller scale (0.25)** and larger world size. It's easier to waste space than to resize a persisted world.

---

## 8. LOD propagation logic changes

**Required changes (from #2 and #7):**

### Hard constraint: max LOD difference of 1 between neighbors
This isn't optional — it's required for:
- Transvoxel meshing (only handles 2x resolution boundaries).
- Visual correctness (no cracks/seams).
- Edit consistency (know which chunks are at LOD 0).

### Chunk processing count
At scale 0.25, the LOD 0 volume is smaller, but there are more total chunks in the world. The propagation logic touches more chunks per update.

**Mitigation:**
- **Hysteresis** (see #7) — reduce update frequency.
- **Incremental propagation** — only re-propagate when the player moves beyond the threshold, and only for chunks whose LOD actually changes.
- **Budget system** — cap the number of LOD transitions per frame. Spread work over multiple frames. Voxel Tools (Godot) uses this approach: it limits the number of chunk loads/meshes per frame to maintain framerate.

### Browser budget
For WebGL/browser, a reasonable target might be:
- Max 4–8 chunk mesh rebuilds per frame.
- Max 2–4 chunk loads from disk per frame (via OPFS in a Web Worker).
- LOD propagation itself is cheap (tree traversal) — the cost is in the resulting mesh/load work.

---

## Browser-Specific: Storage with OPFS

**IndexedDB is not the answer.** It has severe performance problems with large binary data in Chrome.

**OPFS (Origin Private File System) is the right choice:**
- 3–4x faster than IndexedDB for binary data.
- Supports synchronous read/write via `createSyncAccessHandle()` (Web Worker only).
- Designed for exactly this use case: large binary blobs, high-frequency access.

### Architecture
- **Main thread:** Game loop, rendering, player input.
- **Web Worker 1:** Chunk serialization/deserialization, OPFS reads/writes.
- **Web Worker 2 (optional):** Mipmap computation, mesh generation.

### File layout on OPFS
```
/world/
  manifest.json          # world size, scale, version
  /chunks/
    /lod0/
      chunk_x_y_z.bin    # RLE-compressed LOD 0 source
    /lod1/
      chunk_x_y_z.bin    # cached mipmap (regeneratable)
    /lod2/
      ...
```

### Key constraint
`createSyncAccessHandle()` only works in Web Workers, not on the main thread. All disk IO must be offloaded to a worker. This is actually good architecture — it forces async IO and prevents frame drops.

---

## Suggested Implementation Order

1. **Lock world size and scale.** This blocks everything else.
2. **Implement player-position-based LOD 0 forcing** within edit radius. Enforce max LOD difference of 1.
3. **LOD 0 chunk serialization to OPFS** (Web Worker). Save/load individual chunks.
4. **Dirty-flagging + debounced save pipeline.**
5. **Incremental mipmap propagation** (bottom-up, one octant per level).
6. **Mipmap caching to OPFS.**
7. **Budget system** for chunk processing per frame.
8. **Hysteresis** for LOD update distance thresholds.

---

## Sources

- [Voxel Terrain Storage (zeux.io)](https://zeux.io/2017/03/27/voxel-terrain-storage/) — RLE compression, chunk serialization
- [The Transvoxel Algorithm](http://transvoxel.org/) — canonical LOD seam solution, max 1-level difference constraint
- [Voxel Plugin: World Size and LOD](https://wiki.voxelplugin.com/World_Size_and_Level_Of_Details) — LOD octree, invoker distance threshold
- [Voxel Tools: VoxelLodTerrain](https://voxel-tools.readthedocs.io/en/latest/api/VoxelLodTerrain/) — LOD update scheduling, chunk budget
- [Voxel Tools: Performance](https://voxel-tools.readthedocs.io/en/latest/performance/) — bulk edit optimization, mesh rebuild budgeting
- [A Level of Detail Method for Blocky Voxels (0fps.net)](https://0fps.net/2018/03/03/a-level-of-detail-method-for-blocky-voxels/)
- [LOD Seams with Dual Contouring](http://ngildea.blogspot.com/2014/09/dual-contouring-chunked-terrain.html)
- [OPFS (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system) — createSyncAccessHandle, Web Worker constraint
- [OPFS Caching (Autodesk)](https://aps.autodesk.com/blog/viewer-performance-update-part-2-3-opfs-caching) — 2-4x load time improvement over IndexedDB
- [LocalStorage vs IndexedDB vs OPFS (RxDB)](https://rxdb.info/articles/localstorage-indexeddb-cookies-opfs-sqlite-wasm.html) — performance comparison
- [High Performance Voxel Engine (Nick's Blog)](https://nickmcd.me/2021/04/04/high-performance-voxel-engine/) — vertex pooling, chunk optimization
- [Let's Make a Voxel Engine: Chunk Management](https://sites.google.com/site/letsmakeavoxelengine/home/chunk-management) — visibility lists, chunk lifecycle
