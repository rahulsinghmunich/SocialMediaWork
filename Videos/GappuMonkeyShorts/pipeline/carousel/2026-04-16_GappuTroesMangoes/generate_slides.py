"""
Gappu Carousel — Bespoke HTML Slide Generator
Story    : Gappu Tries Mangoes for the First Time
Movement : "Golden Suspicion"
Fonts    : NothingYouCouldDo (script number) + Italiana (headline)
           CrimsonPro Italic (kicker) + InstrumentSans (body)
           All loaded LOCAL via @font-face — no Google Fonts CDN
Canvas   : 1080 x 1350 px (4:5 portrait)
Renderer : Playwright Chromium

Usage    : python generate_slides.py
"""

import base64, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

# ── Paths ──────────────────────────────────────────────────────────────────────
STORY      = Path(__file__).parent
IMAGES     = STORY / "images"
SLIDES     = STORY / "slides"
FONTS      = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
LOGO       = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/gappuNewProfilePic.png")
SLIDES.mkdir(exist_ok=True)

W, H = 1080, 1350

# ── Luxury_Gold palette ────────────────────────────────────────────────────────
BG     = "#212121"
TEXT   = "#FFD700"
ACCENT = "#B8860B"
WHITE  = "rgba(255,255,255,0.88)"

# ── Font file paths (local) ────────────────────────────────────────────────────
F_SCRIPT   = (FONTS / "NothingYouCouldDo-Regular.ttf").as_posix()
F_HEADLINE = (FONTS / "Italiana-Regular.ttf").as_posix()
F_KICKER   = (FONTS / "CrimsonPro-Italic.ttf").as_posix()
F_BODY     = (FONTS / "InstrumentSans-Regular.ttf").as_posix()
F_LABEL    = (FONTS / "InstrumentSans-Bold.ttf").as_posix()

# ── Beat pack ──────────────────────────────────────────────────────────────────
BEAT_PACK = [
    {"num": 1, "arc": "HOOK",     "headline": "What IS this thing?",         "image": "slide_01.png"},
    {"num": 2, "arc": "SETUP",    "headline": "It smells\u2026 suspicious.", "image": "slide_02.png"},
    {"num": 3, "arc": "TENSION",  "headline": "One brave little bite.",      "image": "slide_03.png"},
    {"num": 4, "arc": "STRUGGLE", "headline": "His brain stopped working.",  "image": "slide_04.png"},
    {"num": 5, "arc": "TURN",     "headline": "Oh. OH.",                     "image": "slide_05.png"},
    {"num": 6, "arc": "PAYOFF",   "headline": "Mangoes changed his life.",   "image": "slide_06.png"},
    {"num": 7, "arc": "CTA",      "headline": "Follow for more Gappu magic", "image": None},
]

# ── Per-slide copy ─────────────────────────────────────────────────────────────
COPY = {
    1: ("He'd never seen one before.\nHe stared at it for a very long time.",
        "Curiosity is the beginning of everything."),
    2: ("He sniffed it. Frowned. Sniffed again.\nThis thing had opinions.",
        "Some things smell like a decision waiting to happen."),
    3: ("Eyes shut. Heart pounding.\nOne tiny, terrifying bite.",
        "Bravery looks different at two feet tall."),
    4: ("Sweet. Sour. Both at once.\nHis whole face stopped working.",
        "Some flavours need a moment to land."),
    5: ("One more bite. Then another.\nHe couldn't stop.",
        "The best things always surprise you."),
    6: ("He held it above his head like a trophy.\nThe market watched. He didn't care.",
        "Mangoes didn't change. He did."),
}


def b64img(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_face_css() -> str:
    """Build @font-face declarations for all local fonts."""
    return f"""
    @font-face {{
        font-family: 'Script';
        src: url('file:///{F_SCRIPT}') format('truetype');
    }}
    @font-face {{
        font-family: 'Headline';
        src: url('file:///{F_HEADLINE}') format('truetype');
    }}
    @font-face {{
        font-family: 'Kicker';
        src: url('file:///{F_KICKER}') format('truetype');
        font-style: italic;
    }}
    @font-face {{
        font-family: 'Body';
        src: url('file:///{F_BODY}') format('truetype');
    }}
    @font-face {{
        font-family: 'Label';
        src: url('file:///{F_LABEL}') format('truetype');
        font-weight: bold;
    }}
    """


def slide_html(slide: dict) -> str:
    n   = slide["num"]
    img = slide["image"]

    # Background
    if img and (IMAGES / img).exists():
        data   = b64img(IMAGES / img)
        bg_css = f"background-image:url('data:image/png;base64,{data}');background-size:cover;background-position:center top;"
    else:
        bg_css = f"background-color:{BG};"

    fonts = font_face_css()

    # ── CTA slide ─────────────────────────────────────────────────────────────
    if slide["arc"] == "CTA":
        logo_b64 = b64img(LOGO) if LOGO.exists() else None
        logo_img = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""

        return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:{BG}; }}
.slide {{
    width:{W}px; height:{H}px; position:relative;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    {bg_css}
}}
/* Perimeter frame */
.frame {{
    position:absolute; inset:8px;
    border:1.5px solid {ACCENT};
    border-radius:2px; z-index:5; pointer-events:none;
}}
/* Corner brackets */
.c {{ position:absolute; width:28px; height:28px; z-index:6; }}
.tl {{ top:22px;  left:22px;  border-top:2px solid {TEXT}; border-left:2px solid {TEXT};  opacity:0.55; }}
.tr {{ top:22px;  right:22px; border-top:2px solid {TEXT}; border-right:2px solid {TEXT}; opacity:0.55; }}
.bl {{ bottom:22px; left:22px;  border-bottom:2px solid {TEXT}; border-left:2px solid {TEXT};  opacity:0.55; }}
.br {{ bottom:22px; right:22px; border-bottom:2px solid {TEXT}; border-right:2px solid {TEXT}; opacity:0.55; }}
/* Center content */
.center {{ position:relative; z-index:4; text-align:center; padding:0 80px; }}
/* Logo — circular profile pic */
.logo-wrap {{
    width:220px; height:220px;
    border-radius:50%;
    border:3px solid {ACCENT};
    overflow:hidden;
    margin:0 auto 32px;
    box-shadow: 0 0 40px rgba(184,134,11,0.35);
}}
.logo-wrap img {{
    width:100%; height:100%; object-fit:cover;
}}
.page-name {{
    font-family:'Label'; font-size:28px;
    color:rgba(255,255,255,0.55);
    letter-spacing:5px; text-transform:uppercase;
    margin-bottom:12px;
}}
.tagline {{
    font-family:'Script'; font-size:100px;
    color:{TEXT}; line-height:1;
    margin-bottom:24px;
    text-shadow: 0 2px 30px rgba(0,0,0,0.4);
}}
.divider {{
    width:55px; height:1.5px;
    background:{ACCENT}; margin:0 auto 24px;
}}
.handle {{
    font-family:'Label'; font-size:34px;
    color:{ACCENT}; letter-spacing:4px;
    text-transform:uppercase;
}}
/* Progress dots */
.dots {{
    position:absolute; bottom:80px;
    left:0; right:0;
    display:flex; justify-content:center; gap:10px; z-index:4;
}}
.dot {{
    width:8px; height:8px; border-radius:50%;
    background:{ACCENT}; opacity:0.35;
}}
.dot.on {{ background:{TEXT}; opacity:1; transform:scale(1.25); }}
</style></head><body>
<div class="slide">
    <div class="frame"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="center">
        <div class="logo-wrap"><img src="{logo_img}" /></div>
        <div class="page-name">Gappu Magic Land</div>
        <div class="tagline">Follow us</div>
        <div class="divider"></div>
        <div class="handle">@gappumagicworld</div>
    </div>
    <div class="dots">
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
        <div class="dot on"></div>
    </div>
</div></body></html>"""

    # ── Image slides 1–6 ──────────────────────────────────────────────────────
    body, kicker = COPY.get(n, ("", ""))
    body_html    = body.replace("\n", "<br>")
    num_str      = f"0{n}"

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:#000; }}

/* ── Layer 1: Full-bleed image ── */
.slide {{
    width:{W}px; height:{H}px;
    position:relative;
    {bg_css}
}}

/* ── Layer 2: Directional dark tint ── */
/* Overall subtle veil so image reads as moody editorial */
.tint {{
    position:absolute; inset:0;
    background:rgba(0,0,0,0.28);
    z-index:2;
}}

/* ── Layer 3: Bottom gradient — transparent → near-black ── */
.grad {{
    position:absolute; bottom:0; left:0; right:0;
    height:72%;
    background:linear-gradient(
        to bottom,
        rgba(0,0,0,0)    0%,
        rgba(0,0,0,0.52) 30%,
        rgba(0,0,0,0.93) 100%
    );
    z-index:3;
}}

/* ── Perimeter border frame — edge only, never over image content ── */
.frame {{
    position:absolute; inset:8px;
    border:1.5px solid {ACCENT};
    border-radius:2px;
    z-index:6; pointer-events:none;
}}
/* Corner brackets at canvas corners */
.c {{ position:absolute; width:26px; height:26px; z-index:7; }}
.tl {{ top:20px;  left:20px;  border-top:2px solid {TEXT}; border-left:2px solid {TEXT};  opacity:0.50; }}
.tr {{ top:20px;  right:20px; border-top:2px solid {TEXT}; border-right:2px solid {TEXT}; opacity:0.50; }}
.bl {{ bottom:20px; left:20px;  border-bottom:2px solid {TEXT}; border-left:2px solid {TEXT};  opacity:0.50; }}
.br {{ bottom:20px; right:20px; border-bottom:2px solid {TEXT}; border-right:2px solid {TEXT}; opacity:0.50; }}

/* ── Top label: "GAPPU MAGIC  ·  01 OF 06" ── */
.top-label {{
    position:absolute; top:46px; left:0; right:0;
    text-align:center; z-index:5;
    font-family:'Label'; font-size:20px;
    letter-spacing:6px; text-transform:uppercase;
    color:rgba(255,255,255,0.42);
}}

/* ── Layer 4: Text block — bottom-left anchored ── */
.text-block {{
    position:absolute;
    bottom:64px; left:62px; right:62px;
    z-index:5; text-align:left;
}}

/* Large handwritten number — the soul of the slide */
.script-num {{
    font-family:'Script';
    font-size:188px;
    color:{TEXT};
    line-height:0.92;
    margin-bottom:8px;
    display:block;
    text-shadow:
        0 2px 8px rgba(0,0,0,0.6),
        0 0  40px rgba(184,134,11,0.25);
}}

/* Headline — tall elegant Italiana */
.headline {{
    font-family:'Headline';
    font-size:72px;
    color:{TEXT};
    line-height:1.15;
    letter-spacing:1px;
    margin-bottom:18px;
    text-shadow: 0 2px 12px rgba(0,0,0,0.7);
}}

/* Body copy — quiet, light InstrumentSans */
.body {{
    font-family:'Body';
    font-size:32px;
    color:{WHITE};
    line-height:1.65;
    margin-bottom:24px;
    font-weight:normal;
}}

/* Kicker — CrimsonPro Italic, gold, left border */
.kicker {{
    font-family:'Kicker';
    font-style:italic;
    font-size:38px;
    color:{TEXT};
    line-height:1.4;
    border-left:3px solid {ACCENT};
    padding-left:20px;
    opacity:0.95;
}}
</style></head><body>
<div class="slide">
    <div class="tint"></div>
    <div class="grad"></div>
    <div class="frame"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="top-label">Gappu Magic &nbsp;&nbsp;·&nbsp;&nbsp; 0{n} of 06</div>
    <div class="text-block">
        <span class="script-num">{num_str}</span>
        <div class="headline">{slide['headline']}</div>
        <div class="body">{body_html}</div>
        <div class="kicker">{kicker}</div>
    </div>
</div></body></html>"""


def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page    = browser.new_page(viewport={"width": W, "height": H})

        for slide in BEAT_PACK:
            n        = slide["num"]
            out_path = SLIDES / f"slide_{n:02d}.png"

            html = slide_html(slide)

            with tempfile.NamedTemporaryFile(
                    suffix=".html", delete=False, mode="w", encoding="utf-8") as f:
                f.write(html)
                tmp = f.name

            page.goto(f"file:///{tmp}", wait_until="networkidle")
            page.wait_for_timeout(1000)   # local fonts need a beat to load
            page.screenshot(path=str(out_path),
                            clip={"x": 0, "y": 0, "width": W, "height": H})
            Path(tmp).unlink(missing_ok=True)

            kb = out_path.stat().st_size // 1024
            print(f"  [{slide['arc']:8s}] slide_{n:02d}.png  {kb} KB")

        browser.close()
    print(f"\nDone — {len(BEAT_PACK)} slides in {SLIDES}")


if __name__ == "__main__":
    run()
