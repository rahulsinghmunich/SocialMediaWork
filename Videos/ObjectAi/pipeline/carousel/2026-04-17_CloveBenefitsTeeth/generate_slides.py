#!/usr/bin/env python3
"""
ObjectAi Carousel — Clove Benefits for Teeth (लौंग के दांतों के लिए लाभ)
Design Philosophy: Ayurvedic Warmth
Layout: Soft_Blob | Palette: Sunset_Orange | Fonts: Hind (Devanagari)
"""

from pathlib import Path
from playwright.sync_api import sync_playwright

STORY = Path(__file__).parent
IMAGES = STORY / "images"
SLIDES = STORY / "slides"
FONTS = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
HERO = IMAGES / "hero.png"

W, H = 1080, 1350

# Color Palette — Sunset_Orange
BG_HEX = "#FFF5F0"
TEXT_HEX = "#2D2D2D"
ACCENT_HEX = "#E65100"

# Beat Pack — 5 content slides + 1 CTA
BEAT_PACK = [
    {"num": 1, "arc": "HOOK", "headline": "लौंग: दांतों का प्राकृतिक दर्द निवारक", "image": "hero.png"},
    {"num": 2, "arc": "BODY", "headline": "कीटाणुओं से लड़ने की शक्ति", "image": "hero.png"},
    {"num": 3, "arc": "BODY", "headline": "मसूड़ों को मजबूत बनाता है", "image": "hero.png"},
    {"num": 4, "arc": "BODY", "headline": "दांत दर्द में तुरंत राहत", "image": "hero.png"},
    {"num": 5, "arc": "BODY", "headline": "सांसों को ताजा रखे", "image": "hero.png"},
    {"num": 6, "arc": "CTA", "headline": "Follow for more ObjectAi", "image": None},
]

COPY = {
    1: ("लौंग में यूजेनॉल होता है जो दर्द को सुन्न करता है।\nयह मसूड़ों की सूजन भी कम करता है।", "प्राकृतिक राहत, बिना किसी रसायन के"),
    2: ("लौंग के तेल में एंटी-बैक्टीरियल गुण होते हैं\nजो मुंह के कीटाणुओं को मारते हैं।", "स्वस्थ मुंह, स्वस्थ दांत"),
    3: ("रोजाना लौंग का उपयोग मसूड़ों को ताकत देता है\nऔर खून आना बंद करता है।", "मजबूत मसूड़े, मजबूत दांत"),
    4: ("लौंग को पीसकर पेस्ट बनाएं और दर्द वाले दांत पर लगाएं —\n10 मिनट में आराम।", "घरेलू उपाय, त्वरित परिणाम"),
    5: ("लौंग चबाने से मुंह की दुर्गंध मिटती है\nऔर सांसें ताजा रहती हैं।", "ताजी सांसें, आत्मविश्वास"),
    6: ("", "@objectwithbrainsai"),
}

def b64img(path: Path) -> str:
    import base64
    ext = path.suffix.lower()
    if ext == ".png":
        mime = "image/png"
    elif ext == ".jpg" or ext == ".jpeg":
        mime = "image/jpeg"
    else:
        mime = "image/png"
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode()

def generate_slides():
    hero_b64 = b64img(HERO)

    html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>ObjectAi — Clove Benefits Carousel</title>
    <style>
        @font-face {{
            font-family: 'Headline';
            src: url('file:///{FONTS / 'Hind-Bold.ttf'}') format('truetype');
            font-weight: bold;
            unicode-range: U+0900-097F;
        }}
        @font-face {{
            font-family: 'Body';
            src: url('file:///{FONTS / 'Hind-Regular.ttf'}') format('truetype');
            font-weight: normal;
            unicode-range: U+0900-097F;
        }}
        @font-face {{
            font-family: 'Script';
            src: url('file:///{FONTS / 'NothingYouCouldDo-Regular.ttf'}') format('truetype');
        }}
        @font-face {{
            font-family: 'Kicker';
            src: url('file:///{FONTS / 'CrimsonPro-Italic.ttf'}') format('truetype');
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        .slide {{
            width: {W}px;
            height: {H}px;
            position: relative;
            overflow: hidden;
            font-family: 'Body', sans-serif;
        }}

        /* Layer 1: Full-bleed hero image */
        .hero-layer {{
            position: absolute;
            inset: 0;
            background-image: url({hero_b64});
            background-size: cover;
            background-position: center;
        }}

        /* Layer 2: Dark tint overlay */
        .tint-layer {{
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.28);
        }}

        /* Layer 3: Bottom gradient */
        .gradient-layer {{
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: {int(H * 0.72)}px;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.65) 40%, transparent 100%);
        }}

        /* Layer 4: Typography */
        .type-layer {{
            position: absolute;
            inset: 0;
            padding: 60px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }}

        /* Label — top center */
        .label {{
            position: absolute;
            top: 40px;
            left: 50%;
            transform: translateX(-50%);
            font-family: 'Headline', sans-serif;
            font-size: 11px;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: {TEXT_HEX};
            opacity: 0.42;
        }}

        /* Script number — bottom-left */
        .script-number {{
            font-family: 'Script', cursive;
            font-size: 180px;
            color: {TEXT_HEX};
            opacity: 0.85;
            line-height: 1;
            margin-bottom: 20px;
        }}

        /* Headline */
        .headline {{
            font-family: 'Headline', sans-serif;
            font-size: 72px;
            font-weight: bold;
            color: {TEXT_HEX};
            line-height: 1.15;
            margin-bottom: 24px;
        }}

        /* Body copy */
        .body {{
            font-family: 'Body', sans-serif;
            font-size: 34px;
            color: {TEXT_HEX};
            line-height: 1.5;
            margin-bottom: 28px;
            white-space: pre-line;
        }}

        /* Kicker */
        .kicker {{
            font-family: 'Kicker', serif;
            font-size: 36px;
            font-style: italic;
            color: {ACCENT_HEX};
            border-left: 3px solid {ACCENT_HEX};
            padding-left: 16px;
        }}

        /* Border frame — edge only */
        .border-frame {{
            position: absolute;
            inset: 8px;
            border: 2px solid {ACCENT_HEX};
            pointer-events: none;
        }}

        /* Corner brackets */
        .corner-bracket {{
            position: absolute;
            width: 22px;
            height: 22px;
            border-color: {ACCENT_HEX};
            border-style: solid;
            border-width: 0;
        }}
        .corner-bracket.tl {{ top: 8px; left: 8px; border-top-width: 3px; border-left-width: 3px; }}
        .corner-bracket.tr {{ top: 8px; right: 8px; border-top-width: 3px; border-right-width: 3px; }}
        .corner-bracket.bl {{ bottom: 8px; left: 8px; border-bottom-width: 3px; border-left-width: 3px; }}
        .corner-bracket.br {{ bottom: 8px; right: 8px; border-bottom-width: 3px; border-right-width: 3px; }}

        /* CTA slide specific */
        .cta-slide {{
            background: {BG_HEX};
        }}
        .cta-slide .hero-layer,
        .cta-slide .tint-layer,
        .cta-slide .gradient-layer {{
            display: none;
        }}
        .cta-content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            gap: 24px;
        }}
        .logo-circle {{
            width: 220px;
            height: 220px;
            border-radius: 50%;
            border: 3px solid {ACCENT_HEX};
            box-shadow: 0 4px 12px rgba(230, 81, 0, 0.3);
            background: {BG_HEX};
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Script', cursive;
            font-size: 80px;
            color: {ACCENT_HEX};
        }}
        .channel-label {{
            font-family: 'Headline', sans-serif;
            font-size: 12px;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: {TEXT_HEX};
            opacity: 0.5;
        }}
        .follow-text {{
            font-family: 'Script', cursive;
            font-size: 64px;
            color: {TEXT_HEX};
        }}
        .divider {{
            width: 120px;
            height: 2px;
            background: {ACCENT_HEX};
        }}
        .handle {{
            font-family: 'Headline', sans-serif;
            font-size: 16px;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: {ACCENT_HEX};
        }}
    </style>
</head>
<body>
"""

    for i, beat in enumerate(BEAT_PACK):
        num = beat["num"]
        arc = beat["arc"]
        headline = beat["headline"]
        body, kicker = COPY.get(num, ("", ""))

        if arc == "CTA":
            html += f"""
    <div class="slide cta-slide">
        <div class="border-frame"></div>
        <div class="corner-bracket tl"></div>
        <div class="corner-bracket tr"></div>
        <div class="corner-bracket bl"></div>
        <div class="corner-bracket br"></div>
        <div class="cta-content">
            <div class="logo-circle">OA</div>
            <div class="channel-label">ObjectAi</div>
            <div class="follow-text">Follow us</div>
            <div class="divider"></div>
            <div class="handle">@objectwithbrainsai</div>
        </div>
    </div>
"""
        else:
            html += f"""
    <div class="slide">
        <div class="hero-layer"></div>
        <div class="tint-layer"></div>
        <div class="gradient-layer"></div>
        <div class="type-layer">
            <div class="label">OBJECTAI · {num:02d} of {len(BEAT_PACK):02d}</div>
            <div class="script-number">{num}</div>
            <div class="headline">{headline}</div>
            <div class="body">{body}</div>
            <div class="kicker">{kicker}</div>
        </div>
        <div class="border-frame"></div>
        <div class="corner-bracket tl"></div>
        <div class="corner-bracket tr"></div>
        <div class="corner-bracket bl"></div>
        <div class="corner-bracket br"></div>
    </div>
"""

    html += "</body></html>"

    # Render slides via Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": W, "height": H})

        # Write HTML to temp file
        html_path = STORY / "slides_temp.html"
        html_path.write_text(html, encoding="utf-8")
        page.goto(f"file:///{html_path}")

        for i, beat in enumerate(BEAT_PACK):
            num = beat["num"]
            slide_path = SLIDES / f"slide_{num:02d}.png"
            page.screenshot(path=str(slide_path), full_page=False)
            print(f"Saved: {slide_path} ({slide_path.stat().st_size} bytes)")

        browser.close()
        html_path.unlink()

    print(f"\n✓ Generated {len(BEAT_PACK)} slides")

if __name__ == "__main__":
    generate_slides()
