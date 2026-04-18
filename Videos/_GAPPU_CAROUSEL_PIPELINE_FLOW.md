# Gappu Carousel Pipeline — Complete Flow

**Pipeline Rule:** `activate gappu carousel`
**Main CLAUDE.md:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\CLAUDE.md`
**Corrected STEP 4B:** `D:\oldCOMPUTER\Videos\_Rules\gappu-carousel-step4b-corrected.md`

---

## Important Clarification: Content-Week

⚠️ **STEP 5 uses content-week PRINCIPLES, NOT the full content-week skill.**

- **Content-Week Principles**: Hook structure, Body-Arc format, CTA structure (used in STEP 5)
- **Content-Week Skill** (`activate content-week`): Full multi-platform repurposing tool (generates Instagram, LinkedIn, TikTok, email, scheduling — OPTIONAL, not required for carousel)

**In this pipeline:** STEP 5 is manual writing using content-week guidelines. The full skill is optional if you want to repurpose the carousel into a full week of content.

---

## COMPLETE PIPELINE FLOW

```
START
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 0: LOGIN CHECK & SETUP                             │
├─────────────────────────────────────────────────────────┤
│ • Open Google Flow: https://labs.google/fx/tools/flow  │
│ • Verify logged in (profile icon visible)              │
│ • Take screenshot to confirm                           │
│ • If NOT logged in: pause → tell user to log in        │
│ └─→ Proceed to STEP 1                                  │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 1: BEAT PACK GENERATION                            │
├─────────────────────────────────────────────────────────┤
│ INPUT: User provides topic or story idea               │
│ Example: "Gappu tries mangoes for the first time"      │
│                                                         │
│ PROCESS:                                               │
│ 1. Read Gappu_Master_Prompt_v8.md (emotion atlas, arc) │
│ 2. Generate beat pack (6 story slides + 1 CTA)         │
│ 3. Select 3 Vault Design variables:                    │
│    ├─ Layout (e.g., Centered_Arch)                     │
│    ├─ Font (e.g., Elegant = Playfair Display + Inter)  │
│    └─ Color (e.g., Luxury_Gold = #212121, #FFD700)     │
│ 4. For each slide, define:                             │
│    ├─ arc (HOOK/SETUP/TENSION/STRUGGLE/TURN/PAYOFF)   │
│    ├─ headline (3–6 words)                             │
│    ├─ subtext (optional, ≤8 words)                     │
│    ├─ gappu_in_scene (YES or NO)                       │
│    ├─ action (frozen frame + movement)                 │
│    ├─ emotion (ATLAS state + expression)               │
│    ├─ location (setting + light + time)                │
│    ├─ shot (CLOSE-UP / MEDIUM / WIDE)                  │
│    ├─ lighting (type + color temp)                     │
│    └─ composition (position in frame)                  │
│                                                         │
│ OUTPUT: Beat pack table + Design vault selections      │
│ WAIT: User reviews & confirms or edits                 │
│ └─→ If OK: Create story folder → Proceed to STEP 2    │
│     If NO: Iterate until user approves                 │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 2: IMAGE PROMPT ASSEMBLY (Nano Banana 2)           │
├─────────────────────────────────────────────────────────┤
│ For each slide where gappu_in_scene: YES               │
│                                                         │
│ ASSEMBLE image_prompt (6-factor structure):            │
│ 1. [CHARACTER]: Gappu anchor + emotion expression      │
│ 2. [ACTION]: action field verbatim (frozen frame)      │
│ 3. [SETTING]: location + environment detail            │
│ 4. [COMPOSITION]: shot type + rule of thirds position  │
│ 5. [LIGHTING]: lighting field + color temp             │
│ 6. [STYLE]: Hardcoded Roger Rabbit style line:         │
│    "Ultra-realistic photorealistic environment +       │
│     stylized 3D Gappu (Pixar). Environment 100%        │
│     cinematic DSLR, Gappu 100% stylized 3D."           │
│                                                         │
│ ADD: NEGATIVE (always append):                         │
│ "no cartoon environment, no illustrated background,    │
│  no 3D environment, no extra limbs, no Gappu redesign" │
│                                                         │
│ OUTPUT: Complete image_prompt for each slide           │
│ └─→ Proceed to STEP 3                                  │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 3: IMAGE GENERATION (Google Flow)                  │
├─────────────────────────────────────────────────────────┤
│ For each slide (1–6) where gappu_in_scene: YES         │
│                                                         │
│ 1. Navigate to Google Flow (already open)              │
│ 2. Confirm settings:                                   │
│    ├─ Model: Nano Banana 2                             │
│    ├─ Ratio: 4:5                                       │
│    └─ Quantity: x1                                     │
│ 3. Clear prompt bar (Ctrl+A → Delete)                  │
│ 4. Paste image_prompt for this slide                   │
│ 5. Click Generate                                      │
│ 6. Wait for image to appear (30–60 sec)               │
│ 7. Download image from Assets                          │
│ 8. Save to: images/slide_NN.png                        │
│ 9. Update SESSION-RESUME.md: IMAGE: DONE               │
│                                                         │
│ OUTPUT: 5–6 Nano Banana 2 PNG images (4:5)             │
│ FAILURE: Mark FAILED-1, rewrite if safety rejected,    │
│          retry once. If fails again, skip + log.       │
│ └─→ Proceed to STEP 4 when all images done             │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 4A: DESIGN PHILOSOPHY (Canvas Design Prep)         │
├─────────────────────────────────────────────────────────┤
│ Before designing slides, document design rationale.     │
│                                                         │
│ 1. Extract Vault variables from STEP 1:                │
│    ├─ design_layout (e.g., Centered_Arch)              │
│    ├─ design_font (e.g., Elegant)                      │
│    └─ design_color (e.g., Luxury_Gold)                 │
│                                                         │
│ 2. Create design-philosophy.md explaining:             │
│    "Why does this Vault combo match the story emotion?"│
│                                                         │
│ 3. Save to: design-philosophy.md                       │
│                                                         │
│ OUTPUT: 1-paragraph design philosophy                  │
│ └─→ Proceed to STEP 4B                                 │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 4B: CAROUSEL SLIDE DESIGN (Canvas-Design Skill)    │
├─────────────────────────────────────────────────────────┤
│ THIS IS THE CORRECTED STEP (4 MANDATORY RULES)         │
│                                                         │
│ For each slide (1–7):                                  │
│                                                         │
│ 1. Open CANVAS-DESIGN-PROMPT-TEMPLATE.md               │
│ 2. Copy blank template                                 │
│ 3. Fill 9 required values:                             │
│    ├─ Slide number                                     │
│    ├─ Image path (from STEP 3)                         │
│    ├─ Headline (from beat pack)                        │
│    ├─ Subtext (from beat pack)                         │
│    ├─ Design Layout rules (from Vault ref)             │
│    ├─ Typography (headline + body fonts)               │
│    ├─ Colors (BG, Text, Accent hex values)             │
│    └─ Image size (e.g., 75%)                           │
│                                                         │
│ 4. Paste filled template into canvas-design skill      │
│ 5. Generate PNG (1080×1350px, 4:5)                     │
│ 6. VERIFY CHECKLIST (8 items):                         │
│    ☐ PNG dimensions correct                            │
│    ☐ Layout architecture evident                       │
│    ☐ Headline font correct (visual check)              │
│    ☐ Body font correct (visual check)                  │
│    ☐ BG hex verified with color picker                 │
│    ☐ Text hex verified with color picker               │
│    ☐ Accent hex verified with color picker             │
│    ☐ Gappu image centered, unobstructed                │
│    ☐ Slide number visible                              │
│                                                         │
│ 7. If ANY checklist fails → DO NOT SAVE                │
│    ├─ Identify which rule failed (1/2/3/4)             │
│    ├─ Rewrite prompt with clearer language             │
│    └─ Regenerate                                       │
│                                                         │
│ 8. If ALL checks pass → Save to: slides/slide_NN.png   │
│ 9. Update SESSION-RESUME.md: SLIDE: DONE               │
│                                                         │
│ THE 4 DESIGN INJECTION RULES (ALL MANDATORY):          │
│ ═════════════════════════════════════════════          │
│ RULE 1: LAYOUT STRUCTURE                               │
│   └─ Replicate CSS logic of design_layout              │
│      (e.g., Centered_Arch = soft curves, centered)     │
│                                                         │
│ RULE 2: TYPOGRAPHY                                     │
│   └─ Load exact Google Fonts (no substitutions)        │
│      (e.g., Playfair Display for headline)             │
│                                                         │
│ RULE 3: COLOR MAPPING                                  │
│   └─ Apply exact hex values (no approximations)        │
│      BG → background, Text → text, Accent → borders    │
│                                                         │
│ RULE 4: GAPPU FOCAL POINT                              │
│   └─ Image centered, unobstructed, prominent           │
│                                                         │
│ OUTPUT: 7 carousel slides (1080×1350px, 4:5)           │
│         with proper Vault design injected              │
│ FAILURE: Mark FAILED-1, adjust prompt, retry.          │
│          If fails again, skip + log.                   │
│ └─→ Proceed to STEP 5 when all slides done             │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 5: SOCIAL COPY (Instagram + Facebook)              │
├─────────────────────────────────────────────────────────┤
│ After ALL slides (1–7) are done                        │
│                                                         │
│ NOTE: This step uses content-week PRINCIPLES (hook,    │
│ body, CTA structure) but NOT the full skill.           │
│ STEP 5 is manual writing based on guidelines.          │
│                                                         │
│ PROCESS:                                               │
│ 1. Extract key moments from each slide (headlines)     │
│ 2. Build narrative arc from beat pack                  │
│ 3. Write two separate posts (Instagram + Facebook)    │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│ 5A — INSTAGRAM CAPTION (per content-week rules):       │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                                         │
│ HOOK (Opening line — must stop scroll):                │
│ • Bold statement                                       │
│ • <15 words                                            │
│ • Pulled from Slide 1 headline or variation            │
│ • Example: "This fruit changed everything for Gappu"  │
│                                                         │
│ BODY (Walk through emotional arc):                     │
│ • 3–5 short sentences (one idea per slide)             │
│ • Toddler wonder tone (curiosity, discovery)           │
│ • Show progression: suspicion → fear → discovery → joy │
│ • Keep it conversational, not summarizing               │
│                                                         │
│ CTA (Call-to-action — hardcoded):                      │
│ "Follow @gappumagicworld for more Gappu magic stories" │
│ + emoji (🐵)                                            │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│ 5B — FACEBOOK POST (narrative format):                 │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                                         │
│ OPENING LINE:                                          │
│ • Hook sentence (storytelling tone)                    │
│ • Setup the moment (who, what, where)                  │
│ • Example: "Watch what happens when Gappu discovers   │
│   his first mango..."                                  │
│                                                         │
│ STORY PARAGRAPH:                                       │
│ • Full narrative of the arc (2–3 sentences per slide)  │
│ • Human, emotional, conversational voice               │
│ • Include the emotional beats (fear, amazement, joy)   │
│                                                         │
│ INSIGHT/LESSON:                                        │
│ • The quiet truth the story carries                    │
│ • What makes this moment meaningful                    │
│ • Example: "Sometimes the most magical moments come   │
│   when we're brave enough to try something new"        │
│                                                         │
│ CTA + HASHTAGS:                                        │
│ • Call: "Watch the full story on YouTube 👇"           │
│ • Link: [YouTube video URL if available]               │
│ • Hashtags: 2–3 relevant tags                          │
│   (e.g., #GappuMagicWorld #YouTubeShorts)             │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│ SAVE OUTPUT:                                            │
│ Both posts saved to: slides/caption.txt                │
│                                                         │
│ FORMAT:                                                │
│ # INSTAGRAM CAPTION                                    │
│ [Instagram post here]                                  │
│                                                         │
│ # FACEBOOK POST                                        │
│ [Facebook post here]                                   │
│                                                         │
│ OPTIONAL: Use full content-week skill                  │
│ If you want to generate multi-platform content         │
│ (LinkedIn, email, TikTok, etc.) from this carousel:    │
│ • Tell Claude: "activate content-week"                │
│ • Paste carousel beat pack + captions                  │
│ • Skill generates full week of posts                   │
│ • NOT required for carousel pipeline                   │
│                                                         │
│ OUTPUT: Instagram caption + Facebook post              │
│ └─→ Proceed to STEP 6                                  │
└─────────────────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 6: FINAL REPORT                                    │
├─────────────────────────────────────────────────────────┤
│ CAROUSEL PIPELINE COMPLETE                             │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                                         │
│ Topic: [story title]                                   │
│ Folder: D:\...\YYYY-MM-DD_TopicName\                   │
│                                                         │
│ Design Theme:                                          │
│   Layout: [design_layout]                              │
│   Font: [design_font]                                  │
│   Color: [design_color]                                │
│                                                         │
│ Status:                                                │
│   Images: [X]/6 done                                   │
│   Slides: [X]/7 done                                   │
│   Caption: DONE                                        │
│                                                         │
│ Assets Ready:                                          │
│   ✓ images/slide_01.png ... slide_06.png              │
│   ✓ slides/slide_01.png ... slide_07.png              │
│   ✓ slides/caption.txt (Instagram + Facebook)         │
│                                                         │
│ Next: Post to Instagram @gappumagicworld               │
│       + Facebook Gappu Magic Story Land                │
│                                                         │
│ └─→ END (Ready for social posting!)                    │
└─────────────────────────────────────────────────────────┘
  │
  ▼
END — Carousel ready for Instagram & Facebook!
```

---

## File References During Pipeline

| Step | Read | Write | Location |
|------|------|-------|----------|
| 0 | — | SESSION-RESUME.md | carousel/YYYY-MM-DD_TopicName/ |
| 1 | Gappu_Master_Prompt_v8.md | Beat pack output | (shown to user) |
| 1 | — | SESSION-RESUME.md (updated) | carousel/YYYY-MM-DD_TopicName/ |
| 2 | Beat pack | image_prompts | (used in STEP 3) |
| 3 | image_prompts | slide_NN.png | images/ folder |
| 3 | — | SESSION-RESUME.md (IMAGE: DONE) | carousel/YYYY-MM-DD_TopicName/ |
| 4A | design-philosophy.md | design-philosophy.md | slides/ folder |
| 4B | CANVAS-DESIGN-PROMPT-TEMPLATE.md | slide_NN.png | slides/ folder |
| 4B | — | SESSION-RESUME.md (SLIDE: DONE) | carousel/YYYY-MM-DD_TopicName/ |
| 5 | Beat pack + slides | caption.txt | slides/ folder |
| 6 | SESSION-RESUME.md | Final report | (shown to user) |

---

## Folder Structure During Pipeline

```
GappuMonkeyShorts/
└── pipeline/
    └── carousel/
        └── 2026-04-16_GappuTroesMangoes/
            ├── SESSION-RESUME.md              ← Track progress
            ├── design-philosophy.md           ← Created STEP 4A
            ├── images/
            │   ├── slide_01.png               ← Created STEP 3
            │   ├── slide_02.png               ← Nano Banana 2 outputs
            │   ├── slide_03.png
            │   ├── slide_04.png
            │   ├── slide_05.png
            │   └── slide_06.png
            └── slides/
                ├── slide_01.png               ← Created STEP 4B
                ├── slide_02.png               ← Canvas-designed (1080×1350)
                ├── slide_03.png               ← With Vault injection
                ├── slide_04.png
                ├── slide_05.png
                ├── slide_06.png
                ├── slide_07.png               ← CTA slide (no image)
                └── caption.txt                ← Created STEP 5
```

---

## Key Tools Used

| Tool | Step | Purpose | URL |
|------|------|---------|-----|
| Google Flow | 0 | Login check | https://labs.google/fx/tools/flow |
| Google Flow | 3 | Nano Banana 2 image generation | https://labs.google/fx/tools/flow |
| Canvas Design Skill | 4B | Slide PNG rendering with Vault injection | (Claude skill) |
| Content Week Rules | 5 | Caption writing | (from Scripts/GitSkills/) |

---

## Session Resume Tracking

Update `SESSION-RESUME.md` at these points:

```markdown
## Slide Progress

| Slide | Headline | Image | Slide | Status |
|-------|----------|-------|-------|--------|
| 01 | What IS this thing? | DONE | DONE | ✓ |
| 02 | It smells… suspicious. | DONE | DONE | ✓ |
| 03 | One brave little bite. | DONE | DONE | ✓ |
| 04 | His brain stopped working. | DONE | DONE | ✓ |
| 05 | Oh. OH. | DONE | DONE | ✓ |
| 06 | Mangoes changed his life. | DONE | DONE | ✓ |
| 07 | Follow for more magic | SKIP | DONE | ✓ |

Caption: DONE
```

---

## Error Recovery

**If session interrupts:**
1. Read `SESSION-RESUME.md`
2. Find first `PENDING` or `FAILED` row
3. Resume from that exact step
4. Continue pipeline

**Example:**
- Session crashes after STEP 3, Slide 4
- Read SESSION-RESUME.md → finds `slide_05 | IMAGE: PENDING`
- Resume STEP 3 for Slide 5
- Continue STEP 3 for remaining slides
- Then STEP 4

---

## Now Ready?

This is the **COMPLETE, CORRECTED flow** with:
- ✅ STEP 4B fixed with 4 mandatory design rules
- ✅ Canvas-design template (copy/fill/paste)
- ✅ Vault variable support (1000 design combos)
- ✅ Proper design injection (no more generic/flat slides)

Ready to regenerate the mango carousel with this flow? 🎨

