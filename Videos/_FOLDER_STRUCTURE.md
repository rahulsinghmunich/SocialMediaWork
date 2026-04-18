# Videos Project — Folder Structure (Based on Rules)

Created: 2026-04-16
Last Updated: 2026-04-16

---

## Folder Organization by Pipeline

Each rule/pipeline has a specific folder structure. This document defines the canonical structure.

---

## 1. GAPPU MAGIC LAND SHORTS

**Pipeline Rule:** `activate gappu pipeline`
**Main CLAUDE.md:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\CLAUDE.md`

```
GappuMonkeyShorts/
├── PICTURE/                          ← Existing (keep as-is)
├── pipeline/
│   ├── CLAUDE.md                    ← Main pipeline rules
│   ├── SESSION-RESUME.md             ← Template (copy to each story folder)
│   ├── reference/
│   │   └── gappu_dhoti.png          ← Character reference image
│   ├── YYYY-MM-DD_StoryTitle1/      ← Per-story folder (created per run)
│   │   ├── SESSION-RESUME.md        ← Current story tracking
│   │   ├── images/                  ← Nano Banana Pro output (9:16, 2K)
│   │   │   ├── scene_01.png
│   │   │   ├── scene_02.png
│   │   │   └── ...
│   │   └── videos/                  ← Kling 3.0 output (9:16, 720p)
│   │       ├── scene_01.mp4
│   │       ├── scene_02.mp4
│   │       └── ...
│   ├── YYYY-MM-DD_StoryTitle2/
│   │   ├── SESSION-RESUME.md
│   │   ├── images/
│   │   └── videos/
│   └── ...
└── [other folders]

Key Points:
- All story folders use YYYY-MM-DD_StoryTitle naming
- Reference image gappu_dhoti.png in pipeline/reference/
- SESSION-RESUME.md tracks Higgsfield login, image/video completion
```

---

## 2. GAPPU MAGIC LAND CAROUSEL

**Pipeline Rule:** `activate gappu carousel`
**Main CLAUDE.md:** `D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\carousel\CLAUDE.md`
**Step 4B Rules:** 
  - `D:\oldCOMPUTER\Videos\_Rules\gappu-carousel-step4b-corrected.md`
  - `D:\oldCOMPUTER\Videos\_Rules\gappu-carousel-canvas-design-template.md`

```
GappuMonkeyShorts/
├── pipeline/
│   ├── carousel/
│   │   ├── CLAUDE.md                ← Main carousel pipeline rules
│   │   ├── SESSION-RESUME.md         ← Template
│   │   ├── reference/               ← (Optional, references parent pipeline/reference/)
│   │   ├── YYYY-MM-DD_TopicName1/  ← Per-carousel folder (created per run)
│   │   │   ├── SESSION-RESUME.md   ← Current carousel tracking
│   │   │   ├── design-philosophy.md ← Vault variable rationale (STEP 4A)
│   │   │   ├── images/              ← Nano Banana 2 output (4:5, Google Flow)
│   │   │   │   ├── slide_01.png
│   │   │   │   ├── slide_02.png
│   │   │   │   └── ...
│   │   │   └── slides/              ← Canvas-designed carousel slides (1080×1350, 4:5)
│   │   │       ├── slide_01.png     ← With Vault design injected
│   │   │       ├── slide_02.png
│   │   │       ├── slide_03.png
│   │   │       ├── ...
│   │   │       ├── slide_07.png     ← CTA slide (no image)
│   │   │       └── caption.txt      ← Instagram + Facebook copy (STEP 5)
│   │   ├── YYYY-MM-DD_TopicName2/
│   │   │   ├── SESSION-RESUME.md
│   │   │   ├── design-philosophy.md
│   │   │   ├── images/
│   │   │   └── slides/
│   │   └── ...
│   └── reference/
│       └── gappu_dhoti.png          ← Shared with main pipeline

Key Points:
- STEP 4B uses corrected rules (see _Rules folder)
- design-philosophy.md created before designing slides
- Canvas fonts from Scripts/GitSkills/canvas-design/canvas-fonts/
- slides/ folder contains final carousel PNGs (1080×1350)
- caption.txt contains Instagram + Facebook posts
```

---

## 3. BHAKTI CHANNEL

**Pipeline Rule:** `activate bhakti pipeline`
**Main CLAUDE.md:** `D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\CLAUDE.md`

```
BhaktiChannel/
├── pipeline/
│   ├── CLAUDE.md                    ← Main pipeline rules
│   ├── SESSION-RESUME.md             ← Template
│   ├── reference/                   ← (Optional, for character refs if needed)
│   ├── YYYY-MM-DD_StoryTitle1/     ← Per-story folder (created per run)
│   │   ├── SESSION-RESUME.md       ← Current story tracking
│   │   ├── research/               ← NotebookLM research output
│   │   │   └── [research docs]
│   │   ├── script.md               ← Claude-generated script (waiting for approval)
│   │   ├── images/                 ← Nano Banana Pro output (9:16, 2K, Higgsfield)
│   │   │   ├── scene_01.png
│   │   │   └── ...
│   │   ├── videos/                 ← Kling 3.0 output (9:16, 720p, Higgsfield)
│   │   │   ├── scene_01.mp4
│   │   │   └── ...
│   │   └── narration.txt           ← ElevenLabs V3 narration script
│   ├── YYYY-MM-DD_StoryTitle2/
│   │   └── ...
│   └── ...
└── [other folders]

Key Points:
- NotebookLM research in research/ folder (auto-fetched via nlm.py)
- script.md written by Claude, awaits user approval before proceeding
- Images/videos generated on Higgsfield (9:16, character descriptions in prompts)
- narration.txt is ElevenLabs script (not actual audio)
```

---

## 4. OBJECTAI SHORTS

**Pipeline Rule:** `activate objectai pipeline`
**Main CLAUDE.md:** `D:\oldCOMPUTER\Videos\ObjectAi\pipeline\CLAUDE.md`

```
ObjectAi/
├── pipeline/
│   ├── CLAUDE.md                    ← Main pipeline rules
│   ├── SESSION-RESUME.md             ← Template
│   ├── YYYY-MM-DD_Topic1/           ← Per-topic folder (created per run)
│   │   ├── SESSION-RESUME.md       ← Current topic tracking
│   │   ├── veo-jsons/              ← VEO scene JSON files (structured motion)
│   │   │   ├── scene_01.json
│   │   │   ├── scene_02.json
│   │   │   └── ...
│   │   ├── images/                 ← Nano Banana 2 output (Google Flow)
│   │   │   ├── scene_01.png
│   │   │   └── ...
│   │   └── videos/                 ← Veo 3.1 output (Google Flow, Frames mode)
│   │       ├── scene_01.mp4
│   │       └── ...
│   ├── YYYY-MM-DD_Topic2/
│   │   └── ...
│   └── ...
└── [other folders]

Key Points:
- veo-jsons/ contains structured motion data (JSON format)
- Images from Nano Banana 2 in Google Flow
- Videos from Veo 3.1 Fast in Frames mode (Google Flow)
- No character reference image — all chars described in prompt
```

---

## 5. SHARED SCRIPTS & REFERENCE

**Location:** `D:\oldCOMPUTER\Videos\Scripts\`

```
Scripts/
├── Gappu/
│   ├── Gappu_Master_Prompt_v8.md   ← Core rules for Gappu scene generation
│   │                                  (emotion atlas, dopamine arc, prompt assembly)
│   └── [other Gappu-specific resources]
│
├── ObjectAi/
│   ├── CLAUDE_VEO_RULES.md         ← VEO JSON structure rules
│   ├── Gemini_ObjectAi_Scene_Prompt.md ← Scene generation template
│   ├── html-tools/
│   │   └── veo-pacer-v9-fixed.html ← Manual VEO JSON builder
│   └── [other ObjectAi resources]
│
├── GitSkills/
│   ├── canvas-design/
│   │   ├── SKILL.md                ← Canvas design skill rules
│   │   ├── canvas-fonts/           ← Google Fonts for carousel designs
│   │   │   ├── Playfair Display/
│   │   │   ├── Inter/
│   │   │   ├── Elegant/
│   │   │   └── ...
│   │   └── [design assets]
│   │
│   ├── nano-banana-prompt-generator/
│   │   ├── SKILL.md                ← Nano Banana image prompt rules
│   │   └── [nano banana assets]
│   │
│   ├── content-week/
│   │   ├── SKILL.md                ← Caption/copy writing rules
│   │   └── [content assets]
│   │
│   └── [other skills]
│
└── [other shared resources]

Key Points:
- Gappu_Master_Prompt_v8.md is THE source for Gappu scene packs
- Canvas fonts shared across all carousel projects
- Skills in GitSkills/ are shared across all pipelines
```

---

## 6. RULES & CONFIGURATION

**Location:** `D:\oldCOMPUTER\Videos\_Rules\`

```
_Rules/
├── README.md                                ← Index of all rules

├── gappu-pipeline.md                       ← Activate: "activate gappu pipeline"
├── gappu-carousel.md                       ← Activate: "activate gappu carousel"
├── gappu-carousel-step4b-corrected.md      ← (NEW) STEP 4B fixed workflow
├── gappu-carousel-canvas-design-template.md ← (NEW) Canvas design prompt template

├── bhakti-pipeline.md                      ← Activate: "activate bhakti pipeline"
├── bhakti-suno-prompt.md                   ← Activate: "activate suno prompt"

├── objectai-pipeline.md                    ← Activate: "activate objectai pipeline"
├── objecttalk-veo-prompt.md                ← Activate: "activate veo prompt"
├── objecttalk-viral-strategy.md            ← Activate: "activate viral strategy"

└── [other rules as added]

Key Points:
- All rules live here (not in project folders)
- Each rule is OFF by default
- Activate with "activate [rule name]"
- New rules: add file + update README.md table
```

---

## 7. MEMORY & PROJECT TRACKING

**Location:** `D:\oldCOMPUTER\Videos\.claude\`

```
.claude/
├── projects/
│   └── D--oldCOMPUTER-Videos/
│       └── memory/
│           ├── MEMORY.md            ← Index of all memory files
│           ├── user_*.md            ← User profile memory
│           ├── feedback_*.md        ← User feedback & preferences
│           ├── project_*.md         ← Active project state
│           └── reference_*.md       ← Reusable references
│
└── [IDE/editor config]

Key Points:
- Memory persists across sessions
- MEMORY.md is the index (max 200 lines)
- Each memory type in separate file
- Used to inform future conversation behavior
```

---

## 8. MISSING FOLDERS TO CREATE

Based on the rules, create these folders if not already present:

```bash
# Bhakti pipeline
mkdir -p D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\reference

# Gappu shorts
mkdir -p D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\reference

# Scripts structure (verify and complete)
mkdir -p D:\oldCOMPUTER\Videos\Scripts\Gappu
mkdir -p D:\oldCOMPUTER\Videos\Scripts\ObjectAi\html-tools
mkdir -p D:\oldCOMPUTER\Videos\Scripts\GitSkills\canvas-design\canvas-fonts
mkdir -p D:\oldCOMPUTER\Videos\Scripts\GitSkills\nano-banana-prompt-generator
mkdir -p D:\oldCOMPUTER\Videos\Scripts\GitSkills\content-week
```

---

## 9. NAMING CONVENTIONS

### Per-Story/Per-Carousel Folders:
- **Format:** `YYYY-MM-DD_StoryName` or `YYYY-MM-DD_TopicName`
- **Example:** `2026-04-16_GappuTroesMangoes`
- **Reason:** Chronological sorting + easy identification

### File Naming:
- **Images:** `scene_01.png`, `scene_02.png`, ..., `scene_NN.png`
- **Videos:** `scene_01.mp4`, `scene_02.mp4`, ..., `scene_NN.mp4`
- **Carousel slides:** `slide_01.png`, `slide_02.png`, ..., `slide_07.png` (1080×1350)
- **Carousel images (pre-design):** `slide_01.png`, `slide_02.png` (4:5 from Google Flow)
- **Reason:** Consistent sorting, easy script automation

### SESSION-RESUME.md:
- **Location:** In each story/carousel folder
- **Purpose:** Track progress, login status, asset IDs, image/video completion
- **Reset:** Fresh copy created at start of each story/carousel

---

## 10. CHECKLIST FOR NEW PROJECT SETUP

When starting a new story/carousel project:

- [ ] Create `YYYY-MM-DD_TopicName/` folder
- [ ] Copy `SESSION-RESUME.md` template into folder
- [ ] Fill in story title, date, and project metadata
- [ ] Create `images/` subfolder
- [ ] Create `videos/` subfolder (or `slides/` for carousel)
- [ ] (For carousel) Create `design-philosophy.md` in STEP 4A
- [ ] Update SESSION-RESUME.md as pipeline progresses
- [ ] Log all failures with reason + attempt number

---

**This structure ensures:**
✓ Consistency across all projects
✓ Easy recovery if work is interrupted
✓ Centralized rules (not scattered in project folders)
✓ Clear separation between setup, rules, and outputs
✓ Scalable for new projects and pipelines
