# Shared Rule: Carousel Slide Generation (Post Image)
**Applies to:** All carousel pipelines — Gappu, ObjectAI, and any future channel.
**Activate point:** After all images are generated and saved to `images/` folder.

---

## WHAT THIS RULE COVERS

Everything **after image generation** up to caption:
- Design Vault selection (layout + typography + color)
- Art Manifesto (design-philosophy.md)
- Writing generate_slides.py (bespoke per carousel)
- Running generate_slides.py → PNG output
- Verifying slides

This rule is **channel-agnostic**. Channel-specific values (palette, fonts, logo, handle, image path) are injected per carousel — the structure is always the same.

---

## STEP 0 — Design Vault Selection (MANDATORY — all pipelines, all channels)

Before writing any code or manifesto, select ONE from each category below.

**Selection is always story-driven — not random, not default.**
Read the story topic + emotional arc → pick what serves THIS story.
The Vault is a menu of options. Override freely if the story demands it.
Justify your choices in one line each — this becomes the seed of the art manifesto.

---

### CATEGORY 1 — Layout Architecture (pick 1)

| Option | Feel | Use when |
|--------|------|----------|
| `Centered_Arch` | Soft, welcoming, centralized | Warm emotional stories, wonder, joy |
| `Professional_Sidebar` | Structured, educational, grounded | Informational, health, science topics |
| `Floating_UI_Card` | Modern, digital, clean | Tech, apps, product-style topics |
| `Editorial_Split` | High-end, magazine, sophisticated | Premium feel, fashion, luxury |
| `Brutalist_Box` | Loud, high-energy, chaotic | Shock/warning topics, bold hooks |
| `Polaroid_Scrapbook` | Nostalgic, memory-focused, messy | Childhood, nostalgia, personal stories |
| `Cyber_Terminal` | Tech-focused, glowing, dark | Science, AI, futurism |
| `Soft_Blob` | Organic, fluid, calming | Nature, wellness, mindfulness |
| `Minimal_Border` | Extremely clean, quiet, museum-like | Premium simplicity, art, culture |
| `Neon_Marquee` | Aggressive, bold, moving | High-energy, viral, entertainment |

---

### CATEGORY 2 — Typography Pair (pick 1)

| Option | Fonts | Feel |
|--------|-------|------|
| `Elegant` | Italiana + InstrumentSans | Refined, warm, editorial |
| `Tech` | Space Grotesk + Space Mono | Digital, precise, future |
| `Editorial` | Gloock + Montserrat | High-contrast, magazine |
| `Boho` | Cormorant Garamond + Jost | Earthy, organic, free |
| `Impact` | BigShoulders-Bold + InstrumentSans | Strong, direct, punchy |
| `Corporate` | Oswald + WorkSans | Clear, trustworthy, formal |
| `Classic` | Lora + InstrumentSans | Timeless, readable, neutral |
| `Retro` | Abril Fatface + Lato | Nostalgic, fun, bold |
| `Bold` | BricolageGrotesque + WorkSans | Strong grotesque, modern |
| `Friendly` | YoungSerif + InstrumentSans | Warm, approachable, soft |

> **Note:** All fonts loaded LOCAL via `file:///` from `D:\oldCOMPUTER\Videos\Scripts\GitSkills\canvas-design\canvas-fonts\` — never Google CDN.
> NothingYouCouldDo-Regular.ttf is ALWAYS used for the script number — this is hardcoded, not a choice.

---

### CATEGORY 3 — Color Palette (pick 1)

| Option | BG | TEXT | ACCENT | Feel |
|--------|----|------|--------|------|
| `Minimal_Cream` | #FDFBF7 | #3E362E | #E6D5C3 | Quiet, paper, artisanal |
| `Dark_Tech` | #0A0A0A | #FFFFFF | #00FFFF | Dark mode, cyber, sharp |
| `Sunset_Orange` | #FFF3E0 | #E65100 | #FFB74D | Energy, heat, urgency |
| `Ocean_Blue` | #E3F2FD | #0D47A1 | #64B5F6 | Trust, calm, depth |
| `Earthy_Green` | #E8F5E9 | #1B5E20 | #81C784 | Nature, health, Ayurvedic |
| `Neon_Cyber` | #12005E | #00E5FF | #FF007F | Electric, sci-fi, vibrant |
| `Pastel_Pink` | #FCE4EC | #880E4F | #F48FB1 | Soft, emotional, gentle |
| `Luxury_Gold` | #212121 | #FFD700 | #B8860B | Premium, warm, cinematic |
| `Retro_Mustard` | #FFECB3 | #5C4033 | #FFCA28 | Vintage, nostalgic, earthy |
| `Lavender_Dream` | #F3E5F5 | #4A148C | #CE93D8 | Calm, spiritual, soft |

---

### Output of STEP 0 (confirm before proceeding)

```
Layout:    [chosen layout name]     — [1-line reason tied to story]
Font Pair: [chosen font pair name]  — [1-line reason tied to story]
Palette:   [chosen palette name]    — [1-line reason tied to story]

BG_HEX:     #......
TEXT_HEX:   #......
ACCENT_HEX: #......
```

⛔ Do NOT proceed to STEP A (Art Manifesto) until this is confirmed.

---

## STEP A — Write Art Manifesto (design-philosophy.md)

Before writing any code, write `slides/design-philosophy.md` as a design manifesto for this specific story.

**Structure:**
```
# Design Philosophy — [Episode Title]

## Movement Name
"[2–3 word movement name]" (e.g. "Herbalist's Wisdom", "Golden Suspicion", "Electric Anatomy")

## Space & Geometry
How the layout breathes and focuses the eye.

## Color & Material
What the palette communicates emotionally. Why these hex values for this story.

## Typography
How fonts are part of the art, not just labels. What each font choice signals.

## Visual Hierarchy
What the viewer sees first, second, third.

## Craftsmanship Intention
Why this looks hand-made, not templated.

## Emotional Arc
How the slides flow from Hook → Payoff → CTA emotionally.
```

Save to: `slides/design-philosophy.md`

---

## STEP B — Write generate_slides.py

Claude writes a **fresh, bespoke** `generate_slides.py` for EACH carousel.
NOT a template. NOT copied from previous carousel. Tailored to this story's exact design.

### Required Structure (always use this — all carousels)

```python
"""
[Channel] Carousel — Bespoke HTML Slide Generator
Story    : [Episode Title]
Movement : "[Movement Name from design-philosophy.md]"
Fonts    : [font choices]
Canvas   : 1080 x 1350 px (4:5 portrait)
Renderer : Playwright Chromium
"""

import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

# ── Paths ──────────────────────────────────────────────────────────────────────
STORY  = Path(__file__).parent
IMAGES = STORY / "images"
SLIDES = STORY / "slides"
FONTS  = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
LOGO   = Path("[channel logo path]")
HERO   = IMAGES / "[hero image filename]"   # hero.png (ObjectAI/Bhakti) or slide_NN.png (Gappu)
SLIDES.mkdir(exist_ok=True)

W, H = 1080, 1350

# ── Color Palette (episode-specific) ──────────────────────────────────────────
BG     = "#..."
TEXT   = "#..."
ACCENT = "#..."

# ── Font paths (local — never CDN) ────────────────────────────────────────────
F_SCRIPT   = (FONTS / "NothingYouCouldDo-Regular.ttf").as_posix()   # Always — hardcoded
F_HEADLINE = (FONTS / "[chosen headline font].ttf").as_posix()
F_BODY     = (FONTS / "[chosen body font].ttf").as_posix()
F_KICKER   = (FONTS / "[chosen kicker/italic font].ttf").as_posix()
F_LABEL    = (FONTS / "[chosen label font].ttf").as_posix()

# ── Beat pack (one dict per slide including CTA) ───────────────────────────────
BEAT_PACK = [
    {"num": 1, "arc": "HOOK", "headline": "...", "body": "...", "kicker": "..."},
    {"num": 2, "arc": "FACT", "headline": "...", "body": "...", "kicker": "..."},
    # ... content slides ...
    {"num": N, "arc": "CTA",  "headline": "...", "body": None,  "kicker": None},
]

CHANNEL_LABEL = "[CHANNEL_NAME]"   # e.g. "OBJECTAI" / "SANATAN DHARMA" / "GAPPU MAGIC"
HANDLE        = "@[handle]"        # e.g. "@objectwithbrainsai"
LOGO_EXT      = "png"              # "jpg" for Bhakti logo


# ── Helper: encode image as base64 data URI ────────────────────────────────────
def b64img(path: Path) -> str:
    if not path.exists():
        return ""
    ext  = path.suffix.lower().lstrip(".")
    mime = "jpeg" if ext in ("jpg", "jpeg") else "png"
    return f"data:image/{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


# ── Helper: @font-face CSS block ──────────────────────────────────────────────
def fonts_css() -> str:
    return f"""
    @font-face {{ font-family:'Script';   src:url('file:///{F_SCRIPT}')   format('truetype'); }}
    @font-face {{ font-family:'Headline'; src:url('file:///{F_HEADLINE}') format('truetype'); font-weight:bold; }}
    @font-face {{ font-family:'Body';     src:url('file:///{F_BODY}')     format('truetype'); }}
    @font-face {{ font-family:'Kicker';   src:url('file:///{F_KICKER}')   format('truetype'); font-style:italic; }}
    @font-face {{ font-family:'Label';    src:url('file:///{F_LABEL}')    format('truetype'); font-weight:bold; }}
    """


# ── Content slide HTML ─────────────────────────────────────────────────────────
def content_slide(slide: dict, img_uri: str) -> str:
    n        = slide["num"]
    total    = len(BEAT_PACK)
    headline = (slide.get("headline") or "").replace("\n", "<br>")
    body     = (slide.get("body") or "").replace("\n", "<br>")
    kicker   = slide.get("kicker") or ""
    label    = f"{CHANNEL_LABEL}  ·  {n:02d} of {total:02d}"

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts_css()}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:#000; }}

/* ── Layer 1: Full-bleed hero image ── */
.slide {{
    width:{W}px; height:{H}px; position:relative;
    background-image:url('{img_uri}');
    background-size:cover; background-position:center top;
}}

/* ── Layer 2: Dual tint — cool top shadow + warm bottom pool ── */
.tint-top {{
    position:absolute; inset:0; z-index:1;
    background:linear-gradient(to bottom,
        rgba(0,0,0,0.55) 0%,
        rgba(0,0,0,0.10) 38%,
        transparent 55%);
}}
.tint-bottom {{
    position:absolute; inset:0; z-index:2;
    background:linear-gradient(to top,
        rgba(0,0,0,0.92) 0%,
        rgba(0,0,0,0.72) 30%,
        rgba(0,0,0,0.30) 58%,
        transparent 78%);
}}

/* ── Layer 3: Accent color wash — bleeds brand color into scene ── */
.color-wash {{
    position:absolute; inset:0; z-index:3;
    background:linear-gradient(to top,
        {ACCENT}22 0%,
        {ACCENT}08 40%,
        transparent 65%);
}}

/* ── Frame: edge-only, never across image ── */
.frame {{
    position:absolute; inset:10px; z-index:8;
    border:1.5px solid rgba(255,255,255,0.18);
    pointer-events:none;
}}
/* Corner brackets — accent color, sharp */
.c {{
    position:absolute; width:24px; height:24px;
    border-color:{ACCENT}; border-style:solid; border-width:0;
    z-index:9;
}}
.tl {{ top:10px;  left:10px;  border-top-width:2.5px; border-left-width:2.5px; }}
.tr {{ top:10px;  right:10px; border-top-width:2.5px; border-right-width:2.5px; }}
.bl {{ bottom:10px; left:10px;  border-bottom-width:2.5px; border-left-width:2.5px; }}
.br {{ bottom:10px; right:10px; border-bottom-width:2.5px; border-right-width:2.5px; }}

/* ── Top label ── */
.label {{
    position:absolute; top:44px; left:50%; transform:translateX(-50%);
    font-family:'Label'; font-size:11px; letter-spacing:3px;
    color:rgba(255,255,255,0.45); text-transform:uppercase;
    z-index:5; white-space:nowrap;
}}

/* ── Script number — watermark style, bleeds off-bottom-left ── */
.number {{
    position:absolute; bottom:340px; left:28px;
    font-family:'Script'; font-size:220px; line-height:0.85;
    color:{ACCENT}; opacity:0.22; z-index:4;
    /* no text-shadow — opacity wash is the effect */
}}
/* Solid number layered on top for depth */
.number-solid {{
    position:absolute; bottom:352px; left:40px;
    font-family:'Script'; font-size:180px; line-height:0.85;
    color:{ACCENT}; opacity:0.90; z-index:5;
    filter:drop-shadow(0 4px 24px {ACCENT}66);
}}

/* ── Accent rule line above headline ── */
.rule {{
    width:48px; height:2.5px;
    background:{ACCENT};
    margin-bottom:18px;
    border-radius:2px;
}}

/* ── Text block — bottom-anchored ── */
.text-box {{
    position:absolute; bottom:56px; left:60px; right:60px; z-index:6;
}}
.headline {{
    font-family:'Headline'; font-size:74px; font-weight:bold;
    color:#fff; line-height:1.08; margin-bottom:22px;
    text-shadow: 0 2px 16px rgba(0,0,0,0.7), 0 1px 3px rgba(0,0,0,0.9);
}}
.body {{
    font-family:'Body'; font-size:31px;
    color:rgba(255,255,255,0.82); line-height:1.45;
    margin-bottom:22px;
    text-shadow: 0 1px 8px rgba(0,0,0,0.6);
}}
.kicker {{
    font-family:'Kicker'; font-size:36px; font-style:italic;
    color:{ACCENT}; line-height:1.25;
    padding-left:18px;
    border-left:3px solid {ACCENT};
    filter:drop-shadow(0 0 12px {ACCENT}55);
}}
</style></head><body>
<div class="slide">
    <div class="tint-top"></div>
    <div class="tint-bottom"></div>
    <div class="color-wash"></div>
    <div class="frame"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="label">{label}</div>
    <div class="number">{n}</div>
    <div class="number-solid">{n}</div>
    <div class="text-box">
        <div class="rule"></div>
        <div class="headline">{headline}</div>
        {'<div class="body">' + body + '</div>' if body else ''}
        {'<div class="kicker">' + kicker + '</div>' if kicker else ''}
    </div>
</div></body></html>"""


# ── CTA slide HTML ─────────────────────────────────────────────────────────────
def cta_slide() -> str:
    logo_uri = b64img(LOGO)

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts_css()}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:{BG}; }}

.slide {{
    width:{W}px; height:{H}px; position:relative;
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0;
}}

/* Subtle radial glow at center — brand warmth */
.bg-glow {{
    position:absolute; inset:0; z-index:0;
    background:radial-gradient(ellipse 70% 55% at 50% 50%,
        {ACCENT}18 0%, transparent 70%);
}}

/* Top + bottom accent bars */
.bar-top {{
    position:absolute; top:0; left:0; right:0; height:4px;
    background:linear-gradient(to right, transparent, {ACCENT}, transparent);
    z-index:1;
}}
.bar-bottom {{
    position:absolute; bottom:0; left:0; right:0; height:4px;
    background:linear-gradient(to right, transparent, {ACCENT}, transparent);
    z-index:1;
}}

/* Frame + corners */
.frame {{
    position:absolute; inset:10px; z-index:2;
    border:1.5px solid {ACCENT}55; pointer-events:none;
}}
.c {{
    position:absolute; width:28px; height:28px;
    border-color:{ACCENT}; border-style:solid; border-width:0; z-index:3;
}}
.tl {{ top:10px;  left:10px;  border-top-width:2.5px; border-left-width:2.5px; }}
.tr {{ top:10px;  right:10px; border-top-width:2.5px; border-right-width:2.5px; }}
.bl {{ bottom:10px; left:10px;  border-bottom-width:2.5px; border-left-width:2.5px; }}
.br {{ bottom:10px; right:10px; border-bottom-width:2.5px; border-right-width:2.5px; }}

/* Logo */
.logo-ring {{
    width:230px; height:230px; border-radius:50%;
    border:3px solid {ACCENT};
    box-shadow:0 0 40px {ACCENT}44, 0 8px 32px rgba(0,0,0,0.18);
    overflow:hidden; z-index:4; margin-bottom:36px;
    background:{BG};
    display:flex; align-items:center; justify-content:center;
}}
.logo-ring img {{ width:100%; height:100%; object-fit:cover; }}

.channel-name {{
    font-family:'Label'; font-size:13px; letter-spacing:3.5px;
    color:{TEXT}; opacity:0.45; text-transform:uppercase;
    z-index:4; margin-bottom:16px;
}}
.follow-script {{
    font-family:'Script'; font-size:108px; line-height:0.95;
    color:{TEXT}; z-index:4; margin-bottom:28px; text-align:center;
}}
.divider {{
    width:80px; height:2px; background:{ACCENT}; border-radius:1px;
    z-index:4; margin-bottom:28px;
    box-shadow:0 0 8px {ACCENT}88;
}}
.handle {{
    font-family:'Label'; font-size:28px; letter-spacing:2px;
    text-transform:uppercase; color:{ACCENT}; z-index:4;
}}
</style></head><body>
<div class="slide">
    <div class="bg-glow"></div>
    <div class="bar-top"></div><div class="bar-bottom"></div>
    <div class="frame"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="logo-ring">
        {'<img src="' + logo_uri + '" alt="Logo">' if logo_uri else ''}
    </div>
    <div class="channel-name">{CHANNEL_LABEL}</div>
    <div class="follow-script">Follow us</div>
    <div class="divider"></div>
    <div class="handle">{HANDLE}</div>
</div></body></html>"""


# ── Renderer ──────────────────────────────────────────────────────────────────
def render_slide(html: str, out_path: Path) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page    = browser.new_page(viewport={"width": W, "height": H})
        page.set_content(html, wait_until="networkidle")
        page.screenshot(path=str(out_path), full_page=False)
        browser.close()
    size_kb = out_path.stat().st_size // 1024
    print(f"[OK] {out_path.name}  ({size_kb} KB)")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"\n{'='*60}")
    print(f"[Channel] Carousel — [Episode Title]")
    print(f"Movement : [Movement Name]")
    print(f"Slides   : {len(BEAT_PACK)}")
    print(f"{'='*60}\n")

    # IMPORTANT for Gappu: pre-load all per-slide images before loop
    # For ObjectAI/Bhakti: load hero once
    hero_uri = b64img(HERO)   # single hero — ObjectAI / Bhakti
    # Gappu: use b64img(IMAGES / slide["image"]) inside the loop instead

    for slide in BEAT_PACK:
        out = SLIDES / f"slide_{slide['num']:02d}.png"
        if slide["arc"] == "CTA":
            html = cta_slide()
        else:
            # ObjectAI/Bhakti: pass hero_uri
            # Gappu: pass b64img(IMAGES / slide["image"])
            html = content_slide(slide, hero_uri)
        render_slide(html, out)

    print(f"\n[DONE] {len(BEAT_PACK)} slides → {SLIDES}\n")


if __name__ == "__main__":
    main()
```

---

## Channel-Specific Values to Inject

When writing generate_slides.py, inject these per channel:

### Gappu Magic Land
```python
LOGO  = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/gappuNewProfilePic.png")
# Image per slide (each slide has its own generated image):
img_b64 = b64img(IMAGES / slide["image"])   # slide["image"] = "slide_01.png" etc.
# Beat pack: 6 content slides + 1 CTA
# CHANNEL_LABEL = "GAPPU MAGIC  ·  0N of NN"
# HANDLE = "@gappumagicworld"
```

### ObjectAI
```python
LOGO = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png")
HERO = IMAGES / "hero.png"
# Single hero image used on ALL content slides:
img_b64 = b64img(HERO)
# Beat pack: N content slides (driven by content points) + 1 CTA
# CHANNEL_LABEL = "OBJECTAI  ·  0N of NN"
# HANDLE = "@objectwithbrainsai"
```

### Bhakti Channel (Sanatan Dharma)
```python
LOGO = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/657973132_18075711047188622_535010279705404318_n.jpg")
HERO = IMAGES / "hero.png"
# Single hero image used on ALL content slides:
img_b64 = b64img(HERO)
# Beat pack: N content slides (driven by content points) + 1 CTA
# CHANNEL_LABEL = "SANATAN DHARMA  ·  0N of NN"
# HANDLE = "@sanatandharmatheeternalpath"
```

### Future Channel (template)
```python
LOGO = Path("[logo path]")
HERO = IMAGES / "[hero filename]"
# CHANNEL_LABEL = "[CHANNEL_NAME]  ·  0N of NN"
# HANDLE = "@[handle]"
```

---

## STEP C — Run generate_slides.py

```bash
cd "D:\oldCOMPUTER\Videos\[Channel]\pipeline\carousel\YYYY-MM-DD_TopicName"
python generate_slides.py
```

**Prerequisites:**
- Hero image(s) must exist in `images/` folder BEFORE running
- `slides/` folder created automatically by script

**Verify output:**
- Check file sizes — each content slide typically 700KB–1.5MB (not <10KB)
- Read each slide PNG to confirm visual alignment
- Confirm script number and text are separated (not overlapping)
- Confirm CTA slide logo is visible

---

## STEP D — Verify Slides

After running, visually confirm each slide:

```
□ Hero image: full-bleed, fills entire canvas
□ Top shadow: upper area slightly darkened (label still readable)
□ Bottom pool: lower 70%+ deeply darkened — text fully legible
□ Color wash: faint ACCENT tint visible at very bottom of image
□ Ghost number: large faint watermark behind solid number (depth effect)
□ Solid number: ACCENT colored, glowing, not overlapping headline
□ Accent rule: short horizontal ACCENT line above headline
□ Headline: white, crisp, text-shadow giving depth — Devanagari/Latin correct
□ Body: slightly smaller, 82% white opacity
□ Kicker: italic, ACCENT color, glowing left border
□ Frame: near-invisible white edge border (18% opacity, inset 10px)
□ Corner brackets: ACCENT, solid, 4 corners
□ CTA slide: logo in glowing ring, radial glow on BG, ACCENT bars at top+bottom
```

If any slide fails → fix the CSS in `slide_html()` → re-run → re-verify.

---

## CSS Layer Stack (hardcoded — never change)

**Content slide:**
```
z-index 1: .tint-top      → cool shadow from top (0%→55%)
z-index 2: .tint-bottom   → deep pool from bottom (0%→78%) — primary legibility layer
z-index 3: .color-wash    → accent color bleed from bottom (brand warmth)
z-index 4: .number        → ghost watermark number (opacity 0.22)
z-index 5: .number-solid  → solid script number with glow (opacity 0.90)
z-index 5: .label         → top channel label (rgba white, 0.45 opacity)
z-index 6: .text-box      → rule + headline + body + kicker
z-index 8: .frame         → white 18% edge border
z-index 9: .c (corners)   → ACCENT corner brackets (topmost)
```

**CTA slide:**
```
z-index 0: .bg-glow       → radial ACCENT glow at center
z-index 1: .bar-top/bottom→ full-width ACCENT gradient bars at edges
z-index 2: .frame         → ACCENT 55% opacity edge border
z-index 3: .c (corners)   → solid ACCENT corner brackets
z-index 4: logo/text      → all content elements
```

---

## Font Rules (always apply)

- `NothingYouCouldDo-Regular.ttf` → Script number ONLY (always this font, no exceptions)
- Headline font → chosen per episode emotion from canvas-fonts
- Body font → clean, legible, not the same as headline
- Kicker font → italic variant of body OR CrimsonPro-Italic / InstrumentSerif-Italic
- Label font → bold sans (InstrumentSans-Bold or WorkSans-Bold)
- **NEVER use Google Fonts CDN** — local `file:///` paths only
- **NEVER use system fonts** — always explicit @font-face

---

## Common Fixes

| Problem | Fix |
|---------|-----|
| Script number overlaps headline | Increase `.number` bottom: value (e.g. 320px → 420px) |
| Text cut off at bottom | Decrease `.text-box` bottom: value |
| Image not showing | Check b64img path, confirm file exists |
| Font not rendering | Check file:/// path, confirm .ttf exists in canvas-fonts/ |
| Slide too dark | Reduce tint opacity (0.28 → 0.18) |
| Text hard to read | Increase gradient height (72% → 80%) |
| Print/emoji errors on Windows | Avoid emoji in print() — use [OK] prefix |
