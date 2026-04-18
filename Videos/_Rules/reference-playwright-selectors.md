# Reference: Playwright Selectors for Google Flow

**Shared across:** ObjectAi pipeline, Gappu pipeline, Bhakti pipeline, all carousel pipelines

**Local LLM users:** See `browser-automation-standalone.md` for standalone script that doesn't require MCP extension.

---

## Core Selectors (Google Flow)

```javascript
// Navigation
URL: https://labs.google/fx/tools/flow

// Project creation
New project: btns.find(b => b.textContent.includes('New project')).click()

// Tab selection
Image tab: tab with text 'Image' or 'imageImage'
Video tab: tab with text 'Video' or 'videocamVideo'
Frames mode: tab with text 'Frames' or 'crop_freeFrames'

// Settings
9:16 ratio: tab with text '9:16'
4:5 ratio: tab with text '4:5'
x1 quantity: tab with text 'x1'

// Generation
Prompt box: textbox[placeholder*="What do you want to create?"]
Generate: btns.find(b => b.textContent.includes('arrow_forwardCreate')).click()

// File upload
File input: document.querySelector('input[type="file"]').click()

// Wait for completion
Image: await page.waitForSelector('[data-testid="generated-image"]', { timeout: 120000 })
Video: await page.waitForSelector('[data-testid="generated-video"]', { timeout: 180000 })

// Download
Video src: document.querySelector('video').src
// → Navigate to that URL → redirects to GCS signed URL
// → Download: curl -L --ssl-no-revoke "[GCS_URL]" -o "path/to/output.mp4"
```

**Helper:** `btns = Array.from(document.querySelectorAll('button'))`

---

## Download Methods

### Method 1: Direct GCS URL (Recommended)

1. Get media ID from URL: `https://labs.google/fx/tools/flow/project/[PROJECT-ID]/edit/[MEDIA-ID]`
2. Build redirect URL: `https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=[MEDIA-ID]`
3. Navigate to redirect URL
4. Extract GCS URL: `const gcsUrl = await page.$$eval('img', imgs => imgs[0]?.src)`
5. Download: `curl -L --ssl-no-revoke "[GCS_URL]" -o "path/to/output.png"`

### Method 2: Playwright Screenshot (Fallback)

```javascript
await page.screenshot({
  path: 'path/to/output.png',
  scale: 'css',
  type: 'png'
});
```

### Method 3: Download Button (Manual)

1. Click Download button: `button:has-text("Download")` or `button:has-text("download")`
2. Check `.playwright-mcp/` folder for downloaded file
3. Move to target location

---

## Common Issues

| Issue | Fix |
|-------|-----|
| SSL error `CRYPT_E_NO_REVOCATION_CHECK` | Add `--ssl-no-revoke` to curl |
| Redirect URL expires | Re-navigate to get fresh GCS signed URL |
| Image wrong resolution (1200×896 vs 1080×1350) | This is Flow's default output — upscale or regenerate with explicit size |
| Download button not working | Use Method 1 (GCS URL extraction) |

---

## Usage in Pipeline Rules

Instead of duplicating selectors in every pipeline file, reference this file:

```markdown
**Selectors Reference:** See `D:\oldCOMPUTER\Videos\_Rules\reference-playwright-selectors.md`
```

This saves ~40 lines per pipeline file while maintaining full functionality.
