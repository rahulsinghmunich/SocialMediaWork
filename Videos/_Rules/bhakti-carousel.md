# Rule: Bhakti Carousel
**Channel:** Sanatan Dharma | **IG:** @sanatandharmatheeternalpath | **Logo:** `Bhakti/branding/logo.jpg`
**Activate:** "activate bhakti carousel" | **Execute:** `BhaktiChannel/pipeline/carousel/CLAUDE.md`

**Flow:** Topic → Content points (4–8) → Hero image (Nano Banana 2, 4:5) → Design Matrix → Manifesto → generate_slides.py → Caption

---

## Design Matrix (3-line format)

```
Major Deity→Centered_Arch|Hind-Bold+Hind-Regular+NothingYouCouldDo|Luxury_Gold|Golden rim-light, brackets 28px
Shiva/Ascetic→Brutalist_Box|Hind-Bold+Hind-Regular+NothingYouCouldDo|Dark_Tech|Ash-particle texture, inset 12px
Festival/Ritual→Polaroid_Scrapbook|Hind-Bold+Hind-Regular+InstrumentSerif-Italic|Retro_Mustard|Confetti CSS, gradient 65%
Shloka/Verse→Minimal_Border|Hind-Bold+Hind-Regular+NothingYouCouldDo|Minimal_Cream|Text-box 100px, kicker 5px
Temple/Pilgrimage→Editorial_Split|Hind-Bold+Hind-Regular+IBMPlexSerif-Italic|Earthy_Green|Arch SVG top-center
Nature/Ayurveda→Soft_Blob|Hind-Bold+Hind-Regular+Cormorant-Italic|Earthy_Green|Blob bg, radius 40px, tint 0.18
```

**Typography (Devanagari):** Headline Hind-Bold 72px | Body Hind-Regular 34px | Script Number NothingYouCouldDo 180px (Latin) | Kicker CrimsonPro-Italic/Lora-Italic 36px

**Palettes:** Luxury_Gold (#FFFBF0/#D4AF37) | Sunset_Orange (#FFF5F0/#E65100) | Dark_Tech (#0D0D1A/#00FFFF) | Retro_Mustard (#FFF8E6/#E1AD01) | Minimal_Cream (#FAF9F6/#8B7355) | Earthy_Green (#F5F5F0/#556B2F)

**DNA Locks:** Single hero all slides | Devanagari only (Hind) | Edge border (inset 8px) | Warm color temp | CHARACTER_REFERENCE.md for deity descriptions

---

## Caption Formula

**Instagram:** Shloka/Hook + Teaching (2–3 lines) + Emojis 🙏🕉️🪔 + #SanatanDharma #Hinduism #[Deity] #VedicWisdom #Bhakti

**Facebook:** Same + longer explanation (4–6 lines)

---

## Failure Handling

| Failure | Action |
|---------|--------|
| IMAGE | Retry simplified prompt |
| SLIDE | Log, fallback PNG |
| Hindi rendering | Check unicode-range, Hind fonts |

**Never pause for failures.** Log, skip, report.
