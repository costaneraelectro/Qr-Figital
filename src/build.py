#!/usr/bin/env python3
"""
Empaqueta la app en un unico archivo `index.html` autocontenido (funciona offline).

Inyecta dentro de `app_template.html`:
  - vendor/jspdf.umd.min.js      -> generador de PDF
  - vendor/qrcode.min.js         -> generador de codigo QR
  - vendor/jsbarcode.min.js      -> codigos de barra (Plan 1 / Plan 2)
  - assets/logos3.png            -> logos CMR + Debito + Seguros Falabella (tarjeta)
  - assets/cmr.png               -> logo CMR (header)
  - assets/umbrella.png          -> logo Seguros Falabella (header)

La tarjeta, el texto, el QR, el nombre y la cara B (seguro + comparador) se
dibujan con canvas; las imagenes incrustadas son solo los logos.

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

OUT.write_text(out, encoding="utf-8")
print(f"OK -> {OUT}  ({len(out):,} bytes)")
