const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// ── CONFIG ───────────────────────────────────────────────────────
const SESSION_FILE = path.join(__dirname, '2026-04-17_FreedomFlight', 'SESSION-RESUME.md');
const IMAGES_DIR = path.join(__dirname, '2026-04-17_FreedomFlight', 'images');
const VIDEOS_DIR = path.join(__dirname, '2026-04-17_FreedomFlight', 'videos');
const REFERENCE_IMAGE = path.join(__dirname, 'reference', 'gappu_dhoti.png');
const USER_DATA_DIR = path.join(__dirname, '.browser_profile');

// ── BLOCK 1 + BLOCK 2 FOR FREEDOM FLIGHT ─────────────────────────
const BLOCK1 = `┌─────────────────────────────────────────────────────────────┐
INPUT MODE:       A — Shot Breakdown (15 shots → 15 scenes)
STORY CORE:       A toddler monkey's dream of freedom — earning the right to set another creature free.
REWATCH DETAIL:   Silver ring on Gappu's right pinky (Scene 1) → catches golden light as cage opens (Scene 15)
VISUAL ECHO PAIR: Scene 7 (crying in debris, left third) mirrors Scene 15 (sitting back smiling, right third)
VIRAL TRIGGER:    "This made me cry and I don't know why"
HOOK TECHNIQUE:   (b) ACHIEVEMENT OPEN — Gappu mastering something too big for him
LIGHTING ARC:     Sc1-3 warm golden | Sc4-7 cold blue-grey | Sc8-11 harsh midday | Sc12-13 neutral | Sc14-15 magic hour
COLOR TEMP ARC:   warm → desaturated → harsh → neutral → golden
SHOT SIZE ARC:    MS → CU → WIDE → MS → CU → WIDE → MS → CU → MS → WIDE → CU → MS → WIDE → CU → MW
POSITION ARC:     CENTER → LEFT → LEFT → LEFT → LEFT → LEFT → LEFT → CENTER → CENTER → CENTER → RIGHT → RIGHT → RIGHT → RIGHT → RIGHT
BRIDGE SCENES:    none
TOTAL SCENES:     15
LOCATIONS:        Railway Station Platform, Concrete Wash Area, Outdoor Bird Market, Sunlit Forest
GAPPU OUTFIT:     cream cotton toddler shirt, olive green half pants, bare feet, tail uncovered, small silver ring on right pinky
NEW CHARACTERS:   Officer Singh, Old Bird Seller
└─────────────────────────────────────────────────────────────┘

─────────────────────────────────────────────────────────────
scene: 1
arc:            HOOK
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu stands on a wooden crate and stirs a massive silver pot of steaming tea with a long metal ladle, tail pointing straight up rigid. A small silver ring glints on his right pinky finger.
emotion:        ATLAS 05 (DETERMINED GRIT) + tongue tip visible at corner of mouth, brow pulled low in laser focus
location:       Bustling Indian train station, early morning, warm golden sunlight
characters:     Gappu alone
shot:           MEDIUM SHOT
lens:           35mm
camera_move:    Slow push-in, then holds
duration:       3
lighting:       Warm high-key morning light, 4000K, volumetric steam rising through golden rays
composition:    Gappu centered behind the large pot, steam filling upper frame, silver ring visible on right pinky
music_energy:   LIGHT BEAT
continuity:     OPENS STORY — no prior scene
cut_to:         CLOSE-UP — Gappu tilts heavy metal kettle, both hands gripping the handle
cin_reason:     Viewer must feel immediate competence and scale — a toddler mastering something too big for him triggers protective pride. The MEDIUM SHOT + 35mm lens shows both Gappu's skill and the pot's overwhelming size. Centered composition + warm light = safe, capable opening before the fall.
─────────────────────────────────────────────────────────────
scene: 2
arc:            HOOK
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu pours steaming tea from a heavy metal kettle into a small glass, tail pointing straight up rigid, silver ring catching the light.
emotion:        ATLAS 05 (DETERMINED GRIT) + tongue tip still visible, eyes narrowed in concentration
location:       Bustling Indian train station, early morning, warm golden sunlight
characters:     Gappu alone
shot:           CLOSE-UP
lens:           50mm
camera_move:    Static, then holds
duration:       3
lighting:       Warm golden morning light, 4000K, steam backlit
composition:    Gappu's face and hands filling frame, kettle dominating foreground
music_energy:   LIGHT BEAT
continuity:     Same warm golden light as Scene 1. Gappu still centered. Steam still rising.
cut_to:         MEDIUM SHOT — Gappu offers tea glass to Officer Singh
cin_reason:     Viewer must feel the intimacy of care — small hands doing something precise. CLOSE-UP + 50mm creates tenderness. Backlit steam = warmth before the cold fall.
─────────────────────────────────────────────────────────────
scene: 3
arc:            HOOK
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu offers the tea glass to Officer Singh's uniformed torso, both stubby hands lifting the glass upward, tail pointing straight up rigid.
emotion:        ATLAS 11 (PRIDE / PAYOFF) + chest slightly out, soft satisfied smile, one palm pressed flat to own chest
location:       Bustling Indian train station, early morning, warm golden sunlight
characters:     Officer Singh
shot:           MEDIUM SHOT
lens:           35mm
camera_move:    Slow push-in, then holds
duration:       3
lighting:       Warm golden morning light, 4000K
composition:    Gappu on left third, Officer's uniform filling right two-thirds
music_energy:   LIGHT BEAT
continuity:     Same warm light. Gappu moves from center to left third — first hint of submission.
cut_to:         WIDE SHOT — tea glass smashes on platform (NO Gappu)
cin_reason:     Viewer must feel the offering as genuine love — pride before the fall. MEDIUM SHOT shows both Gappu's gesture and the power imbalance. Left-third positioning = subconscious weakness creeping in.
─────────────────────────────────────────────────────────────
scene: 4
arc:            PAIN
env_name:       Railway Station Platform
gappu_in_scene: NO
action:         A small glass of tea smashes on the concrete platform, brown liquid spreading outward in a dark puddle, shards glinting in the cold light.
emotion:        [NOT IN SCENE]
location:       Bustling Indian train station, early morning, cold blue-grey light
characters:     Officer Singh
shot:           WIDE SHOT
lens:           35mm
camera_move:    Static, then holds
duration:       4
lighting:       Cold blue-grey flat light, 6000K, no warmth
composition:     shattered glass centered, vast empty platform around it
music_energy:   SUDDEN SILENCE
continuity:     Same location as Scene 3, but light has turned cold. Gappu absent — emotional whiplash.
cut_to:         MEDIUM SHOT — Gappu cowers, tail tucked
cin_reason:     Viewer must feel the rejection without seeing the rejector — the object becomes the emotion. WIDE SHOT + absence of Gappu = isolation. Cold light = warmth ripped away.
─────────────────────────────────────────────────────────────
scene: 5
arc:            PAIN
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu cowers on the cold concrete, both stubby hands covering his face, tail tucked completely under body.
emotion:        ATLAS 09 (FULL FEAR) + eyes wide whites showing fully, toes curling downward
location:       Bustling Indian train station, early morning, cold blue-grey light
characters:     Officer Singh
shot:           MEDIUM SHOT
lens:           35mm
camera_move:    Very slow push-in, then holds
duration:       4
lighting:       Cold blue-grey flat light, 6000K
composition:    Gappu on left third, vast empty platform filling right two-thirds
music_energy:   LOW DRONE
continuity:     Same cold light. Gappu now on left third — pain positioning begins.
cut_to:         WIDE SHOT — boot kicks teapot (NO Gappu)
cin_reason:     Viewer must feel the child's instinct — hide the face, make the body small. MEDIUM SHOT + left-third = powerlessness. Slow push-in refuses to look away.
─────────────────────────────────────────────────────────────
scene: 6
arc:            PAIN
env_name:       Railway Station Platform
gappu_in_scene: NO
action:         A heavy black boot kicks the silver teapot, sending it skidding across the concrete with a metallic screech, steam escaping in a dying hiss.
emotion:        [NOT IN SCENE]
location:       Bustling Indian train station, early morning, cold blue-grey light
characters:     Officer Singh
shot:           WIDE SHOT
lens:           35mm
camera_move:    Static, then holds
duration:       3
lighting:       Cold blue-grey flat light, 6000K
composition:     boot and teapot centered, long shadow stretching left
music_energy:   SUDDEN SILENCE
continuity:     Same cold light. Object violence continues — Gappu still absent.
cut_to:         MEDIUM SHOT — Gappu crying in debris
cin_reason:     Viewer must feel the violence without the villain — the boot is enough. WIDE SHOT + static camera = witnessed cruelty. Metallic screech = auditory pain.
─────────────────────────────────────────────────────────────
scene: 7
arc:            PAIN
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu sits in scattered debris, one stubby finger tracing the silver ring on his right pinky, tail limp dragging on the ground, tears streaming silently.
emotion:        ATLAS 10 (AFTERMATH QUIET) + eyes half-open heavy-lidded pink and puffy, one fist pressed against eye
location:       Bustling Indian train station, early morning, cold blue-grey light
characters:     Gappu alone
shot:           MEDIUM SHOT
lens:           50mm
camera_move:    Static, then holds
duration:       5
lighting:       Cold blue-grey flat light, 6000K, tear tracks glistening
composition:    Gappu on left third, debris scattered around, vast emptiness right
music_energy:   SILENT
continuity:     Same cold light. Gappu still left third — pain deepens.
cut_to:         CLOSE-UP — Gappu scrubbing pot at wash area
cin_reason:     Viewer must feel the exhaustion after crying — not active sadness, but spent grief. MEDIUM SHOT + 50mm = intimate witness. Silver ring touch = rehook planted.
─────────────────────────────────────────────────────────────
scene: 8
arc:            STRUGGLE
env_name:       Concrete Wash Area
gappu_in_scene: YES
action:         Gappu scrubs a massive blackened pot with a rough burlap sack, both stubby hands working in circular motions, tail pointing straight up rigid.
emotion:        ATLAS 05 (DETERMINED GRIT) + jaw set forward, tongue tip visible at corner of mouth
location:       Outdoor concrete wash area, harsh midday sunlight
characters:     Gappu alone
shot:           CLOSE-UP
lens:           50mm
camera_move:    Static, then holds
duration:       4
lighting:       Harsh high-contrast midday light, deep shadows
composition:    Gappu centered, pot filling lower half, suds flying
music_energy:   LIGHT BEAT
continuity:     Time skip declared — harsh midday replaces cold morning. Same location feel.
cut_to:         MEDIUM SHOT — Gappu stirring fresh pot
cin_reason:     Viewer must feel the work beginning — effort over emotion. CLOSE-UP + 50mm = focus on the hands doing. Harsh light = no comfort, just labor.
─────────────────────────────────────────────────────────────
scene: 9
arc:            STRUGGLE
env_name:       Concrete Wash Area
gappu_in_scene: YES
action:         Gappu stirs a fresh pot of tea with a long ladle, both hands gripping the handle, tail pointing straight up rigid, brow furrowed.
emotion:        ATLAS 05 (DETERMINED GRIT) + brow pulled low, lips pressed tight
location:       Outdoor concrete wash area, harsh midday sunlight
characters:     Gappu alone
shot:           MEDIUM SHOT
lens:           35mm
camera_move:    Slow push-in, then holds
duration:       4
lighting:       Harsh high-contrast midday light
composition:    Gappu centered, pot steaming, heat waves visible
music_energy:   LIGHT BEAT
continuity:     Same harsh light. Gappu still centered — determination holds.
cut_to:         WIDE SHOT — Gappu walking through crowd
cin_reason:     Viewer must feel the repetition becoming ritual — same action, new purpose. MEDIUM SHOT + slow push-in = momentum building.
─────────────────────────────────────────────────────────────
scene: 10
arc:            STRUGGLE
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu walks through the bustling crowd carrying a small tray of tea glasses, both stubby hands holding it steady, tail wagging with nervous energy.
emotion:        ATLAS 07 (NERVOUS WAIT) + eyes darting slightly, bottom lip being gently bitten
location:       Bustling Indian train station, harsh midday sunlight
characters:     Gappu alone
shot:           WIDE SHOT
lens:           35mm
camera_move:    Tracking, then holds
duration:       4
lighting:       Harsh high-contrast midday light
composition:    Gappu tiny in center, crowd blurring around him
music_energy:   BUILDING STRINGS
continuity:     Same harsh light. Gappu centered — moving through the world now.
cut_to:         CLOSE-UP — Gappu taking money from Passenger
cin_reason:     Viewer must feel the vulnerability — small figure in overwhelming crowd. WIDE SHOT + 35mm deep focus = environment dominates. Tracking shot = journey underway.
─────────────────────────────────────────────────────────────
scene: 11
arc:            TURN
env_name:       Railway Station Platform
gappu_in_scene: YES
action:         Gappu accepts crumpled money from a passenger's hand, both stubby hands reaching up carefully, tail pointing straight up rigid.
emotion:        ATLAS 06 (SMALL HOPE) + eyes wide open soft, not quite smiling yet, one hand loosening its grip
location:       Bustling Indian train station, harsh midday sunlight
characters:     Gappu alone
shot:           CLOSE-UP
lens:           50mm
camera_move:    Static, then holds
duration:       3
lighting:       Harsh midday light, first warm edge at frame right
composition:    Gappu on right third, passenger's hand entering from left
music_energy:   SOFT FOLK
continuity:     Same harsh light, but Gappu shifts to right third — turn begins.
cut_to:         MEDIUM SHOT — Gappu giving money to Bird Seller
cin_reason:     Viewer must feel the first warmth — not joy yet, but the thaw. CLOSE-UP + 50mm = intimacy with the moment. Right-third = agency returning.
─────────────────────────────────────────────────────────────
scene: 12
arc:            TURN
env_name:       Outdoor Bird Market
gappu_in_scene: YES
action:         Gappu hands the crumpled money to the Old Bird Seller, both stubby arms extended fully, tail pointing straight up rigid.
emotion:        ATLAS 06 (SMALL HOPE) + posture straightening slightly, lip corners lifting at one corner
location:       Outdoor bird market, neutral afternoon light
characters:     Old Bird Seller
shot:           MEDIUM SHOT
lens:           35mm
camera_move:    Static, then holds
duration:       4
lighting:       Neutral afternoon light, first warmth at edges
composition:    Gappu on right third, Old Bird Seller filling left
music_energy:   SOFT FOLK
continuity:     Light softening from harsh to neutral. Gappu still right third.
cut_to:         WIDE SHOT — Gappu carrying bird cage
cin_reason:     Viewer must feel the exchange as sacrifice — money becomes freedom. MEDIUM SHOT shows both faces. Neutral light = emotional clarity.
─────────────────────────────────────────────────────────────
scene: 13
arc:            PAYOFF
env_name:       Sunlit Forest
gappu_in_scene: YES
action:         Gappu walks along a forest path carrying a small bird cage, both stubby hands gripping the handle, tail pointing straight up rigid.
emotion:        ATLAS 11 (PRIDE / PAYOFF) + chest slightly out, soft satisfied smile, palm pressed flat to chest
location:       Sunlit forest clearing, magic hour golden light
characters:     Gappu alone
shot:           WIDE SHOT
lens:           35mm
camera_move:    Slow tracking, then holds
duration:       5
lighting:       Rich saturated golden hour, long shadows, warm orange
composition:    Gappu on right third, forest path leading left
music_energy:   SWELLING ORCHESTRA
continuity:     Magic hour declared — golden light replaces neutral. Gappu still right third.
cut_to:         CLOSE-UP — Gappu opening cage door
cin_reason:     Viewer must feel the journey's weight — carrying freedom itself. WIDE SHOT + 35mm = world opening up. Magic hour = earned beauty.
─────────────────────────────────────────────────────────────
scene: 14
arc:            PAYOFF
env_name:       Sunlit Forest
gappu_in_scene: YES
action:         Gappu crouches and opens the bird cage door with one stubby finger, tail pointing straight up rigid, silver ring catching golden light.
emotion:        ATLAS 11 (PRIDE / PAYOFF) + bright eyes wide and soft, closed smile of exhausted victory
location:       Sunlit forest clearing, magic hour golden light
characters:     Gappu alone
shot:           CLOSE-UP
lens:           50mm
camera_move:    Very slow push-in, then holds
duration:       5
lighting:       Rich saturated golden hour, backlight halo
composition:    Gappu centered, cage in foreground, golden bokeh
music_energy:   SWELLING ORCHESTRA
continuity:     Same magic hour. Gappu centered — full agency.
cut_to:         MEDIUM-WIDE — Parrots fly, Gappu sits back
cin_reason:     Viewer must feel the release moment — finger on freedom's door. CLOSE-UP + 50mm = pure intimacy. Backlight halo = sanctification.
─────────────────────────────────────────────────────────────
scene: 15
arc:            PAYOFF
env_name:       Sunlit Forest
gappu_in_scene: YES
action:         Two colorful parrots fly free from the open cage as Gappu sits back on his heels, both stubby hands resting on his knees, tail pointing straight up rigid, silver ring catching golden light.
emotion:        ATLAS 01 (PURE JOY) + eyes completely crinkled shut, widest smile showing all small teeth, whole body jiggles
location:       Sunlit forest clearing, magic hour golden light
characters:     Gappu alone
shot:           MEDIUM-WIDE
lens:           35mm
camera_move:    Static, then holds
duration:       6
lighting:       Rich saturated golden hour, volumetric rays through trees
composition:    Gappu on right third, parrots exiting left, cage open center
music_energy:   SWELLING ORCHESTRA
continuity:     Same magic hour. Gappu right third — visual echo of Scene 7 reversed.
cut_to:         END
cin_reason:     Viewer must feel the release — joy earned through struggle. MEDIUM-WIDE + 35mm = Gappu in his world, free. Right-third positioning = strength achieved. Visual echo of Scene 7 completes.
─────────────────────────────────────────────────────────────`;

const BLOCK2 = `══════════════════════════════════════════════════
LOCKS PACK — Freedom Flight
══════════════════════════════════════════════════

##OUTFIT##
[SCENE 1-5]: cream cotton toddler shirt, olive green half pants, clean, tail uncovered, bare feet, small silver ring on right pinky
[SCENE 6-11]: cream cotton shirt torn and soot-stained, olive green half pants stained, tail limp, bare feet, silver ring tarnished with ash
[SCENE 12-15]: cream cotton shirt scrubbed but worn, olive green half pants worn, tail recovering, bare feet, silver ring catching golden light
[DEFAULT]: cream cotton shirt, olive green half pants, bare feet, tail uncovered, small silver ring on right pinky
##END_OUTFIT##

##ENV_SLOT_START##
NAME: Railway Station Platform
##ENV_LOCK##
Bustling Indian railway station platform, early morning to midday, concrete surface with scattered debris, tea stalls in background, steam rising from pots, passengers walking, warm golden to harsh midday light transition, photorealistic photographic quality
##ENV_SLOT_END##

##ENV_SLOT_START##
NAME: Concrete Wash Area
##ENV_LOCK##
Outdoor concrete wash area at railway station, rough grey concrete surface, water stains, soap suds, harsh midday sunlight, deep shadows, photorealistic photographic quality
##ENV_SLOT_END##

##ENV_SLOT_START##
NAME: Outdoor Bird Market
##ENV_LOCK##
Small outdoor bird market near railway station, wooden cages stacked, colorful parrots visible, old stone pavement, afternoon neutral light, vendor stalls in background, photorealistic photographic quality
##ENV_SLOT_END##

##ENV_SLOT_START##
NAME: Sunlit Forest
##ENV_LOCK##
Forest clearing with tall sal trees, dappled golden hour light filtering through canopy, moss-covered ground, volumetric light rays, magic hour warm orange glow, photorealistic photographic quality
##ENV_SLOT_END##

##CHAR_SLOT_START##
SLOT: 1
NAME: Officer Singh
##CHAR_LOCK##
Type: Photorealistic adult human male
Physical description: Indian police officer, mid-40s, stern weathered face, dark blue uniform with badges, authoritative posture
Outfit for this story: Dark blue police uniform, peaked cap, black boots
Expression default: Stern, disapproving
Key visual rule: Never show softness — face remains stern throughout
Role in story: The rejector — represents authority dismissing love
##CHAR_SLOT_END##

##CHAR_SLOT_START##
SLOT: 2
NAME: Old Bird Seller
##CHAR_LOCK##
Type: Photorealistic adult human male
Physical description: Elderly Indian man, 70s, white beard, kind wrinkled face, thin frame, wears simple cotton kurta
Outfit for this story: Off-white cotton kurta, faded red Gandhi cap
Expression default: Kind, patient
Key visual rule: Eyes always warm — the only adult kindness Gappu receives
Role in story: The enabler — sells Gappu the bird he will free
##CHAR_SLOT_END##

══════════════════════════════════════════════════
END OF LOCKS PACK
══════════════════════════════════════════════════`;

// ── PARSERS ────────────────────────────────────────────────────

function parseBlock1(block) {
  const scenes = [];
  const sceneRegex = /scene:\s*(\d+)[\s\S]*?arc:\s*([^\n]+)\n.*?env_name:\s*([^\n]+)\n.*?gappu_in_scene:\s*([^\n]+)\n.*?action:\s*([\s\S]*?)\n.*?emotion:\s*([^\n]+)\n.*?location:\s*([^\n]+)\n.*?characters:\s*([^\n]+)\n.*?shot:\s*([^\n]+)\n.*?lens:\s*([^\n]+)\n.*?camera_move:\s*([^\n]+)\n.*?duration:\s*([^\n]+)\n.*?lighting:\s*([^\n]+)\n.*?composition:\s*([^\n]+)\n.*?music_energy:\s*([^\n]+)[\s\S]*?cut_to:\s*([^\n]+)/g;

  let match;
  while ((match = sceneRegex.exec(block)) !== null) {
    scenes.push({
      scene_no: parseInt(match[1]),
      arc: match[2].trim(),
      env_name: match[3].trim(),
      gappu_in_scene: match[4].trim(),
      action: match[5].trim(),
      emotion: match[6].trim(),
      location: match[7].trim(),
      characters: match[8].trim(),
      shot: match[9].trim(),
      lens: match[10].trim(),
      camera_move: match[11].trim(),
      duration: parseInt(match[12].trim()),
      lighting: match[13].trim(),
      composition: match[14].trim(),
      music_energy: match[15].trim(),
      cut_to: match[16].trim()
    });
  }
  return scenes;
}

function parseBlock2(block) {
  const locks = { outfit: {}, environments: {}, characters: {} };

  const outfitMatch = block.match(/##OUTFIT##([\s\S]*?)##END_OUTFIT##/);
  if (outfitMatch) {
    const outfitLines = outfitMatch[1].trim().split('\n');
    outfitLines.forEach(line => {
      const tagMatch = line.match(/\[([^\]]+)\]:\s*(.+)/);
      if (tagMatch) {
        locks.outfit[tagMatch[1]] = tagMatch[2].trim();
      }
    });
  }

  const envRegex = /##ENV_SLOT_START##\nNAME:\s*([^\n]+)\n##ENV_LOCK##([\s\S]*?)##ENV_SLOT_END##/g;
  let envMatch;
  while ((envMatch = envRegex.exec(block)) !== null) {
    locks.environments[envMatch[1].trim()] = envMatch[2].trim();
  }

  const charRegex = /##CHAR_SLOT_START##[\s\S]*?SLOT:\s*(\d+)\nNAME:\s*([^\n]+)\n##CHAR_LOCK##([\s\S]*?)##CHAR_SLOT_END##/g;
  let charMatch;
  while ((charMatch = charRegex.exec(block)) !== null) {
    locks.characters[charMatch[2].trim()] = {
      slot: parseInt(charMatch[1]),
      lock: charMatch[3].trim()
    };
  }

  return locks;
}

// ── PROMPT BUILDERS ───────────────────────────────────────────

function buildImagePrompt(scene, locks) {
  const GAPPU_ANCHOR = "3D Pixar-style toddler monkey, chubby round belly, short stubby arms, large dark brown eyes whites clearly visible, oversized round head, round button nose, warm brown fur, smooth 3D render";

  let outfit = locks.outfit['DEFAULT'] || '';
  const sceneRanges = Object.keys(locks.outfit).filter(k => k.startsWith('SCENE'));
  for (const range of sceneRanges) {
    const match = range.match(/SCENE\s*(\d+)-(\d+)/);
    if (match) {
      const start = parseInt(match[1]);
      const end = parseInt(match[2]);
      if (scene.scene_no >= start && scene.scene_no <= end) {
        outfit = locks.outfit[range];
        break;
      }
    }
  }

  const envLock = locks.environments[scene.env_name] || '';

  let prompt = `ASPECT: 9:16\n`;
  prompt += `STYLE: Ultra-realistic environment + stylized 3D Gappu. Roger Rabbit effect.\n`;

  if (scene.gappu_in_scene === 'YES') {
    prompt += `CHARACTER LOCK: ${GAPPU_ANCHOR}, ${outfit}\n`;
    prompt += `PURPOSE: LOCKED to Image 1 reference (gappu_dhoti.png)\n`;
  }

  prompt += `ENVIRONMENT LOCK: ${envLock}\n`;

  if (scene.characters !== 'Gappu alone') {
    const charNames = scene.characters.split(',').map(c => c.trim()).filter(c => c !== 'Gappu alone');
    for (const charName of charNames) {
      if (locks.characters[charName]) {
        prompt += `CHARACTER: ${charName} — ${locks.characters[charName].lock}\n`;
      }
    }
  }

  prompt += `SCENE: ${scene.location}\n`;
  prompt += `SHOT: ${scene.shot}, ${scene.lens}\n`;
  prompt += `LIGHTING: ${scene.lighting}\n`;
  prompt += `COMPOSITION: ${scene.composition}\n`;

  if (scene.gappu_in_scene === 'YES') {
    prompt += `GAPPU EMOTION: ${scene.emotion} — eyes carry 80%\n`;
  }

  prompt += `ACTION: ${scene.action}\n`;
  prompt += `QUALITY: 8K sharp focus`;
  prompt += scene.gappu_in_scene === 'YES' ? ` on Gappu face\n` : `\n`;
  prompt += `NEGATIVE: deformed, blurry, low quality, wrong colors, extra limbs, text, watermark`;

  return prompt;
}

function buildMotionPrompt(scene) {
  const TODDLER_PHYSICS = "Gappu moves with toddler-physics — slight natural wobble, Pixar-exaggerated weight. 10% bigger than real. All motion has organic micro-irregularity.";
  const CONSISTENCY_AVOID = `no Gappu redesign — face/eyes/fur identical to reference image
no identity drift across this clip
no proportion changes — Gappu stays toddler-sized
no fur texture becoming realistic or live-action monkey
no outfit color shift — preserve exact colors from reference
no sudden camera shake, no glitch artifacts, no body duplication`;

  let prompt = `FORMAT: 9:16\n`;
  prompt += `DURATION: ${scene.duration}s\n`;
  prompt += `FPS: 24\n`;
  prompt += `PACING: medium\n\n`;
  prompt += `REFERENCE IMAGE MODE: I2V (image-to-video)\n\n`;
  prompt += `GLOBAL MOTION RULES: ${TODDLER_PHYSICS}\n\n`;
  prompt += `SHOT: ${scene.shot}\n`;
  prompt += `CAMERA MOVE: ${scene.camera_move}\n`;
  prompt += `LENS: ${scene.lens}\n\n`;

  if (scene.gappu_in_scene === 'YES') {
    prompt += `GAPPU PERFORMANCE: ${scene.emotion}\n`;
    prompt += `TODDLER PHYSICS: ${TODDLER_PHYSICS}\n\n`;
  }

  const actionBeats = scene.action.split(',').map(s => s.trim()).filter(s => s.length > 0);
  prompt += `ACTION BEATS:\n`;
  actionBeats.forEach((beat, i) => {
    prompt += `  ${i + 1}. ${beat}\n`;
  });

  prompt += `\nCONSTRAINTS: ${CONSISTENCY_AVOID}\n`;
  prompt += `\nNEGATIVE: morphing, glitch, extra limbs, wrong colors, text, watermark`;

  return prompt;
}

// ── SESSION TRACKER ───────────────────────────────────────────

function readSession() {
  const sessions = {};
  if (!fs.existsSync(SESSION_FILE)) return sessions;

  const content = fs.readFileSync(SESSION_FILE, 'utf8');
  const lines = content.split('\n');

  for (const line of lines) {
    const match = line.match(/\|\s*(\d+)\s*\|\s*(\w+)\s*\|\s*(\w+)\s*\|/);
    if (match) {
      sessions[match[1]] = { image: match[2], video: match[3] };
    }
  }
  return sessions;
}

function updateSession(sceneNo, field, value) {
  if (!fs.existsSync(SESSION_FILE)) return;

  let content = fs.readFileSync(SESSION_FILE, 'utf8');
  content = content.replace(
    new RegExp(`(\\|\\s*${sceneNo}\\s*\\|\\s*)(\\w+)(\\s*\\|\\s*)(\\w+)(\\s*\\|)`, 'g'),
    (match, p1, img, p2, vid, p3) => {
      if (field === 'image') return `${p1}${value}${p2}${vid}${p3}`;
      if (field === 'video') return `${p1}${img}${p2}${value}${p3}`;
      return match;
    }
  );

  fs.writeFileSync(SESSION_FILE, content);
}

// ── HIGGSFIELD AUTOMATION ──────────────────────────────────────

async function generateImage(page, scene, imagePrompt) {
  console.log(`  [IMAGE] Navigating to Nano Banana Pro...`);
  await page.goto('https://higgsfield.ai/image/nano-banana-pro', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);

  // Clear prompt
  console.log(`  [IMAGE] Clearing prompt field...`);
  await page.locator('[id="hf:tour-image-prompt"]').focus();
  await page.keyboard.press('Control+A');
  await page.keyboard.press('Delete');

  // Attach reference if Gappu in scene
  if (scene.gappu_in_scene === 'YES') {
    console.log(`  [IMAGE] Uploading reference image...`);
    const fileInput = await page.locator('input[type="file"]').first();
    await fileInput.setInputFiles(REFERENCE_IMAGE);
    await page.waitForTimeout(1000);
  }

  // Type prompt
  console.log(`  [IMAGE] Typing prompt...`);
  await page.locator('[id="hf:tour-image-prompt"]').fill(imagePrompt);

  // Generate
  console.log(`  [IMAGE] Clicking Generate...`);
  const buttons = await page.locator('button').all();
  const genButton = buttons.find(async b => {
    const text = await b.textContent();
    return text && (text.includes('Generate') || text.includes('Unlimited'));
  });
  if (genButton) await genButton.click();

  // Wait for generation
  console.log(`  [IMAGE] Waiting for generation...`);
  try {
    await page.locator(':has-text("Queued")').first().waitFor({ state: 'detached', timeout: 60000 });
    await page.locator(':has-text("Generating")').first().waitFor({ state: 'detached', timeout: 180000 });
  } catch (e) {
    console.log(`  [IMAGE] Wait timeout - checking if complete...`);
  }

  // Get image URL
  console.log(`  [IMAGE] Extracting image URL...`);
  const imgSrc = await page.locator('img[src*="higgsfield"]').first().getAttribute('src');

  if (imgSrc) {
    // Navigate to image and screenshot
    await page.goto(imgSrc);
    await page.waitForTimeout(2000);

    const outputPath = path.join(IMAGES_DIR, `scene_${String(scene.scene_no).padStart(2, '0')}.png`);
    await page.screenshot({ path: outputPath, type: 'png' });
    console.log(`  [IMAGE] Saved: ${outputPath}`);

    updateSession(scene.scene_no, 'image', 'DONE');
    return true;
  }

  console.log(`  [IMAGE] FAILED - Could not extract image URL`);
  return false;
}

async function generateVideo(page, scene, motionPrompt, imagePath) {
  console.log(`  [VIDEO] Navigating to Kling video...`);
  await page.goto('https://higgsfield.ai/create/video', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(5000);

  // Set duration using JS evaluation (from CLAUDE.md)
  console.log(`  [VIDEO] Setting duration to ${scene.duration}s...`);
  try {
    await page.evaluate((duration) => {
      const slider = document.querySelector('dialog input[type="range"]');
      if (slider) {
        const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(slider, duration);
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, scene.duration);
    await page.waitForTimeout(500);
    await page.keyboard.press('Escape');
  } catch (e) {
    console.log(`  [VIDEO] Duration slider not found - using default`);
  }

  // Upload image
  console.log(`  [VIDEO] Uploading start frame...`);
  try {
    const fileInput = await page.locator('input[type="file"]').first();
    await fileInput.setInputFiles(imagePath);
    await page.waitForTimeout(2000);
  } catch (e) {
    console.log(`  [VIDEO] File upload failed: ${e.message}`);
    return false;
  }

  // Clear and type prompt - use textarea selector as fallback
  console.log(`  [VIDEO] Typing motion prompt...`);
  let promptBox;
  try {
    promptBox = await page.locator('textarea[placeholder*="prompt"]').first();
  } catch (e) {
    try {
      promptBox = await page.locator('input[placeholder*="prompt"]').first();
    } catch (e2) {
      promptBox = await page.locator('textbox').first();
    }
  }

  await promptBox.click();
  await page.keyboard.press('Control+A');
  await page.keyboard.press('Delete');

  // Ensure "then holds" at end
  let finalPrompt = motionPrompt;
  if (!finalPrompt.trim().endsWith('then holds') && !finalPrompt.trim().endsWith('then settles')) {
    finalPrompt += '\nthen holds';
  }
  await promptBox.fill(finalPrompt);
  await page.waitForTimeout(500);

  // Generate
  console.log(`  [VIDEO] Clicking Generate...`);
  const buttons = await page.locator('button').all();
  let genButton = null;
  for (const b of buttons) {
    const text = await b.textContent();
    if (text && text.trim().startsWith('Generate')) {
      genButton = b;
      break;
    }
  }
  if (genButton) {
    await genButton.click();
  } else {
    console.log(`  [VIDEO] Generate button not found`);
    return false;
  }

  // Wait for generation
  console.log(`  [VIDEO] Waiting for generation...`);
  try {
    await page.locator(':has-text("Processing")').first().waitFor({ state: 'detached', timeout: 60000 });
    await page.locator(':has-text("Generating")').first().waitFor({ state: 'detached', timeout: 300000 });
    console.log(`  [VIDEO] Generation complete`);
  } catch (e) {
    console.log(`  [VIDEO] Wait timeout - may still be processing`);
  }

  // Download video
  console.log(`  [VIDEO] Navigating to video assets...`);
  await page.goto('https://higgsfield.ai/asset/video');
  await page.waitForTimeout(3000);

  // Find video element and get src
  const videoCount = await page.locator('video').count();
  if (videoCount > 0) {
    const videoEl = await page.locator('video').first();
    const videoSrc = await videoEl.getAttribute('src');

    if (videoSrc) {
      await page.goto(videoSrc);
      await page.waitForTimeout(2000);

      const outputPath = path.join(VIDEOS_DIR, `scene_${String(scene.scene_no).padStart(2, '0')}.mp4`);
      await page.screenshot({ path: outputPath.replace('.mp4', '_thumb.png'), type: 'png' });
      console.log(`  [VIDEO] Thumbnail saved: ${outputPath.replace('.mp4', '_thumb.png')}`);
      updateSession(scene.scene_no, 'video', 'DONE');
      return true;
    }
  }

  console.log(`  [VIDEO] No video found - checking page...`);
  const pageContent = await page.content();
  console.log(`  [VIDEO] Page has video element: ${videoCount > 0}`);
  return false;
}

// ── MAIN EXECUTION ────────────────────────────────────────────

async function checkLogin(page) {
  console.log('[LOGIN] Checking authentication state...');
  await page.goto('https://higgsfield.ai/image/nano-banana-pro', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);

  const bodyText = await page.locator('body').textContent();
  const isLoggedIn = bodyText.includes('Sign In') === false || bodyText.includes('profile') || bodyText.includes('account');

  if (isLoggedIn) {
    console.log('[LOGIN] ✓ User is logged in\n');
    return true;
  }

  console.log('[LOGIN] ✗ User is NOT logged in');
  console.log('[LOGIN] Please complete login manually, then press Enter to continue...');
  await new Promise(resolve => process.stdin.once('data', resolve));
  return true;
}

async function runPipeline() {
  console.log('═══════════════════════════════════════════════════════════');
  console.log('GAPPU PIPELINE AUTOMATION — Freedom Flight');
  console.log('═══════════════════════════════════════════════════════════\n');

  const scenes = parseBlock1(BLOCK1);
  const locks = parseBlock2(BLOCK2);

  console.log(`Parsed ${scenes.length} scenes from Block 1`);
  console.log(`Parsed ${Object.keys(locks.environments).length} environments from Block 2`);
  console.log(`Parsed ${Object.keys(locks.characters).length} characters from Block 2\n`);

  if (!fs.existsSync(IMAGES_DIR)) fs.mkdirSync(IMAGES_DIR, { recursive: true });
  if (!fs.existsSync(VIDEOS_DIR)) fs.mkdirSync(VIDEOS_DIR, { recursive: true });

  const session = readSession();

  console.log('Launching browser...\n');
  const context = await chromium.launchPersistentContext(USER_DATA_DIR, {
    headless: false,
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled', '--start-maximized', '--no-sandbox']
  });

  const page = await context.newPage();

  // Check login state
  await checkLogin(page);

  for (const scene of scenes) {
    console.log(`\n══════════════════════════════════════════════════`);
    console.log(`SCENE ${scene.scene_no} — ${scene.arc}`);
    console.log(`══════════════════════════════════════════════════`);

    const status = session[scene.scene_no] || { image: 'PENDING', video: 'PENDING' };
    console.log(`Status: IMAGE=${status.image} | VIDEO=${status.video}\n`);

    const imagePrompt = buildImagePrompt(scene, locks);
    const motionPrompt = buildMotionPrompt(scene);

    if (status.image === 'PENDING') {
      console.log('--- IMAGE GENERATION ---');
      const imageSuccess = await generateImage(page, scene, imagePrompt);
      if (!imageSuccess) {
        updateSession(scene.scene_no, 'image', 'FAILED-1');
      }
    }

    const imagePath = path.join(IMAGES_DIR, `scene_${String(scene.scene_no).padStart(2, '0')}.png`);
    if (fs.existsSync(imagePath) && status.video === 'PENDING') {
      console.log('\n--- VIDEO GENERATION ---');
      const videoSuccess = await generateVideo(page, scene, motionPrompt, imagePath);
      if (!videoSuccess) {
        updateSession(scene.scene_no, 'video', 'FAILED-1');
      }
    }

    console.log(`\n[SCENE ${scene.scene_no}] Complete`);
  }

  await context.close();

  console.log('\n══════════════════════════════════════════════════');
  console.log('Pipeline automation complete');
  console.log('══════════════════════════════════════════════════\n');
}

runPipeline().catch(err => {
  console.error('Pipeline error:', err);
  process.exit(1);
});
