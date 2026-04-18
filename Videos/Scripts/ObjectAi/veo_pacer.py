"""
VEO PACER — Full Automation
Exact replica of veo-pacer-v9-fixed.html buildJSON() logic.
Raw script + images -> Final Veo prompts (all [FILL] completed by Claude)

Usage:
  python veo_pacer.py --raw kidney_all_scenes.txt --images s1.jpg,s2.jpg,s3.jpg,s4.jpg,s5.jpg --tone "Funny Swag" --dur 8
  python veo_pacer.py --raw kidney_all_scenes.txt --tone "Funny Swag" --dur 8

Output:
  - [topic]_VEO_PROMPTS.md  — final Veo prompts, ready to paste
  - scene1_*.json ... scene5_*.json — full JSON records
"""

import json, re, sys, os, argparse
from pathlib import Path

# ── CONSTANTS (mirrors HTML tool) ──
MW = 13   # max_words_per_8s
TONES = ["Funny Swag", "Villain Swag", "Savage", "Emotional", "Cute"]


def ft(s):
    return f"{s//60:02d}:{s%60:02d}"


def sanitize(s):
    s = re.sub(r'<[^>]*>', '', s)
    s = re.sub(r'&[a-z]+;', '', s, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', s).strip()


def parse_turns(raw):
    """Mirrors parseTurns() in HTML tool."""
    turns = []
    pattern = re.compile(
        r'(?:^|[\n>*\-])\s*([A-Za-z\u0900-\u097F][A-Za-z\u0900-\u097F ]{0,20}?)\s*:\s*["\u201C\u201c]([^"\u201D\u201d]+)["\u201D\u201d]',
        re.MULTILINE
    )
    for m in pattern.finditer(raw):
        name = m.group(1).strip()
        line = sanitize(m.group(2))
        if re.search(r'image prompt|motion|dialogue|scene|shot|camera|lighting|hindi', name, re.IGNORECASE):
            continue
        if len(name) > 20 or len(line) < 3:
            continue
        turns.append({"name": name, "line": line, "words": len(line.split())})
    if not turns:
        hindi = re.findall(r'["\u201C\u201c]([^"\u201D\u201d]*[\u0900-\u097F]+[^"\u201D\u201d]*)["\u201D\u201d]', raw)
        for c in hindi:
            c = sanitize(c)
            if len(c) > 2:
                turns.append({"name": "Speaker", "line": c, "words": len(c.split())})
    return turns


def get_unique_names(turns):
    seen, order = {}, []
    for t in turns:
        if t["name"] not in seen:
            seen[t["name"]] = True
            order.append(t["name"])
    return order


def detect_content(raw):
    lc = raw.lower()
    if re.search(r'ayurved|health|herb|tulsi|neem|ginger|haldi|kidney|liver', lc): return 'ayurveda'
    if re.search(r'science|physics|magnet', lc): return 'science'
    if re.search(r'funny|comedy|joke', lc): return 'comedy'
    return 'custom'


def split_scenes(raw):
    parts = re.split(r'(?=Scene\s+\d+\s*[:—\-])', raw, flags=re.IGNORECASE)
    scenes = []
    for part in parts:
        part = part.strip()
        if not part: continue
        title_line = part.split('\n')[0].strip()
        scene_title = re.sub(r'^Scene\s+\d+\s*[:—\-]\s*', '', title_line, flags=re.IGNORECASE).strip() or title_line
        img_match = re.search(r'Image Prompt:\s*\[([^\]]+)\]', part, re.IGNORECASE | re.DOTALL)
        motion_match = re.search(r'Motion:\s*\[([^\]]+)\]', part, re.IGNORECASE | re.DOTALL)
        scenes.append({
            "title": scene_title,
            "raw": part,
            "image_prompt": img_match.group(1).strip() if img_match else "",
            "motion": motion_match.group(1).strip() if motion_match else ""
        })
    return scenes


def build_characters(names):
    """Mirrors buildCharacters() in HTML tool."""
    positions = ["RIGHT", "LEFT", "CENTER"]
    chars = []
    for i, name in enumerate(names):
        chars.append({
            "name": name,
            "object_type": f"[FILL: what object is {name}? e.g. bottle/jar/tube/lamp. Repeat 5+ times in final prompt.]",
            "position": positions[i] if i < len(positions) else "CENTER",
            "location_lock": f"[FILL: Where {name} exists for ALL seconds. Where it does NOT appear.]",
            "description": "[FILL: Full Pixar 3D visual — shape, color, texture, material, size]",
            "face": "expressive face formed in [FILL: material] texture",
            "face_geometry_lock": "[FILL: How face sits on surface. Must NOT inflate/balloon/protrude.]",
            "voice": {"language": "Hindi", "tone": "[FILL]", "pace": "natural Hindi conversational"},
            "mouth_animation": {
                "active_beats": "[FILL]",
                "sealed_beats": "[FILL]",
                "style": "loose natural talking rhythm — not strict phoneme sync"
            },
            "animation": {}
        })
    return chars


def build_beats_from_turns(turns, names, dur):
    """Mirrors buildBeatsFromTurns() in HTML tool."""
    beats = []
    seg_count = (dur + 7) // 8
    turn_idx = 0

    for seg in range(seg_count):
        base = seg * 8
        # Silent hook
        beats.append({
            "beat": len(beats)+1,
            "time": f"{ft(base)}-{ft(base+2)}",
            "type": "silent_hook",
            "active_speaker": None,
            "sealed_characters": names[:],
            "visuals": "[FILL: Bring scene to life. All characters breathe subtly. No dialogue.]",
            "foreground_content": "[FILL: List everything in foreground. No empty space.]",
            "character_positions_this_beat": "[FILL: Confirm every character position.]",
            "dialogue": None,
            "audio": {"music": "[FILL: very soft LOW]", "ambient": "[FILL]", "sfx": ["[FILL]"]}
        })

        seg_turns = turns[turn_idx:turn_idx + (2 if len(names) >= 2 else 1)]
        turn_idx += len(seg_turns)
        current_time = base + 2

        for i, turn in enumerate(seg_turns):
            t_end = current_time + 3
            sealed = [n for n in names if n != turn["name"]]
            is_last = (turn_idx >= len(turns)) and (i == len(seg_turns) - 1)
            sealed_note = f" {', '.join(sealed)} reacts from their position, mouth SEALED." if sealed else ""

            beats.append({
                "beat": len(beats)+1,
                "time": f"{ft(current_time)}-{ft(t_end)}",
                "type": "mic_drop" if is_last else "dialogue",
                "active_speaker": turn["name"],
                "sealed_characters": sealed,
                "speaker_activation_rule": f"ONLY {turn['name']} mouth animates this beat. {', '.join(sealed) + ' may react with eyes/posture ONLY — mouth SEALED.' if sealed else ''}",
                "visuals": f"[FILL: {turn['name']} speaks. Action-sync each phrase to visual change.{sealed_note} ]",
                "foreground_content": f"[FILL: Account for ALL foreground space.{' CRITICAL: highest hallucination risk beat.' if is_last else ''} ]",
                "character_positions_this_beat": f"[FILL: {'. '.join([n + ' at [location]' for n in names])}. No teleporting.]",
                "dialogue": {
                    "speaker_name": turn["name"],
                    "line": turn["line"],
                    "delivery": "[FILL]",
                    "word_count": turn["words"],
                    "duration_seconds": t_end - current_time,
                    "pace_note": "natural Hindi conversational",
                    "action_sync": {"[FILL: key phrase]": "[FILL: visual change]"}
                },
                "audio": {"music": "[FILL: LOW]", "ambient": "[FILL]", "sfx": ["[FILL: synced to key word]"]}
            })
            current_time = t_end

    return beats


def update_mouth_schedules(chars, beats):
    for c in chars:
        active = [b["beat"] for b in beats if b.get("active_speaker") == c["name"]]
        sealed = [b["beat"] for b in beats if c["name"] in (b.get("sealed_characters") or [])]
        c["mouth_animation"]["active_beats"] = active if active else "[FILL]"
        c["mouth_animation"]["sealed_beats"] = sealed if sealed else "[FILL]"


def validate(json_data):
    """Mirrors validate() in HTML tool."""
    issues = []
    chars = json_data.get("characters", [])
    beats = json_data.get("beats", [])
    for c in chars:
        ma = c.get("mouth_animation", {})
        if ma.get("active_beats") == "none":
            if any(b.get("active_speaker") == c["name"] for b in beats):
                issues.append({"type": "err", "msg": f"{c['name']} has dialogue beats but mouth_animation.active_beats='none'"})
    for b in beats:
        asp = b.get("active_speaker")
        sealed = b.get("sealed_characters", [])
        if asp and asp in sealed:
            issues.append({"type": "err", "msg": f"Beat {b['beat']}: {asp} is both active_speaker AND in sealed_characters"})
        # Check negative contradictions
        neg = json_data.get("negative_prompt", [])
        for n in neg:
            if isinstance(n, str) and f"no mouth movement for {asp}".lower() in n.lower() if asp else False:
                issues.append({"type": "err", "msg": f'Negative prompt forbids mouth for "{asp}" but they have dialogue. Remove: "{n}"'})
    return issues


def build_json(title, names, turns, has_image, img_desc, motion, tone, content, dur):
    """
    Exact mirror of buildJSON() in veo-pacer-v9-fixed.html.
    Produces identical JSON structure.
    """
    content_label = {
        "ayurveda": "Ayurveda / Health",
        "science": "Science / Knowledge",
        "comedy": "Comedy / Fun",
        "custom": "Custom"
    }.get(content, "Custom")

    is_multi = len(names) > 1
    speaker_mode = "MULTI_SPEAKER" if is_multi else "SINGLE_SPEAKER"

    chars = build_characters(names)
    beats = build_beats_from_turns(turns, names, dur) if turns else []
    update_mouth_schedules(chars, beats)

    turn_rule = (
        "Only ONE character speaks at a time. Per beat: active_speaker has lip sync, all sealed_characters have mouth SEALED and may only react with eyes/posture."
        if is_multi else
        f"Only {names[0]} speaks. All other elements are silent."
    )

    # ── Negatives (mirrors HTML tool exactly) ──
    negatives = []
    if has_image:
        negatives += ["do not regenerate the image", "no scene redesign"]
    negatives += [
        "no human figures — all characters are animated objects",
        "no man, no person, no human body",
        "characters are objects NOT people",
        "no new characters",
        "no additional characters"
    ]
    for i, n in enumerate(names):
        negatives.append(f"no duplicate {n} anywhere in frame")
        if i > 0:
            negatives.append(f"no {n} appearing near {names[0]}'s position")
        negatives.append(f"no mini/small version of {n} spawning")
    negatives += [
        "no subtitles", "no camera cuts", "no camera angle change",
        "no character repositioning", "no exaggerated cartoon motion",
        "no fast speech", "no balloon face or inflated face geometry",
        "no separate 3D head object on any character"
    ]
    never_speaks = [n for n in names if not any(b.get("active_speaker") == n for b in beats)]
    for n in never_speaks:
        negatives.append(f"no mouth movement for {n} — mouth stays sealed entire video")
    negatives.append("[FILL: scene-specific negatives]")

    # ── Fallback dialogue (mirrors HTML tool: beat{i+2}_shorter) ──
    fallback = {}
    for i, t in enumerate(turns):
        fallback[f"beat{i+2}_shorter"] = f"[FILL: shorter version of {t['name']}'s line]"

    # ── Density check ──
    total_words = sum(t["words"] for t in turns)
    spoken_secs = len([b for b in beats if b.get("active_speaker")]) * 3
    silent_secs = dur - spoken_secs
    wps = round(total_words / spoken_secs, 1) if spoken_secs > 0 else 0

    # ── Full JSON — exact field order from HTML tool ──
    result = {
        "_instructions": f"PASTE THIS JSON INTO CLAUDE{' with your reference image' if has_image else ''}. Fill every [FILL]. Hindi Devanagari dialogue. Natural Hindi conversational pace. Veo speaks dialogue AND animates mouth loosely — not strict phoneme sync. Pause-based delivery where it feels natural. Action-synced. (Language: Hindi)(no subtitles). Use character NAMES everywhere (never Hero/Target). Repeat object_type word 5+ times. Never 'muscular character' — always 'muscular BOTTLE'. Fill final_compact_prompt_for_veo.",
        "title": title,
        "duration_seconds": dur,
        "aspect_ratio": "9:16",
        "style": f"cinematic Pixar-style 3D, {tone}",
        "content_type": content_label,
        "generation_mode": "IMAGE_TO_VIDEO" if has_image else "TEXT_TO_VIDEO",
        "model_target": "VEO 3.1",
        "_speaker_mode": speaker_mode,
        "_speaker_count": len(names),
        "_speaker_order": names,
        "_first_speaker": turns[0]["name"] if turns else names[0],
        "_turn_rule": turn_rule,
        "_rules": {
            "tone": tone,
            "mouth_animation": "loose natural talking rhythm — not strict phoneme sync",
            "dialogue_delivery": "Veo speaks Hindi audio AND animates mouth loosely together",
            "pace_note": "Natural Hindi conversational pace — 3 to 4 words per second is normal speech",
            "max_words_per_8s": MW,
            "custom": motion or None   # motion goes into custom context
        },
        "source_image": {
            "mode": "FIXED_FIRST_FRAME",
            "generation_mode": "IMAGE_TO_VIDEO" if has_image else "TEXT_TO_VIDEO_WITH_FRAME1_PROMPT",
            "file_reference": "uploaded image" if has_image else "[generate image first]",
            "first_frame_instruction": "Start on this exact uploaded image. Hold nearly still for 0.3s." if has_image else None,
            "image_prompt": img_desc or "[FILL: Frame 1 image prompt — all characters in starting positions, 9:16 vertical]",
            "scene_description": "[FILL: exact Frame 1 scene]",
            "what_must_not_change": ["camera angle", "camera height", "scene composition", "character positions", "background", "props", "lighting", "character colors/shapes"],
            "allowed_animation_only": ["facial micro-expressions", "subtle breathing", "tiny hand/arm motion", "glow/particle effects", "lip sync only for speakers"]
        },
        "scene_integrity": {
            "character_count": f"EXACTLY {len(names)} characters",
            "character_positions": [f"{n} — [FILL: exact fixed location for all {dur}s. Does NOT appear elsewhere.]" for n in names],
            "position_lock": f"Positions FIXED for all {dur}s. No teleporting, duplicating, or new locations.",
            "foreground_fill_rule": "[FILL: Every beat must explicitly fill ALL foreground space. Empty space = Veo hallucination.]",
            "narrative_completion_warning": "If dialogue is directed at another character, Veo may hallucinate them closer. Anchor positions in EVERY beat."
        },
        "global_motion_rules": {
            "camera_rule": "[FILL: based on scene]",
            "character_rule": "[FILL: based on scene]",
            "animation_rule": "[FILL: based on scene]",
            "style_rule": "[FILL: based on tone]"
        },
        "characters": chars,
        "environment": {
            "setting": "[FILL]",
            "lighting": "[FILL]",
            "atmosphere": "[FILL]",
            "background_elements": ["[FILL]"],
            "foreground_props": ["[FILL]"]
        },
        "beats": beats,
        "audio": {
            "dialogue_priority": "Dialogue dominant over music/effects",
            "subtitles": False,
            "soundtrack_level": "low",
            "overall_feel": "[FILL]"
        },
        "veo_3_1_optimization": {
            "primary_instruction": f"Animate uploaded image into {dur}s cinematic video keeping original composition intact." if has_image else f"Generate {dur}s cinematic Pixar 3D video.",
            "motion_budget": "[FILL: based on scene]",
            "mouth_animation_model": "LOOSE — Veo generates Hindi audio and animates mouth with natural talking rhythm. Not strict phoneme-by-phoneme sync.",
            "priority_order": (
                ["preserve exact source frame" if has_image else "establish scene"] +
                [f"natural loose mouth animation on {n} in their speaking beats only" for n in names] +
                ["[FILL: key visual actions]", "[FILL: camera movement]"]
            ),
            "performance_note": "[FILL]"
        },
        "negative_prompt": negatives,
        "fallback_dialogue": {"use_if_rushed": fallback if fallback else "[FILL]"},
        "final_compact_prompt_for_veo": f"[FILL: Start with SCENE INTEGRITY LOCK. Repeat each object_type 5+ times. Never 'character' — always 'the KIDNEY'. {'Animate uploaded image...' if has_image else 'Generate 9:16 Pixar 3D video...'} Anchor all character positions every mention. Foreground lock on final beat. End with: 'Mouth animation is LOOSE and NATURAL — not strict phoneme sync. Veo speaks the Hindi line and animates mouth with natural talking rhythm.']",
        "density_check": {
            "total_words": total_words,
            "total_spoken_seconds": spoken_secs,
            "total_silent_seconds": silent_secs,
            "natural_speech_pace": "Hindi conversational — 3 to 4 WPS",
            "status": f"{'SAFE' if wps <= 4.5 else 'WARNING: too fast'} — {total_words} words in {spoken_secs}s = {wps} WPS"
        },
        "keywords": ["9:16", "Object Talk AI", "Hindi", content_label, tone, "viral"],
        "original_dialogue_turns": turns
    }

    # Auto-repair: remove negatives that contradict speakers
    issues = validate(result)
    for iss in issues:
        if iss["type"] == "err" and "Negative prompt forbids" in iss["msg"]:
            bad = re.search(r'Remove: "([^"]+)"', iss["msg"])
            if bad:
                result["negative_prompt"] = [n for n in result["negative_prompt"] if n != bad.group(1)]

    return result, validate(result)


def main():
    parser = argparse.ArgumentParser(description="VEO Pacer — Exact HTML tool replica in Python")
    parser.add_argument("--raw", required=True, help="Raw script .txt (single or multi-scene)")
    parser.add_argument("--images", help="Comma-separated image paths: s1.jpg,s2.jpg,...")
    parser.add_argument("--tone", default="Funny Swag", choices=TONES)
    parser.add_argument("--dur", type=int, default=8, choices=[8, 16, 24])
    parser.add_argument("--content", default="auto")
    parser.add_argument("--out", help="Output folder (default: same as input)")
    args = parser.parse_args()

    with open(args.raw, encoding="utf-8") as f:
        raw = f.read()

    content = args.content if args.content != "auto" else detect_content(raw)
    scenes = split_scenes(raw)
    is_multi = len(scenes) > 1
    if not is_multi:
        scenes = [{"title": Path(args.raw).stem, "raw": raw, "image_prompt": "", "motion": ""}]

    image_list = [p.strip() for p in args.images.split(',')] if args.images else []
    out_folder = args.out or str(Path(args.raw).parent)
    os.makedirs(out_folder, exist_ok=True)

    topic_name = Path(args.raw).stem
    print(f"\nVEO PACER — {len(scenes)} scene(s) | {args.tone} | {args.dur}s")
    print("="*60)

    for i, scene in enumerate(scenes):
        img_path = image_list[i] if i < len(image_list) else None
        has_image = bool(img_path and os.path.exists(img_path))
        turns = parse_turns(scene["raw"])
        names = get_unique_names(turns)
        if not names:
            m = re.match(r'(.+?)\s+vs\s+(.+)', scene["title"], re.IGNORECASE)
            names = [m.group(1).strip(), m.group(2).strip()] if m else ["Speaker"]

        result, issues = build_json(
            scene["title"], names, turns, has_image,
            scene["image_prompt"], scene["motion"],
            args.tone, content, args.dur
        )

        safe_title = re.sub(r'[^\w\s-]', '', scene["title"]).strip().replace(' ', '_')
        json_path = os.path.join(out_folder, f"scene{i+1}_{safe_title}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        wps = result["density_check"]["status"]
        warn = f" [{len(issues)} issue(s)]" if issues else " [OK]"
        print(f"Scene {i+1}: {scene['title']}")
        print(f"  Speakers : {', '.join(names)}")
        print(f"  Turns    : {len(turns)} | Image: {Path(img_path).name if has_image else 'none'}")
        print(f"  Density  : {wps}")
        print(f"  Saved    : {json_path}{warn}")
        print()

    print("="*60)
    print("NEXT: Paste each scene JSON + image to Claude.")
    print("Claude fills all [FILL] -> final_compact_prompt_for_veo -> paste into Veo.")
    print("="*60)


if __name__ == "__main__":
    main()
