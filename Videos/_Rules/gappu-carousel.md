# Rule: Gappu Carousel Pipeline
**Project:** Gappu Magic Land | **Instagram:** @gappumagicworld | **Facebook:** Gappu Magic Story Land
**Activate:** "activate gappu carousel" | **Reference:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\CLAUDE.md`

---

## Pipeline Steps (Reference carousel-slide-generation.md for Steps 0-D)

1. **Content Points** → Extract from script/notes (5-7 slides + CTA)
2. **Hero Images** → Nano Banana 2 (4:5, 1080×1350, per-slide images NOT single hero)
3. **Design Selection** → Use Design Matrix below (roll per story arc)
4. **Manifesto** → Write `slides/design-philosophy.md`
5. **Slides** → Run `generate_slides.py` via Playwright
6. **Caption** → Instagram + Facebook

---

## Design Randomness Engine — Gappu Aesthetic

**Designer Intelligence:** Gappu carousels must feel *playful, wonder-filled, toddler-perspective* — warm colors, soft edges, generous whitespace.

### Compact Design Matrix (3-line format)

```
Wonder/Discovery→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Pastel_Pink|Blob opacity 0.6, sparkle dots CSS
Problem/Confusion→Brutalist_Box|SpaceGrotesk+DMMono+NothingYouCouldDo|Dark_Tech|Box shadow 8px, gradient 75%
Joy/Celebration→Neon_Marquee|BigShoulders-Bold+InstrumentSans+NothingYouCouldDo|Sunset_Orange|Neon glow border, scrapbook ±3deg
Lesson/Wisdom→Minimal_Border|Lora+InstrumentSans+NothingYouCouldDo|Minimal_Cream|Padding 80px, tint 0.18
Adventure/Action→Editorial_Split|BricolageGrotesque-Bold+WorkSans+NothingYouCouldDo|Neon_Cyber|Diagonal 15deg, motion-lines CSS
Friendship/Connection→Centered_Arch|Cormorant+Jost+NothingYouCouldDo|Pastel_Pink|Arch stroke 4px, brackets 28px
```

### Typography Locks (English)
- **Headline:** YoungSerif / Lora-Bold / BigShoulders-Bold / BricolageGrotesque-Bold / Cormorant / SpaceGrotesk-Bold — based on arc energy
- **Body:** InstrumentSans-Regular / WorkSans-Regular / Jost-Regular / DMMono-Regular
- **Script Number:** `NothingYouCouldDo-Regular.ttf` — 180-240px, bottom-left (hardcoded)
- **Kicker:** CrimsonPro-Italic / Lora-Italic / InstrumentSerif-Italic — 36-40px
- **Label:** InstrumentSans-Bold / WorkSans-Bold — 11px, top center

### Palette Selection by Arc
| Arc | Palette | BG | Text | Accent |
|-----|---------|----|----|--------|
| Wonder | Pastel_Pink | #FFF0F5 | #2D2D2D | #FF69B4 |
| Problem | Dark_Tech | #0D0D1A | #FFFFFF | #00FFFF |
| Joy | Sunset_Orange | #FFF5F0 | #2D2D2D | #E65100 |
| Lesson | Minimal_Cream | #FAF9F6 | #2D2D2D | #8B7355 |
| Adventure | Neon_Cyber | #0D0D1A | #FFFFFF | #00FF00 |
| Friendship | Earthy_Green | #F5F5F0 | #2D2D2D | #556B2F |

### Variation Triggers (story-driven)
- **Per-Slide Layout:** 6-slide carousels → slides 1-3 primary layout, 4-6 alternate (emotional shift)
- **Tint:** 0.28 base → 0.35 bright images, 0.18 dark images
- **Script Number:** 200px base → 160px quiet, 240px high-energy
- **Kicker Border:** 3px solid base → 5px emphasis, dashed playful

### Gappu DNA Locks (NEVER randomize)
- ALL image prompts MUST follow `D:\oldCOMPUTER\Videos\Scripts\Gappu\Gappu_Master_Prompt_v8.md` logic:
  - Use **Anatomy Anchor** (lines 133-136) for all Gappu presence.
  - Use **Toddler Emotion Atlas** (ATLAS 01-12) for all expressions.
  - Apply **Roger Rabbit Contrast**: Hyper-real environment + stylized 3D Gappu.
  - Follow **Lighting & Color Temperature Arcs** (Part 1D) across slides.
- Gappu's face always in upper 60% — text never overlaps.
- Per-slide images (not single hero) — each slide = unique moment.
- 6 content slides + 1 CTA — fixed structure.
- Reference image attached when `gappu_in_scene: YES` (LOCKED to Image 1).

---

## Gappu-Specific Values

```python
# Channel branding
CHANNEL_NAME = "Gappu Magic Story Land"
INSTAGRAM_HANDLE = "@gappumagicworld"
LOGO_PATH = Path("D:/oldCOMPUTER/Videos/GappuMonkeyShorts/PICTURE/[logo].png")

# Font paths
FONTS = Path("D:/oldCOMPUTER/Videos/Scripts/GitSkills/canvas-design/canvas-fonts")
```

---

## Output Structure

```
D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\YYYY-MM-DD_TopicName\
├── images/                 # Per-slide images (5-7)
├── slides/
│   ├── design-philosophy.md
│   ├── slide_01.png ...    # Generated slides
│   └── canvas-design.png   # Optional STEP 4B overlay
├── caption_instagram.txt
├── caption_facebook.txt
└── SESSION-RESUME.md
```

---

## Caption Formula

**Instagram:**
```
[Hook line — under 15 words, wonder-filled]

[3-5 bullet facts from slides]

Follow @gappumagicworld for more!

#GappuMagic #KidsLearning #[Topic] #Parenting #EarlyEducation #FunFacts
```

**Facebook:** Same + longer explanation (4-6 lines) for parents/grandparents.

---

## Failure Handling

- **Image generation fails:** Retry with simplified prompt (remove "sparkle", "motion" terms)
- **Playwright timeout:** Increase to 30s, check font paths
- **Color contrast issues:** Increase tint to 0.35, verify TEXT_HEX
- **Per-slide image mismatch:** Ensure consistent character design across all images
