# Rule: ObjectTalk VEO Prompt
**Activate:** "activate veo prompt" | **Input:** Script (+ optional images) → **Output:** VEO JSON

**Full Rules:** `Scripts/ObjectAi/CLAUDE_VEO_RULES.md`

---

## Quick Constants
- MW: 13 words/beat | LM: 3s min/turn | WPS: 3–4 (Hindi conversational)
- Beat 1 (00:00–00:02): Silent hook, all SEALED
- Beat 2 (00:02–00:05): Speaker 1
- Beat 3 (00:05–00:08): Speaker 2 / silent payoff
- No hyphens in dialogue — ever
- Repeat `object_type` 5+ times in `final_compact_prompt_for_veo`
- Save: `[TopicName]_VEO_PROMPTS.json` (all scenes in one file)

---

## Input Expected
- Script: Character names + Hindi dialogue
- Optional: Scene images (matched by order)
- Optional: Tone, duration (defaults: Funny Swag, 8s)
