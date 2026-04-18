# /transform-video

Analyse a reference video → generate a complete Gappu scene pack (Block 1 + Block 2) ready to paste into the HTML tools.

## What this skill does

1. Analyse reference video OR raw story input (TwelveLabs OR pasted)
2. Extract style, motion, emotional arc, viral mechanics
3. Confirm understanding with user
4. Generate Similar Ideas List (5-10 concepts)
5. Output full Gappu scene pack — Block 1 (Scene Pack) + Block 2 (Locks Pack)
6. Apply viral engineering layer
7. Pick Hook + Grid 1 + Grid 2 (3-clip Reel structure — Claude decides based on arc, not fixed rules)
8. Generate viral caption pack
9. Save everything to file

The output is designed to paste directly into:
- `GappuViralPromptBuilder.html` → Builder tab (Block 1)
- `GappuViralPromptBuilder.html` → Locks tab (Block 2)

---

## HOW TO START

User provides ONE of:
- Local video path → index with TwelveLabs first
- TwelveLabs video ID → analyse directly
- Pasted analysis text from Gemini or ChatGPT → skip to Step 2
- Plain text description → Claude fills all fields

If local path given → run `mcp__twelvelabs-mcp__start-video-indexing-task`, wait for status "ready", then analyse.

---

## STEP 1 — ANALYSE THE VIDEO

Use `mcp__twelvelabs-mcp__analyse-video` with this prompt:

```
Analyse this video in full detail. Extract:
1. VISUAL STYLE: Animation style, rendering, color palette, aspect ratio, overall aesthetic
2. MOTION STYLE: Camera movement, pacing, cut speed, transitions
3. EMOTIONAL ARC: Label each scene HOOK / PAIN / STRUGGLE / TURN / PAYOFF
4. SCENE BREAKDOWN: For each scene — action, characters, location, lighting, shot type, duration, emotion
5. HOOK MOMENT: Exactly what happens in first 3 seconds that stops the scroll
6. VIRAL MECHANIC: What makes this shareable — curiosity / emotion / relatability / shock / humor
7. VIRAL TRIGGER: Which of these does it hit?
   □ "This is exactly what happened to me"
   □ "I need to call someone right now"
   □ "This made me cry and I don't know why"
   □ "I need to show this to someone specific"
   □ "I want to watch this again immediately"
8. REWATCH DETAIL: Any visual planted in scene 1 that pays off in the last scene?
9. VISUAL ECHO PAIR: Same composition repeated with reversed emotion?
10. CORE MESSAGE: What feeling does the viewer leave with
11. AUDIO: Music mood, sound effects, any dialogue
```

After analysis, show user a **brief scene summary** and ask:
> "Does this look accurate? Anything I missed or got wrong?"

User confirms or corrects → proceed.

---

## STEP 2 — SIMILAR IDEAS LIST

Generate 5-10 video concepts in the same style/niche as the reference.

```
SIMILAR VIDEO IDEAS — based on [reference video title/topic]

1. [Idea Name]
   Concept: [one sentence]
   Hook: [what stops scroll in first 2-3 seconds]
   Viral trigger: [which checklist item it hits]
   Why it works: [viral mechanic]

2. [Idea Name]
   ...
```

Keep same: visual style, emotional tone, target audience. Total under 60 seconds each.

---

## STEP 3 — GAPPU SCENE PACK

Convert the reference video into a full Gappu Magic Land scene pack using the v7 format.

### First — Viral Engineering Header

Before writing any scenes, state:

```
VIRAL ANALYSIS:
Hook Type:      [Curiosity Gap / Relatability Bomb / Emotional Reversal / Maa Factor / Childhood Nostalgia / Underdog Win]
Viral Trigger:  [exact checklist phrase that this story hits]
Story Core:     [one sentence — the central emotion]
Rewatch Detail: [scene 1 plant → last scene payoff]
Visual Echo:    [scene N mirrors scene M — same composition, reversed emotion]
Dopamine Curve: SPIKE → DROP → TENSION → TENSION → RELEASE → PEAK
                [map each scene to its curve position]
```

Then state: "I chose [Hook Type] because [reason]. The rewatch plant is [X] in scene 1 which pays off as [Y] in the last scene."

---

### BLOCK 1 — SCENE PACK

Output this header first:

```
┌─────────────────────────────────────────────────────────────┐
INPUT MODE:       [A — Shot Breakdown (N shots → N scenes)]
                  [B — Free-Form Story (Claude editorial: N scenes)]
STORY CORE:       [one sentence — the central emotion]
REWATCH DETAIL:   [scene 1 plant + last scene payoff — one line]
VISUAL ECHO PAIR: [scene N mirrors scene M, reversed emotion]
VIRAL TRIGGER:    [which checklist item this hits]
TOTAL SCENES:     [number]
LOCATIONS:        [all distinct env_name values]
GAPPU OUTFIT:     [one line — full detail in Block 2]
NEW CHARACTERS:   [names needing locks in Block 2]
└─────────────────────────────────────────────────────────────┘
```

Then output every scene in EXACTLY this format:

```
─────────────────────────────────────────────────────────────
scene: [N]
arc:            [HOOK / PAIN / STRUGGLE / TURN / PAYOFF]
env_name:       [2-4 words — MUST exactly match NAME in Block 2]
gappu_in_scene: [YES or NO — MANDATORY every scene]
action:         [ONE frozen frame. Prompt-fragment style. Max 3 short sentences.
                ONE movement verb. Tail state if gappu_in_scene: YES.
                Other characters' expressions go HERE not in emotion.]
emotion:        [GAPPU ONLY. Eyes. Face. Body. Explicit tail state.
                [NOT IN SCENE] if gappu_in_scene: NO]
location:       [Setting. Time of day. Light quality.]
characters:     [Exact Block 2 slot names. "Gappu alone" if solo.]
shot:           [EXTREME CLOSE-UP / CLOSE-UP / MEDIUM CLOSE-UP / MEDIUM SHOT / MEDIUM-WIDE / WIDE SHOT / TWO-SHOT / POV LOW ANGLE]
lens:           [85mm / 135mm / 50mm / 35mm / 28mm]
camera_move:    [STATIC / VERY SLOW PUSH-IN / SLOW ZOOM OUT / TRACKING / FREEZE THEN PUSH / REVEAL PAN]
duration:       [number only — HOOK: 5-6 | PAIN: 7-9 | STRUGGLE: 6-7 | TURN: 5-6 | PAYOFF: 8-10 | total under 60s]
lighting:       [Type + tone — COLD/PAIN: blue-grey overcast | HARSH/WORK: high contrast hard shadows | WARM/HOPE: golden backlight | MAGIC HOUR: final payoff only | NIGHT/PLAN: single lamp warm | RAIN/GRIEF: blue-grey wet]
composition:    [Subject position + surrounding elements]
music_energy:   [SILENT / BUILDING STRINGS / SOFT FOLK / SUDDEN SILENCE / SWELLING ORCHESTRA / LIGHT BEAT / LOW DRONE]
cut_to:         [First image of next scene. "END — hold on Gappu's face" for last scene.]
cin_reason:     [Director logic. What must viewer feel + why these specific tools achieve it. NOT a scene summary.]
─────────────────────────────────────────────────────────────
```

#### Key rules for action: field

- Single frozen frame — one moment, one emotion
- BANNED words in action: then / as he / after / suddenly / watches
- Must include ONE movement verb (stands, grips, leans, holds, steps, reaches, crouches, turns, lifts, presses)
- gappu_in_scene: YES → include explicit tail state in action
- gappu_in_scene: NO → no tail, describe only what IS in frame
- Other characters' expressions go in action, never in emotion

#### gappu_in_scene: NO — use for:
Object shots, villain-only shots, environment reveals, any frame where Gappu is physically absent.

#### Duration rule:
Durations are guides not fixed rules. Claude decides based on emotional arc. Total must stay under 60 seconds.

---

### BLOCK 2 — LOCKS PACK

```
══════════════════════════════════════════════════
LOCKS PACK — [Story Title]
══════════════════════════════════════════════════

##OUTFIT##
[Gappu outfit. Color, fabric, accessories, footwear.
Scene-specific changes noted by scene number.
Prompt fragment — comma-separated, no prose. Max 4 sentences.]
##END_OUTFIT##

##ENV_SLOT_START##
NAME: [Location name — EXACTLY matching env_name in scenes]
##ENV_LOCK##
[Ultra-realistic environment. 4-6 lines.
Real-world location anywhere on earth.
Specific ground texture, architecture, ambient life,
lighting quality, dominant color palette, time of day.
Must feel like a real photograph. 50 words max.
Prompt fragment, comma-separated.]
##ENV_SLOT_END##

[Repeat for each location. Max 6.]

##CHAR_SLOT_START##
SLOT: 1
NAME: [Exact name matching characters: field in scenes]
##CHAR_LOCK##
Type: [Photorealistic / 3D Pixar same-style as Gappu]
Physical description: [Species/age, build, fur/skin/color, key feature, height vs Gappu]
Outfit for this story: [Colors, fabric, accessories. Scene-specific changes by scene number.]
Expression default: [Neutral baseline face between beats]
Key visual rule: [One consistency rule — enforced every scene]
Role in story: [One sentence — their emotional function]
##CHAR_SLOT_END##

[Repeat for each recurring character. Max 4 slots.]
[No extra characters: write NO EXTRA CHARACTERS]

══════════════════════════════════════════════════
END OF LOCKS PACK
══════════════════════════════════════════════════
```

#### Character rendering rules:
- Gappu → always 3D Pixar (handled by anatomy anchor, not in CHAR_SLOT)
- Animal / non-human characters → 3D Pixar same style as Gappu
- Child characters → 3D Pixar same style
- Adult humans → photorealistic
  - Mother/Maa: NEVER show face — hands/back/silhouette only
  - Father/Baba: CAN show face. Weathered, tired, proud.
  - Background characters → describe in ENV_LOCK or action only, NO CHAR_SLOT

---

## STEP 4 — HOOK + GRID SELECTION (3-CLIP REEL STRUCTURE)

After the full scene pack is done, Claude picks 3 scenes as the **Reel/Short highlight clips**.

These are the 3 clips that carry the entire video as a standalone short-form post.

### How Claude picks:

**HOOK** — always scene 1 or the single most scroll-stopping moment.
Must stop scroll in 2 seconds. Usually the emotional spike.

**GRID 1** — the emotional core. NOT always PAIN. Claude reads the arc and picks whichever scene carries the heaviest weight — could be PAIN, STRUGGLE, or TURN depending on what hits hardest in this specific story.

**GRID 2** — the payoff/resolution. Usually the final PAYOFF scene but not a hard rule — if a TURN scene is more emotionally powerful than the last PAYOFF, Claude picks that.

**The "mix up" rule:** Claude does NOT default to Hook=scene1 / Grid1=PAIN / Grid2=PAYOFF every time. It reads the specific story's emotional arc and picks the 3 scenes that together make the strongest standalone viewing experience. State the reasoning.

### Output format:

```
HOOK + GRID SELECTION — [Story Title]

HOOK:   Scene [N] — [arc label] — [one sentence why this stops the scroll]
GRID 1: Scene [N] — [arc label] — [one sentence why this is the emotional core]
GRID 2: Scene [N] — [arc label] — [one sentence why this is the right ending moment]

Reasoning: [2-3 sentences — why these 3 scenes together tell the complete story
            and what emotional journey the viewer goes on in under 60 seconds]
```

These 3 scenes already exist in the full scene pack above — no new prompts needed. The HTML tool will generate their image + video prompts automatically.

---

## STEP 5 — VIRAL CAPTION PACK  

Generate ready-to-use captions for the video:

```
CAPTION OPTIONS — [Story Title]

SAVE-TRIGGER:
[Hindi/Hinglish caption designed to make viewer save]

COMMENT-HOOK:
[Caption that invites a specific comment response]

SHARE-TRIGGER:
[Caption that makes viewer want to tag/share with someone specific]

TITLE OPTIONS (5):
1. [Title]
2. [Title]
3. [Title]
4. [Title]
5. [Title]

Rules: Match language (Hindi/English/Hinglish). Short and punchy. No emojis in title.
```

---

## STEP 6 — SAVE OUTPUT

Save complete output to:
`d:/oldCOMPUTER/Videos/Scripts/Gappu/[StoryName]_PROMPTS.md`

File contains:
- Viral analysis header
- Similar ideas list
- Block 1 — full scene pack (paste-ready for Builder tab)
- Block 2 — locks pack (paste-ready for Locks tab)
- Caption pack + title options

Also copy to:
`d:/oldCOMPUTER/Videos/AIRelatedCode/transform-video-last-output.md`

---

## ALSO SUPPORTS — Object Talk output

If user says "Object Talk" instead of Gappu:
- Follow all rules from `d:/oldCOMPUTER/Videos/Scripts/ObjectAi/CLAUDE_VEO_RULES.md`
- Generate full Veo JSON prompts instead of Gappu scene pack
- Save to `d:/oldCOMPUTER/Videos/Scripts/ObjectAi/[TopicName]_VEO_PROMPTS.json`

---

## INPUT METHODS SUPPORTED

| Method | How |
|--------|-----|
| Local video path | Claude indexes via TwelveLabs |
| TwelveLabs video ID | Claude analyses directly |
| Pasted Gemini analysis | Skip TwelveLabs, Claude transforms directly |
| Pasted ChatGPT analysis | Skip TwelveLabs, Claude transforms directly |
| Plain text description | Claude fills all fields |

---

## QUICK REFERENCE

| Thing | Where |
|-------|-------|
| Gappu tools folder | `d:/oldCOMPUTER/Videos/Scripts/Gappu/` |
| Master prompt | `Gappu_Master_Prompt_v7.md` |
| Prompt builder | `gappu-prompt-tool.html` |
| Viral builder | `GappuViralPromptBuilder.html` |
| Object Talk tools | `d:/oldCOMPUTER/Videos/Scripts/ObjectAi/` |
| Image tool | Kie AI — Nanobanana 2 — 2K — 9:16 |
| Video tool | Kling AI — Seedance 2.0 — 9:16 |
| Total video length | Under 60 seconds — Claude decides clip durations |

---

## PIPELINE REMINDER

```
This skill → Block 1 → paste into GappuViralPromptBuilder.html Builder tab → ⚡ Create Scene Rows
           → Block 2 → paste into Locks tab → ⚡ Load All Locks
           → ↻ Regen All → copy prompts → Kie AI (images) → Kling AI (videos)
```
