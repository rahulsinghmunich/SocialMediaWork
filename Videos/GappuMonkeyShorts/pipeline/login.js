const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const MODE = process.argv[2] || 'auto';
const userDataDir = path.join(__dirname, '.gappu_profile');
const authFile = path.join(__dirname, 'gappu_auth.json');

async function checkProcesses() {
  try {
    const chrome = execSync('tasklist /FI "IMAGENAME eq chrome.exe"').toString();
    const node = execSync('tasklist /FI "IMAGENAME eq node.exe"').toString();
    if ((chrome.match(/chrome.exe/gi) || []).length > 1) {
      console.warn('[WARN] Multiple Chrome processes. Close other Chrome windows.');
    }
    if ((node.match(/node.exe/gi) || []).length > 1) {
      console.warn('[WARN] Multiple Node processes. Close other Node instances.');
    }
  } catch (e) {}
}

async function launchBrowser() {
  return chromium.launchPersistentContext(userDataDir, {
    headless: false,
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled', '--no-sandbox', '--start-maximized'],
    viewport: { width: 1920, height: 1080 }
  });
}

async function saveAuth(context) {
  const storage = await context.storageState();
  fs.writeFileSync(authFile, JSON.stringify(storage, null, 2));
  console.log('Auth saved:', authFile);
}

async function main() {
  console.log('========================================');
  console.log('GAPPU LOGIN - Modes: handshake | auto | save');
  console.log('========================================');

  checkProcesses();
  const context = await launchBrowser();
  const page = await context.newPage();

  console.log('Navigating to Higgsfield...');
  await page.goto('https://higgsfield.ai/image/nano-banana-pro', { waitUntil: 'networkidle', timeout: 60000 });

  if (MODE === 'handshake') {
    console.log('');
    console.log('--- MANUAL LOGIN ---');
    console.log('Log in, then press Ctrl+C when ready.');
    await new Promise(() => {});
  } else if (MODE === 'auto') {
    console.log('');
    console.log('--- MANUAL LOGIN ---');
    console.log('90s timeout, then auto-save...');
    for (let i = 10; i <= 90; i += 10) {
      await page.waitForTimeout(10000);
      console.log(`  ...${i}s`);
    }
    await page.screenshot({ path: path.join(__dirname, 'auth_verification.png') });
    await saveAuth(context);
    console.log('Done!');
  } else if (MODE === 'save') {
    await page.waitForTimeout(3000);
    await page.screenshot({ path: path.join(__dirname, 'auth_verification.png') });
    await saveAuth(context);
    console.log('Done!');
  } else {
    console.log('Unknown mode. Use: handshake | auto | save');
  }

  await context.close();
}

main().catch(err => { console.error(err); process.exit(1); });
