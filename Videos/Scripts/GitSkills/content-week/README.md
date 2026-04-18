# Content Week - Claude Skill

> A Claude skill that turns one YouTube video into a full week of multi-platform content.
> Works with Claude.ai, Claude Desktop, and Claude Code.
> Generates Instagram carousels, captions, LinkedIn posts, and email copy — with visuals via Blotato.

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-orange)](https://claude.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is this?

A skill for Claude that repurposes a single YouTube video (or transcript, or topic) into a complete week of content across Instagram, LinkedIn, and email — the system behind growing an account from 7K to 17K followers in 30 days with 1.2M organic reach.

Claude extracts multiple angles from your source material so every post feels fresh while reinforcing the same core message. Optionally connects to Blotato to auto-generate carousel visuals and schedule posts directly.

Works with **Claude.ai** (web), **Claude Desktop**, and **Claude Code**.

---

## What it generates

From one input, you get:

- **3 Instagram captions** — each from a different angle, with hook + body + CTA
- **2 Instagram carousels** — one tutorial-style, one myth-busting/contrarian
- **1 LinkedIn post** — storytelling format, professional tone
- **1 Email newsletter draft** — 3 subject line options + personal-voice body copy

If Blotato is connected, it also auto-creates carousel visuals and schedules everything across the week.

---

## Trigger phrases

Claude activates this skill when you say things like:

- "repurpose my video"
- "turn this into content"
- "content week"
- "give me a week of content"
- "create posts from my video"
- "make content from this"
- *(paste a YouTube URL and ask for content)*
- *(share a transcript or topic and ask for social posts)*

---

## Installation

### Claude.ai and Claude Desktop

1. Download **`content-week-skill.zip`** from this repository
2. In Claude.ai or Claude Desktop: go to **Customize > Skills** → click **"+"** → **"Upload a skill"**
3. Upload the ZIP file and toggle the skill on

> **Note:** Skills require code execution to be enabled. If you don't see the Skills section, go to **Settings > Capabilities** and enable "Code execution and file creation" first.

### Claude Code (CLI) - via plugin marketplace

```bash
/plugin marketplace add maciejdzierzek/content-week
/plugin install content-week@maciejdzierzek-content-week
```

### Claude Code (CLI) - manual install

```bash
mkdir -p ~/.claude/skills/content-week
cp skills/content-week/skill.md ~/.claude/skills/content-week/skill.md
```

For project-specific use:
```bash
mkdir -p /your-project/.claude/skills/content-week
cp skills/content-week/skill.md /your-project/.claude/skills/content-week/skill.md
```

Reload Claude Code. The skill activates automatically.

---

## First-time setup

On first run, Claude will ask for:

1. **Your name** — appears on carousels and CTAs
2. **Your handle** — Instagram/social handle with @
3. **Your brand colours** — 2-3 hex codes, or describe them in plain language
4. **Your CTA keyword** — the comment trigger for ManyChat (e.g. "GUIDE"), or leave blank to use save/share CTAs

These are stored for the session. If you've set them up in your Claude project instructions, Claude pulls from there automatically.

---

## Blotato integration (optional)

If you have [Blotato](https://blotato.com) connected as an MCP server, the skill will:

- Auto-generate carousel visuals using your brand colours and one of 4 built-in templates
- Schedule posts across the week with automatic slot selection
- Support Instagram carousels and LinkedIn posts natively

Without Blotato, you get all the text content in a clean format ready to paste into any design or scheduling tool.

---

## Content quality principles

The skill follows a strict set of rules derived from real performance data:

- **Hooks first** — the opening line determines everything
- **One idea per post** — deep > wide
- **Short sentences** — especially on Instagram
- **Specificity over generality** — numbers, names, concrete details
- **Every post ends with action** — never vague inspiration

---

## About the Author

Built by [Maciej Dzierżek](https://maciejdzierzek.com) - consultant, trainer, and creator based in Poland.

- Website: [maciejdzierzek.com](https://maciejdzierzek.com)
- All AI tools: [maciejdzierzek.com/narzedzia](https://maciejdzierzek.com/narzedzia)

---

## License

MIT - use freely, attribution appreciated. See [LICENSE](LICENSE).
