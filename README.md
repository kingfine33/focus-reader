# Focus Reader — GitHub Pages build

This folder is ready to publish as a GitHub Pages static site.

## Publish

1. Create a GitHub repository, for example `focus-reader`.
2. Upload **all files in this folder** to the repository root.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select the `main` branch and `/ (root)`, then save.
6. GitHub will publish the reader at a URL similar to:
   `https://YOUR-USERNAME.github.io/focus-reader/`

`index.html` must stay at the repository root. `.nojekyll` tells GitHub Pages to serve this as a plain static site.

## Put it on iPhone

### Direct web-app method
Open the GitHub Pages URL in Safari, use **Share → Add to Home Screen**, and enable **Open as Web App** if offered.

### Apple Shortcut method
Create a Shortcut with:

1. **URL** — paste the GitHub Pages URL.
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

The reader currently loads PDF.js 3.11.174 from cdnjs when the page opens. The PDFs you choose are read locally in the browser; they are not uploaded by this page.
