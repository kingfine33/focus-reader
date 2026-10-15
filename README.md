# Focus Reader — GitHub Pages build

This repository hosts the mobile Focus Reader as a static GitHub Pages site.

## Publish

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the `main` branch and `/ (root)`, then save.
4. GitHub will publish the reader at:
   `https://kingfine33.github.io/focus-reader/`

`index.html` stays at the repository root. `.nojekyll` tells GitHub Pages to serve this as a plain static site.

## Put it on iPhone

### Direct web-app method
Open the GitHub Pages URL in Safari, use **Share → Add to Home Screen**, and enable **Open as Web App** if offered.

### Apple Shortcut method
Create a Shortcut with:

1. **URL** — `https://kingfine33.github.io/focus-reader/`
2. **Open URLs**.
3. Rename the Shortcut to **Focus Reader** and add it to the Home Screen.

## Reader behavior retained

- PDF picker from Files
- Focus line / paragraph isolation
- Previous / next controls and vertical swipe navigation
- Word outliner
- Auto reading with WPM timing
- Flow continuity across line breaks
- Adaptive letter-spacing vs word-spacing detection
- Strict active-line boundary to avoid hidden-line word detection
- Page and zoom controls
- Persistent reader preferences
- Screen Wake Lock while Auto is running when supported

## Network note

The reader loads PDF.js 3.11.174 from cdnjs when the page opens. PDFs you choose are read locally in the browser; this page does not upload them.
