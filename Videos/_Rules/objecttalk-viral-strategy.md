# Rule: ObjectTalk Viral Strategy
**Activate:** "activate viral strategy" | **Input:** VEO JSON → **Output:** IG + FB caption strategy

**Channel:** Object Talk AI | **Format:** 8s Pixar 3D, Hindi dialogue | **Niche:** Ayurveda + Health + Funny | **Audience:** Hindi Indians 18–45 | **Creator:** Germany (use IST)

---

## JSON Extraction

| Field | Source |
|-------|--------|
| Hero | `characters[].name` + `object_type` |
| Villain | `title` |
| Dialogue | `beats[].dialogue.line` |
| Health fact | `content_type` + `_rules.custom` + `environment.setting` |
| Tone | `style` + `_rules.tone` |
| Keywords | `keywords[]` |
| Visuals | `beats[].visuals` |

---

## Platform Rules

**Instagram:**
- Hashtags: 3–5 niche only — NEVER #reels #viral #explore #trending (suppress reach)
- First 125 chars: hook + primary keyword (visible before "more")
- Hook: 2s landing, works muted (85% Indian mobile muted)
- Ranking: Watch-through → Shares (DMs) → Saves → Comments → Likes
- Length: 100–150 words, Hinglish

**Facebook:**
- Hashtags: 3–5 (slightly broader)
- First 100 chars: hook before "more"
- Ranking: Watch time → Shares → Comments → Reactions
- Seed comment: User posts within 5 min (drives early velocity)
- Family-sharing nudge: "घर के बड़ों को दिखाएं" energy
- Tone: Warmer storytelling, older audience (25–50)

**Posting Time (IST):**
- Best: Tue–Thu 7:30–9:00 PM (post-dinner save+share) | 7:00–8:30 AM (morning scroll)
- Avoid: Mon morning, Fri/Sat night

**Tone Guide:**
- Funny Swag: Punchy, "ओए!" energy | Heroic: Powerful verbs | Dramatic: Suspense + line breaks
- Horror: Shock → reveal + ellipsis | Emotional: Warm, family invoke "माँ सही कहती थीं..."

---

## Output Format

### INSTAGRAM
**Hook** (<125 chars, keyword line 1, works muted)

**Caption** (100–150 words, Hinglish): Hook → Health fact → "घर में होता है" angle → CTA question

**5 Hashtags:** 2 Hindi (#लहसुनकेफायदे) + 2 English (#CholesterolControl) + 1 channel (#ObjectTalkAI)

**Thumbnail:** 3–6 bold words (Hindi/Hinglish)

**Post Time:** IST day+time + reason

---

### FACEBOOK
**Caption** (150–200 words, warmer): Hook (100 chars) → Health fact + warmth → Family nudge → CTA

**5 Hashtags:** Broader mix Hindi+English

**Seed Comment:** 2–3 sentences (user posts within 5 min)

---

### DISCOVERY METADATA
| Primary keyword | Secondary (4) | Emotion tag | Share trigger | Algorithm category |
|-----------------|---------------|-------------|---------------|-------------------|

---

## Hard Rules
- No questions before output — just produce
- Max 5 hashtags per platform
- NO broad hashtags (#reels #viral #explore #trending #funny)
- IG ≠ FB copy (different tone/length)
- Seed comment mandatory for FB
- Activate only for JSON input
