# Standalone Browser Automation (No MCP Extension)

**For:** Local LLM setups where Playwright MCP extension doesn't work

**Use:** `node browser-standalone.js [higgsfield|flow] [action]`

---

## Quick Commands

```bash
# Login (saves session)
node browser-standalone.js higgsfield login
node browser-standalone.js flow login

# Generate image
node browser-standalone.js higgsfield generate --prompt "Pixar 3D monkey..." --output scene_01.png

# Generate video
node browser-standalone.js higgsfield video --input scene_01.png --motion "slow push in, then holds" --output scene_01.mp4

# Check status
node browser-standalone.js higgsfield status
```

---

## Script: `browser-standalone.js`

```javascript
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const MODE = process.argv[2] || 'help';
const ACTION = process.argv[3] || 'login';
const TARGET = process.argv[4] || 'higgsfield';

const userDataDir = path.join(__dirname, '.browser_profile');
const outputDir = process.argv[5] || '.';

const URLS = {
  higgsfield: {
    image: 'https://higgsfield.ai/image/nano-banana-pro',
    video: 'https://higgsfield.ai/create/video',
    assets: 'https://higgsfield.ai/asset/all'
  },
  flow: {
    image: 'https://labs.google/fx/tools/flow',
    assets: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect'
  }
};

async function main() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled', '--start-maximized']
  });
  const page = await context.newPage();

  if (ACTION === 'login') {
    await page.goto(URLS[TARGET].image, { waitUntil: 'networkidle' });
    console.log('Login page loaded. Complete login manually, then press Ctrl+C.');
    await new Promise(() => {});
  }

  if (ACTION === 'generate') {
    const prompt = process.argv.find(a => a.startsWith('--prompt='))?.split('=')[1] || '';
    await page.goto(URLS[TARGET].image);
    await page.fill('[id="hf:tour-image-prompt"]', prompt);
    await page.click('button:has-text("Generate")');
    await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 });
    const imgSrc = await page.$eval('img[src*="higgsfield"]', el => el.src);
    await page.goto(imgSrc);
    await page.screenshot({ path: path.join(outputDir, 'output.png') });
    console.log('Saved:', path.join(outputDir, 'output.png'));
  }

  await context.close();
}

main().catch(console.error);
```

---

## Integration with Pipeline Rules

Replace MCP browser calls with:

```bash
# Instead of: mcp__playwright__browser_navigate
# Use: node browser-standalone.js [target] [action]

# Pipeline integration example:
node browser-standalone.js higgsfield login
# → User logs in manually
node browser-standalone.js higgsfield generate --prompt "[IMAGE_PROMPT]" --output images/scene_01.png
```

---

## Token Savings

| Approach | Tokens | Notes |
|----------|--------|-------|
| MCP Extension | ~50/turn | Requires MCP setup, doesn't work with local LLM |
| Standalone Script | ~0 | Pure Bash call, no MCP overhead |

---

## Hard Rules

- Run login once per session
- Script handles DOM waits internally
- Output goes to specified folder
- No screenshot polling — DOM waits only
- Auth persisted in `.browser_profile/`
