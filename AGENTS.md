# Shared Agent Notes

## Shared Memory (READ + WRITE, every agent, every session)

At session start, READ `MEMORY-SHARED.md` (repo root) — cross-agent durable facts
for Claude, Codex, Antigravity, Gemini. When you learn a durable fact (user
preference, channel/brand fact, lock, tool/env note), APPEND it there using the
format in that file. This is the one shared store; do not keep divergent private
copies of cross-agent facts.

## Draft Review — Full Virality Check (MANDATORY, every agent + code path)

Applies to ALL agents (Claude, Antigravity, Codex, Gemini) and any code-driven
pipeline run. Once the hook, dialogue/narration, image prompt, and motion prompt
are drafted — but BEFORE any image is generated or any clip is rendered — run the
viral + design draft review in
`Videos/_Rules/rule_book/shared/viral-design-review.md`. Five axes (Hook,
Narration, Image prompt, Motion prompt, Viral fit), each PASS/REVISE/BLOCK. Apply
REVISE fixes inline; on a BLOCK critical (banned hook, CTA stacking, channel
identity break, overlay/motion over face/action, devotional/source breach,
invented narration) redraft before generating. The check is the cheap checkpoint;
a post-render failure costs a full re-roll. `generate_metadata.py` also emits this
pointer into every `CONTEXT_BRIEF.md`, so it travels with the metadata brief
regardless of which tool runs the pipeline.

## Screen Hook + CTA — First-Frame HOOK + Per-Platform End-Card CTA (MANDATORY, every agent + code path)

Applies to ALL agents (Claude, Antigravity, Codex, Gemini) and any code-driven
short-form run for Gappu, ObjectAi, and Bhakti. Once the draft passes the virality
check above — but BEFORE any image/clip is produced — apply
`Videos/_Rules/rule_book/shared/screen-hook-cta-rule.md`:

1. **First frame = shared on-screen HOOK.** 3-layer (visual + verbal + promise),
   ≤7 words, problem-first, banned-hook-safe, NO CTA, muted-safe text. One vertical
   render repurposed across YT/IG/FB.
2. **Last frame = per-platform END-CARD CTA.** ONE CTA only (never stack) + §3 loop
   trigger. Channel CTA lock:
   - Gappu: YT=Follow · IG=Tag · FB=Share
   - ObjectAi: YT=Subscribe · IG=Save · FB=Send
   - Bhakti: YT=Subscribe · IG=Share · FB=Share
3. **Constraints:** outro hold ≤2s, overlay compact + low (no face/deity block),
   high contrast. Grounded in `_VIRAL_GROWTH_PLAYBOOK.md` §2/§3/§5/§12.

`generate_metadata.py` emits this guide into every `CONTEXT_BRIEF.md`
(`build_screen_hook_cta_guide`, fires fmt==shorts + ≥1 of YT/IG/FB). Any non-Python
runner must enforce the same first-frame-hook + per-platform-CTA pattern manually.

## ObjectAi Veo — Force I2V + Fill-Correctness Gate (MANDATORY, every agent + code path)

Applies to ALL agents (Claude, Antigravity, Codex, Gemini) and any code-driven
run of the ObjectAi PATH B short-video pipeline.

1. **Always IMAGE_TO_VIDEO.** Every ObjectAi scene sent to Flow/Veo must declare
   `generation_mode: IMAGE_TO_VIDEO`, `model_target: "Veo 3.1 - Fast"`,
   `source_image.generation_mode: IMAGE_TO_VIDEO`, `source_image.file_reference:
   "uploaded image"`. Never TEXT_TO_VIDEO. `veo_pacer.py` now emits I2V
   unconditionally (no `has_image` branch); `generate_videos_agent.py` force-sets
   the same fields at runtime regardless of what the on-disk JSON says. A disk file
   carrying author-time `TEXT_TO_VIDEO` / `_instructions` is fine — runtime overrides it.

2. **Fill-correctness gate before paste.** Before any scene JSON is pasted into the
   Flow Agent, validate it is correctly filled. Abort (do NOT submit) if:
   - any template marker remains: `[FILL]`, `Hero/Target`, `muscular character`
   - any per-character vision field empty/missing: `object_type`, `description`,
     `face`, `face_geometry_lock`
   - `source_image.scene_description` empty/missing
   - `final_compact_prompt_for_veo` empty/missing
   Skip the `_instructions` field — it is authoring guidance, not payload, and
   legitimately contains those marker strings. Reference impl =
   `validate_scene_filled()` in
   `Videos/ObjectAi/pipeline/generate_videos_agent.py`. Any non-Python runner must
   enforce the same checks before submitting.

**Why:** raw JSON paste + TEXT_TO_VIDEO + silent attach-fail made Veo generate from
scratch (wrong scene content, HighwayBlock scene 2). Forcing I2V + gating fill
catches both the wrong-mode and hollow-field failure paths before a wasted render.

## TRIBE v2

- Repository: `D:\oldCOMPUTER\SocialMediaWork\tribev2`
- Python environment: `D:\oldCOMPUTER\SocialMediaWork\.venv-tribev2`
- Run TRIBE commands with:
  `D:\oldCOMPUTER\SocialMediaWork\.venv-tribev2\Scripts\python.exe`
- Installed editable package: `pip install -e D:\oldCOMPUTER\SocialMediaWork\tribev2`
- Before importing TRIBE from outside the repo folder, set:
  `$env:PYTHONPATH='D:\oldCOMPUTER\SocialMediaWork\tribev2'`
- Set a writable home/cache for sandboxed agents before importing `neuralset`/`tribev2`:
  `$env:USERPROFILE='D:\oldCOMPUTER\SocialMediaWork\.cache\tribev2-home'`
- Install date: 2026-05-17

## Hyperframes Rendering

1. **Always use `npx -y`:** Always run `npx` commands (e.g. `npx -y hyperframes render`) with the `-y` flag to prevent them from hanging on package installation prompts in headless environments.
2. **Avoid Docker renders:** The default Docker image (`hyperframes-renderer:0.6.42`) has a packaging bug that causes it to crash immediately, and virtualization through WSL2 lacks GPU access, making software rendering extremely slow (50+ hours vs 1.38 hours locally).
3. **Handle certificate errors on Chrome download:** If the browser download fails with an SSL certificate warning (`unable to verify the first certificate`), run:
   `$env:NODE_TLS_REJECT_UNAUTHORIZED=0; npx -y hyperframes browser ensure`
   This installs the browser and ensures critical files like `icudtl.dat` are fully cached.

