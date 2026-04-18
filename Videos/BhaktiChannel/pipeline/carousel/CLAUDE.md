# Bhakti Channel — Carousel Pipeline

**Channel:** Sanatan Dharma | **Instagram:** @sanatandharmatheeternalpath | **Facebook:** Sanatan Dharma
**Logo:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\PICTURE\657973132_18075711047188622_535010279705404318_n.jpg`

---

## Folder Structure
```
D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\carousel\
    YYYY-MM-DD_TopicName\
        generate_slides.py
        images\
            hero.png
        slides\
            slide_01.png ... slide_NN.png
            design-philosophy.md
        SESSION-RESUME.md
```

---

## Brand Constants
```python
CHANNEL  = "Sanatan Dharma"
HANDLE   = "@sanatandharmatheeternalpath"
LOGO     = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/657973132_18075711047188622_535010279705404318_n.jpg")
```

---

## STEP 0 — Login Check (once per session)

1. Navigate to https://labs.google/fx/tools/flow via Playwright
2. Take one screenshot — confirm logged in (profile icon visible, project list visible)
3. If NOT logged in: tell user "Please log in to Google Flow, then confirm"
4. Do not proceed until confirmed

### 0B — Check Reference Image Support (once per session)
1. Create a temporary new project in Flow → open Image tab → check for "Add image" option
2. Save to SESSION-RESUME.md: `Reference Image: SUPPORTED` or `NOT SUPPORTED`

---

## STEP 1 — Get Episode Topic and Content Points

User provides: deity name + topic, festival/ritual with key facts, shloka/verse, or story summary.

Claude extracts N content points (minimum 4, maximum 8) — one point per slide. Each = a clear, punchy devotional fact or truth.

**Copy rules:**
- Hook line: under 15 words, statement not a question
- Body copy: reverential but accessible, 2 lines max
- Kicker: one-line truth, contemplative or inspiring

**Language rule:**
- Hindi input → all slide text in Hindi (Devanagari). Use Hind-Bold.ttf / Hind-Regular.ttf.
  Hind path: `D:\oldCOMPUTER\Videos\Scripts\GitSkills\canvas-design\canvas-fonts\Hind-Regular.ttf`
- English input → all slide text in English (Latin)
- Set language at START — do not mix scripts on same slide
- NothingYouCouldDo script number stays Latin in all cases

---

## STEP 2 — Generate Hero Image + Create Folder

### 2A — Hero Image Prompt
- Write prompt in ENGLISH always
- Subject: deity, rishi, sacred animal, temple, ritual scene — with full scriptural detail (read `D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\CHARACTER_REFERENCE.md`)
- ALL MOUTHS SEALED — no open mouths, no speech bubbles
- No text, no words, no UI elements in image
- Characters in reverential pose — not action, not combat
- Environment: temple interior / Himalayan peak / forest ashram / cosmic space / riverbank
- Lighting: warm divine glow, rim light, volumetric rays appropriate to scene
- Style line: "cinematic painting, vibrant jewel tones, rich golden light, hyperdetailed, 4K render quality"
- End with: "Format: 4:5 portrait, high resolution. This image will be used as a carousel background."

### 2B — Generate via Playwright
1. Navigate to https://labs.google/fx/tools/flow → create new project
2. Open Image tab → Nano Banana 2 → 4:5 → x1 → Unlimited ON
3. Paste hero image prompt → click Generate: `btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()`
4. **Wait for completion — DOM wait:**
```js
await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 });
```
5. Download via Playwright blob method:
```javascript
const imgs = document.querySelectorAll('img[src*="blob:"], img[src*="googleusercontent"]');
const url = imgs[imgs.length-1].src;
const resp = await fetch(url);
const buf = await resp.arrayBuffer();
const blob = new Blob([buf], {type:'image/png'});
const a = document.createElement('a');
a.href = URL.createObjectURL(blob);
a.download = 'hero.png';
a.click();
```
File saves to `.playwright-mcp/hero.png` → `mv .playwright-mcp/hero.png images/hero.png`

6. Update SESSION-RESUME.md: `IMAGE: DONE` + Flow Asset ID

### 2C — Create Story Folder
```
D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\carousel\YYYY-MM-DD_TopicName\
    images\ (hero.png already saved)
    slides\
    SESSION-RESUME.md
```

---

## STEP 3 — Design Vault Selection

> **Shared Rule:** Follow STEP 0 from `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md`.

Bhakti aesthetic = sacred, timeless, contemplative. Rich jewel tones, warm golds, deep magentas.

**Suggested palettes:**
- `Luxury_Gold` — major deities (Vishnu, Lakshmi, Durga)
- `Lavender_Dream` — Shiva, spiritual topics
- `Earthy_Green` — Ayurveda, nature deities, forest scenes
- `Minimal_Cream` — shloka/verse carousels

These are suggestions — always let the story drive the choice.

Output: Layout name, Font Pair name, Palette name + BG_HEX / TEXT_HEX / ACCENT_HEX confirmed before proceeding.

---

## STEP 4 — Art Manifesto (design-philosophy.md)

> **Shared Rule:** Follow Steps A–D from `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md`.

Write before generate_slides.py:
- Movement name (e.g. "Sacred Fire", "Golden Devotion", "Temple Silence")
- 4–5 paragraphs: Space / Color / Typography / Hierarchy / Craftsmanship
- Palette reasoning tied to the deity/topic's energy, font choices and why

Save to: `slides/design-philosophy.md`

---

## STEP 5 — Write generate_slides.py (Bespoke HTML/CSS)

Fresh script per carousel. NOT a template.

**Tech stack:** Playwright (sync_playwright), local @font-face file:/// (no Google CDN), W=1080 H=1350.
Single hero.png used as full-bleed background on ALL content slides.

**Bhakti-specific values:**
```python
LOGO  = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/657973132_18075711047188622_535010279705404318_n.jpg")
HERO  = IMAGES / "hero.png"
# CHANNEL_LABEL = "SANATAN DHARMA  ·  0N of NN"
# HANDLE = "@sanatandharmatheeternalpath"
```

**Slide structure (4 layers, every content slide):**
1. Full-bleed hero image — base64 data URI in CSS background
2. Dark tint overlay — rgba(0,0,0,0.28)
3. Bottom gradient — transparent → near-black (72% canvas height)
4. Typography — bottom-left anchored, left-aligned

**Border rule (CRITICAL):**
- Thin line at very EDGE only — `inset: 8px`
- Corner bracket accents at 4 corners (20–22px from edge)
- NEVER draws across the image

**Font choices (match devotional emotion):**
- Headline: Italiana / Gloock / IBMPlexSerif-Bold / YoungSerif (or Hind-Bold for Hindi)
- Script number: NothingYouCouldDo (always — hardcoded)
- Body: InstrumentSans-Regular / WorkSans-Regular / BricolageGrotesque-Regular (or Hind-Regular for Hindi)
- Kicker: CrimsonPro-Italic / Lora-Italic / InstrumentSerif-Italic (or Hind-Regular italic for Hindi)
- Label: InstrumentSans-Bold / WorkSans-Bold (or Hind-Bold for Hindi)

**Typography layout (every content slide):**
- Top label: "SANATAN DHARMA  ·  0N of NN" — tiny caps, centered, opacity 0.42
- Large handwritten script number — bottom-left (~180–200px), calligraphic
- Headline — below number (~68–80px elegant serif)
- Body copy — 2 lines max (~30–34px, quiet, light)
- Kicker — italic, accent color, 3px left border (~36–40px)

**CTA slide (always last):**
- Solid BG_HEX background — no hero image
- Circular logo (220px, 3px ACCENT border)
- Channel name label (small caps, low opacity, letter-spaced)
- Large script "Follow us" in TEXT_HEX
- Thin divider line
- Handle @sanatandharmatheeternalpath in ACCENT_HEX (uppercase, letter-spaced)
- Edge-only border frame + corner brackets

**Slide count:** Minimum 5 (4 content + 1 CTA), maximum 9 (8 content + 1 CTA).

---

## STEP 6 — Run generate_slides.py

```bash
cd "D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\carousel\YYYY-MM-DD_TopicName"
python generate_slides.py
```

Prerequisite: `images/hero.png` must exist. Report file sizes, errors, slide count.

---

## STEP 7 — Caption and Post Copy

**Instagram caption:**
```
[Hook line — under 15 words, statement]
[3–5 bullet facts from slides]
Follow @sanatandharmatheeternalpath for more!
#SanatanDharma #[deity/topic hashtags] #HinduDharma #BhaktiVibes
```

**Facebook post:** Same without hashtag block → append "Follow Sanatan Dharma for more!"

---

## STEP 8 — Final Report

```
BHAKTI CAROUSEL COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━
Topic:      [title]
Folder:     D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\carousel\YYYY-MM-DD_TopicName
Design:     [Movement name] | [Palette] | [Fonts]
Hero image: DONE / FAILED
Slides:     [X] / [N] done
Caption:    DONE
Failed:     [list or NONE]
```

---

## Selectors Reference (Google Flow)

```
URL:         https://labs.google/fx/tools/flow
New project: btns.find(b => b.textContent.includes('New project')).click()
Image tab:   tab with text 'Image'
4:5 ratio:   tab with text '4:5'
x1 quantity: tab with text 'x1'
Prompt box:  textbox[placeholder*="What do you want to create"]
Generate:    btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()
```

---

## Failure Handling
- **IMAGE failure (Step 2):** Rewrite prompt, retry once. If fails again → FAILED-2, log, skip to next step.
- **SLIDE failure (Step 6):** Log FAILED, move to next slide. Report at end.
- **NEVER PAUSE PIPELINE FOR FAILURES.** Log, skip, report at end.

---

## Hard Rules
- Do NOT reuse ObjectAI's or Gappu's generate_slides.py — write fresh each time
- Do NOT use Google Fonts CDN — local fonts only via @font-face file:///
- Do NOT use PIL or pre-built templates
- Do NOT draw borders across the hero image — edge frame only (inset: 8px)
- Do NOT open mouths in hero image prompt
- Do NOT use 9:16 ratio for carousel — always 4:5 (1080×1350)
- Do NOT hardcode slide count — let content points drive it
- Do NOT mix Hindi and English on the same carousel — set language at Step 1
- DOM waits only — no screenshot polling for generation status
- Character descriptions: always read CHARACTER_REFERENCE.md — never from memory
