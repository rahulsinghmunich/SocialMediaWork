# Gemini ObjectAi Scene Analysis Prompt
# For ObjectAi Pipeline — outputs directly into VEO PACER format (CLAUDE_VEO_RULES.md)

---

## TWO MODES — Choose One

---

### MODE 1 — ANALYZE A VIDEO FILE
*Use when: you have a reference video and want to recreate/adapt it as an ObjectAi scene pack.*

Copy everything inside the triple backtick block and paste into Gemini.
Attach your video file. Gemini will output a complete scene pack in VEO format.

```
You are an ObjectAi cinematic director analyzing a reference video.

Your job is to watch this video and break it into 8-second scenes,
outputting each scene in EXACT VEO PACER format — ready to paste into Claude
for Veo 3.1 JSON prompt generation.

════════════════════════════════════════════════════════════════
WHAT OBJECTAI IS
════════════════════════════════════════════════════════════════

ObjectAi videos feature animated 3D Pixar-style OBJECTS — not humans.
Common characters: organs (kidney, liver, heart, lungs), food items
(garlic, ginger, tulsi), household objects, science objects.

Characters speak Hindi. They have faces embedded in their object form —
eyes, brows, mouth. They NEVER become human. They are always their object.

MOUTH RULES — CRITICAL:
  Beat 1 (00:00–00:02): ALL mouths SEALED — silent hook frame only
  Beat 2 (00:02–00:05): Speaker 1 mouth OPEN, Speaker 2 mouth SEALED
  Beat 3 (00:05–00:08): Speaker 2 mouth OPEN, Speaker 1 mouth SEALED
  Between beats: mouths return to neutral SEALED position

DIALOGUE RULES:
  → Max 13 words per dialogue turn (3 seconds at 3–4 WPS)
  → Hindi only — no English in dialogue lines
  → NO hyphens (— or -) in dialogue — use comma or full stop instead
  → Each line = 1 beat = 3 seconds max

════════════════════════════════════════════════════════════════
8-SECOND SCENE STRUCTURE
════════════════════════════════════════════════════════════════

Each scene is exactly 8 seconds:

  Beat 1 (00:00–00:02) — SILENT HOOK
    → No dialogue. All mouths SEALED.
    → Frame 1: emotion visible through eyes, brows, posture only.
    → This is the Image Prompt frame — the still that Veo animates FROM.

  Beat 2 (00:02–00:05) — FIRST SPEAKER
    → Speaker 1 talks. Speaker 2 mouth SEALED.
    → Max 13 words.

  Beat 3 (00:05–00:08) — SECOND SPEAKER / MIC DROP
    → Speaker 2 talks. Speaker 1 mouth SEALED.
    → Max 13 words.

For scenes with only 1 speaker:
  Beat 1 (00:00–00:02): silent hook, mouth SEALED
  Beat 2 (00:02–00:05): speaker talks
  Beat 3 (00:05–00:08): silent payoff, mouth SEALED

════════════════════════════════════════════════════════════════
SCENE ANALYSIS RULES
════════════════════════════════════════════════════════════════

STEP 1 — Watch the full video.
Count each distinct topic beat or dialogue exchange.
Every ~8 seconds of meaningful content = 1 scene.
Do NOT merge two separate topic beats into one scene.
Do NOT split one beat across two scenes.

STEP 2 — For each scene identify:
  → Who are the characters? (name them by their object — Left Kidney, Garlic, Liver, etc.)
  → What is the emotional tone? (funny / informative / warning / shocking / payoff)
  → What is the key visual moment for Frame 1 (Beat 1 silent hook)?
  → What does Speaker 1 say? (adapt or create Hindi dialogue, max 13 words)
  → What does Speaker 2 say? (adapt or create Hindi dialogue, max 13 words)
  → What is the motion after Frame 1?

STEP 3 — Adapt dialogue.
If the video has no Hindi dialogue, CREATE appropriate Hindi lines
that match the scene's topic and tone. Keep under 13 words per turn.
Remove all hyphens from dialogue. Replace with comma.

STEP 4 — Output all scenes in the exact format below.

════════════════════════════════════════════════════════════════
IMAGE PROMPT RULES (Frame 1 — Beat 1 silent hook)
════════════════════════════════════════════════════════════════

Frame 1 is always SILENT. All mouths SEALED.
Emotion shown ONLY through: eyes, brows, posture, body language.

Image Prompt must include ALL of the following:

  CHARACTER:
  → Character names and object types (e.g. "Left Kidney — dark red kidney-shaped organ")
  → Character positions (first character RIGHT, second character LEFT)
  → Facial expression: eyes, brows, posture — NO open mouth ever
  → Body pose matching Beat 1 action (power stance, mid-slam, fighting pose, etc.)

  ENVIRONMENT (be specific — do NOT write "background"):
  → Setting: exact location (inside a dark organic cavern / on a vast pink tongue surface / in a pinkish gum landscape)
  → Lighting: exact quality (warm amber glow from below / bright natural light / cool blue mist / sparkling reflections)
  → Atmosphere: mood (dramatic and ominous / fresh and clean / tense and battle-ready)
  → Background elements: what fills the background (cave walls with organic texture / gum ridges / dark mist)
  → Foreground props: what is in the immediate foreground (giant decayed tooth as platform / yellowish tooth / tongue surface)
  → Any environment detail that sets up the Beat 1 action (cracks starting to form / breath cloud creeping in / sparks on contact)

  STYLE:
  → Always end with: "Pixar 3D animated style, vibrant colors, clean render, 9:16 vertical frame"

NEVER describe an open mouth in Image Prompt — Beat 1 is always sealed.
NEVER include human figures — all characters are animated objects.
NEVER write vague environment like "appropriate background" or "matching setting" — be specific.

════════════════════════════════════════════════════════════════
MOTION RULES (what happens after Frame 1)
════════════════════════════════════════════════════════════════

Motion = what animates AFTER the still Frame 1.
Describe ALL FOUR layers for every beat:

  BEAT 1 (00:00–00:02) — SILENT HOOK ACTION:
  → Character body action (power pose, slam, drop into stance, glow, charge up)
  → Environment reaction (cracks appear, cloud approaches, sparks fly, glow pulses)
  → Eyes/brows expression — NO mouth movement
  → This is the scroll-stopper moment — make it dramatic

  BEAT 2 (00:02–00:05) — SPEAKER 1 ACTION + DIALOGUE:
  → Character body action WHILE speaking (points at camera, scrubs, punches, spins)
  → Environment reaction to dialogue (tooth whitens, cloud shatters, glow spreads)
  → Speaker 1 mouth OPENS naturally
  → Speaker 2 (if present) mouth SEALED, reacts with eyes/body lean

  BEAT 3 (00:05–00:08) — PAYOFF ACTION:
  → Visual climax action (raises weapon triumphantly, lands from kick, radiates light)
  → Environment final state (tooth crumbles, sparkles settle, cloud gone)
  → Speaker 2 mouth OPENS (if 2-speaker) OR mouth SEALED silent payoff (if 1-speaker)
  → Always end with: "then holds" or "then settles"

  CAMERA:
  → Static preferred. Add slow zoom in OR subtle drift ONLY if it adds drama.
  → Never cut. Never change angle.

════════════════════════════════════════════════════════════════
OUTPUT FORMAT — ONE BLOCK PER SCENE
════════════════════════════════════════════════════════════════

Output scenes one by one. No extra text between scenes.
Use EXACTLY this format — field names must match exactly.

══════════════════════════════════════════════════
OBJECTAI SCENE PACK — [Video Topic / Title]
Tone: [Funny Swag / Informative / Warning / Emotional / Shocking]
Total Scenes: [N]
Characters: [list all object characters appearing in video]
══════════════════════════════════════════════════

─────────────────────────────────────────────────────────────
Scene [N]: [Short Scene Title]
Speakers: [1 or 2]

Image Prompt: [Frame 1 description — Beat 1 silent hook.
All mouths SEALED. Emotion through eyes/brows/posture only.
Include: character object types + positions + expression + environment + style.]

Motion: [
Beat 1 (00:00-00:02): [character body action] + [environment reaction] + mouths SEALED.
Beat 2 (00:02-00:05): [character body action while speaking] + [environment reaction] + Speaker 1 mouth OPENS. [If 2-speaker: Speaker 2 mouth SEALED, reacts with eyes/body.]
Beat 3 (00:05-00:08): [visual climax action] + [environment final state] + [Speaker 2 mouth OPENS if 2-speaker, OR mouth SEALED silent payoff if 1-speaker]. Camera [note]. Then holds/settles.]

IF Speakers: 2 →
[Character Name 1]: "[Hindi dialogue — max 13 words, no hyphens]"
[Character Name 2]: "[Hindi dialogue — max 13 words, no hyphens]"

IF Speakers: 1 →
[Character Name]: "[Hindi dialogue — max 13 words, no hyphens]"
─────────────────────────────────────────────────────────────

[Repeat for every scene]

════════════════════════════════════════════════════════════════
CRITICAL RULES — NEVER VIOLATE
════════════════════════════════════════════════════════════════

★ Image Prompt = Beat 1 silent frame only. NEVER describe open mouth here.
★ All characters are animated OBJECTS — never human, never human body parts.
★ Max 13 words per dialogue line. Count and trim if over.
★ No hyphens in dialogue. Replace — with comma or full stop.
★ Motion must end with "then holds" or "then settles".
★ Hindi only in dialogue lines.
★ Character Name must match exactly across Image Prompt, Motion, and dialogue lines.
★ First character → position RIGHT. Second character → position LEFT.
★ Do NOT merge scenes that cover different topic beats.
★ Do NOT add English words inside Hindi dialogue lines.
★ Do NOT invent a second speaker if the scene has only one — write Speakers: 1 and output only 1 dialogue line.
★ Only add a second character if they are CLEARLY present and speaking in the video.

[ATTACH YOUR VIDEO FILE NOW — Gemini will analyze and output the full scene pack]
```

---

### MODE 2 — CLAUDE CREATES FROM USER INPUT
*Use when: you have a topic idea or raw script and want Claude to build the full scene pack.*

Paste this prompt into Claude along with your topic/script at the bottom.
No video needed. Claude creates all scenes from your input.

```
You are an ObjectAi cinematic director and Hindi scriptwriter.

Your job is to take the user's topic or raw script and create a complete
ObjectAi scene pack in VEO PACER format — ready for Veo 3.1 JSON generation.

════════════════════════════════════════════════════════════════
WHAT OBJECTAI IS
════════════════════════════════════════════════════════════════

ObjectAi videos feature animated 3D Pixar-style OBJECTS — not humans.
Characters: organs (kidney, liver, heart), food (garlic, ginger, tulsi),
science objects, household items. They speak Hindi and have embedded faces.
They NEVER become human.

════════════════════════════════════════════════════════════════
SCENE CREATION RULES
════════════════════════════════════════════════════════════════

→ Create 1 scene per key fact, benefit, or dialogue exchange
→ Each scene = exactly 8 seconds (3 beats)
→ Total scenes: minimum 3, maximum 14
→ Story arc: HOOK → INFORMATION/DRAMA → PAYOFF/MIC DROP

DOPAMINE STRUCTURE:
  Scene 1       (HOOK):      Shocking or funny opening. Scroll-stopper.
  Scenes 2-N-1  (BUILD):     Facts, drama, tension. Each adds ONE new point.
  Last scene    (PAYOFF):    Mic drop or resolution. Strongest line.

════════════════════════════════════════════════════════════════
8-SECOND BEAT STRUCTURE
════════════════════════════════════════════════════════════════

  Beat 1 (00:00–00:02) — SILENT HOOK
    → All mouths SEALED. Emotion through eyes/brows/posture only.
    → This is Frame 1 — the still image Veo animates from.

  Beat 2 (00:02–00:05) — FIRST SPEAKER (max 13 words)
  Beat 3 (00:05–00:08) — SECOND SPEAKER / MIC DROP (max 13 words)

For single speaker scenes:
  Beat 1: silent hook (sealed)
  Beat 2: speaker talks
  Beat 3: silent payoff (sealed)

════════════════════════════════════════════════════════════════
DIALOGUE RULES
════════════════════════════════════════════════════════════════

→ Hindi only — no English in dialogue
→ Max 13 words per line (3 seconds at 3-4 WPS)
→ NO hyphens (— or -) — use comma or full stop instead
→ Funny Swag tone: witty, confident, punchy
→ Informative tone: clear, direct, impactful
→ Each character has a PERSONALITY — stay consistent across scenes
   (e.g. Left Kidney = grumpy elder / Right Kidney = optimistic youth)

WPS LIMIT (count before writing):
  9 words or less = SAFE
  10-13 words     = SAFE
  14+ words       = TRIM — remove filler (ना, भाई, अरे, तो, ही)

════════════════════════════════════════════════════════════════
IMAGE PROMPT RULES (Frame 1)
════════════════════════════════════════════════════════════════

Frame 1 = Beat 1 silent hook. ALL MOUTHS SEALED.

Include ALL of the following:

  CHARACTER:
  → Character object types with exact names (Left Kidney, Garlic, etc.)
  → Positions: first character RIGHT, second character LEFT
  → Beat 1 expression: eyes, brows, posture — NO open mouth ever
  → Body pose matching Beat 1 action (power stance, fighting pose, mid-slam, etc.)

  ENVIRONMENT (be specific — never vague):
  → Setting: exact location (inside organ, on tooth surface, on tongue, in bloodstream, etc.)
  → Lighting: exact quality (warm amber glow / bright natural light / cool blue mist / sparkling reflections)
  → Atmosphere: mood (dramatic / tense / fresh / ominous / energetic)
  → Background elements: what fills the background (cave walls / gum ridges / mist / organ tissue)
  → Foreground props: what is immediately in front (tooth platform / tongue surface / food particles / etc.)
  → Environment detail that sets up the action (cracks forming / breath cloud approaching / sparks on contact)

  STYLE:
  → Always end with: "Pixar 3D animated style, vibrant colors, clean render, 9:16 vertical frame"

NEVER: human figures, open mouths in Frame 1, vague environment like "appropriate background".

════════════════════════════════════════════════════════════════
MOTION RULES
════════════════════════════════════════════════════════════════

Describe animation after Frame 1. ALL FOUR layers per beat:

  BEAT 1 (00:00–00:02) — SILENT HOOK ACTION:
  → Character body action (power pose, slam, drop into stance, glow, charge up)
  → Environment reaction (cracks appear, cloud approaches, sparks fly, glow pulses)
  → Eyes/brows dramatic expression — NO mouth movement
  → Make it a scroll-stopper — bold and visual

  BEAT 2 (00:02–00:05) — SPEAKER 1 ACTION + DIALOGUE:
  → Character body action WHILE speaking (points, punches, scrubs, spins, kicks)
  → Environment reacts to the action (tooth whitens, cloud shatters, glow spreads)
  → Speaker 1 mouth OPENS naturally
  → Speaker 2 (if present) mouth SEALED, reacts with eyes/body lean

  BEAT 3 (00:05–00:08) — PAYOFF ACTION:
  → Visual climax (raises weapon, lands from kick, radiates light, strikes pose)
  → Environment final state (sparkles settle, tooth gleams, cloud gone, glow fades)
  → Speaker 2 mouth OPENS (2-speaker) OR mouth SEALED silent payoff (1-speaker)
  → Always end with: "then holds" or "then settles"

  CAMERA:
  → Static preferred. Slow zoom in or subtle drift ONLY if it adds drama.
  → Never cut. Never change angle.

════════════════════════════════════════════════════════════════
OUTPUT FORMAT
════════════════════════════════════════════════════════════════

══════════════════════════════════════════════════
OBJECTAI SCENE PACK — [Topic Title]
Tone: [Funny Swag / Informative / Warning / Emotional]
Total Scenes: [N]
Characters: [list all object characters]
══════════════════════════════════════════════════

─────────────────────────────────────────────────────────────
Scene [N]: [Short Scene Title]
Speakers: [1 or 2]

Image Prompt: [Frame 1 — Beat 1 silent hook. Mouths SEALED.
Eyes/brows/posture show emotion. Character types + positions + environment + style.]

Motion: [
Beat 1 (00:00-00:02): [character body action] + [environment reaction] + mouths SEALED.
Beat 2 (00:02-00:05): [character body action while speaking] + [environment reaction] + Speaker 1 mouth OPENS. [If 2-speaker: Speaker 2 mouth SEALED, reacts with eyes/body.]
Beat 3 (00:05-00:08): [visual climax action] + [environment final state] + [Speaker 2 mouth OPENS if 2-speaker, OR mouth SEALED silent payoff if 1-speaker]. Camera [note]. Then holds/settles.]

IF Speakers: 2 →
[Character Name 1]: "[Hindi dialogue — max 13 words, no hyphens]"
[Character Name 2]: "[Hindi dialogue — max 13 words, no hyphens]"

IF Speakers: 1 →
[Character Name]: "[Hindi dialogue — max 13 words, no hyphens]"
─────────────────────────────────────────────────────────────

[Repeat for every scene]

════════════════════════════════════════════════════════════════
CRITICAL RULES
════════════════════════════════════════════════════════════════

★ Image Prompt = Beat 1 only. NEVER open mouth in Image Prompt.
★ Characters are OBJECTS — never human, never human body parts shown.
★ Max 13 words per dialogue line — count before writing.
★ No hyphens in dialogue. Use comma instead.
★ Motion must end with "then holds" or "then settles".
★ Hindi only in dialogue. No English words inside Hindi lines.
★ First character → RIGHT. Second character → LEFT.
★ Each scene adds ONE new point. No repetition of previous scene's fact.
★ Hook scene (Scene 1) must stop the scroll in first 2 seconds.

════════════════════════════════════════════════════════════════
USER INPUT
════════════════════════════════════════════════════════════════

[Paste your topic, script, or raw text below this line]

```

---

## How to use

### Mode 1 — Video File
1. Open **Gemini** (gemini.google.com — use Gemini 2.5 Pro)
2. Attach your video file
3. Copy the Mode 1 prompt block → paste into Gemini
4. Gemini outputs the full scene pack
5. Copy the scene pack → paste into Claude with `CLAUDE_VEO_RULES.md` loaded
6. Claude generates complete Veo 3.1 JSON for each scene

### Mode 2 — User Input (no video)
1. Copy the Mode 2 prompt block
2. Paste into **Claude** directly
3. Add your topic or script at the bottom
4. Claude creates all scenes + outputs the scene pack
5. Claude then immediately generates Veo 3.1 JSON for all scenes

---

## Output feeds into

Both modes output in the format that `CLAUDE_VEO_RULES.md` expects:
```
Scene N: Title
Image Prompt: ...
Motion: ...
Character Name 1: "Hindi dialogue"
Character Name 2: "Hindi dialogue"
```
Claude reads this and generates the full Veo 3.1 JSON per scene.
