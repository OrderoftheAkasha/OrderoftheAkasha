# akashicmonk.blog — Official Artist Site

Single-file artist site (`index.html` + `assets/`). No build step — open `index.html` in a browser to preview.

## What's on it
- Scrolling announcement ticker + **American Blueprint** album section with live countdown and fan sign-up
- Full-screen hero with the "08" music video playing in the background (muted, with sound toggle)
- Latest album (Static Signal) with an Apple Music player
- Music video player + queue, Behind the Scenes / Interviews / 100-Day Marathon tabs, Vlog rail
- Full discography (41 releases, auto-pulled artwork from Apple Music)
- Order of the Akasha section with concept art
- Listen hub (Spotify, Apple Music, YouTube, YouTube Music, SoundCloud, Amazon, Deezer, Tidal, Genius)
- Socials (Instagram, TikTok, X, Facebook, Discord, YouTube) and booking/press contact

## Editing
Everything lives in the `CONFIG`, `MUSIC_VIDEOS`, `TABS`, `VLOGS` and `RELEASES` blocks at the top of the `<script>` in `index.html`.
- **Spotify:** replace `CONFIG.spotify` with your exact artist link (Spotify for Artists → Profile → Share → Copy link).
- **Album date:** change `CONFIG.albumRelease` when the release date is locked.
- **New video:** add `{id:"YOUTUBE_ID", t:"Title", tag:"Official Video"}` to the top of `MUSIC_VIDEOS`.

## Putting it live on akashicmonk.blog
The current site is on Hostinger's AI Website Builder, which doesn't accept uploaded HTML. Options:
1. **Hostinger Web Hosting** (hPanel → File Manager → `public_html`): upload `index.html` and the `assets/` folder.
2. **GitHub Pages / Netlify / Vercel (free):** deploy this `website/` folder, then point the akashicmonk.blog DNS at it from Hostinger → Domains → DNS.
