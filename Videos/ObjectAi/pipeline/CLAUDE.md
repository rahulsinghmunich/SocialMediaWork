# ObjectAi — Full Production Pipeline

## Workflow
1. Script input → Claude generates image_prompt only
2. Flow (Google) → image generation per scene (Nano Banana 2)
3. Claude reads generated image → writes complete scene JSON from scratch
4. Flow (Google) → video generation per scene (Veo 3.1 Fast, Frames mode)
5. DONE — all scene videos saved

---

## Paths & Tools
- **Pipeline folder**: `D:\oldCOMPUTER\Videos\ObjectAi\pipeline\`
- **VEO rules**: `D:\oldCOMPUTER\Videos\Scripts\ObjectAi\CLAUDE_VEO_RULES.md`
- **Scene prompt**: `D:\oldCOMPUTER\Videos\Scripts\ObjectAi\Gemini_ObjectAi_Scene_Prompt.md`
- **HTML tool reference**: `D:\oldCOMPUTER\Videos\Scripts\ObjectAi\html-tools\veo-pacer-v9-fixed.html`
- **Image + Video tool**: Google Flow — https://labs.google/fx/tools/flow
- **No character reference image** — characters fully described in image prompt

---

## STEP 0 — Login Check (once per session)

1. Navigate to https://labs.google/fx/tools/flow via Playwright
2. Take one screenshot — confirm logged in (profile icon visible, project list visible)
3. If NOT logged in: tell user "Please log in to Google Flow, then confirm"
4. Do not proceed until confirmed

---

## STEP 1 — Take Script Input

User provides one of:
- **PATH A** — Gemini scene pack already exists (has Image Prompt + Motion + Dialogue per scene)
- **PATH B** — Topic, raw script, or input with NO Motion field → Claude generates scene pack

### PATH A — Pre-assembled scene pack
Read CLAUDE_VEO_RULES.md → extract image_prompt using Nano Banana template → go to Step 2.

### PATH B — Generate scene pack
1. Read BOTH rule files:
   - `D:\oldCOMPUTER\Videos\Scripts\ObjectAi\CLAUDE_VEO_RULES.md`
   - `D:\oldCOMPUTER\Videos\Scripts\ObjectAi\Gemini_ObjectAi_Scene_Prompt.md` (Mode 2 section)
2. Output full scene pack: Title, Speakers count, Image Prompt, Motion (all 3 beats), Dialogue lines
3. Wait for user to confirm or edit
4. Then extract image_prompt using Nano Banana template → go to Step 2

### 1A — Read VEO rules
Read `CLAUDE_VEO_RULES.md` fully before generating anything.

### 1B — Build image_prompt only (NOT the full JSON yet)
Using the Nano Banana Keyframe Template from CLAUDE_VEO_RULES.md:
- SUBJECT: object + material detail + face (SEALED) + face geometry lock
- ACTION: Beat 1 pose only (frozen frame, no open mouth)
- SETTING: exact environment from scene pack
- CAMERA: 9:16 vertical, character centered, static shot
- LIGHTING: from scene pack
- STYLE: Pixar 3D animated, vibrant colors, clean render
- PURPOSE: "This image will be used as a Veo 3.1 animation start frame..."

⛔ Do NOT write the full scene JSON yet. Only image_prompt. JSON is written AFTER reading the generated image.

### 1C — Create story folder
```
D:\oldCOMPUTER\Videos\ObjectAi\pipeline\YYYY-MM-DD_TopicName\
├── SESSION-RESUME.md
├── images\
└── videos\
```
Confirm folder path to user before proceeding.

---

## STEP 2 — Image Generation (Nano Banana 2, Google Flow)

### 2A — Open/confirm Flow project (once per session)
1. Navigate to https://labs.google/fx/tools/flow
2. Click `+ New project`: `btns.find(b => b.textContent.includes('New project')).click()`
3. Save Flow project URL to SESSION-RESUME.md

**Confirm settings (one screenshot):**
- Image tab selected
- 9:16 aspect ratio
- x1 quantity
- Nano Banana 2 model

### 2B — Per scene: generate image
1. Clear prompt and type `image_prompt` for this scene (use `slowly: false`)
2. Click Generate: `btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()`
3. **Wait for completion — DOM wait, no screenshot polling:**
```js
await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 });
```

### 2C — Read the generated image
1. Navigate to the image asset (click image card → full view)
2. Note the Flow asset ID from URL: `/edit/[ASSET-ID]` — save to SESSION-RESUME.md
3. Take screenshot with `browser_take_screenshot` ← this IS intentional (Claude reads image to write JSON)
4. Claude reads the image visually — this is the source of truth for ALL JSON fields

### 2D — Download image
Save to: `images\scene_NN.png`

### 2E — Update SESSION-RESUME.md: IMAGE → DONE

---

## STEP 3 — Write Complete Scene JSON (after image read)

⛔ This is the ONLY place the full JSON is written. Never before the image is read.

Read CLAUDE_VEO_RULES.md for the complete JSON structure. Must match `veo-pacer-v9-fixed.html` (V10.1) exactly.

From the image just read, fill ALL fields:
- `object_type`, `description`, `face`, `face_geometry_lock` — from image
- `location_lock` — exact screen position from image
- `environment.*` — setting, lighting, atmosphere, background, foreground_props — from image
- `source_image.scene_description` — describe Frame 1 exactly as visible
- `source_image.first_frame_instruction` — start on this exact image
- `scene_integrity.character_positions` — from image
- `global_motion_rules.*` — from Motion field camera note + beat summary
- `beats[].visuals` — FROM MOTION FIELD verbatim, not invented
- `beats[].speaker_activation_rule` — "ONLY X speaks. Y mouth SEALED."
- `dialogue.line` — exact Hindi text from script (no hyphens)
- `mouth_animation.active_beats` / `sealed_beats` — computed from beat structure
- `negative_prompt[]` — built per rules, never block intentional Motion props
- `final_compact_prompt_for_veo` — full paragraph using 5-Element Formula
- `density_check` — computed WPS, not [FILL]

Set `generation_mode`: `"IMAGE_TO_VIDEO"`, `source_image.mode`: `"FIXED_FIRST_FRAME"`, `source_image.file_reference`: `"uploaded image"`

Run all validation checks from CLAUDE_VEO_RULES.md before saving.

Save to: `D:\oldCOMPUTER\Videos\ObjectAi\pipeline\YYYY-MM-DD_TopicName\[TopicName]_VEO_PROMPTS.json`

---

## STEP 4 — Video Generation (Veo 3.1 Fast, Google Flow — Frames mode)

### 4A — Confirm settings (one screenshot)
- Video tab selected
- Frames mode selected (not Ingredients)
- 9:16 aspect ratio
- x1 quantity
- Veo 3.1 - Fast model

### 4B — Upload scene image as Start frame
**Method A — from local file (preferred):**
```js
document.querySelector('input[type="file"]').click()
```
Upload: `d:\oldCOMPUTER\Videos\ObjectAi\pipeline\YYYY-MM-DD_TopicName\images\scene_NN.png`
Confirm thumbnail appears.

**Method B — from Flow project library (fallback):**
Click Start frame slot → asset picker → select by asset ID → confirm thumbnail.

### 4C — Paste full JSON + generate

⛔ READ THIS BEFORE TYPING:
1. Read the saved JSON file: `[TopicName]_VEO_PROMPTS.json`
2. Copy the complete scene object — everything inside `scenes[N]` (NOT the outer array wrapper)
3. Click prompt textbox → type the FULL scene JSON object (use `slowly: false`)
4. Click Generate: `btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()`
5. **Wait for completion — DOM wait:**
```js
await page.waitForSelector('[data-testid="generated-video"]', { timeout: 180000 });
```

### 4D — Download video
- Navigate to video asset page → click Download
- If Playwright auto-download fails:
```js
document.querySelector('video').src
// → navigate to that URL → redirects to signed GCS URL → download via:
curl -L --ssl-no-revoke "[GCS_URL]" -o "d:\path\to\videos\scene_NN.mp4"
```
Save to: `videos\scene_NN.mp4`

### 4E — Update SESSION-RESUME.md: VIDEO → DONE → next scene → back to Step 2B

---

## STEP 5 — Final Report

```
Topic:  [Title]
Folder: D:\oldCOMPUTER\Videos\ObjectAi\pipeline\YYYY-MM-DD_TopicName\

Images:  [X] / [N] done
Videos:  [X] / [N] done

Failed scenes: [list with reason, or NONE]
JSON saved:    [TopicName]_VEO_PROMPTS.json
```

---

## Selectors Reference (Google Flow)

```
URL:           https://labs.google/fx/tools/flow
New project:   btns.find(b => b.textContent.includes('New project')).click()
Image tab:     tab with text 'imageImage' or 'Image'
Video tab:     tab with text 'videocamVideo' or 'Video'
Frames mode:   tab with text 'crop_freeFrames' or 'Frames'
9:16 ratio:    tab with text '9:16'
x1 quantity:   tab with text 'x1'
Prompt box:    textbox[placeholder*="What do you want to create?"]
Generate:      btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()
File input:    document.querySelector('input[type="file"]').click()
Video src:     document.querySelector('video').src
```
(`btns` = `Array.from(document.querySelectorAll('button'))`)

**Download fallback:**
```js
document.querySelector('video').src
// navigate to that URL → curl -L --ssl-no-revoke "[GCS_URL]" -o "d:\...\scene_NN.mp4"
```

---

## Failure Handling

**IMAGE failure:**
- FAILED-1: Rewrite image_prompt (simplify, remove ambiguous terms). Wait 30s if server error. Retry.
- FAILED-2: Log reason, skip scene, move on.

**VIDEO failure:**
- FAILED-1: Use "Reuse Prompt" button: `btns.find(b => b.textContent.includes('Reuse Prompt')).click()`. If unavailable: re-open Frames → re-upload image → re-read JSON → re-paste → generate. Wait full 3 min.
- FAILED-2: Log reason, skip, move on.

Never pause pipeline for failures. Log, skip, report at end.

SESSION-RESUME.md values: `PENDING` / `DONE` / `FAILED-1` / `FAILED-2` / `SKIP`

---

## SESSION-RESUME.md Format

```markdown
# ObjectAi Pipeline — Session Resume
## Topic / Date / Story Folder / Flow Project URL / JSON File

## Scene Progress
| Scene | Title | Image File   | Flow Image Asset ID | VIDEO   | IMAGE   |
|-------|-------|--------------|---------------------|---------|---------|
| 01    |       | scene_01.png | [fill after gen]    | PENDING | PENDING |

## Next Scene: 01 — Step: IMAGE
## Images done: 0 / N — Videos done: 0 / N
```

---

## Crash Recovery

User says: "Read SESSION-RESUME.md and continue"
→ Read SESSION-RESUME.md → read JSON file → find first PENDING scene
→ Resume from correct step (IMAGE / JSON-WRITE / VIDEO)

---

## Hard Rules

- Login check before any generation
- Confirm Image tab + 9:16 + x1 + Nano Banana 2 before generating image (one screenshot)
- Confirm Video tab + Frames + 9:16 + x1 + Veo 3.1 Fast before generating video (one screenshot)
- NEVER generate x2 — always x1
- NEVER use Ingredients mode — always Frames mode for video
- Image prompt = Beat 1 frozen pose ONLY — no open mouth, no Beat 2/3 actions
- Motion field = authoritative source for beats[].visuals — NEVER invent visuals
- Full JSON written AFTER reading the generated image — NEVER before
- Video prompt = read JSON file → paste FULL scene object — NEVER from memory
- Always update SESSION-RESUME.md after each completed step
- PATH B: output scene pack first → user confirms → then proceed
- Playwright paths: lowercase `d:\` not `D:\`
