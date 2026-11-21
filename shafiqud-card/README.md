# Digital business card: shafiqud.doulah.com

A redesigned version of the QR-code landing page for **A. B. M. Shafiqud Doulah, Partner, Doulah & Doulah**.
Upload the contents of this folder (except `tools/` and this README) to the web root of `shafiqud.doulah.com`, replacing the old files.

## What was wrong with the current page (review of 21 Nov 2026)

| # | Issue | Impact |
|---|-------|--------|
| 1 | **No WhatsApp** at all | The most common way Bangladeshi and international clients reach someone. |
| 2 | **WeChat is plain text only** (`💬 WeChat: +880 1911 930955`) | Nothing to tap or scan. Chinese clients have to retype the number. |
| 3 | Phone, email and website in the contact list **can't be tapped** | People have to copy text by hand on a page made for phones. |
| 4 | **`photo.jpg` is 1.18 MB, 3771×3735 px** (straight from a Canon camera) | Slow to open after scanning, especially on mobile data. Displayed at only 180 px. |
| 5 | QR image loaded from **`api.qrserver.com` at 1000×1000** | Extra third-party request, slower, and breaks if that service is down or blocked (e.g. in China). |
| 6 | The QR code sits in the middle of the page with no label | Visitors who just scanned it don't know why it's there. It only helps if you explain that it's for sharing. |
| 7 | No `alt` text on the logo or photo, no `lang` attribute | Accessibility and SEO. |
| 8 | No meta description, **no Open Graph tags**, no favicon | Shared on WhatsApp, WeChat or LinkedIn, the link shows no photo or title. |
| 9 | Address is not linked to a map | Visitors can't get directions. |
| 10 | vCard: no photo, no WhatsApp, address abbreviated ("BL A, Sec 12") | The saved contact looks incomplete. |
| 11 | Unused CSS (`.qr`), empty decorative header/footer bars, logo and firm name repeated | Minor clean-up. |

## What the new version does

- **Four one-tap buttons:** Call · WhatsApp · WeChat · Email.
  - WhatsApp opens a chat via `wa.me` with a polite greeting already filled in.
  - WeChat opens a panel with the WeChat QR code, the number, **Copy number** and **Open WeChat** buttons. A web link can't add a WeChat contact directly; this is the standard workaround.
  - Email opens with the subject "Enquiry via business card".
- **Save to Contacts** downloads an improved vCard (`Shafiqud_Doulah.vcf`) with the **photo embedded** plus mobile, WeChat line, email, website, LinkedIn, WhatsApp and the full address.
- **Every contact row is tappable.** The address opens Google Maps.
- **Share this card:** a self-hosted QR (`site-qr.svg`) so someone can scan it from your screen, and a **Share link** button that uses the phone's native share sheet.
- **Fast:** photo cut from 1.18 MB to about 18 KB. No external fonts, scripts or APIs, so it also loads inside China and inside the WeChat browser.
- **Link previews** (Open Graph) with photo and title, plus favicon and home-screen icon.
- Accessible: alt text, `lang`, visible focus outlines, honours reduced motion. WeChat label also shown as 微信.

## ⚠️ Two things to confirm or provide

1. **WhatsApp number.** I used the main mobile, **+880 1755 559884**. If WhatsApp is on a different number, change `wa.me/8801755559884` (2 places) and the visible number in `index.html`, and `WHATSAPP` in `tools/build_assets.py`.
2. **WeChat QR image.** In WeChat go to *Me → tap your name → My QR Code → ⋯ → Save Image*. Crop it to a square, name it **`wechat-qr.png`** and upload it next to `index.html`. Until then the WeChat panel just shows the number with copy and open buttons. The QR block hides itself automatically.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The card (single file, no dependencies) |
| `photo.jpg` | Optimised portrait, 480×480 |
| `logo.png`, `favicon.png`, `apple-touch-icon.png` | Logo and icons |
| `site-qr.svg` | QR code → https://shafiqud.doulah.com |
| `Shafiqud_Doulah.vcf` | Contact file with embedded photo |
| `wechat-qr.png` | **You add this** (see above) |
| `tools/build_assets.py` | Rebuilds photo, icons, QR and vCard from the originals (`pip install pillow segno`) |

## Tips for the printed card

- Print the QR at least **2 cm × 2 cm** with a white margin around it, and put a short label under it such as "Scan to save my contact".
- Keep the QR pointing at `https://shafiqud.doulah.com`. Then you can change the page later without reprinting cards.
- Optionally add a second small QR on the back for the WeChat code, for Chinese clients.
