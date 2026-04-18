# Gappu Carousel Pipeline

**Input:** Pre-assembled beat pack (design_layout/font/color + per-slide: slide_no, arc, gappu_in_scene, image_prompt, headline, subtext, story_title)

**Output:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\YYYY-MM-DD_TopicName\`
- images/ (Nano Banana 2, 4:5) | slides/ (HTML/CSS PNGs) | caption.txt | SESSION-RESUME.md

**Social:** Instagram @gappumagicworld | Facebook: Gappu Magic Story Land

**Design Vault:** See `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md` — do not duplicate here.

---

## STEP 0 — Login Check

Navigate to https://labs.google/fx/tools/flow → screenshot confirms profile icon (not "Sign In") → wait for user confirmation.

Check reference image support: Image tab → "Add image" option → save to SESSION-RESUME.md.

---

## STEP 1 — Create Folder

```
D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\YYYY-MM-DD_TopicName\
├── images\ | slides\ | SESSION-RESUME.md
```

---

## STEP 2 — Image Generation (Nano Banana 2)

**Settings (once, screenshot):** Image tab | 4:5 | x1 | Nano Banana 2

**Per Slide (gappu_in_scene: YES):**
1. New project: `btns.find(b => b.textContent.includes('New project')).click()` → save URL
2. Attach reference (if supported + gappu_in_scene: YES): upload `gappu_dhoti.png`
3. Type image_prompt → Generate: `btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()`
4. Wait: `await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 })`
5. Download: `img[src*="googleusercontent"].src` → navigate → save `images/slide_NN.png`
6. Update SESSION-RESUME.md: IMAGE → DONE

CTA slide (gappu_in_scene: NO) → skip image gen.

---

## STEP 3 — Slide Generation

**Follow:** `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md` Steps A–D.

**3A — Manifesto:** Write `slides/design-philosophy.md` (aesthetic name + 4–6 paragraphs: space/form, color, typography, hierarchy, intention).

**3B — generate_slides.py:**
- 4 layers: [1] full-bleed image [2] layout decoration (per design_layout) [3] gradient bottom 65% [4] typography (headline 95–110px, subtext 42–48px, lower-third)
- Fonts: local via @font-face file:/// (never Google CDN)
- CTA slide: solid BG_HEX, headline + @gappumagicworld

**3C — Run:** `python carousel/generate_slides.py` → verify → SESSION-RESUME.md: SLIDE → DONE

---

## STEP 4 — Caption

Instagram: Hook (<15 words) + Body (emotional arc) + CTA "Follow @gappumagicworld"
Facebook: Hook + Story paragraph + Lesson + CTA with link + hashtags

Save: `slides/caption.txt`

---

## STEP 5 — Final Report

```
CAROUSEL COMPLETE
Topic: [title] | Design: [Layout]|[Font]|[Color]
Images: [X]/[N] | Slides: [X]/[N] | Caption: DONE
Failed: [list or NONE]
```

---

## Selectors Reference

See `D:\oldCOMPUTER\Videos\_Rules\reference-playwright-selectors.md`

---

## Failure Handling

| Failure | Action |
|---------|--------|
| IMAGE FAILED-1 | Rewrite prompt (safety), retry |
| IMAGE FAILED-2 | Skip, log |
| SLIDE FAILED | Log, fallback plain PNG |

**Never pause for failures.** Log, skip, report at end.

Values: `PENDING` / `DONE` / `FAILED-1` / `FAILED-2` / `SKIP`

---

## Hard Rules

- Login check before generation
- Confirm 4:5 + x1 + Nano Banana 2 (screenshot)
- Reference only if supported + gappu_in_scene: YES
- DOM waits only — no screenshot polling
- Local fonts via @font-face — no Google CDN
- No PIL / html_templates/ — generate HTML fresh
