# Google Flow — Image Download Reference

## Method 1: Direct GCS URL (Fastest, Recommended)

1. **Get the media ID from the image page URL:**
   ```
   https://labs.google/fx/tools/flow/project/[PROJECT-ID]/edit/[MEDIA-ID]
   ```
   Example: `5c038843-d533-4608-9e5c-1d998c7f25e1`

2. **Build the GCS URL:**
   ```
   https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=[MEDIA-ID]
   ```

3. **Navigate Playwright to that URL** — it redirects to Google Cloud Storage signed URL

4. **Extract the GCS URL** from the redirected page:
   ```js
   const imgSrc = await page.$$eval('img', imgs => imgs[0]?.src);
   // Returns: https://storage.googleapis.com/ai-sandbox-videofx/[MEDIA-ID]?GoogleAccessId=...&Expires=...&Signature=...
   ```

5. **Download via curl:**
   ```bash
   curl -L --ssl-no-revoke "[GCS_URL]" -o "path/to/hero.png"
   ```

---

## Method 2: Playwright Screenshot (Fallback)

If curl fails or authentication issues:

```js
// Navigate to image edit page
await page.goto('https://labs.google/fx/tools/flow/project/[PROJECT-ID]/edit/[MEDIA-ID]');

// Take full-page screenshot (captures the image)
await page.screenshot({
  path: 'path/to/hero.png',
  scale: 'css',
  type: 'png'
});
```

**Note:** This captures the viewport, not the original resolution. Use only when Method 1 fails.

---

## Method 3: Download Button (Manual)

1. Click the **Download** button in the Flow UI
2. Playwright may auto-download to `.playwright-mcp/` folder
3. Move file manually:
   ```bash
   mv ".playwright-mcp/[filename].png" "path/to/hero.png"
   ```

---

## Selectors Reference

| Element | Selector |
|---------|----------|
| Download button | `button:has-text("Download")` or `button:has-text("download")` |
| Generated image | `img[src*="google"]` with width > 500 |
| Media redirect URL | `/api/trpc/media.getMediaUrlRedirect?name=[MEDIA-ID]` |

---

## Common Issues

**Issue:** curl SSL error (`CRYPT_E_NO_REVOCATION_CHECK`)
**Fix:** Add `--ssl-no-revoke` flag

**Issue:** Redirect URL expires
**Fix:** Re-navigate to the media redirect URL to get fresh GCS signed URL

**Issue:** Image is 1200×896 instead of 1080×1350
**Fix:** This is Flow's default output. The image was generated at 4:5 but saved at a different resolution. Consider upscaling or re-generating with explicit size settings.

---

## Quick Download Snippet (Playwright + curl)

```js
// Get media ID from current URL
const url = page.url(); // https://labs.google/fx/tools/flow/project/.../edit/[MEDIA-ID]
const mediaId = url.split('/edit/')[1];

// Build redirect URL
const redirectUrl = `https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=${mediaId}`;

// Navigate to get GCS URL
await page.goto(redirectUrl);
await page.waitForTimeout(2000);

// Extract GCS URL
const gcsUrl = await page.$$eval('img', imgs => imgs[0]?.src);
console.log('GCS URL:', gcsUrl);
```

Then run curl externally:
```bash
curl -L --ssl-no-revoke "[GCS_URL]" -o "path/to/image.png"
```
