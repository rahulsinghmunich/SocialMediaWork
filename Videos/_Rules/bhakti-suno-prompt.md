# Rule: Bhakti Suno Prompt
**Activate:** "activate suno prompt" | **Output:** Suno V5.5 Style field + Lyrics (IAST) + Tips

**Flow:** Ask 4 question groups in order → Generate prompt (no HTML/API)

---

## Question Groups (ask in order, wait between groups)

### Group 1 — Core
1. **Deity/Theme:** Shiva | Vishnu | Krishna | Rama | Durga | Kali | Lakshmi | Saraswati | Ganesha | Hanuman | Navratri | Surya | Radha-Krishna | Sita-Ram | Murugan | General
2. **Genre:** Bhajan (65–85) | Kirtan (90–120) | Vedic Chant (40–60) | Sufi/Qawwali (80→160) | Cinematic Devotional (60–90) | Carnatic (50–100) | Hindustani Classical (40–120) | Lo-Fi Spiritual (65–80) | Temple Ambient (40–55) | Modern Devotional Pop (80–100) | Mantra Electronic (100–120) | Dhrupad (30–50) | Devotional Folk (70–95) | Aarti (80→120) | Sanskrit Stotra (55–75)
3. **Mantra/Stotra:** User types or "you decide"

### Group 2 — Mood & Voice
4. **Mood:** Meditative | Pure Bhakti | Powerful | Blissful | Longing | Triumphant | Ancient/Cosmic | Festive | Mystical | Surrender
5. **Voice:** Single Male (Pandit/Bhajan/Baritone) | Group Male (Priests) | Single Female (Classical/Devotional) | Group Female | Mixed | Child | Aged Male | Instrumental
6. **Vocal Style:** Monotone Chant | Melodic Classical | Folk/Natural | Call & Response | Repetitive Loop | Whispering | Powerful Belt | Sufi/Ecstatic | Spoken | Harmonized Choir

### Group 3 — Sound
7. **Instruments (2–4):** Harmonium | Tabla | Tanpura | Bansuri | Sitar | Mridangam | Dholak | Temple Bells | Veena | Manjira | Shankh | Sarangi | Sarod | Santoor | Shehnai | Dhol | Pakhawaj | Nagara | Nadaswaram | Orchestra | Choir | Electronic Pads | Ektara
8. **Production:** Raw Acoustic | Warm Analog | Temple Ambiance | Studio Polished | Cinematic Mix | Lo-Fi Tape | Outdoor/Ghats
9. **Structure:** Mantra Loop | Verse+Chorus | Full Song | Building Climax | Alap→Jor→Jhala | Instrumental
10. **Exclude:** User lists or skip

### Group 4 — Lyrics
11. **Lyrics:** A) User paste | B) Search & suggest (Claude picks 3 stotra options) | C) Generate original
12. **Emotional Texture:** (optional) Tearful Surrender | Deep Reverence | Divine Love | Building Intensity | Inner Stillness | Cosmic Awe | Joyful | Warrior Spirit | Longing | Grace | Ancient | Ecstatic Bliss
13. **Special Notes:** (optional)
14. **IAST Mode:** ON (default) | OFF (Devanagari)

---

## Output Format (after all answers collected)

### SUNO STYLE FIELD (max 1000 chars)
```
[genre], BPM [number], [instruments], [vocal type], [vocal style], [mood], [production], [language], [structure], [emotion], no [exclusions]
```

### LYRICS — IAST ROMANIZED
```
[Intro] [Verse] [Chorus] [Verse] [Outro]
```
(Use inline cues: `(whispered)` `(building intensity)` `(monotone chant)` `(ecstatic)`)

### CLAUDE'S TIPS
2–4 deity+genre specific tips + Suno V5.5 quirks

---

## Suno V5.5 Rules

**Limits:** Style 1000 chars | Lyrics 3000 chars | 8–15 tags | First tag = dominant genre

**Syntax:**
- BPM: `BPM 75` (not "75 BPM")
- Tempo change in lyrics: `[Tempo Change: 140 BPM]`
- Negatives at END: `no electric guitar, no autotune`
- Language: `singing in Hindi` | `Sanskrit pronunciation`
- Vedic/Mantra: MUST include `monotone`
- Sufi: `ecstatic devotional cry, building tempo`
- Cinematic: `cinematic orchestral, epic strings`

**Section Tags:** `[Intro]` `[Verse]` `[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Build-Up]` `[Outro]`

**Inline Cues:** `(whispered)` `(belted)` `(building intensity)` `(monotone chant)` `(ecstatic)` `(harmonized)`

**IAST Diacritics:** ā ī ū ṛ ṝ ḷ ṃ ḥ ś ṣ ṭ ḍ ṇ ñ ṅ

**Genre Defaults:**
| Genre | Instruments |
|-------|-------------|
| Bhajan | Harmonium, Tabla, Tanpura |
| Kirtan | Dholak, Manjira, Harmonium |
| Vedic Chant | Tanpura only |
| Cinematic | Orchestra, Temple Bells, Tabla |
| Lo-Fi | Electronic Pads, Bansuri, Tabla |
| Temple Ambient | Tanpura, Bells, Shankh |
| Aarti | Dholak, Bells, Manjira, Harmonium |
| Stotra | Tanpura, Harmonium |

---

## Hard Rules
- Ask groups in order — never all at once
- IAST copyright note for stotra/mantra
- Never output until ALL groups answered
- IAST mode ON = Roman diacritics, never Devanagari
- Style field ≤1000 chars
- Never reproduce copyrighted bhajan verbatim
