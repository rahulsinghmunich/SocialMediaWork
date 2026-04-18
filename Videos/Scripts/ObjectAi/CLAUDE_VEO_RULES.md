# Claude VEO Prompt Generation Rules
**Based on:** veo-pacer-v9-fixed.html (V10.1) | **Model:** Veo 3.1 Fast

---

## CORE CONSTANTS

```
MW = 13 (max words per 3s beat) | LM = 3s (min per dialogue turn) | WPS target = 3-4 (Hindi conversational)
Beat 1 = 00:00-00:02 (silent hook, all SEALED) | Beat 2 = 00:02-00:05 (Speaker 1) | Beat 3 = 00:05-00:08 (Speaker 2/mic drop)
```

---

## MOTION FIELD PARSING (MANDATORY)

**Motion field = authoritative source for beat visuals. Never invent.**

### Parse Rules
1. Split by `Beat N (MM:SS-MM:SS):` sections
2. Copy each beat's visuals verbatim into `beats[N].visuals`
3. Extract camera note → `global_motion_rules.camera_rule`
4. Extract props/effects (clouds, blasts, sparkles) → `environment.foreground_props` + `source_image.allowed_animation_only` + each beat's `foreground_content`
5. **DO NOT** add intentional props to `negative_prompt` — they are wanted scene elements

### Example
```
Motion:
Beat 1: Green Tea Leaf snaps into striking pose, bad breath cloud shrinks back + mouths SEALED.
Beat 2: punches forward, blue energy blast from hands + Speaker 1 mouth OPENS.
Beat 3: calm power stance, bad breath cloud shatters/vanishes + mouth SEALED. Camera slow zoom in. Then settles.
```
→ `camera_rule`: "Static camera with slow push in on Beat 3, then settles"
→ `foreground_props`: "Bad breath cloud — present Beat 1, shrinks, shatters/vanishes by Beat 3"
→ `beats[0].visuals`: "Green Tea Leaf snaps into striking pose. Bad breath cloud shrinks back. Mouth SEALED."

---

## IMAGE-DERIVED FIELDS (FILL AFTER READING GENERATED IMAGE)

| Field | Source |
|-------|--------|
| `object_type` | What object IS the character? |
| `description` | Pixar 3D visual — shape, color, texture, material, size |
| `face` | How face formed IN material |
| `face_geometry_lock` | How face sits flush (no balloon/protrude) |
| `location_lock` | Exact screen position |
| `environment.setting/lighting/atmosphere` | From image |
| `source_image.scene_description` | Describe Frame 1 exactly |

**Add scene-specific negatives when image provided:**
- Tooth in scene → `"no tooth texture change without action sync"`
- Mist in scene → `"no mist removal"`
- Character holds prop → `"no [prop] disappearing between beats"`

---

## 5-ELEMENT CINEMATIC PROMPT FORMULA

For `final_compact_prompt_for_veo`:

```
[Cinematography] + [Subject with material specificity] + [Action FROM MOTION] + [Context/Environment] + [Style & Ambiance]
```

### Element 1: Cinematography
- **STATIC/LOCKED** camera always (our Object Talk scenes)
- Slow zoom allowed ONLY on Beat 3 payoff: `slow push in` (one movement)
- NEVER stack: "dolly while panning", "orbit and zoom"

### Element 2: Subject — MATERIAL SPECIFICITY
- Not "clove" → "dark brown dried clove with wrinkled bark-like texture, woody aromatic surface"
- Repeat `object_type` 5+ times in compact prompt — never say "character"

### Element 3: Action — FROM MOTION FIELD
- Beat 1: power pose, SEALED mouth
- Beat 2: physical action WHILE speaking + environment reacts
- Beat 3: victory/payoff + environment climax, SEALED mouth

### Element 4: Context — SPECIFIC ENVIRONMENT
- Not "dark place" → "dark organic cavern, ribbed walls of dental tissue, amber bioluminescent mist"
- Atmospheric elements: `mist`, `god rays`, `dust motes`, `bokeh`, `caustic light`, `bioluminescent glow`, `rim light`

### Element 5: Style & Ambiance
- Pixar 3D animated (always)
- Color direction per scene: Clove→amber-orange/dark crushed/warm rim | Baking Soda→bright clinical white/pink gum | Green Tea→vibrant green/fresh natural
- Cinematic grade: `high contrast`, `volumetric light`, `specular highlights on [material]`

---

## SCENARIO 1 — MULTI-SPEAKER, 8s (MOST COMMON)

**Input:** 2 characters + image

### Beat Structure
```
Beat 1 (00:00-00:02): silent_hook — all SEALED
Beat 2 (00:02-00:05): Speaker 1 talks, Speaker 2 SEALED
Beat 3 (00:05-00:08): Speaker 2 talks, Speaker 1 SEALED
```

### Character Positions
```
First character (index 0) → RIGHT | Second character (index 1) → LEFT | Third+ → CENTER
```

### Mouth Animation
```
Speaker 1: active_beats=[2], sealed_beats=[1,3]
Speaker 2: active_beats=[3], sealed_beats=[1,2]
```

### Density Check (COMPUTE, never [FILL])
```json
"density_check": {
  "total_words": 20, "total_spoken_seconds": 6, "total_silent_seconds": 2,
  "natural_speech_pace": "Hindi conversational — 3 to 4 WPS",
  "status": "SAFE — 3.3 WPS"
}
```

### Fallback Dialogue
```json
"fallback_dialogue": {
  "use_if_rushed": {
    "beat2_shorter": "trimmed Speaker 1 line",
    "beat3_shorter": "trimmed Speaker 2 line"
  }
}
```

---

## SCENARIO 2 — SINGLE SPEAKER, 8s

**Input:** 1 character only

### Beat Structure
```
Beat 1 (00:00-00:02): silent_hook — mouth SEALED
Beat 2 (00:02-00:05): speaker talks
Beat 3 (00:05-00:08): silent_payoff — mouth SEALED (visual climax)
```

### Character Position + Mouth
```
Only character → CENTER
active_beats: [2] | sealed_beats: [1, 3]
```

### Fallback Dialogue
```json
"fallback_dialogue": {
  "use_if_rushed": {
    "beat2_shorter": "trimmed dialogue line"
  }
}
```

---

## SCENARIO 3 — MULTI-SPEAKER, 16s (2 SEGMENTS)

**Input:** 2+ turns across 16 seconds

### Beat Structure
```
Segment 1: Beat 1 (00:00-00:02) silent | Beat 2 (00:02-00:05) Speaker A | Beat 3 (00:05-00:08) Speaker B
Segment 2: Beat 4 (00:08-00:10) silent | Beat 5 (00:10-00:13) Speaker A/C | Beat 6 (00:13-00:16) Speaker B/D
```

### Formula
```
segCount = ceil(16/8) = 2 | totalDialogueTime = 16 - (2×2) = 12s | timePerTurn = max(3, floor(12/totalTurns))
```

### Fallback Dialogue
```json
"fallback_dialogue": {
  "use_if_rushed": {
    "beat2_shorter": "...", "beat3_shorter": "...",
    "beat5_shorter": "...", "beat6_shorter": "..."
  }
}
```

---

## SCENARIO 4 — MULTI-SPEAKER, 24s (3 SEGMENTS)

Same logic as 16s but 3 segments:
```
segCount = 3 | totalDialogueTime = 24 - 6 = 18s | timePerTurn = max(3, floor(18/totalTurns))
```

### Fallback Dialogue
```json
"fallback_dialogue": {
  "use_if_rushed": {
    "beat2_shorter": "...", "beat3_shorter": "...",
    "beat5_shorter": "...", "beat6_shorter": "...",
    "beat8_shorter": "...", "beat9_shorter": "..."
  }
}
```

---

## SCENARIO 5 — RAW IMPORT (FREE-FORM TEXT)

**Input:** `Character: "Hindi dialogue"` pattern

### Parsing Rules
- Match: `Name: "Hindi line"` or `Name: "Hindi line"`
- Skip names matching: image prompt / motion / dialogue / scene / shot / showing / camera / lighting / hindi
- Skip names >20 chars or lines <3 chars
- If no named turns → extract any Hindi in quotes as "Speaker"

### Auto-detect Content Type
- ayurved/health/herb/tulsi/neem/ginger/haldi → "ayurveda"
- science/physics/magnet → "science"
- funny/comedy/joke → "comedy"
- Otherwise → "custom"

### When Motion Missing → GENERATE IT
- Beat 1: power pose matching personality + environment reaction
- Beat 2: physical action while speaking + environment reacts to dialogue
- Beat 3: victory/payoff pose + environment climax + "then settles"
- Camera: static, slow push in on Beat 3 if dramatic

---

## SCENARIO 6 — NO IMAGE (TEXT_TO_VIDEO MODE)

**When:** No image attached

### Differences
- `generation_mode`: "TEXT_TO_VIDEO"
- `source_image.generation_mode`: "TEXT_TO_VIDEO_WITH_FRAME1_PROMPT"
- `source_image.file_reference`: "[generate image first]"
- `source_image.first_frame_instruction`: null
- `negative_prompt`: omit "do not regenerate the image" / "no scene redesign"
- `final_compact_prompt_for_veo`: starts with "Generate 9:16 Pixar 3D video..."
- All image-derived fields → note "image required for accuracy"

---

## NEGATIVE PROMPT (BASELINE)

**Always include:**
```
"no human figures — all characters are animated objects"
"no man, no person, no human body"
"characters are objects NOT people"
"no new characters" | "no additional characters"
"no subtitles" | "no camera cuts" | "no camera angle change" | "no character repositioning"
"no exaggerated cartoon motion" | "no fast speech"
"no balloon face or inflated face geometry"
"no separate 3D head object on any character"
```

**If image provided, also add:**
```
"do not regenerate the image" | "no scene redesign"
```

**Per character (by name):**
```
"no duplicate [Name] anywhere in frame"
"no mini/small version of [Name] spawning"
```

**For multi-speaker (not first character):**
```
"no [Name] appearing near [names[0]]'s position"
```

**Only for characters who NEVER speak:**
```
"no mouth movement for [Name] — mouth stays sealed entire video"
```

**Scene-specific (from image):**
```
"no tooth texture change without action sync" (if tooth)
"no mist removal" (if mist)
"no [prop] disappearing between beats" (if prop)
```

**CRITICAL:** Do NOT add negatives for intentional Motion props (clouds, blasts, sparkles — these are WANTED).

### Auto-Validation
If `negative_prompt` contains "no mouth movement for X" but X has dialogue beats → **auto-remove** and note the fix.

---

## VALIDATION CHECKS (AUTO-RUN BEFORE OUTPUT)

1. Motion parsed? → `beats[].visuals` match Motion content (not generic)
2. If character has `active_beats="none"` but appears as `active_speaker` → ERROR
3. If `negative_prompt` contains "no mouth movement for X" but X has dialogue → ERROR (auto-remove)
4. If `active_speaker` in `sealed_characters` of same beat → ERROR
5. If `final_compact_prompt_for_veo` contains "character" instead of `object_type` → WARNING (replace)
6. If compact prompt has stacked camera movements → ERROR (use single)
7. If any dialogue line contains hyphen `—` or `-` → ERROR (replace with comma/full stop)
8. If `fallback_dialogue` keys not wrapped in `use_if_rushed` → ERROR (fix structure)
9. If Motion has props but `negative_prompt` blocks them → ERROR (remove contradictory negative)
10. `object_type` appears 5+ times in compact prompt? → WARNING if less

---

## DIALOGUE FORMATTING RULES

**NO HYPHENS in dialogue lines — ever.**

Veo reads dialogue text aloud including punctuation. Hyphens will be spoken as "dash" or cause unnatural pauses.

| Wrong | Right |
|-------|-------|
| `मैं हूँ लहसुन — देसी और तीखा` | `मैं हूँ लहसुन, देसी और तीखा` |
| `निगल ले मुझे — नसों में खून` | `निगल ले मुझे, नसों में खून` |

Applies to: `dialogue.line`, `fallback_dialogue`, `final_compact_prompt_for_veo` spoken lines.

---

## WPS LIMITS QUICK REF

| Words | Duration | WPS | Status |
|-------|----------|-----|--------|
| ≤9 | 3s | ≤3.0 | SAFE |
| 10-12 | 3s | 3.3-4.0 | SAFE |
| 13 | 3s | 4.33 | SAFE (limit) |
| 14 | 3s | 4.67 | DENSE — trim 1 word |
| 15+ | 3s | 5.0+ | WILL_TRUNCATE |

**Trimming:** remove filler words like "ना", "भाई", "अरे", "तो", "ही"

---

## JSON FIELD ORDER (SCHEMA REFERENCE)

Full schema in veo-pacer-v9-fixed.html. Key structure:

```
_instructions → title → duration_seconds → aspect_ratio → style → content_type → generation_mode → model_target
_speaker_mode → _speaker_count → _speaker_order → _first_speaker → _turn_rule
_rules { tone, mouth_animation, dialogue_delivery, pace_note, max_words_per_8s, custom }
source_image { mode, generation_mode, file_reference, first_frame_instruction, image_prompt, scene_description, what_must_not_change, allowed_animation_only }
scene_integrity { character_count, character_positions, position_lock, foreground_fill_rule, narrative_completion_warning }
global_motion_rules { camera_rule, character_rule, animation_rule, style_rule }
characters [{ name, object_type, position, location_lock, description, face, face_geometry_lock, voice{language,tone,pace}, mouth_animation{active_beats,sealed_beats,style}, animation{} }]
environment { setting, lighting, atmosphere, background_elements, foreground_props }
beats [{ beat, time, type, active_speaker, sealed_characters, speaker_activation_rule, visuals, foreground_content, character_positions_this_beat, dialogue{speaker_name,line,delivery,word_count,duration_seconds,pace_note,action_sync}, audio{music,ambient,sfx[]} }]
audio { dialogue_priority, subtitles, soundtrack_level, overall_feel }
veo_3_1_optimization { primary_instruction, motion_budget, mouth_animation_model, priority_order[], performance_note }
negative_prompt []
fallback_dialogue { use_if_rushed { beat2_shorter, beat3_shorter, ... } }
final_compact_prompt_for_veo
density_check { total_words, total_spoken_seconds, total_silent_seconds, natural_speech_pace, status }
keywords []
original_dialogue_turns []
```

---

## COMPACT PROMPT TEMPLATE

```
SCENE INTEGRITY LOCK: [N] [object_type]s only — [Name1] [object_type] anchored at [position], [Name2] [object_type] anchored at [position]. No repositioning, no duplication, no new characters.

[IMAGE_TO_VIDEO: "Animate uploaded image into"] / [TEXT_TO_VIDEO: "Generate"] [X]s cinematic Pixar 3D video. Static camera. [Name1] [object_type] [material detail] on [position]. [Name2] [object_type] [material detail] on [position]. [Motion-field environment props present from start].

Beat 1 (00:00-00:02): [Name1/Name2] [object_type] [MOTION Beat 1 action]. [MOTION environment reaction]. Eyes fierce, brows furrowed, mouth strictly SEALED. Silent hook.

Beat 2 (00:02-00:05): [Speaker] [object_type] [MOTION Beat 2 action while speaking]. [MOTION environment reaction]. Mouth opens naturally: "[Hindi line]". [Other character] [object_type] mouth SEALED [if multi-speaker].

Beat 3 (00:05-00:08): [Name1/Name2] [object_type] [MOTION Beat 3 action]. [MOTION environment climax]. Mouth SEALED, then settles. FOREGROUND LOCK: [what fills foreground].

Mouth animation is LOOSE and NATURAL — not strict phoneme sync. Veo speaks the Hindi line and animates mouth with natural talking rhythm. (Language: Hindi)(no subtitles)
```

**Rules:**
- Beat descriptions FROM Motion — never generic
- Never use "character" — always `object_type`
- Repeat `object_type` 5+ times minimum
- Anchor positions in EVERY beat
- Static camera ALWAYS stated
- Include material specificity + environment reaction per beat
- Final beat has FOREGROUND LOCK statement
- End with mouth animation disclaimer (exact wording)

---

## MULTI-SCENE SCRIPTS HANDLING

When user pastes script with "Scene 1:", "Scene 2:":

1. Split on `Scene N:` pattern
2. Extract per scene: Title, Image Prompt, **Motion** (MANDATORY), Character dialogues
3. Match images to scenes by order (image 1 = Scene 1)
4. **Read each image** and fill image-derived fields from actual image
5. Generate one complete JSON per scene — `beats[].visuals` FROM Motion
6. **Save ALL scenes into ONE JSON file** with wrapper:
   ```json
   { "scenes": [{ "scene": 1, ... }, { "scene": 2, ... }] }
   ```
   Save as: `[TopicName]_VEO_PROMPTS.json`
7. Also save summary `[TopicName]_VEO_PROMPTS.md` with all compact prompts (human-readable reference)

**SUBMISSION TO FLOW:** Read JSON file → paste individual scene object (not outer `scenes[]` wrapper) into Flow prompt box. Read from file every time — never from memory.

---

## OBJECT TALK PIPELINE FLOW

**PATH A — Scene pack exists (Gemini/user/Claude output):**
User pastes scene pack with Image Prompt + Motion + Dialogue → Claude parses → JSON generation.

**PATH B — Claude generates scene pack from topic/raw script:**
User gives topic/raw script without Motion → Claude FIRST outputs full scene pack (Title, Image Prompt, Motion all 3 beats, Dialogue) → User confirms/edits → Claude generates Veo JSONs using its own Motion as authoritative.

**In BOTH paths:** Motion field = single source of truth for beat visuals. Never invent different visuals.

### Pipeline Steps
```
STEP 1: Scene pack exists (or Claude generates it first)
STEP 2: Claude generates full JSON per scene
        → Parses Motion → copies verbatim into beats[].visuals
        → Extracts props → adds to environment.foreground_props
        → Uses Motion camera note → global_motion_rules.camera_rule
        → [FILL] for image-derived fields
        → generation_mode = TEXT_TO_VIDEO (placeholder)
STEP 3: Claude validates all checks
STEP 4: Claude writes final_compact_prompt_for_veo (5-Element Formula)
STEP 5: Save [Topic]_VEO_PROMPTS.json + [Topic]_VEO_PROMPTS.md
STEP 6: User generates keyframe image in Google Flow (Image tab → Nano Banana 2 → 9:16 → x1 → image_prompt → Generate)
STEP 7: *** Claude reads the generated image ***
        (Playwright screenshot in Flow OR user shares image)
        Claude reads image → fills ALL image-derived fields from what is visible:
        object_type, description, face, face_geometry_lock, location_lock, environment.*,
        source_image.scene_description, source_image.first_frame_instruction
        Claude switches generation_mode to "FIXED_FIRST_FRAME"
        Claude outputs updated scene JSON → saves back to [TopicName]_VEO_PROMPTS.json
STEP 8: Attach image as Start frame in Flow → paste FULL UPDATED SCENE JSON → Create
```

**MANDATORY:** Claude must never submit to Flow without having read the actual generated image. If image not yet shared/screenshotted → ask for it first.

---

## QUICK REFERENCE — GOOGLE FLOW SELECTORS

```
URL:         https://labs.google/fx/tools/flow
New project: btns.find(b => b.textContent.includes('New project')).click()
Image tab:   tab with text 'Image'
Video tab:   tab with text 'Video'
Frames mode: tab with text 'Frames'
9:16 ratio:  tab with text '9:16'
x1 quantity: tab with text 'x1'
Prompt box:  textbox[placeholder*="What do you want to create?"]
Generate:    btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()
File input:  document.querySelector('input[type="file"]').click()
Video src:   document.querySelector('video').src
```

**Download fallback:**
```js
document.querySelector('video').src
// → navigate to that URL → curl -L --ssl-no-revoke "[GCS_URL]" -o "path/to/scene_NN.mp4"
```
