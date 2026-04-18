# Metadata Generator

Unified YouTube / Instagram / Facebook metadata generator for all channels.

---

## How it works

1. You run the Python script with channel name + input (folder or file).
2. Script gathers all data (pipeline files OR input template) + channel rules + SEO/social skill rules.
3. Script produces **`CONTEXT_BRIEF.md`** — a single file with everything Claude needs.
4. You tell Claude in chat: *"Generate metadata from CONTEXT_BRIEF.md in [folder]"*.
5. Claude produces **`YOUTUBE.md`**, **`INSTAGRAM.md`**, **`FACEBOOK.md`** inside the folder.

**Why this split?** Python gathers data cheaply; Claude does the language/tone work.

---

## Channels supported

| Channel | Type | Platforms | Input |
|---|---|---|---|
| **gappu** | Pipeline folder | YouTube, Instagram, Facebook | `--folder` |
| **bhakti** | Pipeline folder | YouTube, Instagram, Facebook | `--folder` |
| **objectai** | Pipeline folder | Instagram, Facebook | `--folder` |
| **tattva** | Input file | YouTube, Instagram, Facebook | `--input` |
| **shodh** | Input file | YouTube, Instagram, Facebook | `--input` |

---

## Usage

### Pipeline channels (Gappu / Bhakti / ObjectAI)

Already generated your images/video for an episode? Run:

```bash
python generate_metadata.py --channel gappu --folder "D:\oldCOMPUTER\Videos\GappuMonkeyShorts\pipeline\2026-04-17_StoryName"
```

Script reads: `SESSION-RESUME.md`, image list, scene JSON, any prompt files.
Output: `CONTEXT_BRIEF.md` in that same folder.

---

### Input-file channels (Tattva / Shodh Chakra)

1. Copy the template:
   - Tattva: `templates/tattva-input-template.md`
   - Shodh: `templates/shodh-input-template.md`

2. Fill it out with:
   - **Tattva:** deity, mantra, Suno prompt output, duration, purpose
   - **Shodh:** topic, category, NotebookLM research output, duration

3. Save as `tattva-input.md` or `shodh-input.md` anywhere.

4. Run:

```bash
python generate_metadata.py --channel tattva --input "D:\path\to\tattva-input.md"
python generate_metadata.py --channel shodh --input "D:\path\to\shodh-input.md"
```

Script reads that input file.
Output: `CONTEXT_BRIEF.md` in the same folder as the input.

---

## What Claude does with the brief

After `CONTEXT_BRIEF.md` is created, tell Claude:

> *"Read `CONTEXT_BRIEF.md` at `<path>` and generate the metadata files."*

Claude will produce:

- **`YOUTUBE.md`** — Title variants, full description, tags, chapters, hashtags, thumbnail brief
- **`INSTAGRAM.md`** — Caption, hashtags, alt text
- **`FACEBOOK.md`** — Post copy, CTA

All files copy-paste ready for upload.

---

## Folder structure

```
_MetadataGenerator/
├── generate_metadata.py        # Main script
├── README.md                   # This file
├── rules/                      # Per-channel tone/formula rules
│   ├── gappu-rule.md
│   ├── bhakti-rule.md
│   ├── objectai-rule.md
│   ├── tattva-rule.md
│   └── shodh-chakra-rule.md
├── skills_reference/           # Extracted from claude-youtube + claude-skills
│   ├── youtube-seo.md
│   └── social-optimizer.md
└── templates/                  # Blank input templates
    ├── tattva-input-template.md
    └── shodh-input-template.md
```

---

## Adding a new channel

1. Create `rules/<channel>-rule.md` with tone, formulas, templates
2. Add channel to `CHANNEL_RULE_FILES`, `CHANNEL_PLATFORMS`, and either `PIPELINE_CHANNELS` or `INPUT_FILE_CHANNELS` in the script
3. (Optional) Create an input template if it's a non-pipeline channel

---

## Skills used

- **`claude-youtube`** → rules extracted to `skills_reference/youtube-seo.md`
- **`claude-skills/marketing-skill/social-content` + `social-media-analyzer`** → rules extracted to `skills_reference/social-optimizer.md`

Rules are condensed for fast loading. Full skills remain at:
- `D:\oldCOMPUTER\Videos\Scripts\GitSkills\claude-youtube\`
- `D:\oldCOMPUTER\Videos\Scripts\GitSkills\claude-skills\`
