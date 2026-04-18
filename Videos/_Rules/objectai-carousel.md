# Rule: ObjectAi Carousel
**Channel:** objectwithbrainsai | **IG:** @objectwithbrainsai | **Logo:** `GappuMonkeyShorts/PICTURE/8e8017a2-5ef3-4613-9b72-610bf6539948.png`
**Activate:** "activate objectai carousel" | **Execute:** `ObjectAi/pipeline/carousel/CLAUDE.md`

**Flow:** Topic → Content points (4–8 + CTA) → Hero image (Nano Banana 2, 4:5, Pixar 3D) → Design Matrix → Manifesto → generate_slides.py → Caption

---

## Design Matrix (3-line format)

```
Anatomy/Biology→Professional_Sidebar|IBMPlexSerif-Bold+InstrumentSans+NothingYouCouldDo|Ocean_Blue|Sidebar 35%, ACCENT ring behind character
Physics/Chemistry→Cyber_Terminal|SpaceGrotesk-Bold+DMMono+NothingYouCouldDo|Dark_Tech|Scanlines 5%, border glow
Food/Nutrition→Soft_Blob|YoungSerif+WorkSans+NothingYouCouldDo|Sunset_Orange|Blob bg, radius 30px, tint 0.20
Household Science→Floating_UI_Card|WorkSans-Bold+JetBrainsMono+NothingYouCouldDo|Minimal_Cream|Card semi-transparent, shadow 20px
Space/Cosmic→Dark_Tech-bg|Gloock+SpaceMono+NothingYouCouldDo|Neon_Cyber|Starfield CSS (20 dots), gradient 80%
Environment/Nature→Earthy_Green-bg|Cormorant+Jost+NothingYouCouldDo|Earthy_Green|Leaf CSS (2–3 shapes), border 3px
```

**Typography (ENGLISH — NEVER Hind):** Headline IBMPlexSerif/SpaceGrotesk/YoungSerif/WorkSans/Gloock/Cormorant | Body InstrumentSans/DMMono/WorkSans/JetBrainsMono/SpaceMono/Jost | Script Number NothingYouCouldDo 180px | Kicker CrimsonPro-Italic/Lora-Italic 36px

**Palettes:** Ocean_Blue (#F0F4FF/#0066CC) | Dark_Tech (#0D0D1A/#00FFFF) | Sunset_Orange (#FFF5F0/#E65100) | Minimal_Cream (#FAF9F6/#8B7355) | Neon_Cyber (#0D0D1A/#00FF00) | Earthy_Green (#F5F5F0/#556B2F)

**Variation Triggers:** Gradient bottom-up → left-to-right (landscape) | Tint 0.28 → 0.15 (bright) / 0.40 (dramatic) | Headline weight 700 → 900 (bold) / 400 (gentle) | Brackets 22px → 14px (minimal) / 36px (bold)

**DNA Locks:** Single hero all slides | SEALED mouths (no open) | Face flush with material | Edge border (inset 8px) | Script number bottom-left | No Hind fonts (English content)

---

## Caption Formula

**Instagram:** Hook (<15 words) + Facts (3–5 bullets) + CTA "Follow @objectwithbrainsai" + #ObjectAi #[Topic] #ScienceFacts #AnimatedObjects #STEM

**Facebook:** Same without hashtags → "Follow objectwithbrainsai for more!"

---

## Failure Handling

| Failure | Action |
|---------|--------|
| IMAGE | Retry simplified prompt |
| SLIDE | Log, fallback PNG |
| Color contrast | Increase tint to 0.35 |
| Hero mismatch | Regenerate consistent character |

**Never pause for failures.** Log, skip, report.
