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

## Putting it live on akashicmonk.blog (GitHub Pages)
The site publishes automatically via `.github/workflows/pages.yml` whenever `website/` changes on the default branch. `website/CNAME` tells GitHub Pages to serve it at akashicmonk.blog.

One-time setup:
1. Merge the pull request.
2. GitHub repo → **Settings → Pages → Source: GitHub Actions**. Under **Custom domain** enter `akashicmonk.blog`.
3. Hostinger → **Domains → akashicmonk.blog → DNS / Nameservers**. Disconnect the domain from the Website Builder, then set:

| Type  | Name | Points to                  |
|-------|------|----------------------------|
| A     | @    | 185.199.108.153            |
| A     | @    | 185.199.109.153            |
| A     | @    | 185.199.110.153            |
| A     | @    | 185.199.111.153            |
| AAAA  | @    | 2606:50c0:8000::153        |
| AAAA  | @    | 2606:50c0:8001::153        |
| AAAA  | @    | 2606:50c0:8002::153        |
| AAAA  | @    | 2606:50c0:8003::153        |
| CNAME | www  | orderoftheakasha.github.io |

   Delete any other existing A / AAAA / ALIAS records on `@` (the old Hostinger builder ones).
4. After DNS updates (minutes to a few hours), tick **Enforce HTTPS** in Settings → Pages.
