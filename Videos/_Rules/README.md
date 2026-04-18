# _Rules Index — Token-Optimized Reference

**Activation Pattern:** `"activate [pipeline name]"` → Read execution file → Run pipeline

---

## Pipeline Quick Reference

| Pipeline | Activate | Execution File | Tools | Output |
|----------|----------|----------------|-------|--------|
| **Gappu** | `"activate gappu pipeline"` | `GappuMonkeyShorts/pipeline/CLAUDE.md` | Nano Banana Pro + Kling V3 | 9:16 images + videos |
| **Gappu Carousel** | `"activate gappu carousel"` | `GappuMonkeyShorts/pipeline/carousel/CLAUDE.md` | Nano Banana 2 (Flow) | 4:5 carousel slides |
| **Bhakti** | `"activate bhakti pipeline"` | `BhaktiChannel/pipeline/CLAUDE.md` | NotebookLM + Higgsfield | 12-scene shorts |
| **Bhakti Carousel** | `"activate bhakti carousel"` | `BhaktiChannel/pipeline/carousel/CLAUDE.md` | Nano Banana 2 (Flow) | 4:5 Devanagari slides |
| **ObjectAi** | `"activate objectai pipeline"` | `ObjectAi/pipeline/CLAUDE.md` + `Scripts/ObjectAi/CLAUDE_VEO_RULES.md` | Google Flow + VEO 3.1 | 8s object talk videos |
| **ObjectAi Carousel** | `"activate objectai carousel"` | `ObjectAi/pipeline/carousel/CLAUDE.md` | Nano Banana 2 (Flow) | 4:5 science slides |
| **Bhakti Suno** | `"activate suno prompt"` | `_Rules/bhakti-suno-prompt.md` | Suno V5.5 (manual) | Style + IAST lyrics |
| **ObjectTalk VEO** | `"activate veo prompt"` | `Scripts/ObjectAi/CLAUDE_VEO_RULES.md` | VEO 3.1 (manual) | JSON prompts |
| **ObjectTalk Viral** | `"activate viral strategy"` | `_Rules/objecttalk-viral-strategy.md` | — | IG + FB captions |

---

## Constants Cache

**See:** `.cache/pipeline-constants.md` for:
- Design Matrices (all channels)
- WPS/BPM limits
- DNA locks
- Typography tables
- Palette hex values

---

## Shared References

| File | Purpose |
|------|---------|
| `reference-playwright-selectors.md` | Google Flow + Higgsfield selectors |
| `carousel-slide-generation.md` | Shared carousel Steps 0–D (all channels) |
| `sonnet-optimization.md` | Compression patterns used in this folder |

---

## Channel Branding

| Channel | IG Handle | FB Page | Logo Path |
|---------|-----------|---------|-----------|
| Gappu | @gappumagicworld | Gappu Magic Story Land | `GappuMonkeyShorts/pipeline/reference/gappu_dhoti.png` |
| Bhakti | @sanatandharmatheeternalpath | Sanatan Dharma | `Bhakti/branding/logo.jpg` |
| ObjectAi | @objectwithbrainsai | — | `GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png` |

---

## Usage

**Claude reads this file first** (~150 tokens), then:
1. Constants from `.cache/pipeline-constants.md` (~200 tokens)
2. Execution file ONLY when pipeline activated (~50–100 tokens per turn)

**Total baseline:** ~350 tokens vs ~857 lines (~2,500 tokens) = **-86%**
