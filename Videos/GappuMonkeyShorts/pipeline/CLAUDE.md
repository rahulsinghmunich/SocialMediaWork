# Gappu Magic Land — Execution Pipeline

**Tools:** Nano Banana Pro (Image) | Kling 3.0 I2V (Video) | Reference: `gappu_dhoti.png`

---

## STEP 00 — GENERATE FINAL PROMPTS (MANDATORY FIRST STEP)

**DO NOT SKIP.** Before any generation, you MUST generate final prompts using the v8 Master Prompt.

**Action:** Read `D:\oldCOMPUTER\Videos\Scripts\Gappu\Gappu_Master_Prompt_v8.md` → Copy entire v8 prompt → Paste into Claude with your shot breakdown/story input → Claude outputs header + final `image_prompt` + `motion_prompt` for every scene.

**Output per scene:**
- `image_prompt` — Nano Banana Pro format (ASPECT, STYLE, CHARACTER LOCK, OUTFIT, ENV LOCK, SHOT/ANGLE, LENS/DOF, LIGHTING, COMPOSITION, GAPPU EMOTION, WHAT WE SEE, QUALITY, NEGATIVE)
- `motion_prompt` — Kling V3 I2V format (FORMAT, DURATION, FPS, PACING, REFERENCE IMAGE MODE, GLOBAL MOTION RULES, SHOT, CAMERA MOVE, LENS/DOF, GAPPU PERFORMANCE, ACTION BEATS, CONSTRAINTS, ORGANIC CAMERA FEEL, AVOID)

**No tool step needed.** Prompts ready to use directly.
Proceed to STEP 0 below.

---

## Input Expected

Final `image_prompt` + `motion_prompt` per scene from Step 00 output.
Also: `gappu_in_scene` (YES/NO), `duration`, `story_title` for folder naming.

**Missing prompts?** → Generate using v8 Master Prompt first.

---

## STEP 0 — Login Check

**Using MCP Extension:**
Navigate to https://higgsfield.ai/image/nano-banana-pro → screenshot confirms profile icon (not "Sign In") → wait for user confirmation.

**Using Standalone Script (Local LLM):**
```bash
node browser-standalone.js higgsfield login
```
→ User logs in manually in opened Chrome → Auth saved to `.browser_profile/`

---

## STEP 1 — Create Story Folder

```
d:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\YYYY-MM-DD_StoryTitle\
├── SESSION-RESUME.md (all scenes PENDING)
├── images\
└── videos\
```

---

## STEP 2 — Image Generation (Nano Banana Pro)

### Settings (once, screenshot confirms)
- URL: https://higgsfield.ai/image/nano-banana-pro
- 9:16 aspect | 2K quality | Unlimited ON (blue toggle, "Unlimited →" button)

### Per Scene
1. **Clear prompt:** `document.querySelector('[id="hf:tour-image-prompt"]').focus()` → Ctrl+A → Delete
2. **Attach reference** (if `gappu_in_scene: YES`): Click `#image-form-reference` → upload `gappu_dhoti.png` → confirm thumbnail
3. **Type image_prompt:** `[id="hf:tour-image-prompt"]`, `slowly: true`
4. **Generate:** Button at left > 1000px, top 390–490px ("Unlimited →")
5. **Wait (DOM):**
   ```js
   await page.waitForSelector(':has-text("Queued")', { state: 'detached', timeout: 60000 });
   await page.waitForSelector(':has-text("Generating")', { state: 'detached', timeout: 120000 });
   ```
6. **Download:** Navigate to https://higgsfield.ai/asset/all → `img[src*="higgsfield"].src` → navigate to URL → auto-saves → move to `images/scene_NN.png`
7. **Update:** SESSION-RESUME.md IMAGE → DONE → proceed to Step 3 immediately

---

## STEP 3 — Video Generation (Kling 3.0)

1. **Navigate:** https://higgsfield.ai/create/video
2. **Set duration (JS, no slider drag):**
   ```js
   const s = document.querySelector('dialog input[type="range"]');
   const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
   setter.call(s, DURATION); s.dispatchEvent(new Event('input', { bubbles: true })); s.dispatchEvent(new Event('change', { bubbles: true }));
   ```
   Press Escape to close dialog.
3. **Upload image:** First `input[type="file"]` → scene PNG → confirm thumbnail in Start frame slot
4. **Clear prompt:** Click textbox → Ctrl+A → Delete
5. **Type motion_prompt:** `slowly: true` → if not ending with "then holds" or "then settles", append "then holds"
6. **Generate:** `btns.find(b => b.textContent.trim().startsWith('Generate')).click()`
7. **Wait (DOM):**
   ```js
   await page.waitForSelector(':has-text("Processing")', { state: 'detached', timeout: 60000 });
   await page.waitForSelector(':has-text("Generating")', { state: 'detached', timeout: 180000 });
   ```
8. **Download:** https://higgsfield.ai/asset/video → checkbox top-left on hover → Download → move from `.playwright-mcp\` to `videos/scene_NN.mp4`
9. **Update:** SESSION-RESUME.md VIDEO → DONE → next scene → Step 2

---

## STEP 4 — Final Report

Read SESSION-RESUME.md → report: completed scenes, FAILED-2 scenes with reasons, folder paths.

---

## Selectors Reference

See `D:\oldCOMPUTER\Videos\_Rules\reference-playwright-selectors.md` for shared selectors.

**Master Prompt:** `D:\oldCOMPUTER\Videos\Scripts\Gappu\Gappu_Master_Prompt_v8.md` — ALWAYS read this first to generate Block 1 + Block 2 before execution.

**Gappu-specific:**
| Element | Selector |
|---------|----------|
| Image prompt | `[id="hf:tour-image-prompt"]` |
| Reference upload | `#image-form-reference` |
| Unlimited toggle | `[role="switch"]` (bottom toolbar) |
| Video duration slider | `dialog input[type="range"]` |
| Video prompt | `textbox` (plain input, NOT contenteditable) |
| Video start frame | First `input[type="file"]` on page |

---

## Failure Handling

| Failure | Action |
|---------|--------|
| IMAGE FAILED-1 | Screenshot error. Content policy/toddler rejection → rewrite prompt (remove age-suggestive words). Server error → wait 30s, retry. |
| IMAGE FAILED-2 | Log reason. Skip. Continue. |
| VIDEO FAILED-1 | Re-navigate, re-upload, re-type prompt, retry full 3-min wait. |
| VIDEO FAILED-2 | Log reason. Skip. Continue. |

**Never pause pipeline for failures.** Log, skip, report at end.

Values: `PENDING` / `DONE` / `FAILED-1` / `FAILED-2` / `SKIP`

---

## Crash Recovery

User: "Read SESSION-RESUME.md and continue"
→ First IMAGE: PENDING → Step 2 | First VIDEO: PENDING → Step 3

---

## Hard Rules

- Login check before any generation
- 9:16 + 2K + Unlimited ON confirmed (screenshot) before first scene
- Clear prompt every scene (Ctrl+A → Delete)
- Reference only when `gappu_in_scene: YES`
- 1 scene = 1 image = 1 video — never merge
- DOM waits only — no screenshot polling
- Lowercase drive: `d:\` not `D:\`
