# Bhakti Channel — Full Production Pipeline

## Workflow
Research (NotebookLM) → Script (Claude writes) → YOU APPROVE → Images + Videos (Higgsfield) → Narration script (ElevenLabs V3)

---

## Paths & Tools
- **Pipeline folder**: `D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\`
- **Character reference**: `D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\CHARACTER_REFERENCE.md` ← read when writing any VISUAL PROMPT
- **nlm.py**: `D:\oldCOMPUTER\Videos\AIRelatedCode\notebooklm-skill\scripts\nlm.py`
- **Image tool**: Higgsfield Nano Banana Pro — https://higgsfield.ai/image/nano-banana-pro
- **Video tool**: Higgsfield Kling 3.0 V3 I2V — https://higgsfield.ai/create/video
- **No character reference image** — all characters fully described in each VISUAL PROMPT

---

## STEP 0 — Login Check (once per session)

1. Navigate to https://higgsfield.ai/image/nano-banana-pro via Playwright
2. Take one screenshot — confirm profile icon visible (not Sign In button)
3. If NOT logged in: tell user "Please log in to Higgsfield in the Playwright browser, then confirm"
4. Do not proceed until user confirms

---

## STEP 1 — NotebookLM Research

User gives a story idea (e.g. "Hanuman swallows the sun" or "Shiv drinks halahala poison").

### 1A — Create notebook
```bash
python "D:\oldCOMPUTER\Videos\AIRelatedCode\notebooklm-skill\scripts\nlm.py" create "[StoryTitle] Research"
```

### 1B — Add sources (minimum 3)
```bash
python "D:\...\nlm.py" add-source --notebook-id NOTEBOOK_ID --url "https://en.wikipedia.org/wiki/[relevant_page]"
python "D:\...\nlm.py" add-source --notebook-id NOTEBOOK_ID --url "https://en.wikipedia.org/wiki/[character_name]"
python "D:\...\nlm.py" add-source --notebook-id NOTEBOOK_ID --url "https://en.wikipedia.org/wiki/[purana_name]"
```

### 1C — Ask user for extra sources
PAUSE and tell user: "NotebookLM notebook created with [X] sources. Add more? (paste links, PDFs, or text) Or say NO to continue."
Wait for response before proceeding.

### 1D — Run 3 research queries (save all outputs)

**Query 1 — Unknown Facts**
```bash
python "D:\...\nlm.py" ask "What are 3 lesser-known or surprising facts about [STORY] from original Puranic texts such as Valmiki Ramayana, Shiv Purana, Bhagavata Purana, or Hanuman Chalisa? Include exact Sanskrit shlokas with Hindi meaning and source (Purana name, chapter or verse if available). Focus on facts that most people do not know." --notebook-id NOTEBOOK_ID
```

**Query 2 — Emotional Peak**
```bash
python "D:\...\nlm.py" ask "What is the single most emotionally powerful or painful moment in [STORY]? Describe the internal state of the main character — their fear, sacrifice, love, or rage. What did they risk or lose? What makes this moment human despite being divine?" --notebook-id NOTEBOOK_ID
```

**Query 3 — Hook Contradiction**
```bash
python "D:\...\nlm.py" ask "What event or fact in [STORY] sounds impossible, shocking, or contradictory when stated in one sentence? Something that creates disbelief in the listener — a divine paradox, a reversal, an unknown consequence. Must be scripturally accurate." --notebook-id NOTEBOOK_ID
```

---

## STEP 2 — Write Scene Script

Using the 3 research outputs, write a complete 10–12 scene script.

### Dharmic Accuracy Rules (NEVER SKIP)
- Every fact used in narration must come from NotebookLM research output
- If a fact is not confirmed by research, do NOT invent it — mark it [GENERAL TRADITION]
- Sanskrit shlokas must be taken from research — do not generate shlokas
- Character attributes must be scripturally accurate — read `CHARACTER_REFERENCE.md`
- Do NOT mix attributes across characters

### Arc Structure
```
Scene 01 — HOOK      → The shocking contradiction. Stops the scroll.
Scene 02 — HOOK      → Deepen the hook. Show what's at stake.
Scene 03 — BUILD     → Context. The world before the event.
Scene 04 — BUILD     → The challenge or threat appears.
Scene 05 — BUILD     → Rising tension. Characters react.
Scene 06 — CLIMAX    → The peak divine act. Most powerful visual.
Scene 07 — CLIMAX    → Consequence of the act. Universe reacts.
Scene 08 — TURN      → Unexpected truth or lesser-known detail.
Scene 09 — TURN      → Emotional depth. The human inside the divine.
Scene 10 — PAYOFF    → Resolution. The blessing or lesson.
Scene 11 — PAYOFF    → Moral revelation. Why this matters today.
Scene 12 — PAYOFF    → Call to devotion. Final image. Jai [Character].
```

### Scene Format (write every scene in this exact format)
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎬 SCENE [N] — [ARC]
⏱️ [0:00–0:07]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 DHARMIC SOURCE:
[Exact Purana name + chapter/verse if available]

📸 VISUAL PROMPT:
[Full Nano Banana Pro prompt — English only, 6-factor structure below]

🎥 MOTION PROMPT:
[Full Kling V3 motion prompt — English only, formula below]

🎙️ NARRATION (Hindi):
[1–2 powerful Hindi sentences. Max 20 words total.]

🕉️ SHLOKA (only if research provided one):
[Sanskrit line] — [Hindi meaning in 1 line]

💫 EMOTION: [भय / श्रद्धा / रोमांच / करुणा / वीरता / आनंद]
🔥 VIRAL SCORE: [1–10]
──────────────────────────────────────
```

### VISUAL PROMPT — 6-Factor Structure
Write full sentences like a creative director. NO tag lists. Explain the WHY. Under 150 words.
```
[SUBJECT]     — who/what, with specific scriptural attributes (read CHARACTER_REFERENCE.md)
[ACTION]      — what is happening or the emotional state expressed
[SETTING]     — exact environment (temple type, forest, ocean, cosmic space, battlefield)
[COMPOSITION] — camera angle, framing, shot type, spatial positions
[LIGHTING]    — specific real light sources only (never "dramatic lighting")
[STYLE]       — photorealistic cinematic render, Unreal Engine 5 quality, 9:16 vertical
```

Key rules:
- English only — never mix Hindi/Sanskrit into the image prompt
- Use ONLY real light sources: "sacred fire glow," "diya candlelight," "golden hour rays," "moonlight through temple arch"
- Add micro-texture: "silk fabric with visible thread weave," "ash-smeared skin," "serpent scales gleaming"
- Add particles: "lotus petals drifting," "ash particles in light," "divine energy orbs," "battle dust"
- NEVER use "dramatic," "epic," "ultra-realistic," "beautiful" alone — be specific instead

### MOTION PROMPT — Formula
```
[Subject action with start and end point] + [Camera movement with endpoint] + [Atmosphere behavior] + [What stays still]
```

Non-negotiable rules:
1. **Always include a motion endpoint**: "slow push in, then holds" ✅ / "slow push in" alone ❌
2. **Specify camera explicitly** — without instruction, camera improvises unpredictably
3. **One main action per shot** — max 2 simultaneous camera movements
4. **State what stays still** — "Background stone pillars remain static"
5. Prompt length: 30–60 words — describe motion only, not the image

Motion endpoints: `then holds` / `then settles` / `settles on [face/crown/hands]` / `returns to starting position`

---

## STEP 3 — Present Script for Approval

Show user:
- Complete 12-scene script
- Opening Hook line (scene 01 narration)
- Viral scores

PAUSE — tell user: "Script complete. Review it above. Say GO to start generation. Or tell me what to change."

**DO NOT proceed to Higgsfield until user says GO.**

---

## STEP 4 — Create Story Folder

```
D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\YYYY-MM-DD_StoryTitle\
├── SESSION-RESUME.md
├── images\
├── videos\
└── narration.txt  ← created in Step 7
```

Confirm path to user before generating anything.

---

## STEP 5 — Image Generation (Nano Banana Pro, Higgsfield)

No reference image for Bhakti — never attach a reference PNG.

### 5A — Page Setup (once per session)
1. Navigate to https://higgsfield.ai/image/nano-banana-pro
2. Set aspect ratio to 9:16: click ratio button → pick "9:16"
3. Set quality to 2K: click quality button → pick "2K"
4. Turn Unlimited ON: click `[role="switch"]` toggle until blue — Generate button shows "Unlimited →"
5. Take ONE screenshot confirming all three settings before first scene

### 5B — Per Scene: Generate Image

**1. Clear prompt bar**
- Focus: `document.querySelector('[id="hf:tour-image-prompt"]').focus()`
- Press Ctrl+A then Delete

**2. Skip reference image** — Bhakti has no reference PNG

**3. Type the VISUAL PROMPT** — use `slowly: true` on `[id="hf:tour-image-prompt"]`

**4. Click Generate** — button at left > 1000px, top 390–490px (shows "Unlimited →")

**5. Wait for completion — DOM wait, no screenshot polling**
```js
await page.waitForSelector(':has-text("Queued")', { state: 'detached', timeout: 60000 });
await page.waitForSelector(':has-text("Generating")', { state: 'detached', timeout: 120000 });
```

**6. Download image**
- Navigate to https://higgsfield.ai/asset/all
- Get latest image src: `document.querySelector('img[src*="higgsfield"]').src`
- Navigate to that URL → Playwright downloads automatically
- Save to: `d:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\YYYY-MM-DD_StoryTitle\images\scene_NN.png`

**7.** Update SESSION-RESUME.md: IMAGE → DONE → proceed to Step 6 for this scene

### 5C — If image is 80% right, edit don't re-roll
```
Keep everything identical. ONLY change: [specific element].
KEEP UNCHANGED: character appearance, pose, setting, lighting, color palette.
```

---

## STEP 6 — Video Generation (Kling 3.0 V3, Higgsfield)

Immediately after each image confirmed:

**1.** Navigate to https://higgsfield.ai/create/video

**2. Set duration to 4s via JS** — do not manually drag slider:
```js
const s = document.querySelector('dialog input[type="range"]');
const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
setter.call(s, 4);
s.dispatchEvent(new Event('input', { bubbles: true }));
s.dispatchEvent(new Event('change', { bubbles: true }));
```
Close dialog with Escape.

**3. Upload scene image** — first `input[type="file"]` on page → scene PNG path
- Confirm thumbnail appears in Start frame slot

**4. Clear prompt** — click textbox → Ctrl+A → Delete

**5. Type MOTION PROMPT** — use `slowly: true`
- Confirm prompt ends with "then holds" or "then settles" — append if missing

**6. Click Generate** — `btns.find(b => b.textContent.trim().startsWith('Generate')).click()`

**7. Wait for completion — DOM wait, no screenshot polling**
```js
await page.waitForSelector(':has-text("Processing")', { state: 'detached', timeout: 60000 });
await page.waitForSelector(':has-text("Generating")', { state: 'detached', timeout: 180000 });
```

**8. Download video**
- Navigate to https://higgsfield.ai/asset/video
- Click checkbox on Today card (appears top-left on hover)
- Click Download in bottom toolbar — Playwright saves to `.playwright-mcp\`
- Move: `mv ".playwright-mcp\<filename>.mp4" "d:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\YYYY-MM-DD_StoryTitle\videos\scene_NN.mp4"`

**9.** Update SESSION-RESUME.md: VIDEO → DONE → next scene → back to Step 5B

---

## STEP 7 — ElevenLabs V3 Narration Script

After ALL scenes complete, extract NARRATION from every scene in order and generate `narration.txt`.

### Emotion → Audio Tag Mapping
```
भय (fear)         → [ominous][dark tone]
करुणा (compassion) → [sorrowful]
रोमांच (thrill)    → [rising intensity][excited]
श्रद्धा (devotion)  → [reverent][drawn out]
वीरता (valor)      → [heroic][intense]
आनंद (joy)         → [warm][peaceful]
```

### Format Rules
- Start with `[deep voice][dramatic]`
- Use `[pause]` between scenes, `[long pause]` between major arc shifts
- Use `...` for dramatic pauses within sentences
- CAPITALS for key divine words (e.g. SHIVA, SHAKTI, OM)
- Keep Hindi text EXACTLY as written — do NOT translate or modify
- One continuous block — no scene numbers, no labels

### Example
```
[deep voice][dramatic] जब सारे देवता हार गए... [pause] [shouting] तब प्रकट हुई वो शक्ति!

[long pause]

[ominous][dark tone] महिषासुर ने तीनों लोकों पर अधिकार कर लिया था।
```

Save to: `D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\YYYY-MM-DD_StoryTitle\narration.txt`

Tell user when done: ElevenLabs V3 settings — Model: Eleven V3, Stability: 0.45–0.55, Clarity: 0.75, Style: 0.35–0.45

---

## STEP 8 — Final Report

```
Story: [Title]
Folder: D:\oldCOMPUTER\Videos\BhaktiChannel\pipeline\YYYY-MM-DD_StoryTitle\

Images:    [X] / 12 done
Videos:    [X] / 12 done
Narration: narration.txt saved

Failed scenes: [list with reason, or NONE]

Next step: Open narration.txt → paste into ElevenLabs V3
```

---

## Selectors Reference

| Element | Selector |
|---------|----------|
| Image prompt bar | `[id="hf:tour-image-prompt"]` |
| Unlimited toggle | `[role="switch"]` in bottom toolbar |
| Generate (image) | button at left > 1000px, top 390–490px |
| Video prompt | `textbox` (plain input — NOT contenteditable) |
| Video start frame | first `input[type="file"]` on page |
| Generate (video) | `btns.find(b => b.textContent.trim().startsWith('Generate'))` |
| Video assets | https://higgsfield.ai/asset/video → checkbox top-left on hover → Download |

---

## Failure Handling

**IMAGE failure:**
- FAILED-1: If content policy → rewrite VISUAL PROMPT, make description more reverent, remove ambiguous terms. If server error → wait 30s, retry.
- FAILED-2: Log in SESSION-RESUME.md with reason. Skip scene. Continue pipeline.

**VIDEO failure:**
- FAILED-1: Re-navigate, re-upload image, re-type motion prompt, retry full 3-min wait.
- FAILED-2: Log, skip, continue pipeline.

Never pause the pipeline for failures. Log, skip, move on. Report all at end.

SESSION-RESUME.md values: `PENDING` / `DONE` / `FAILED-1` / `FAILED-2` / `SKIP`

---

## SESSION-RESUME.md Format

```markdown
# Bhakti Pipeline — Session Resume

## Story Title / Date / NotebookLM Notebook ID / Story Folder

## Scene Progress

| Scene | Arc    | Image File   | Video File   | IMAGE   | VIDEO   |
|-------|--------|--------------|--------------|---------|---------|
| 01    | HOOK   | scene_01.png | scene_01.mp4 | PENDING | PENDING |

## Next Scene to Process
Scene: 01 — Step: IMAGE

## Completed Summary
Images done: 0 / 12 — Videos done: 0 / 12
```

---

## Crash Recovery

User says: "Read SESSION-RESUME.md and continue"
→ Find first PENDING scene → resume from Step 5B (image) or Step 6 (video)

---

## Hard Rules

- Login check before any generation
- Confirm 9:16 + 2K + Unlimited ON before first scene (one screenshot)
- Clear prompt bar before every scene — Ctrl+A → Delete
- NEVER attach a reference image for Bhakti
- NEVER invent dharmic facts — only use what NotebookLM research confirmed
- NEVER modify Sanskrit shlokas — use exactly as research provided
- Always show script to user and wait for GO before starting Higgsfield
- Never start next scene until current image confirmed saved to disk
- DOM waits only — no screenshot polling for generation status
- Motion prompts MUST end with: "then holds" / "then settles" / "returns to starting position"
- VISUAL PROMPTs: read CHARACTER_REFERENCE.md — never describe characters from memory
- Playwright paths: lowercase `d:\` not `D:\`
