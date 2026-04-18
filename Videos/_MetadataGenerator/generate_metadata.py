#!/usr/bin/env python3
"""
Unified Metadata Generator for all channels.

This script gathers all inputs (pipeline folder files OR input template)
plus channel rules and skill references, and packages them into a single
CONTEXT_BRIEF.md file. You then paste that brief into Claude chat, which
generates the final YOUTUBE.md / INSTAGRAM.md / FACEBOOK.md files.

Why this design?
- Metadata generation needs judgement (tone, language, cultural nuance)
- Python alone can't do that — needs LLM
- Instead of burning an API key, the script PREPARES the brief
- Claude in chat generates the final metadata from that brief

Usage:
    # Pipeline channels
    python generate_metadata.py --channel gappu --folder "D:\\...\\2026-04-17_StoryName"
    python generate_metadata.py --channel bhakti --folder "D:\\...\\2026-04-17_StoryName"
    python generate_metadata.py --channel objectai --folder "D:\\...\\2026-04-17_TopicName"

    # Input-file channels
    python generate_metadata.py --channel tattva --input "D:\\...\\tattva-input.md"
    python generate_metadata.py --channel shodh --input "D:\\...\\shodh-input.md"
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime


SCRIPT_DIR = Path(__file__).resolve().parent
RULES_DIR = SCRIPT_DIR / "rules"
SKILLS_DIR = SCRIPT_DIR / "skills_reference"

PIPELINE_CHANNELS = {"gappu", "bhakti", "objectai"}
INPUT_FILE_CHANNELS = {"tattva", "shodh"}

CHANNEL_RULE_FILES = {
    "gappu": "gappu-rule.md",
    "bhakti": "bhakti-rule.md",
    "objectai": "objectai-rule.md",
    "tattva": "tattva-rule.md",
    "shodh": "shodh-chakra-rule.md",
}

CHANNEL_PLATFORMS = {
    "gappu": ["youtube", "instagram", "facebook"],
    "bhakti": ["youtube", "instagram", "facebook"],
    "objectai": ["instagram", "facebook"],
    "tattva": ["youtube", "instagram", "facebook"],
    "shodh": ["youtube", "instagram", "facebook"],
}


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"[Could not read {path}: {e}]"


def detect_format(folder: Path) -> str:
    """Detect whether pipeline folder is 'carousel' or 'shorts'.

    Carousel = has slides/ folder with PNGs (or design-philosophy.md + generate_slides.py).
    Shorts = has images/ with named scene files (Hook/Grid/scene) OR videos/ folder.
    """
    slides_dir = folder / "slides"
    videos_dir = folder / "videos"
    generate_slides = folder / "generate_slides.py"
    design_phil = folder / "slides" / "design-philosophy.md"

    if slides_dir.exists() and any(slides_dir.iterdir()):
        if generate_slides.exists() or design_phil.exists():
            return "carousel"
        slide_pngs = list(slides_dir.glob("*.png"))
        if len(slide_pngs) >= 3:
            return "carousel"

    if videos_dir.exists() and any(videos_dir.iterdir()):
        return "shorts"

    if "carousel" in str(folder).lower():
        return "carousel"

    return "shorts"


def gather_pipeline_data(folder: Path) -> dict:
    """Gather all relevant files from a pipeline folder."""
    fmt = detect_format(folder)
    data = {"folder_path": str(folder), "files_found": [], "format": fmt}

    session_resume = folder / "SESSION-RESUME.md"
    if session_resume.exists():
        data["session_resume"] = read_file(session_resume)
        data["files_found"].append("SESSION-RESUME.md")

    for pattern in ("*.json", "*VEO_PROMPTS*", "*PROMPTS*"):
        for match in folder.glob(pattern):
            key = match.name
            if key not in data:
                data[f"file_{key}"] = read_file(match)
                data["files_found"].append(key)

    images_dir = folder / "images"
    if images_dir.exists():
        images = sorted([f.name for f in images_dir.iterdir() if f.is_file()])
        data["images_list"] = images

    slides_dir = folder / "slides"
    if slides_dir.exists():
        slides = sorted([f.name for f in slides_dir.iterdir() if f.is_file()])
        data["slides_list"] = slides

    videos_dir = folder / "videos"
    if videos_dir.exists():
        videos = sorted([f.name for f in videos_dir.iterdir() if f.is_file()])
        data["videos_list"] = videos

    design_phil = folder / "slides" / "design-philosophy.md"
    if design_phil.exists():
        data["design_philosophy"] = read_file(design_phil)
        data["files_found"].append("slides/design-philosophy.md")

    for md in folder.glob("*.md"):
        if md.name not in {"SESSION-RESUME.md", "CONTEXT_BRIEF.md",
                           "YOUTUBE.md", "INSTAGRAM.md", "FACEBOOK.md"}:
            data[f"md_{md.name}"] = read_file(md)
            data["files_found"].append(md.name)

    return data


def build_brief(channel: str, data: dict, output_path: Path, platforms: list) -> list:
    """Build the CONTEXT_BRIEF.md file. Returns final platforms list (may exclude YouTube for carousels)."""
    rule_content = read_file(RULES_DIR / CHANNEL_RULE_FILES[channel])
    youtube_rules = read_file(SKILLS_DIR / "youtube-seo.md")
    social_rules = read_file(SKILLS_DIR / "social-optimizer.md")

    fmt = data.get("format", "shorts")

    if fmt == "carousel":
        platforms = [p for p in platforms if p != "youtube"]

    platform_files_needed = []
    for p in platforms:
        platform_files_needed.append(f"{p.upper()}.md")

    format_instructions = {
        "shorts": (
            "**Format: SHORTS / video**\n"
            "- Vertical 9:16 video\n"
            "- Hook in first 2 sec (visual, no talking)\n"
            "- YouTube Shorts + Instagram Reels + Facebook Reels formatting\n"
            "- Caption tells different story than video (extra value)"
        ),
        "carousel": (
            "**Format: CAROUSEL (Instagram + Facebook only — NO YouTube)**\n"
            "- Swipe-through slides (check slides_list count)\n"
            "- Caption must hook for slide 1 scroll-stop\n"
            "- Include per-slide alt text suggestions in INSTAGRAM.md (important for IG search)\n"
            "- Slide 1 hook, Slide 2-9 value, Slide 10 CTA (if 10 slides)\n"
            "- Mixed carousels (photo+video) get 1.4x reach — note if applicable\n"
            "- DO NOT produce YOUTUBE.md for carousel format"
        ),
    }

    brief = f"""# CONTEXT BRIEF — Metadata Generation

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Channel:** {channel}
**Format (auto-detected):** {fmt}
**Platforms required:** {', '.join(platforms)}
**Output folder:** {data.get('folder_path', output_path.parent)}

---

## INSTRUCTIONS FOR CLAUDE

{format_instructions[fmt]}

Read this entire brief, then generate these files and save them to the output folder:
{chr(10).join(f"- {f}" for f in platform_files_needed)}

Follow:
1. **Channel rule** (below) — tone, formulas, hashtags, templates
2. **YouTube SEO skill rules** (below) — title/description/tags/chapters (skip if carousel)
3. **Social optimizer skill rules** (below) — Instagram/Facebook algorithm signals
4. **Source data** (below) — the actual content to build metadata from

Each output file should be **copy-paste ready** for the platform.

---

## CHANNEL RULE — {channel.upper()}

{rule_content}

---

## YOUTUBE SEO RULES (applies if YouTube is in platforms list)

{youtube_rules}

---

## SOCIAL OPTIMIZER RULES (Instagram + Facebook)

{social_rules}

---

## SOURCE DATA

"""

    if channel in PIPELINE_CHANNELS:
        brief += "### Pipeline folder files\n\n"
        brief += f"**Folder:** `{data.get('folder_path')}`\n\n"
        brief += f"**Files found:** {', '.join(data.get('files_found', []))}\n\n"

        if "images_list" in data:
            brief += f"**Images ({len(data['images_list'])}):** {', '.join(data['images_list'])}\n\n"
        if "slides_list" in data:
            brief += f"**Slides ({len(data['slides_list'])}):** {', '.join(data['slides_list'])}\n\n"

        if "session_resume" in data:
            brief += "### SESSION-RESUME.md\n\n```markdown\n"
            brief += data["session_resume"]
            brief += "\n```\n\n"

        if "design_philosophy" in data:
            brief += "### slides/design-philosophy.md\n\n```markdown\n"
            brief += data["design_philosophy"]
            brief += "\n```\n\n"

        for k, v in data.items():
            if k.startswith("file_") or k.startswith("md_"):
                fname = k.replace("file_", "").replace("md_", "")
                brief += f"### {fname}\n\n```\n{v}\n```\n\n"

    else:
        brief += "### Input file content\n\n```markdown\n"
        brief += data.get("input_content", "[No input found]")
        brief += "\n```\n\n"

    brief += "---\n\n## EXPECTED OUTPUT\n\n"
    for p in platforms:
        brief += f"- `{p.upper()}.md` — full {p} metadata (follow channel rule template)\n"
    brief += "\nSave all files in: `" + str(output_path.parent) + "`\n"

    output_path.write_text(brief, encoding="utf-8")
    return platforms


def main():
    parser = argparse.ArgumentParser(
        description="Generate metadata context brief for Claude.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--channel", required=True,
                        choices=list(PIPELINE_CHANNELS | INPUT_FILE_CHANNELS),
                        help="Channel name")
    parser.add_argument("--folder", help="Pipeline folder path (for gappu/bhakti/objectai)")
    parser.add_argument("--input", help="Input file path (for tattva/shodh)")
    args = parser.parse_args()

    channel = args.channel.lower()

    if channel in PIPELINE_CHANNELS:
        if not args.folder:
            print(f"ERROR: --folder required for pipeline channel '{channel}'")
            sys.exit(1)
        folder = Path(args.folder)
        if not folder.exists() or not folder.is_dir():
            print(f"ERROR: folder does not exist: {folder}")
            sys.exit(1)
        data = gather_pipeline_data(folder)
        output_path = folder / "CONTEXT_BRIEF.md"

    else:
        if not args.input:
            print(f"ERROR: --input required for input-file channel '{channel}'")
            sys.exit(1)
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"ERROR: input file does not exist: {input_path}")
            sys.exit(1)
        data = {
            "input_content": read_file(input_path),
            "folder_path": str(input_path.parent),
        }
        output_path = input_path.parent / "CONTEXT_BRIEF.md"

    platforms = CHANNEL_PLATFORMS[channel]
    final_platforms = build_brief(channel, data, output_path, platforms)
    fmt = data.get("format", "n/a")

    print(f"\n[OK] Brief created: {output_path}")
    print(f"     Format: {fmt}")
    print(f"     Platforms: {', '.join(final_platforms)}")
    print(f"\nNext step:")
    print(f"  1. Open {output_path.name} in Claude chat")
    print(f"  2. Claude will generate {', '.join(p.upper() + '.md' for p in final_platforms)}")
    print(f"  3. All files save to: {output_path.parent}\n")


if __name__ == "__main__":
    main()
