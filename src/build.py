#!/usr/bin/env python3
"""
Empaqueta la app en un unico archivo `index.html` autocontenido (funciona offline).

Inyecta dentro de `app_template.html`:
  - vendor/jspdf.umd.min.js   -> PDF
  - vendor/qrcode.min.js      -> codigo QR
  - vendor/jsbarcode.min.js   -> codigos de barra
  - assets/*.png (base64)     -> logos y tarjetas

Uso:
    python3 src/build.py
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT  = ROOT.parent / "index.html"

def js(p):  return "<script>\n" + (ROOT / "vendor" / p).read_text(encoding="utf-8") + "\n</script>"
def b64(p): return "data:image/png;base64," + base64.b64encode((ROOT / "assets" / p).read_bytes()).decode()

out = (ROOT / "app_template.html").read_text(encoding="utf-8")
out = out.replace("<!--__LIB_JSPDF__-->",   js("jspdf.umd.min.js"))
out = out.replace("<!--__LIB_QRCODE__-->",  js("qrcode.min.js"))
out = out.replace("<!--__LIB_BARCODE__-->", js("jsbarcode.min.js"))
out = out.replace("__LOGOS3_B64__",   b64("logos3.png"))
out = out.replace("__CMR_B64__",      b64("cmr.png"))
out = out.replace("__UMBRELLA_B64__", b64("umbrella.png"))
out = out.replace("__SEG_B64__",      b64("seg-logo.png"))
out = out.replace("__GREEN_B64__",    b64("card-green.png"))
out = out.replace("__GRAY_B64__",     b64("card-gray.png"))
out = out.replace("__BLACK_B64__",    b64("card-black.png"))

OUT.write_text(out, encoding="utf-8")
print(f"OK -> {OUT}  ({len(out):,} bytes)")
