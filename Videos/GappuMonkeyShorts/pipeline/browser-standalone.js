const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const TARGET = process.argv[2] || 'help';
const ACTION = process.argv[3] || 'login';

const userDataDir = path.join(__dirname, '.browser_profile');
const authFile = path.join(__dirname, 'browser_auth.json');

const URLS = {
  higgsfield: {
    image: 'https://higgsfield.ai/image/nano-banana-pro',
    video: 'https://higgsfield.ai/create/video',
    assets: 'https://higgsfield.ai/asset/all',
    videoAssets: 'https://higgsfield.ai/asset/video'
  },
  flow: {
    image: 'https://labs.google/fx/tools/flow',
    assets: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect'
  }
};

async function saveAuth(context) {
  const storage = await context.storageState();
  fs.writeFileSync(authFile, JSON.stringify(storage, null, 2));
  console.log('[AUTH] Saved to:', authFile);
}

async function login(target) {
  console.log('========================================');
  console.log(`BROWSER LOGIN - ${target.toUpperCase()}`);
  console.log('========================================');

  const context = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled', '--start-maximized', '--no-sandbox']
  });

  const page = await context.newPage();
  await page.goto(URLS[target].image, { waitUntil: 'networkidle', timeout: 60000 });

  console.log('');
  console.log('Login page loaded.');
  console.log('Complete login manually, then press Ctrl+C when done.');
  console.log('');

  try {
    await new Promise(() => {});
  } catch (e) {
    await saveAuth(context);
    await context.close();
    console.log('Done! Auth saved. Close this window and run your pipeline.');
  }
}

async function generateImage(prompt, outputFile) {
  const context = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled']
  });

  const page = await context.newPage();
  await page.goto(URLS.higgsfield.image, { waitUntil: 'networkidle' });

  // Clear prompt
  await page.focus('[id="hf:tour-image-prompt"]');
  await page.keyboard.press('Control+A');
  await page.keyboard.press('Delete');

  // Type prompt
  await page.fill('[id="hf:tour-image-prompt"]', prompt);

  // Generate
  const buttons = await page.$$('button');
  const genButton = buttons.find(b => b.textContent().includes('Generate') || b.textContent().includes('arrow_forward'));
  if (genButton) await genButton.click();

  // Wait for completion
  await page.waitForSelector(':has-text("Queued")', { state: 'detached', timeout: 60000 });
  await page.waitForSelector(':has-text("Generating")', { state: 'detached', timeout: 120000 });
  await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 });

  // Get image URL
  const imgSrc = await page.$eval('img[src*="higgsfield"]', el => el.src);
  console.log('Image URL:', imgSrc);

  // Download
  await page.goto(imgSrc);
  await page.waitForTimeout(2000);

  // Screenshot as fallback
  await page.screenshot({ path: outputFile, type: 'png' });
  console.log('Saved:', outputFile);

  await context.close();
}

async function main() {
  if (TARGET === 'help') {
    console.log('Usage:');
    console.log('  node browser-standalone.js higgsfield login');
    console.log('  node browser-standalone.js higgsfield generate --prompt="..." --output=scene_01.png');
    console.log('  node browser-standalone.js flow login');
    return;
  }

  if (ACTION === 'login') {
    await login(TARGET);
  } else if (ACTION === 'generate') {
    const promptArg = process.argv.find(a => a.startsWith('--prompt='));
    const outputArg = process.argv.find(a => a.startsWith('--output='));
    const prompt = promptArg ? promptArg.split('=')[1].replace(/"/g, '') : '';
    const output = outputArg ? outputArg.split('=')[1] : 'output.png';
    await generateImage(prompt, output);
  }
}

main().catch(err => { console.error(err); process.exit(1); });
