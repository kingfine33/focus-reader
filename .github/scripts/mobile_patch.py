from pathlib import Path
import json

ROOT = Path('.')
reader = ROOT / 'reader.html'
index = ROOT / 'index.html'
version = ROOT / 'version.json'

s = reader.read_text(encoding='utf-8')

def repl(old, new, label):
    global s
    if old not in s:
        raise SystemExit(f'missing reader pattern: {label}')
    s = s.replace(old, new)

repl("const RENDER_QUALITY = Math.max(3, Math.min(3.5, (window.devicePixelRatio || 1) * 1.5));",
     "const PHONE_MEDIA = '(max-width:720px), (max-height:500px) and (pointer:coarse)';\nconst PHONE_RENDER_QUALITY = Math.min(2, Math.max(1.6, (window.devicePixelRatio || 1) * .67));\nconst RENDER_QUALITY = (window.matchMedia && window.matchMedia(PHONE_MEDIA).matches) ? PHONE_RENDER_QUALITY : Math.max(3, Math.min(3.5, (window.devicePixelRatio || 1) * 1.5));",
     'render quality')
repl("const isPhoneUI=()=>window.matchMedia && window.matchMedia('(max-width:720px)').matches;",
     "const isPhoneUI=()=>window.matchMedia && window.matchMedia(PHONE_MEDIA).matches;",
     'phone media JS')
repl("@media(max-width:720px){", "@media(max-width:720px), (max-height:500px) and (pointer:coarse){", 'phone media CSS')
repl(".mobileTopActions button{min-height:38px;", ".mobileTopActions button{min-height:44px;", 'top hit target')
repl("min-height:42px!important", "min-height:44px!important", 'done hit target')
repl("padding:calc(7px + env(safe-area-inset-top)) 10px 7px;gap:8px;",
     "padding-top:calc(7px + env(safe-area-inset-top));padding-bottom:7px;padding-left:calc(10px + env(safe-area-inset-left));padding-right:calc(10px + env(safe-area-inset-right));gap:8px;",
     'header safe area')
repl(".toolbar{display:none;position:fixed;left:10px;right:10px;bottom:",
     ".toolbar{display:none;position:fixed;left:calc(10px + env(safe-area-inset-left));right:calc(10px + env(safe-area-inset-right));bottom:",
     'toolbar safe area')
repl(".normalWrap{padding:14px 12px calc(112px + env(safe-area-inset-bottom));",
     ".normalWrap{padding-top:14px;padding-bottom:calc(112px + env(safe-area-inset-bottom));padding-left:calc(12px + env(safe-area-inset-left));padding-right:calc(12px + env(safe-area-inset-right));",
     'normal safe area')
repl(".focusWrap{padding:8px 33px calc(116px + env(safe-area-inset-bottom)) 10px;",
     ".focusWrap{padding-top:8px;padding-bottom:calc(116px + env(safe-area-inset-bottom));padding-left:calc(10px + env(safe-area-inset-left));padding-right:calc(33px + env(safe-area-inset-right));",
     'focus safe area')
repl(".railPanel{right:2px;", ".railPanel{right:calc(2px + env(safe-area-inset-right));", 'rail safe area')
repl(".readout{left:10px;right:10px;", ".readout{left:calc(10px + env(safe-area-inset-left));right:calc(10px + env(safe-area-inset-right));", 'readout safe area')
repl(".mobileDock{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:7px;position:fixed;left:8px;right:8px;",
     ".mobileDock{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:7px;position:fixed;left:calc(8px + env(safe-area-inset-left));right:calc(8px + env(safe-area-inset-right));",
     'dock safe area')
repl(".flowStack{gap:8px}", ".flowStack{gap:8px;align-items:flex-start}\n    .cropCard.textUnit.paragraphMode,.cropCard.visualUnit{align-self:center}", 'line left alignment')
repl(".focusWrap{padding-left:7px;padding-right:27px}",
     ".focusWrap{padding-left:calc(7px + env(safe-area-inset-left));padding-right:calc(27px + env(safe-area-inset-right))}",
     'small phone safe area')
repl("@media(max-width:720px) and (orientation:landscape){",
     "@media (max-height:500px) and (orientation:landscape) and (pointer:coarse){",
     'landscape phone media')
repl(".mobileDock{left:auto;width:300px;right:8px;",
     ".mobileDock{left:auto;width:300px;right:calc(8px + env(safe-area-inset-right));",
     'landscape dock')
repl(".readout{right:316px;left:8px;",
     ".readout{right:calc(316px + env(safe-area-inset-right));left:calc(8px + env(safe-area-inset-left));",
     'landscape readout')
repl(".toolbar{bottom:calc(62px + env(safe-area-inset-bottom));left:auto;width:min(430px,94vw)}",
     ".toolbar{bottom:calc(62px + env(safe-area-inset-bottom));left:auto;right:calc(10px + env(safe-area-inset-right));width:min(430px,calc(94vw - env(safe-area-inset-left) - env(safe-area-inset-right)))}",
     'landscape toolbar')
repl("dst.getContext('2d',{alpha:false}).drawImage(src,0,0); dst.style.width='min('+Math.round(pageState.displayWidth||src.width)+'px, calc(100vw - 150px))'; dst.style.height='auto';",
     "dst.getContext('2d',{alpha:false}).drawImage(src,0,0); const phoneMax=isPhoneUI()?'calc(100vw - 24px - env(safe-area-inset-left) - env(safe-area-inset-right))':'calc(100vw - 150px)'; dst.style.width='min('+Math.round(pageState.displayWidth||src.width)+'px, '+phoneMax+')'; dst.style.height='auto';",
     'normal page phone width')
repl("if(cache.size>4){ const first=cache.keys().next().value; cache.delete(first); }",
     "const cacheLimit=isPhoneUI()?2:4;\n  if(cache.size>cacheLimit){ const first=cache.keys().next().value; cache.delete(first); }",
     'phone cache limit')
repl("if(n<pdfDoc.numPages) preparePage(n+1).catch(()=>{});\n  if(n>1) preparePage(n-1).catch(()=>{});",
     "if(isPhoneUI()){\n    const warm=n+(direction<0?-1:1);\n    if(warm>=1&&warm<=pdfDoc.numPages) preparePage(warm).catch(()=>{});\n  }else{\n    if(n<pdfDoc.numPages) preparePage(n+1).catch(()=>{});\n    if(n>1) preparePage(n-1).catch(()=>{});\n  }",
     'phone warm cache')
repl("window.matchMedia?.('(max-width:720px)').addEventListener?.('change',()=>setMobileSheet(false));",
     "window.matchMedia?.(PHONE_MEDIA).addEventListener?.('change',()=>setMobileSheet(false));",
     'media listener')
reader.write_text(s, encoding='utf-8')

# Small launcher hardening for touch + future launcher refreshes.
i = index.read_text(encoding='utf-8')
i = i.replace('#readerFrame{position:fixed;inset:0;width:100%;height:100%;', '#readerFrame{position:fixed;inset:0;width:100%;height:100dvh;')
i = i.replace('#updateBanner button{border:0;', '#updateBanner button{min-height:44px;border:0;')
i = i.replace('<iframe id="readerFrame" title="Focus Reader"></iframe>', '<iframe id="readerFrame" title="Focus Reader" allow="screen-wake-lock"></iframe>')
old_apply = "function applyUpdate(meta=pendingMeta){\n    if(!meta||!meta.version)return;\n    hideBanner();\n    currentVersion=String(meta.version);\n    window.FOCUS_READER_VERSION=currentVersion;\n    bootEl.textContent='Updating Focus Reader…';\n    bootEl.classList.remove('hide');\n    frame.src=versionedReaderUrl(currentVersion)+'&refresh='+Date.now();\n  }"
new_apply = "function applyUpdate(meta=pendingMeta){\n    if(!meta||!meta.version)return;\n    hideBanner();\n    const next=String(meta.version);\n    // Reload the launcher itself with a versioned URL so Safari/Home Screen cannot keep an old shell.\n    const u=new URL(location.href);\n    u.searchParams.set('v',next);\n    u.searchParams.set('refresh',Date.now());\n    location.replace(u.href);\n  }"
if old_apply not in i:
    raise SystemExit('missing index applyUpdate pattern')
i = i.replace(old_apply, new_apply)
index.write_text(i, encoding='utf-8')

version.write_text(json.dumps({
    'version':'2026.10.15.2',
    'released_at':'2026-10-15T22:55:00Z',
    'notes':'Mobile compatibility pass: landscape phone mode, safe areas, larger touch targets, full-width page view, reachable moving-line start, lower memory rendering, and launcher cache refresh.'
}, indent=2)+'\n', encoding='utf-8')
