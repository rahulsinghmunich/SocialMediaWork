# ObjectAi Carousel Pipeline

**Channel:** objectwithbrainsai | **Instagram:** @objectwithbrainsai
**Logo:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\PICTURE\8e8017a2-5ef3-4613-9b72-610bf6539948.png`

---

## Folder Structure
```
D:\oldCOMPUTER\Videos\ObjectAi\pipeline\carousel\
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
CHANNEL  = "objectwithbrainsai"
HANDLE   = "@objectwithbrainsai"
LOGO     = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png")
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

User provides: episode title + topic summary, key facts/points, or ObjectAi video script.

Claude extracts N content points (minimum 4, maximum 8) — one point per slide.

**Copy rules:**
- Hook line: under 15 words, statement not a question
- Body copy: conversational, 2 lines max
- Kicker: one-line truth, punchy, emotional

**Language rule:**
- Hindi input → all slide text in Hindi (Devanagari). Use Hind-Bold.ttf / Hind-Regular.ttf.
  Hind path: `D:\oldCOMPUTER\Videos\Scripts\GitSkills\canvas-design\canvas-fonts\Hind-Regular.ttf`
- English input → all slide text in English (Latin)
- Set language at START — do not mix scripts on same slide
- NothingYouCouldDo script number stays Latin in all cases

---

## STEP 2 — Generate Hero Image + Create Folder

### 2A — Hero Image Prompt
- Write prompt in ENGLISH (even if carousel is Hindi)
- Characters: Pixar 3D animated objects (organ/food/household characters)
- Faces embedded IN material — NOT separate heads. Face geometry lock: sits flush, does NOT inflate/balloon
- ALL MOUTHS SEALED — no open mouths, no teeth
- First character → position RIGHT, second → position LEFT
- Specific environment, exact lighting quality, foreground props
- Style: "Pixar 3D animated, cinematic render quality, vibrant colors, clean sharp edges"
- End with: "Format: 4:5 portrait, high resolution. This image will be used as a carousel background."

### 2B — Generate via Playwright
1. Navigate to https://labs.google/fx/tools/flow → create new project
2. Open Image tab → Nano Banana 2 → 4:5 → x1 → Unlimited ON
3. Paste hero image prompt → click Generate: `btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()`
4. **Wait for completion — DOM wait:**
```js
await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 });
```
5. Download image → save as `images/hero.png`
6. Update SESSION-RESUME.md: `IMAGE: DONE` + Flow Asset ID

### 2C — Create Story Folder
```
D:\oldCOMPUTER\Videos\ObjectAi\pipeline\carousel\YYYY-MM-DD_TopicName\
    images\ (hero.png already saved)
    slides\
    SESSION-RESUME.md
```

---

## STEP 3 — Design Vault Selection

> **Shared Rule:** Follow STEP 0 from `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md` — select Layout + Typography + Color from the full Design Vault, driven by this episode's emotional tone.

ObjectAi aesthetic = bold, scientific, energetic. NOT golden editorial. Let the topic guide the choice.

Output: Layout name, Font Pair name, Palette name + BG_HEX / TEXT_HEX / ACCENT_HEX confirmed before proceeding.

---

## STEP 4 — Art Manifesto (design-philosophy.md)

> **Shared Rule:** Follow Steps A–D from `D:\oldCOMPUTER\Videos\_Rules\carousel-slide-generation.md`.

Write design manifesto before generate_slides.py:
- Movement name (e.g. "Electric Anatomy", "Green Thunder", "Neon Classroom")
- 4–5 paragraphs: Space / Color / Typography / Hierarchy / Craftsmanship
- Palette reasoning tied to episode emotion, font choices and why

Save to: `slides/design-philosophy.md`

---

## STEP 5 — Write generate_slides.py (Bespoke HTML/CSS)

Fresh script per carousel. NOT a template. Tailored to this episode.

**Tech stack:** Playwright (sync_playwright), local @font-face file:/// (no Google CDN), W=1080 H=1350 (4:5 portrait).

**Slide structure (4 layers, every content slide):**
1. Full-bleed hero image — base64 data URI in CSS background, covers entire canvas
2. Dark tint overlay — rgba(0,0,0,0.28)
3. Bottom gradient — transparent → near-black (72% canvas height)
4. Typography — bottom-left anchored, left-aligned

**Border rule (CRITICAL):**
- Thin line at very EDGE only — `inset: 8px`
- Corner bracket accents at 4 corners (20–22px from edge)
- NEVER draws across the image or over the characters — like a picture frame

**Font choices (match episode emotion):**
- Headline: Italiana / Gloock / IBMPlexSerif-Bold / BigShoulders-Bold / YoungSerif
- Script number: NothingYouCouldDo (always — calligraphic bottom-left)
- Body: InstrumentSans-Regular / WorkSans-Regular / BricolageGrotesque-Regular
- Kicker: CrimsonPro-Italic / Lora-Italic / InstrumentSerif-Italic
- Label: InstrumentSans-Bold / WorkSans-Bold
- Hindi carousels: Hind-Bold (headline/label), Hind-Regular (body/kicker)

**Typography layout (every content slide):**
- Top label: "OBJECTAI  ·  0N of NN" — tiny caps, centered, opacity 0.42
- Large handwritten script number — bottom-left (~180–200px), calligraphic
- Headline — below number (~68–80px elegant serif)
- Body copy — 2 lines max (~30–34px, quiet, light)
- Kicker — italic, accent color, 3px left border (~36–40px)

**CTA slide (always last):**
- Solid BG_HEX background — no hero image
- Circular logo (220px, 3px ACCENT border, gold shadow)
- Channel name label (small caps, low opacity, letter-spaced)
- Large script "Follow us" in TEXT_HEX
- Thin divider line
- Handle @objectwithbrainsai in ACCENT_HEX (uppercase, letter-spaced)
- Edge-only border frame + corner brackets + progress dots

**Slide count:** Minimum 5 (4 content + 1 CTA), maximum 9 (8 content + 1 CTA). No filler slides.

**generate_slides.py skeleton:**
```python
STORY  = Path(__file__).parent
IMAGES = STORY / "images"
SLIDES = STORY / "slides"
FONTS  = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
LOGO   = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png")
HERO   = IMAGES / "hero.png"
W, H = 1080, 1350

BEAT_PACK = [
    {"num": 1, "arc": "HOOK", "headline": "...", "image": "hero.png"},
    ...
    {"num": N, "arc": "CTA", "headline": "Follow for more ObjectAi", "image": None},
]
COPY = { 1: ("body line 1\nbody line 2", "kicker truth line"), ... }
```

---

## STEP 6 — Run generate_slides.py

```bash
cd "D:\oldCOMPUTER\Videos\ObjectAi\pipeline\carousel\YYYY-MM-DD_TopicName"
python generate_slides.py
```

Prerequisite: `images/hero.png` must exist. Report file sizes, errors, slide count.

---

## STEP 7 — Caption and Post Copy

**Instagram caption:**
```
[Hook line — under 15 words, statement]
[3–5 bullet facts from slides]
Follow @objectwithbrainsai for more!
#ObjectAi #[topic hashtags] #ScienceFacts #AnimatedObjects
```

**Facebook post:** Same without hashtag block → append "Follow objectwithbrainsai for more!"

---

## STEP 8 — Final Report

```
OBJECTAI CAROUSEL COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━
Topic:      [title]
Folder:     D:\oldCOMPUTER\Videos\ObjectAi\pipeline\carousel\YYYY-MM-DD_TopicName
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
- Do NOT reuse Gappu's generate_slides.py — write fresh for each ObjectAi carousel
- Do NOT use Google Fonts CDN — local fonts only via @font-face file:///
- Do NOT use PIL or pre-built templates
- Do NOT draw borders across hero image — edge frame only (inset: 8px)
- Do NOT open character mouths in hero image prompt
- Do NOT use 9:16 ratio for carousel — always 4:5 (1080×1350)
- Do NOT hardcode slide count — let content points drive it
- DOM waits only — no screenshot polling for generation status
