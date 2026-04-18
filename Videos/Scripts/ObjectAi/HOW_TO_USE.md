# VEO PACER — How To Use (No Terminal Needed)

## The Simplest Way

Just open Claude Code and send ONE message like this:

---

> Here is my script and images. Generate all Veo prompts.
> Tone: Funny Swag | Duration: 8s
>
> Scene 1: The Interruption
> Left Kidney: "अरे रुक रुक रुक।"
> Right Kidney: "पानी कहां है भाई?"
>
> [attach s1.jpg, s2.jpg, s3.jpg... in same message]

---

Claude will:
1. Parse all scenes from your text
2. Read each image you attached
3. Fill all visual/scene details
4. Save VEO_PROMPTS.md to this folder
5. Give you ready-to-paste Veo prompts

## Script Format (paste directly in chat)

```
Scene 1: Title Here
Image Prompt: [describe the scene]
Motion: [describe the motion]
Character Name 1: "Hindi dialogue"
Character Name 2: "Hindi dialogue"

Scene 2: Title Here
...
```

## Options you can specify
- Tone: Funny Swag / Villain Swag / Savage / Emotional / Cute
- Duration: 8s / 16s / 24s
- Speakers: auto-detected from character names

## Output
Saved to: Scripts/ObjectAi/[TopicName]_VEO_PROMPTS.md
Each scene has a ready-to-copy Veo prompt block.
