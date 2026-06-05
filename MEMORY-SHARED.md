# Shared Memory — ALL Agents (Claude · Codex · Antigravity · Gemini)

Single cross-agent memory. **Every agent reads this at session start and appends
new durable facts here.** Plain markdown, git-tracked. One fact per bullet, dated.

**Write rules:**
- Append under the right `##` section. Newest at bottom of its section.
- Format: `- [YYYY-MM-DD] <fact>. Why: <reason>. Apply: <how>.`
- Update/delete a wrong line instead of duplicating.
- Channel pipeline RULES live in `Videos/_Rules/` — link, don't copy them here.
- Claude also keeps its own private store at
  `C:\Users\rahul\.claude\projects\d--oldCOMPUTER-SocialMediaWork\memory\`; mirror
  only the cross-agent-relevant facts into this file.

---

## User

- User = solo social-media creator. Channels: Gappu (kids monkey), ObjectAi
  (talking objects/body-parts science), Bhakti/Sanatan (devotional), Tattva
  (music), ShodhChakra (YT long-form). Terse output preferred (caveman mode).

## Channel / Brand Facts

- [2026-06-03] Handle map: Gappu IG=@gappumagicworld / FB="Gappu Magic Story Land".
  Bhakti = Sanatan ONE brand split by platform: FB/IG @sanatandharmatheeternalpath,
  YT @SanatanDharma-g7g. ObjectAi IG=@objectwithbrainsai (Meta hub, no YT primary).
  Apply: use exact handle per platform; ObjectAi is IG/FB-led.
- [2026-06-03] Tattva = music release channel. 3 sub-formats (shloka / instrumental /
  bhakti song) × dual-cut (single + loop) × single UPC. Spotify save-rate ≥4.5% = scale.

## Mandatory Gates (also in AGENTS.md — enforce in every run)

- [2026-06-03] Draft Review virality check BEFORE any image/clip:
  `Videos/_Rules/rule_book/shared/viral-design-review.md` (5 axes PASS/REVISE/BLOCK).
- [2026-06-03] Screen Hook + CTA: first frame = shared 3-layer on-screen HOOK (≤7
  words, no CTA, muted-safe); last frame = per-platform ONE end-card CTA + loop.
  CTA lock: Gappu Follow/Tag/Share · ObjectAi Subscribe/Save/Send · Bhakti
  Subscribe/Share/Share. Rule: `Videos/_Rules/rule_book/shared/screen-hook-cta-rule.md`.
- [2026-06-03] ObjectAi Veo = always IMAGE_TO_VIDEO + fill-correctness gate before
  paste. See AGENTS.md "ObjectAi Veo" section.

## Channel Generation Locks

- [2026-06-03] Gappu image prompts MUST inject 6-line hardened CHARACTER LOCK
  (CHARACTER+IDENTITY+CRITICAL SCALE+TEXTURE+STYLE+CAMERA SAFETY). Short single-line
  lock caused face/scale drift. Ref `gappu_dhoti.png` Image 1.
- [2026-06-03] ObjectAi आँत भाई (intestine cop) = squat coiled-loop mound, NEVER
  "long tube" (phallic drift). Append NOT-phallic / NOT-single-tube negative.
- [2026-06-03] Bhakti = gappu-style CHAR_LOCK.md + 2 ref PNGs (char_a_ref.png /
  char_b_ref.png) uploaded as Image 1/2. Env cap 10 images/story.
- [2026-06-03] Tattva videos: set defaultLanguage + defaultAudioLanguage = "hi"
  (never en/en-IN).

## Tooling / Env

- [2026-06-03] TRIBE v2 repo: `D:\oldCOMPUTER\SocialMediaWork\tribev2`, venv
  `.venv-tribev2`. Run via that venv python. See AGENTS.md "TRIBE v2" for env vars.
- [2026-06-03] ElevenLabs TTS model = `eleven_v3` (not multilingual_v2).
- [2026-06-05] Hyperframes rendering: Always run local GPU renders via npx with auto-install (e.g. `npx -y hyperframes render`). The Docker image (`0.6.42`) has a missing manifest bug. If Chrome fails to download due to SSL cert issues, run `$env:NODE_TLS_REJECT_UNAUTHORIZED=0; npx -y hyperframes browser ensure` first to force download of `icudtl.dat`. Why: Bypasses npx prompt hangs and WSL2 software-rendering slow speed (1.38h vs 50h).


---

## Log (append-only, any agent)

- [2026-06-03] Claude: created this shared memory file + wired into AGENTS.md /
  GEMINI.md / CLAUDE.md so Codex + Antigravity + Gemini read+write same store.
