# contact-card

Business-card contact pages for Sembuh AI, served by the Cloudflare Worker `contact-card`.

| Person | Page |
| --- | --- |
| David Jendra, COO & Co-Founder | `public/david/index.html` → `/david` |
| Indi Bintang, Commercial Lead | `public/indi/index.html` → `/indi` |

`/` redirects to www.codemasters.id. Unknown paths show `public/404.html`.

## Deploy
The Worker is connected to this repo (Cloudflare → Workers & Pages → contact-card → Settings → Build).
Every push to `main` redeploys automatically. Config is in `wrangler.jsonc`.

## Add or edit a person
- Edit: change the text in `public/<name>/index.html` and push. The QR keeps working because the path stays the same.
- Add: copy a folder, e.g. `public/david` → `public/budi`, edit it, push, then make a QR (below).

## QR codes
```
pip install segno
python tools/make_qr.py https://<your-domain>/david
```
Use the SVG for print, at least 2.5 cm wide, with the white margin kept.
Never rename a path (`/david`, `/indi`) or change the domain after cards are printed.
