#!/usr/bin/env python3
"""
ObjectAi Carousel — Clove Teeth Protection
Movement: Herbalist's Wisdom
Design Palette: Earthy Green (BG #E8F5E9, TEXT #1B5E20, ACCENT #81C784)
Fonts: Hind-Bold, Hind-Regular, NothingYouCouldDo (local, no CDN)
Canvas: 1080 x 1350 px (4:5 portrait)
Renderer: Playwright Chromium → PNG
"""

import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

# ── Paths ──────────────────────────────────────────────────────────────────────
STORY  = Path(__file__).parent
IMAGES = STORY / "images"
SLIDES = STORY / "slides"
FONTS  = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
LOGO   = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png")
HERO   = IMAGES / "hero.png"
SLIDES.mkdir(exist_ok=True)

W, H = 1080, 1350

# ── Color Palette: Earthy Green ────────────────────────────────────────────────
BG     = "#E8F5E9"
TEXT   = "#1B5E20"
ACCENT = "#81C784"
WHITE  = "rgba(255,255,255,0.88)"

# ── Font paths (local) ──────────────────────────────────────────────────────────
F_SCRIPT   = (FONTS / "NothingYouCouldDo-Regular.ttf").as_posix()
F_HEADLINE = (FONTS / "Hind-Bold.ttf").as_posix()
F_BODY     = (FONTS / "Hind-Regular.ttf").as_posix()
F_LABEL    = (FONTS / "Hind-Bold.ttf").as_posix()

# ── Beat pack ───────────────────────────────────────────────────────────────────
BEAT_PACK = [
    {
        "num": 1,
        "arc": "HOOK",
        "headline": "लौंग सिर्फ मसाला नहीं,\nदांतों की ताकत है",
        "body": "एक छोटा सा दाना, बड़ी ताकत।",
        "kicker": "स्वाद और सेहत एक साथ।"
    },
    {
        "num": 2,
        "arc": "FACT",
        "headline": "यूजेनॉल नामक तत्व\nदर्द को सुन्न करता है",
        "body": "लौंग में छिपा प्राकृतिक दर्द निवारक।",
        "kicker": "विज्ञान मिलता है परंपरा से।"
    },
    {
        "num": 3,
        "arc": "FACT",
        "headline": "बैक्टीरिया को मारती है\nप्राकृतिक एंटीसेप्टिक",
        "body": "संक्रमण से रक्षा, बिना दुष्प्रभाव के।",
        "kicker": "प्रकृति का अपना फार्मेसी।"
    },
    {
        "num": 4,
        "arc": "FACT",
        "headline": "मसूड़ों की सूजन\nकम करती है",
        "body": "स्वस्थ मुंह, खुशी की हंसी।",
        "kicker": "सूजन गायब, दांत मजबूत।"
    },
    {
        "num": 5,
        "arc": "FACT",
        "headline": "दांतों के कीड़ों को\nरोकती है",
        "body": "प्राकृतिक सुरक्षा, हर दिन।",
        "kicker": "कैविटी से बचाव, सदियों से।"
    },
    {
        "num": 6,
        "arc": "PAYOFF",
        "headline": "हजारों साल पुराना\nआयुर्वेदिक उपाय",
        "body": "समय ने साबित किया, परंपरा सही है।",
        "kicker": "विश्वास और विज्ञान का मिलन।"
    },
    {
        "num": 7,
        "arc": "CTA",
        "headline": "और जानने के लिए\nहमें फॉलो करें",
        "body": None,
        "kicker": None
    }
]


def b64img(path: Path) -> str:
    """Encode image as base64."""
    return base64.b64encode(path.read_bytes()).decode() if path.exists() else ""


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
        font-weight: bold;
    }}
    @font-face {{
        font-family: 'Body';
        src: url('file:///{F_BODY}') format('truetype');
        font-weight: normal;
    }}
    @font-face {{
        font-family: 'Label';
        src: url('file:///{F_LABEL}') format('truetype');
        font-weight: bold;
    }}
    """


def slide_html(slide: dict) -> str:
    """Generate HTML for any slide (content or CTA)."""
    n = slide["num"]

    # Hero image background
    hero_b64 = b64img(HERO)
    bg_css = f"background-image:url('data:image/png;base64,{hero_b64}');background-size:cover;background-position:center;" if hero_b64 else ""

    fonts = font_face_css()

    # ── CTA Slide ──────────────────────────────────────────────────────────────
    if slide["arc"] == "CTA":
        logo_b64 = b64img(LOGO)
        logo_img = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""

        return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:{BG}; }}
.slide {{
    width:{W}px; height:{H}px; position:relative;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
}}
/* Perimeter frame */
.frame {{
    position:absolute; inset:8px; border:2px solid {ACCENT};
    z-index:5; pointer-events:none;
}}
/* Corner brackets */
.c {{ position:absolute; width:22px; height:22px; border:2px solid {ACCENT}; z-index:6; }}
.tl {{ top:-2px; left:-2px; border-right:none; border-bottom:none; }}
.tr {{ top:-2px; right:-2px; border-left:none; border-bottom:none; }}
.bl {{ bottom:-2px; left:-2px; border-right:none; border-top:none; }}
.br {{ bottom:-2px; right:-2px; border-left:none; border-top:none; }}
/* Logo circle */
.logo-wrap {{
    width:220px; height:220px; border-radius:50%;
    border:3px solid {ACCENT}; overflow:hidden; margin:0 auto 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1); z-index:2;
}}
.logo-wrap img {{ width:100%; height:100%; object-fit:contain; }}
/* Channel label */
.channel {{
    font-family:'Label'; font-size:14px; font-weight:bold;
    letter-spacing:2px; color:{TEXT}; opacity:0.58;
    text-transform:uppercase; margin-bottom:20px; z-index:2;
}}
/* CTA headline */
.cta-headline {{
    font-family:'Headline'; font-size:54px; font-weight:bold;
    color:{TEXT}; text-align:center; margin-bottom:30px; z-index:2;
    line-height:1.2;
}}
/* Divider */
.divider {{
    width:60px; height:2px; background:{ACCENT};
    margin-bottom:30px; z-index:2;
}}
/* Handle */
.handle {{
    font-family:'Label'; font-size:32px; font-weight:bold;
    color:{ACCENT}; letter-spacing:1px; z-index:2;
}}
</style></head><body>
<div class="slide">
    <div class="frame"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="logo-wrap"><img src="{logo_img}" alt="Logo"></div>
    <div class="channel">ObjectAi · सीखें</div>
    <div class="cta-headline">और जानने के लिए<br/>हमें फॉलो करें</div>
    <div class="divider"></div>
    <div class="handle">@objectwithbrainsai</div>
</div>
</body></html>"""

    # ── Content Slides 1–6 ─────────────────────────────────────────────────────
    headline = slide["headline"].replace("\n", "<br>")
    body = slide.get("body", "")
    kicker = slide.get("kicker", "")
    label = f"OBJECTAI · {n:02d} का {len(BEAT_PACK)}"

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:#000; }}

/* Layer 1: Full-bleed image */
.slide {{
    width:{W}px; height:{H}px; position:relative;
    {bg_css} background-size:cover; background-position:center;
}}

/* Layer 2: Tint overlay */
.tint {{
    position:absolute; inset:0; background:rgba(0,0,0,0.28); z-index:1;
}}

/* Layer 3: Bottom gradient */
.grad {{
    position:absolute; bottom:0; left:0; right:0; height:810px;
    background:linear-gradient(to bottom,
        rgba(0,0,0,0),
        rgba(0,0,0,0.85));
    z-index:2;
}}

/* Border frame */
.frame {{
    position:absolute; inset:8px; border:2px solid {ACCENT};
    z-index:1.5; pointer-events:none;
}}

/* Corner brackets */
.c {{ position:absolute; width:22px; height:22px; border:2px solid {ACCENT}; z-index:2; }}
.tl {{ top:-2px; left:-2px; border-right:none; border-bottom:none; }}
.tr {{ top:-2px; right:-2px; border-left:none; border-bottom:none; }}
.bl {{ bottom:-2px; left:-2px; border-right:none; border-top:none; }}
.br {{ bottom:-2px; right:-2px; border-left:none; border-top:none; }}

/* Top label */
.label {{
    position:absolute; top:40px; left:50%; transform:translateX(-50%);
    font-family:'Label'; font-size:12px; font-weight:bold;
    letter-spacing:2px; color:{TEXT}; opacity:0.42;
    text-transform:uppercase; z-index:3;
}}

/* Script number */
.number {{
    position:absolute; bottom:420px; left:40px;
    font-family:'Script'; font-size:200px; font-weight:normal;
    color:{ACCENT}; line-height:0.9; z-index:3; opacity:0.85;
}}

/* Text box */
.text-box {{
    position:absolute; bottom:60px; left:60px; right:60px; z-index:4;
}}

.headline {{
    font-family:'Headline'; font-size:72px; font-weight:bold;
    color:{WHITE}; line-height:1.1; margin-bottom:24px;
}}

.body {{
    font-family:'Body'; font-size:32px; font-weight:normal;
    color:{WHITE}; line-height:1.3; margin-bottom:20px; opacity:0.88;
}}

.kicker {{
    font-family:'Body'; font-size:38px; font-style:italic;
    color:{ACCENT}; line-height:1.2;
    padding-left:16px; border-left:3px solid {ACCENT};
}}
</style></head><body>
<div class="slide">
    <div class="tint"></div>
    <div class="grad"></div>
    <div class="frame">
        <div class="c tl"></div><div class="c tr"></div>
        <div class="c bl"></div><div class="c br"></div>
    </div>
    <div class="label">{label}</div>
    <div class="number">{n}</div>
    <div class="text-box">
        <div class="headline">{headline}</div>
        <div class="body">{body}</div>
        <div class="kicker">{kicker}</div>
    </div>
</div>
</body></html>"""


def render(html_content, output_path):
    """Render HTML to PNG using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H})
        page.set_content(html_content)
        page.screenshot(path=output_path, full_page=False)
        browser.close()
    print(f"[OK] {output_path.name}")


def main():
    print(f"\n{'='*60}")
    print("ObjectAi Carousel — Clove Teeth Protection")
    print("Movement: Herbalist's Wisdom")
    print(f"{'='*60}\n")

    for slide in BEAT_PACK:
        html = slide_html(slide)
        output = SLIDES / f"slide_{slide['num']:02d}.png"
        render(html, output)

    print(f"\n{'='*60}")
    print(f"All {len(BEAT_PACK)} slides rendered!")
    print(f"Output: {SLIDES}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
