# Pipeline Constants — Cached Reference

**Loaded once per session** (~200 tokens) → referenced by all pipelines

---

## Design Matrices (All Channels)

### Gappu (Emotion-Driven)
```
Wonder→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Pastel_Pink|Blob 0.6, sparkle dots
Confusion→Brutalist_Box|SpaceGrotesk+DMMono+NothingYouCouldDo|Dark_Tech|Box shadow 8px, gradient 75%
Joy→Neon_Marquee|BigShoulders+InstrumentSans+NothingYouCouldDo|Sunset_Orange|Neon border, ±3deg
```

### Bhakti (Devanagari, Mood-Driven)
```
Major Deity→Centered_Arch|Hind-Bold+Hind-Regular+NothingYouCouldDo|Luxury_Gold|Rim-light 28px
Shiva/Ascetic→Brutalist_Box|Hind-Bold+Hind-Regular+NothingYouCouldDo|Dark_Tech|Ash texture, inset 12px
Festival→Polaroid_Scrapbook|Hind-Bold+Hind-Regular+InstrumentSerif-Italic|Retro_Mustard|Confetti CSS
Shloka→Minimal_Border|Hind-Bold+Hind-Regular+NothingYouCouldDo|Minimal_Cream|Text-box 100px
Temple→Editorial_Split|Hind-Bold+Hind-Regular+IBMPlexSerif-Italic|Earthy_Green|Arch SVG
Nature→Soft_Blob|Hind-Bold+Hind-Regular+Cormorant-Italic|Earthy_Green|Blob radius 40px
```

### ObjectAi (Topic-Driven, English Only — NEVER Hind)
```
Anatomy→Professional_Sidebar|IBMPlexSerif+InstrumentSans+NothingYouCouldDo|Ocean_Blue|Sidebar 35%
Physics→Cyber_Terminal|SpaceGrotesk+DMMono+NothingYouCouldDo|Dark_Tech|Scanlines 5%, glow
Food→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Sunset_Orange|Blob radius 30px
Household→Floating_UI_Card|WorkSans+JetBrainsMono+NothingYouCouldDo|Minimal_Cream|Card transparent
Space→Dark_Tech-bg|Gloock+SpaceMono+NothingYouCouldDo|Neon_Cyber|Starfield 20 dots
Nature→Earthy_Green-bg|Cormorant+Jost+NothingYouCouldDo|Earthy_Green|Leaf CSS 2-3
```

---

## Typography Locks

| Channel | Headline | Body | Script Number | Kicker |
|---------|----------|------|---------------|--------|
| Gappu | YoungSerif/SpaceGrotesk/BigShoulders | WorkSans/InstrumentSans/DMMono | NothingYouCouldDo 180px | CrimsonPro-Italic/Lora-Italic |
| Bhakti | Hind-Bold 72px | Hind-Regular 34px | NothingYouCouldDo 180px (Latin) | CrimsonPro-Italic/Lora-Italic |
| ObjectAi | IBMPlexSerif/SpaceGrotesk/Gloock | InstrumentSans/DMMono/JetBrainsMono | NothingYouCouldDo 180px | CrimsonPro-Italic/Lora-Italic |

---

## Palette Hex Values

| Palette | BG | Text | Accent |
|---------|----|----|--------|
| Luxury_Gold | #FFFBF0 | #2D2D2D | #D4AF37 |
| Sunset_Orange | #FFF5F0 | #2D2D2D | #E65100 |
| Dark_Tech | #0D0D1A | #FFFFFF | #00FFFF |
| Minimal_Cream | #FAF9F6 | #2D2D2D | #8B7355 |
| Earthy_Green | #F5F5F0 | #2D2D2D | #556B2F |
| Ocean_Blue | #F0F4FF | #2D2D2D | #0066CC |
| Neon_Cyber | #0D0D1A | #FFFFFF | #00FF00 |
| Pastel_Pink | #FCE4EC | #2D2D2D | #F48FB1 |
| Retro_Mustard | #FFF8E6 | #2D2D2D | #E1AD01 |

---

## DNA Locks (NEVER Randomize)

**All Channels:**
- Single hero image across ALL content slides
- Edge-only border frame (inset 8px, never crosses characters)
- Script number bottom-left, calligraphic (NothingYouCouldDo always)

**Gappu:**
- Pixar 3D monkey, sealed mouths, face flush with material

**Bhakti:**
- Devanagari fonts only (Hind family) for Hindi/Sanskrit
- Warm color temperature (even Dark_Tech softened)
- CHARACTER_REFERENCE.md for deity descriptions

**ObjectAi:**
- SEALED mouths (no open, ever)
- Face geometry locked flush with material (no balloon heads)
- NEVER use Hind fonts (English content only)

---

## VEO Constants (ObjectTalk)

```
MW = 13 (max words per 3s beat)
LM = 3s (min per dialogue turn)
WPS target = 3–4 (Hindi conversational)

Beat 1 (00:00–00:02): Silent hook, all SEALED
Beat 2 (00:02–00:05): Speaker 1
Beat 3 (00:05–00:08): Speaker 2 / silent payoff

No hyphens in dialogue — ever
Repeat object_type 5+ times in final_compact_prompt_for_veo
```

---

## Suno V5.5 Constants (Bhakti Music)

```
Style field: max 1,000 chars, 8–15 tags, first tag = dominant genre
Lyrics field: max 3,000 chars
BPM syntax: BPM 75 (not "75 BPM")
Vedic/Mantra: MUST include "monotone" in style field

IAST Diacritics: ā ī ū ṛ ṝ ḷ ṃ ḥ ś ṣ ṭ ḍ ṇ ñ ṅ
```

---

## Viral Strategy Constants (ObjectTalk)

```
Hashtags: 3–5 ONLY — NEVER #reels #viral #explore #trending
IG first 125 chars: hook + keyword (visible before "more")
FB first 100 chars: hook before "more"
FB seed comment: User posts within 5 min

Best post time (IST): Tue–Thu 7:30–9:00 PM | 7:00–8:30 AM
Avoid: Mon morning, Fri/Sat night
```

---

## Selectors Reference

**See:** `reference-playwright-selectors.md` for:
- Google Flow selectors (Nano Banana 2)
- Higgsfield selectors (Nano Banana Pro + Kling V3)
- Download methods (GCS URL extraction)
