# Gemini 2.5 Flash TTS — Cost Estimate & Scaling Analysis

**Date:** 2026-02-11
**Context:** Hojoon implemented TTS + BGM for the pet chat feature

## What Was Built

- **TTS**: Uses **Gemini 2.5 Flash Preview TTS** — each pet gets a unique generated voice
- **BGM**: 5 free stock music tracks hard-coded locally, mapped to hunger status (zero marginal cost)

## Assumptions

| Parameter | Estimate | Rationale |
|---|---|---|
| Avg message length | ~100 characters (~25 text tokens) | Pet responses are short, conversational |
| Input tokens per call | ~200 tokens | Text + voice/system instructions |
| Audio output per call | ~300-1,000 tokens | ~3-8 sec of speech |
| TTS messages per user/day | ~15 | ~3-4 sessions/day, 4-5 messages each |
| DAU/MAU ratio | ~25% | Industry avg for mobile games/apps |
| Cost per TTS message | ~$0.004 | Midpoint estimate |

## Unit Economics

**Gemini 2.5 Flash TTS pricing:**

| Component | Standard (per 1M tokens) | Batch (per 1M tokens) |
|---|---|---|
| Input (text) | $0.50 | $0.25 |
| Output (audio) | $10.00 | $5.00 |

**Per-message breakdown:**

- Input: ~200 tokens x $0.50/1M = **$0.0001**
- Audio output: ~500 tokens x $10/1M = **$0.005**
- **Total: ~$0.004-0.005 per message** (half a cent)

**Per-user daily cost:**

- 15 messages/day x $0.004 = **~$0.06/user/day**
- **~$1.80/user/month** (if daily active every day)

## Scaling Projections (Standard Pricing)

### By DAU (Daily Active Users)

| DAU | Daily messages | Daily cost | Monthly cost | Annual cost |
|---|---|---|---|---|
| 100 | 1,500 | $6 | $180 | $2,160 |
| 1,000 | 15,000 | $60 | $1,800 | $21,600 |
| 10,000 | 150,000 | $600 | $18,000 | $216,000 |
| 50,000 | 750,000 | $3,000 | $90,000 | $1,080,000 |
| 100,000 | 1,500,000 | $6,000 | $180,000 | $2,160,000 |

### By MAU (Monthly Active Users, assuming 25% DAU/MAU)

| MAU | Effective DAU | Monthly cost | Annual cost |
|---|---|---|---|
| 1,000 | 250 | $450 | $5,400 |
| 10,000 | 2,500 | $4,500 | $54,000 |
| 100,000 | 25,000 | $45,000 | $540,000 |
| 500,000 | 125,000 | $225,000 | $2,700,000 |
| 1,000,000 | 250,000 | $450,000 | $5,400,000 |

### With Batch Pricing (50% discount on output)

| DAU | Monthly (standard) | Monthly (batch) | Savings |
|---|---|---|---|
| 1,000 | $1,800 | $1,000 | $800 |
| 10,000 | $18,000 | $10,000 | $8,000 |
| 100,000 | $180,000 | $100,000 | $80,000 |

*Note: Batch pricing requires async processing — may not suit real-time chat UX.*

## Provider Comparison

| Provider | Cost per message (~100 chars) | Monthly at 10K DAU | Quality |
|---|---|---|---|
| **Gemini 2.5 Flash TTS** | ~$0.004 | ~$18,000 | Good, unique voices per pet |
| **Google Cloud TTS (Standard)** | ~$0.0004 | ~$1,800 | Basic, limited voices |
| **Google Cloud TTS (WaveNet)** | ~$0.0016 | ~$7,200 | Good, natural sounding |
| **ElevenLabs (Scale plan)** | ~$0.018 | ~$81,000 | Premium, most natural |
| **ElevenLabs (Business)** | ~$0.012 | ~$54,000 | Premium, most natural |

### Key Takeaways

1. **Gemini Flash TTS is mid-tier on cost** — 10x more expensive than basic Google Cloud TTS, but 3-4x cheaper than ElevenLabs
2. **Google Cloud TTS Standard is cheapest** but voices are generic — no LLM-driven unique voice generation
3. **ElevenLabs has best quality** but is 3-5x more expensive than Gemini Flash
4. **At 10K DAU, TTS becomes a real line item** (~$18K/mo) — worth optimizing at that point

## Cost Optimization Strategies

1. **Cache common responses** — If pets say similar things often, cache the audio
2. **Limit TTS per session** — e.g., first 10 messages are voiced, rest are text-only
3. **Shorter responses** — Tune pet personality to be concise (fewer tokens = less cost)
4. **Batch pricing** — If any TTS can be pre-generated (greetings, reactions), use batch
5. **Hybrid approach** — Use cheap Google Cloud TTS for generic lines, Gemini Flash for unique/personality-driven lines
6. **Tiered access** — Free users get limited TTS, premium users get unlimited

## Sources

- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Google Cloud TTS Pricing](https://cloud.google.com/text-to-speech/pricing)
- [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api)
