# Song Analysis & Lyrics Format
**Project:** Tattava Music
**Purpose:** Drop a YouTube link or audio file → Gemini/Claude populates this template → use output directly for Suno prompt building

---

## HOW TO USE

1. Drop a YouTube link or audio file
2. Gemini analyzes and fills every field below
3. Use the Technical Analysis Report → build Suno style field
4. Use the Lyrics & Arrangement section → paste directly into Suno lyrics field

---

## TEMPLATE

---

### 📺 Video Details

| Field | Value |
|---|---|
| **Title** | [Song Name] |
| **Channel** | [Channel Name] |
| **Duration** | [e.g., 35:00] |
| **YouTube URL** | [link] |

---

### 🎶 Lyrics & Arrangement
*(Using meditative/rhythmic structure with instrumentation cues)*

```
[Intro]
(Description of starting sounds — e.g., tanpura drone, soft harmonium swells, silence)
(Opening mantras or vocalizations)

[Verse]
(Vocal style: monotone / melodic / chanting)
(Lyrics in IAST or Devanagari as requested)

[Chorus]
(Musical shift: harmonies, percussion entry, dholak/tabla enters)
(Main hook or repetitive mantra)

[Bridge]
(Musical peak: tempo build, cymbal rise, intensity increase)
(Bridge lyrics / mantras)

[Outro]
(Fading elements, trailing vocals, final drone)
(Closing sounds — e.g., tanpura remains, whispered)
```

**IAST Diacritics Reference:** ā ī ū ṛ ṝ ḷ ṃ ḥ ś ṣ ṭ ḍ ṇ ñ ṅ

---

### 📊 Technical Analysis Report

| Metric | Value | Details |
|---|---|---|
| **Key** | [e.g., D Major] | Tonal center of the track |
| **Alt Key (Camelot)** | [e.g., 10B] | Camelot Wheel notation for harmonic mixing |
| **BPM** | [e.g., 144] | Beats Per Minute — tempo |
| **Energy** | [Low / Med / High] | Overall intensity and power |
| **Danceability** | [0–100%] | How easy to follow the rhythm physically |
| **Happiness / Valence** | [0–100%] | Musical emotional brightness |

---

### 🧘 Mood & Style Summary

| Field | Value |
|---|---|
| **Musical Style** | [e.g., Indian Devotional, Kirtan, Ambient, Bhajan] |
| **Genre Tags** | [e.g., hindi bhakti, rama dhun, devotional chanting] |
| **Instrumentation** | [e.g., Harmonium, Tabla, Manjira, Tanpura Drone, Dholak] |
| **Vocal Type** | [e.g., Single Male — Devotional, Group — Mixed Congregation] |
| **Vocal Style** | [e.g., Monotone Chant, Melodic Classical, Repetitive Mantra Loop] |
| **Vibe / Mood** | [e.g., Grounding, Triumphant, Deep Focus, Inner Stillness] |
| **Production Quality** | [e.g., Raw Acoustic, Studio Polished, Temple Ambiance] |
| **Best Use** | [e.g., Meditation background, Yoga, Morning puja, YouTube loop] |

---

### 🎛 Suno V5.5 Style Field Output
*(Auto-generated from analysis above — paste directly into Suno)*

```
[genre tags], BPM [number], [key], [instruments], [vocal type],
[vocal style tags], [mood tags], [production], [language tag],
[emotional texture], no [exclusions]
```

**Character count:** [X] / 1000

---

### 📝 Notes
*(Any extra observations — copyright notes, loop structure, extension tips)*

---

## FILLED EXAMPLE — Shri Ram Jai Ram (Reference Recording)

### 📺 Video Details

| Field | Value |
|---|---|
| **Title** | Vijay Mantra for Success — Shree Ram Jai Ram Sita Ram Chanting (35 Mins) |
| **Channel** | Shree Dhun Bhakti |
| **Duration** | 35:00 |
| **YouTube URL** | https://www.youtube.com/watch?v=xURhMzeLGhc |

### 📊 Technical Analysis Report

| Metric | Value | Details |
|---|---|---|
| **Key** | D Major | Tonal center |
| **Alt Key (Camelot)** | 10B | Harmonic mixing reference |
| **BPM** | 144 | Mid-tempo feel despite high BPM — chant phrase spans 2–4 beats |
| **Energy** | Low–Medium | Steady, grounding, not intense |
| **Danceability** | 30% | Rhythmic but not dance-oriented |
| **Happiness / Valence** | 60% | Peaceful, positive, devotional |

### 🧘 Mood & Style Summary

| Field | Value |
|---|---|
| **Musical Style** | Indian Devotional — Ram Dhun / Kirtan |
| **Genre Tags** | hindi bhakti kirtan, rama dhun, devotional chanting |
| **Instrumentation** | Harmonium, Manjira Cymbals, Soft Dholak, Tanpura Drone |
| **Vocal Type** | Single Male — Devotional Bhajan Singer |
| **Vocal Style** | Monotone Hypnotic Chant, Repetitive Mantra Loop |
| **Vibe / Mood** | Meditative, Tranquil, Grounding, Deep Focus, Inner Stillness |
| **Production Quality** | Temple Ambiance, High-Fidelity |
| **Best Use** | 35-min YouTube meditation loop, yoga background, morning puja |

### 🎛 Suno V5.5 Style Field Output

```
hindi bhakti kirtan, rama dhun, devotional chanting, BPM 144, D major,
harmonium melody, manjira cymbals, soft dholak, tanpura drone,
single male devotional vocals, singing in Hindi, Devanagari lyrics,
monotone hypnotic chant, repetitive mantra loop, cyclical rhythm,
meditative, tranquil, grounding, deep focus, inner stillness,
deep reverence, ancient and timeless, sacred ambient, temple atmosphere,
high-fidelity, no electric guitar, no autotune, no western drums,
no synthesizer, no bass guitar, no pop production
```

**Character count: 568 / 1000**
