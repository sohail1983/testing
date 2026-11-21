"""Build optimised assets for the digital business card.

Usage:  python3 tools/build_assets.py <original-photo.jpg> <original-logo.jpg>
Needs:  pip install pillow segno
Outputs (in the card folder): photo.jpg, logo.png, apple-touch-icon.png,
favicon.png, site-qr.svg, Shafiqud_Doulah.vcf
"""
import base64, io, sys
from pathlib import Path
from PIL import Image, ImageOps
import segno

OUT = Path(__file__).resolve().parent.parent
SITE = "https://shafiqud.doulah.com"

# ---- contact data (edit here, then re-run) --------------------------------
MOBILE   = "+8801755559884"   # main mobile / Call button
WHATSAPP = "+8801755559884"   # WhatsApp number
WECHAT   = "+8801911930955"   # WeChat (also a phone line)
EMAIL    = "shdoulah@doulah.com"
# ---------------------------------------------------------------------------

photo_src, logo_src = Path(sys.argv[1]), Path(sys.argv[2])

# 1. Photo: square-crop, 480px (sharp on 2x screens at 160px), ~40 KB
img = ImageOps.exif_transpose(Image.open(photo_src)).convert("RGB")
img = ImageOps.fit(img, (480, 480), Image.LANCZOS, centering=(0.5, 0.42))
img.save(OUT / "photo.jpg", "JPEG", quality=82, optimize=True, progressive=True)

# 2. Logo + icons
logo = Image.open(logo_src).convert("RGB")
logo.resize((240, 240), Image.LANCZOS).save(OUT / "logo.png", optimize=True)
logo.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png", optimize=True)
logo.resize((64, 64), Image.LANCZOS).save(OUT / "favicon.png", optimize=True)

# 3. QR code for the card itself (self-hosted, no third-party API)
segno.make(SITE, error="m").save(OUT / "site-qr.svg", scale=10, border=2,
                                 dark="#1a1a1a", light=None)

# 4. vCard 3.0 with embedded photo so the saved contact has a picture
thumb = img.resize((240, 240), Image.LANCZOS)
buf = io.BytesIO(); thumb.save(buf, "JPEG", quality=80)
b64 = base64.b64encode(buf.getvalue()).decode()

def fold(line):  # RFC 2425: fold at 75 octets, continuation starts with a space
    out = [line[:75]]; line = line[75:]
    while line:
        out.append(" " + line[:74]); line = line[74:]
    return "\r\n".join(out)

wa = WHATSAPP.lstrip("+")
lines = [
    "BEGIN:VCARD", "VERSION:3.0",
    "N:Doulah;A. B. M. Shafiqud;;;",
    "FN:A. B. M. Shafiqud Doulah",
    "ORG:Doulah & Doulah",
    "TITLE:Partner",
    f"TEL;TYPE=CELL,VOICE,PREF:{MOBILE}",
    f"TEL;TYPE=WORK,VOICE:{WECHAT}",
    f"EMAIL;TYPE=INTERNET,WORK,PREF:{EMAIL}",
    "URL;TYPE=WORK:https://www.doulah.com",
    f"URL:{SITE}",
    "ADR;TYPE=WORK:;;Plot 153/2\\, Road 2/2\\, Block A\\, Section 12\\, Mirpur\\, Pallabi;Dhaka;;1216;Bangladesh",
    "X-SOCIALPROFILE;TYPE=linkedin:https://www.linkedin.com/in/shafiquddoulah/",
    f"X-SOCIALPROFILE;TYPE=whatsapp:https://wa.me/{wa}",
    f"IMPP;X-SERVICE-TYPE=WhatsApp:x-apple:{WHATSAPP}",
    f"X-WECHAT:{WECHAT}",
    f"NOTE:Corporate Advisory\\, Regulatory Compliance and Company Secretarial Service.\\nWhatsApp: {WHATSAPP}\\nWeChat: {WECHAT}",
    f"PHOTO;ENCODING=b;TYPE=JPEG:{b64}",
    "END:VCARD",
]
(OUT / "Shafiqud_Doulah.vcf").write_bytes(("\r\n".join(fold(l) for l in lines) + "\r\n").encode())
print("done")
