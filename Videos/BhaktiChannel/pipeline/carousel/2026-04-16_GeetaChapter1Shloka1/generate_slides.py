"""
Bhakti Channel Carousel — Bespoke HTML Slide Generator
Story    : Bhagavad Gita — Chapter 1, Shloka 1
Movement : "Golden Dharma"
Fonts    : Hind-Bold (headline/label/kicker) + Hind-Regular (body) + NothingYouCouldDo (script number)
Canvas   : 1080 x 1350 px (4:5 portrait)
Renderer : Playwright Chromium
Language : Hindi (Devanagari)
"""

import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

# -- Paths -------------------------------------------------------------------
STORY  = Path(__file__).parent
IMAGES = STORY / "images"
SLIDES = STORY / "slides"
FONTS  = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
LOGO   = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/657973132_18075711047188622_535010279705404318_n.jpg")
HERO   = IMAGES / "hero.png"
SLIDES.mkdir(exist_ok=True)

W, H = 1080, 1350

# -- Color Palette (Golden Dharma) -------------------------------------------
BG     = "#212121"
TEXT   = "#FFD700"
ACCENT = "#B8860B"
WHITE  = "rgba(255,255,255,0.88)"

# -- Font paths (local — never CDN) ------------------------------------------
F_SCRIPT   = (FONTS / "NothingYouCouldDo-Regular.ttf").as_posix()
F_HEADLINE = (FONTS / "Hind-Bold.ttf").as_posix()
F_BODY     = (FONTS / "Hind-Regular.ttf").as_posix()
F_KICKER   = (FONTS / "Hind-Regular.ttf").as_posix()
F_LABEL    = (FONTS / "Hind-Bold.ttf").as_posix()

# -- Beat pack ---------------------------------------------------------------
TOTAL = 7
BEAT_PACK = [
    {
        "num": 1, "arc": "HOOK",
        "headline": "धर्मक्षेत्र कुरुक्षेत्र —\nयुद्ध का पहला क्षण",
        "body": "महाभारत के युद्ध से पहले धृतराष्ट्र ने\nसंजय से पूछा — मेरे और पांडु के पुत्र क्या कर रहे हैं?",
        "kicker": "यह प्रश्न एक अंधे राजा का नहीं, एक भयभीत पिता का था।"
    },
    {
        "num": 2, "arc": "SHLOKA",
        "headline": "श्लोक — अध्याय १, श्लोक १",
        "body": "धृतराष्ट्र उवाच —\nधर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः।\nमामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय॥",
        "kicker": "— श्रीमद्भगवद्गीता, अध्याय १, श्लोक १"
    },
    {
        "num": 3, "arc": "WORDS",
        "headline": "शब्दार्थ",
        "body": "धर्मक्षेत्रे = धर्म की भूमि पर  |  कुरुक्षेत्रे = कुरुक्षेत्र में\nयुयुत्सवः = युद्ध की इच्छा रखने वाले  |  मामकाः = मेरे (पुत्र)\nपाण्डवाः = पांडु के पुत्र  |  किम् = क्या  |  अकुर्वत = किया",
        "kicker": "हर शब्द एक संसार है।"
    },
    {
        "num": 4, "arc": "MEANING",
        "headline": "हिंदी अर्थ",
        "body": "धृतराष्ट्र ने कहा — हे संजय! धर्मभूमि कुरुक्षेत्र में\nएकत्रित हुए मेरे और पांडु के युद्धेच्छु पुत्रों ने क्या किया?",
        "kicker": "एक प्रश्न जिसने अठारह दिन के युद्ध को जन्म दिया।"
    },
    {
        "num": 5, "arc": "CONTEXT",
        "headline": "धृतराष्ट्र क्यों पूछ रहे थे?",
        "body": "धृतराष्ट्र जन्म से अंधे थे — वे युद्ध नहीं देख सकते थे।\nसंजय को दिव्यदृष्टि मिली थी — वे सब कुछ देख सकते थे।",
        "kicker": "यही संवाद गीता का आधार बना।"
    },
    {
        "num": 6, "arc": "INSIGHT",
        "headline": "गहरा अर्थ",
        "body": "धर्मक्षेत्र — यह केवल कुरुक्षेत्र नहीं, यह मनुष्य का अंतर्मन है।\nहर व्यक्ति के भीतर धर्म और अधर्म का युद्ध चलता है।",
        "kicker": "गीता का युद्ध बाहर नहीं, भीतर है।"
    },
    {
        "num": 7, "arc": "CTA",
        "headline": "Follow us",
        "body": None,
        "kicker": None
    },
]


# -- Helper: encode image as base64 ------------------------------------------
def b64img(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode() if path.exists() else ""


# -- Helper: @font-face CSS declarations -------------------------------------
def font_face_css() -> str:
    return f"""
    @font-face {{ font-family:'Script';   src:url('file:///{F_SCRIPT}')   format('truetype'); }}
    @font-face {{ font-family:'Headline'; src:url('file:///{F_HEADLINE}') format('truetype'); font-weight:bold; }}
    @font-face {{ font-family:'Body';     src:url('file:///{F_BODY}')     format('truetype'); }}
    @font-face {{ font-family:'Kicker';   src:url('file:///{F_KICKER}')   format('truetype'); font-style:italic; }}
    @font-face {{ font-family:'Label';    src:url('file:///{F_LABEL}')    format('truetype'); font-weight:bold; }}
    """


# -- Main generator: ONE function handles ALL slide types --------------------
def slide_html(slide: dict) -> str:
    n = slide["num"]
    fonts = font_face_css()

    # -- CTA slide -----------------------------------------------------------
    if slide["arc"] == "CTA":
        logo_b64 = b64img(LOGO)
        logo_ext = "jpeg" if str(LOGO).lower().endswith(".jpg") else "png"
        logo_img = f"data:image/{logo_ext};base64,{logo_b64}" if logo_b64 else ""
        return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:{BG}; }}
.slide {{
    width:{W}px; height:{H}px; position:relative;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
}}
.frame-outer {{ position:absolute; inset:12px; border:4px solid {ACCENT}; z-index:5; pointer-events:none; }}
.frame-inner {{ position:absolute; inset:28px; border:2px dashed {TEXT}; z-index:5; pointer-events:none; opacity:0.6; }}
.c {{ position:absolute; width:60px; height:60px; z-index:6; }}
.c::before {{ content:''; position:absolute; background:{ACCENT}; }}
.c::after  {{ content:''; position:absolute; background:{ACCENT}; }}
.tl {{ top:8px;    left:8px;    }}
.tl::before {{ width:60px; height:5px; top:0;    left:0; }}
.tl::after  {{ width:5px;  height:60px; top:0;  left:0; }}
.tr {{ top:8px;    right:8px;   }}
.tr::before {{ width:60px; height:5px; top:0;    right:0; }}
.tr::after  {{ width:5px;  height:60px; top:0;  right:0; }}
.bl {{ bottom:8px; left:8px;    }}
.bl::before {{ width:60px; height:5px; bottom:0; left:0; }}
.bl::after  {{ width:5px;  height:60px; bottom:0; left:0; }}
.br {{ bottom:8px; right:8px;   }}
.br::before {{ width:60px; height:5px; bottom:0; right:0; }}
.br::after  {{ width:5px;  height:60px; bottom:0; right:0; }}
.c-dot {{ position:absolute; width:14px; height:14px; background:{TEXT}; transform:rotate(45deg); z-index:7; }}
.c-dot.tl {{ top:12px;    left:12px;  }}
.c-dot.tr {{ top:12px;    right:12px; }}
.c-dot.bl {{ bottom:12px; left:12px;  }}
.c-dot.br {{ bottom:12px; right:12px; }}
.logo-wrap {{
    width:220px; height:220px; border-radius:50%;
    border:3px solid {ACCENT}; overflow:hidden;
    margin:0 auto 40px; box-shadow:0 10px 40px rgba(0,0,0,0.4);
}}
.logo-wrap img {{ width:100%; height:100%; object-fit:cover; }}
.channel {{ font-family:'Label'; font-size:14px; letter-spacing:3px; color:{TEXT}; opacity:0.55; text-transform:uppercase; margin-bottom:20px; }}
.tagline {{ font-family:'Script'; font-size:100px; color:{TEXT}; line-height:1; margin-bottom:24px; text-align:center; }}
.divider {{ width:60px; height:2px; background:{ACCENT}; margin-bottom:28px; }}
.handle {{ font-family:'Label'; font-size:26px; color:{ACCENT}; letter-spacing:1px; text-transform:uppercase; text-align:center; padding:0 40px; }}
</style></head><body>
<div class="slide">
    <div class="frame-outer"></div>
    <div class="frame-inner"></div>
    <div class="c tl"></div><div class="c tr"></div><div class="c bl"></div><div class="c br"></div>
    <div class="c-dot tl"></div><div class="c-dot tr"></div><div class="c-dot bl"></div><div class="c-dot br"></div>
    <div class="logo-wrap"><img src="{logo_img}" alt="Logo"></div>
    <div class="channel">सनातन धर्म</div>
    <div class="tagline">Follow us</div>
    <div class="divider"></div>
    <div class="handle">@sanatandharmatheeternalpath</div>
</div></body></html>"""

    # -- Content slide -------------------------------------------------------
    img_b64  = b64img(HERO)
    bg_css   = f"background-image:url('data:image/jpeg;base64,{img_b64}');background-size:cover;background-position:center 30%;" if img_b64 else f"background:{BG};"
    headline = slide["headline"].replace("\n", "<br>")
    body     = (slide.get("body") or "").replace("\n", "<br>")
    kicker   = slide.get("kicker") or ""
    label    = f"सनातन धर्म  ·  {n:02d} of {TOTAL}"

    # Shloka slide (arc == SHLOKA) gets slightly smaller headline for longer text
    hl_size = "52px" if slide["arc"] in ("SHLOKA", "WORDS") else "68px"
    body_size = "28px" if slide["arc"] in ("SHLOKA", "WORDS") else "32px"

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
{fonts}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; background:#000; }}

/* Layer 1: Full-bleed image */
.slide {{ width:{W}px; height:{H}px; position:relative; {bg_css} }}

/* Layer 2: Tint overlay */
.tint {{ position:absolute; inset:0; background:rgba(0,0,0,0.38); z-index:1; }}

/* Layer 3: Bottom gradient */
.grad {{
    position:absolute; bottom:0; left:0; right:0; height:75%;
    background:linear-gradient(to bottom, rgba(0,0,0,0), rgba(10,8,4,0.92));
    z-index:2;
}}

/* Outer border — thick solid gold */
.frame-outer {{ position:absolute; inset:12px; border:4px solid {ACCENT}; z-index:6; pointer-events:none; }}
/* Inner border — dashed gold, wide gap from outer */
.frame-inner {{ position:absolute; inset:28px; border:2px dashed {TEXT}; z-index:6; pointer-events:none; opacity:0.6; }}
/* Corner L-brackets — sit at very edge, cover both frame lines */
.c {{ position:absolute; width:60px; height:60px; z-index:8; }}
.c::before {{ content:''; position:absolute; background:{ACCENT}; }}
.c::after  {{ content:''; position:absolute; background:{ACCENT}; }}
.tl {{ top:8px;    left:8px;    }}
.tl::before {{ width:60px; height:5px; top:0;    left:0; }}
.tl::after  {{ width:5px;  height:60px; top:0;  left:0; }}
.tr {{ top:8px;    right:8px;   }}
.tr::before {{ width:60px; height:5px; top:0;    right:0; }}
.tr::after  {{ width:5px;  height:60px; top:0;  right:0; }}
.bl {{ bottom:8px; left:8px;    }}
.bl::before {{ width:60px; height:5px; bottom:0; left:0; }}
.bl::after  {{ width:5px;  height:60px; bottom:0; left:0; }}
.br {{ bottom:8px; right:8px;   }}
.br::before {{ width:60px; height:5px; bottom:0; right:0; }}
.br::after  {{ width:5px;  height:60px; bottom:0; right:0; }}
/* Diamond dots at corner tips */
.c-dot {{ position:absolute; width:14px; height:14px; background:{TEXT}; transform:rotate(45deg); z-index:9; }}
.c-dot.tl {{ top:12px;    left:12px;  }}
.c-dot.tr {{ top:12px;    right:12px; }}
.c-dot.bl {{ bottom:12px; left:12px;  }}
.c-dot.br {{ bottom:12px; right:12px; }}

/* Top label */
.label {{
    position:absolute; top:40px; left:50%; transform:translateX(-50%);
    font-family:'Label'; font-size:13px; letter-spacing:2px;
    color:{TEXT}; opacity:0.42; text-transform:uppercase; z-index:3; white-space:nowrap;
}}

/* Script number */
.number {{
    position:absolute; bottom:430px; left:40px;
    font-family:'Script'; font-size:190px; color:{ACCENT};
    line-height:0.9; z-index:3; opacity:0.75;
}}

/* Text block */
.text-box {{ position:absolute; bottom:60px; left:60px; right:60px; z-index:4; }}
.headline {{
    font-family:'Headline'; font-size:{hl_size}; font-weight:bold;
    color:{TEXT}; line-height:1.2; margin-bottom:20px;
}}
.body {{
    font-family:'Body'; font-size:{body_size}; color:{WHITE};
    opacity:0.88; line-height:1.5; margin-bottom:18px;
}}
.kicker {{
    font-family:'Kicker'; font-size:34px; font-style:italic;
    color:{ACCENT}; line-height:1.3; padding-left:16px;
    border-left:3px solid {ACCENT};
}}
</style></head><body>
<div class="slide">
    <div class="tint"></div>
    <div class="grad"></div>
    <div class="frame-outer"></div>
    <div class="frame-inner"></div>
    <div class="c tl"></div><div class="c tr"></div>
    <div class="c bl"></div><div class="c br"></div>
    <div class="c-dot tl"></div><div class="c-dot tr"></div>
    <div class="c-dot bl"></div><div class="c-dot br"></div>
    <div class="label">{label}</div>
    <div class="number">{n}</div>
    <div class="text-box">
        <div class="headline">{headline}</div>
        <div class="body">{body}</div>
        <div class="kicker">{kicker}</div>
    </div>
</div></body></html>"""


# -- Renderer ----------------------------------------------------------------
def render(html_content, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H})
        page.set_content(html_content)
        page.wait_for_timeout(300)
        page.screenshot(path=output_path, full_page=False)
        browser.close()
    print(f"[OK] {output_path.name}")


# -- Main --------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Bhakti Carousel -- Bhagavad Gita Chapter 1 Shloka 1")
    print("Movement: Golden Dharma")
    print("=" * 60)

    for slide in BEAT_PACK:
        html = slide_html(slide)
        render(html, SLIDES / f"slide_{slide['num']:02d}.png")

    print("=" * 60)
    print(f"All {len(BEAT_PACK)} slides rendered!")
    print(f"Output: {SLIDES}")
    print("=" * 60)


if __name__ == "__main__":
    main()
