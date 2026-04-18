# Rule: ObjectAi Pipeline
**Activate:** "activate objectai pipeline" | **Execute:** `ObjectAi/pipeline/CLAUDE.md` + `Scripts/ObjectAi/CLAUDE_VEO_RULES.md`

**Flow:** Topic/script → Scene pack + Veo JSONs → Images (Flow Image tab) → Videos (Flow Video tab)

**Hard Rules:**
- Login check before Flow
- Motion field = authoritative for beat visuals (never invent)
- Image-derived fields filled after reading generated image
- DOM waits only — no screenshot polling
- Never pause for failures — log, skip, report
