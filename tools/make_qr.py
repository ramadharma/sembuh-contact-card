"""
Generate the business-card QR code for David Jendra's contact page.

Usage:
    pip install segno
    python make_qr.py                                  # default URL below
    python make_qr.py https://www.codemasters.id/david  # any other final URL

Outputs (next to this script, rename them per person):
    qr-contact-page.svg   vector, use this for print
    qr-contact-page.png   2000 x 2000 px, for previews / tools that need raster

Print guidance: keep the QR at least 2.5 cm wide on the card and keep the white
margin (quiet zone) around it. Short URL + error correction "M" keeps the code small
(33 x 33 modules for the workers.dev URL), so it scans easily on a business card.
"""
import sys
from pathlib import Path
import segno

DEFAULT_URL = "https://contact-card.sembuh.workers.dev/david"
DARK = "#273b83"   # brand-900 (Codemasters Design System), strong contrast on white
LIGHT = "#ffffff"

url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
here = Path(__file__).resolve().parent

qr = segno.make(url, error="m", boost_error=False)
qr.save(here / "qr-contact-page.svg", scale=10, border=4, dark=DARK, light=LIGHT, xmldecl=False, svgns=True)
px = 2000
scale = max(1, px // (qr.symbol_size(scale=1, border=4)[0]))
qr.save(here / "qr-contact-page.png", scale=scale, border=4, dark=DARK, light=LIGHT)
print(f"QR for {url}: version {qr.version}, ECC {qr.error}, {qr.symbol_size(scale=1, border=0)[0]} modules")
