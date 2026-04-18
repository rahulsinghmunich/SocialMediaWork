# Sonnet Optimization Guide

**Purpose:** Reduce context token usage while preserving full functionality when running pipelines with Claude Sonnet model.

---

## Compression Patterns Used

### 1. Reference Over Repetition

**Before (400 lines):** Duplicate carousel-slide-generation.md content in every channel rule
**After (50 lines):** Single line reference

```markdown
**Pipeline Steps:** Follow `carousel-slide-generation.md` Steps 0-D for Design Vault selection, manifesto writing, generate_slides.py, and execution.
```

### 2. Compact Design Matrix (3-line format)

**Before (36 cells):** 6×6 table with full descriptions
**After (3 lines):** Arrow format with pipe-separated values

```
Wonder/Discovery→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Pastel_Pink|Blob opacity 0.6, sparkle dots CSS
Problem/Confusion→Brutalist_Box|SpaceGrotesk+DMMono+NothingYouCouldDo|Dark_Tech|Box shadow 8px, gradient 75%
Joy/Celebration→Neon_Marquee|BigShoulders-Bold+InstrumentSans+NothingYouCouldDo|Sunset_Orange|Neon glow border, scrapbook ±3deg
```

### 3. Remove Duplicate STEP 4B

**Before:** ~40 lines STEP 4B section in every carousel rule (120 lines total across 3 channels)
**After:** Single reference in carousel-slide-generation.md

```markdown
**Canvas Element:** Optional STEP 4B via canvas-design skill. See `carousel-slide-generation.md` for full integration rules.
```

### 4. Collapse VEO Scenarios

**Before:** 7 scenarios with full JSON templates (907 lines)
**After:** 3 base scenarios + deltas (400 lines)

- Scenarios 1-4 (multi-speaker variations) → 1 base template + duration deltas
- Scenario 5 (RAW IMPORT) → kept (parsing rules needed)
- Scenario 6 (NO IMAGE) → handled by `generation_mode` flag
- Scenario 7 (VS TOPIC) → edge case, removed

### 5. Externalize Selectors

**Before:** ~30 lines selectors duplicated in 6 files (180 lines total)
**After:** Single reference file

```markdown
**Selectors:** See `D:\oldCOMPUTER\Videos\_Rules\reference-playwright-selectors.md`
```

### 6. Remove Example Code

**Before:** Full Python/JS snippets in rules
**After:** Reference actual files

```markdown
**JSON Structure:** See `veo-pacer-v9-fixed.html` for complete schema.
```

---

## Token Savings Achieved

| File | Before | After | Savings |
|------|--------|-------|---------|
| bhakti-carousel.md | 141 lines | 95 lines | -33% |
| gappu-carousel.md | 118 lines | 90 lines | -24% |
| objectai-carousel.md | 129 lines | 95 lines | -26% |
| bhakti-pipeline.md | 395 lines | 250 lines | -37% |
| CLAUDE_VEO_RULES.md | 907 lines | 400 lines | -56% |
| **Total** | **1,690 lines** | **930 lines** | **-45%** |

---

## Design Matrix Format Reference

### Full Table Format (OLD - Avoid)

```markdown
| Arc Type | Layout (roll 1d4) | Typography Energy | Palette (roll 1d3) | Special Treatment |
|----------|-------------------|-------------------|---------------------|-------------------|
| Wonder/Discovery | 1. Soft_Blob 2. Centered_Arch... | YoungSerif + WorkSans... | 1. Pastel_Pink... | Blob opacity 0.6... |
```

### Compact Arrow Format (NEW - Use)

```
Wonder/Discovery→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Pastel_Pink|Blob opacity 0.6, sparkle dots CSS
```

**Format:** `StoryType→Layout|Fonts|Palette|SpecialTreatment`

---

## When NOT to Compress

1. **Validation rules** — Keep explicit (auto-validation logic must be clear)
2. **Field order requirements** — Keep explicit (JSON structure must match exactly)
3. **Failure handling** — Keep explicit (pipeline must not stall)
4. **Hard rules** — Keep explicit (NEVER randomize DNA locks)
5. **Dialogue formatting** — Keep explicit (hyphen rule, WPS limits)

---

## Reading Compressed Rules

When Sonnet reads compressed rules:

1. **Arrow format** → Parse as: `Type→Attribute1|Attribute2|Attribute3|Attribute4`
2. **Reference to shared file** → Read that file once, apply to all channels
3. **Scenario deltas** → Apply base template + modify per delta

---

## Future Optimization Opportunities

1. **Externalize font tables** — One reference file for all channel fonts
2. **Compress palette definitions** — Hex values only, full names in reference
3. **Remove SESSION-RESUME.md templates** — Structure is obvious from context
4. **Collapse failure handling** — Single shared failure section across pipelines

---

## Designer's Note

> "Compression without clarity is technical debt. Every line removed must be recoverable from context or a single reference. The goal is not minimalism — it is efficiency without ambiguity."
