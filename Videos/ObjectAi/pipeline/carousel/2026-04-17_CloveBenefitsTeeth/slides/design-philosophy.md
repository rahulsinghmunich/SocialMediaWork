# Design Philosophy: Ayurvedic Warmth

## Movement Name
**Ayurvedic Warmth** — a design language that honors traditional healing wisdom through modern, accessible visuals.

## Space
The hero image (clove + tooth characters) dominates the full canvas — 1080×1350px, full-bleed. No cropping, no inset. The characters deserve to breathe, to feel present. A dark tint overlay (rgba 0.28) ensures text legibility without hiding the warm golden lighting of the original render. The bottom 72% fades via gradient from transparent to near-black, creating a natural reading platform for the Hindi text.

## Color
Sunset_Orange palette selected for its connection to warmth, health, and traditional Indian spices:
- **Background:** `#FFF5F0` — a soft cream with peach undertones, like turmeric milk
- **Text:** `#2D2D2D` — near-black, but softer than pure black for extended reading
- **Accent:** `#E65100` — deep orange, echoing the clove's natural warmth and ayurvedic fire

The accent color appears only in the kicker border (3px left) and the script number opacity — restrained, intentional.

## Typography
Hindi content demands Devanagari-optimized fonts:
- **Headline:** `Hind-Bold.ttf` — clean, modern Devanagari, excellent screen rendering at 72px
- **Body:** `Hind-Regular.ttf` — highly legible at 34px for 2-line body copy
- **Script Number:** `NothingYouCouldDo-Regular.ttf` — calligraphic Latin numerals (180px, bottom-left), adding artistic flair
- **Kicker:** `CrimsonPro-Italic.ttf` — Latin italic for the English handle on CTA, creating bilingual harmony
- **Label:** `Hind-Bold.ttf` — small caps, top center, letter-spaced ("OBJECTAI · 01 of 05")

Font pair reasoning: Hind family was designed specifically for Devanagari script on digital screens. The bold weight carries authority for headlines; the regular weight reads effortlessly for body copy. NothingYouCouldDo adds the human touch — a handwritten number that says "crafted with care."

## Hierarchy
Top-to-bottom flow:
1. **Label** (top center, opacity 0.42) — subtle branding, never distracting
2. **Script Number** (bottom-left, 180px) — the visual anchor, calligraphic art
3. **Headline** (below number, 72px) — the main truth, bold and clear
4. **Body Copy** (2 lines max, 34px) — supporting detail, quiet and legible
5. **Kicker** (italic, accent border, 36px) — the emotional turn, the takeaway

Each slide follows this rhythm. The eye enters at the number, rises to the headline, settles on the body, and rests on the kicker.

## Craftsmanship
The border frame is critical: `inset: 8px` means the line lives at the very edge — like a picture frame, never crossing the characters. Corner brackets (22px, accent color) mark the four corners with precision. This is not decoration; it is structure.

The gradient rises from 72% canvas height — enough to support text, not so much that it drowns the hero. Tint at 0.28 balances legibility with image visibility.

For this clove benefits carousel, the design should feel like *a wise friend sharing home remedies* — not a clinic, not a textbook. Warm colors, soft edges, generous whitespace. The hero image (clove character touching tooth character) tells the story; the design simply frames it with care.

## Canvas Element (Optional)
For enhanced visual depth, a canvas-design overlay could add:
- **Element:** Nutrient molecule pattern or spice texture
- **Style:** Botanical Art Nouveau
- **Opacity:** 12–15% (subtle enrichment)
- **Placement:** Between hero image and tint layer
- **Purpose:** Educational texture without distraction
