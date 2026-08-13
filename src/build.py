#!/usr/bin/env python3
"""
Empaqueta la app en un unico archivo `index.html` autocontenido (funciona offline).

Inyecta dentro de `app_template.html`:
  - vendor/jspdf.umd.min.js   -> generador de PDF
  - vendor/qrcode.min.js      -> generador de codigo QR
  - assets/card-base.png      -> tarjeta oficial (sin el texto promocional) en base64
  - assets/umbrella.png       -> logo Seguros Falabella para el header

El texto promocional, el QR y el nombre se dibujan sobre la tarjeta con canvas,
por eso el texto es editable desde la app.

Uso:
    python3 src/build.py
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent          # .../src
OUT  = ROOT.parent / "index.html"                        # .../index.html

def b64(p): return "data:image/png;base64," + base64.b64encode((ROOT / p).read_bytes()).decode()

out = (ROOT / "app_template.html").read_text(encoding="utf-8")
out = out.replace("<!--__LIB_JSPDF__-->",  "<script>\n" + (ROOT/"vendor"/"jspdf.umd.min.js").read_text(encoding="utf-8") + "\n</script>")
out = out.replace("<!--__LIB_QRCODE__-->", "<script>\n" + (ROOT/"vendor"/"qrcode.min.js").read_text(encoding="utf-8") + "\n</script>")
out = out.replace("__CARD_BASE_B64__", b64("assets/card-base.png"))
out = out.replace("__UMBRELLA_B64__",  b64("assets/umbrella.png"))

OUT.write_text(out, encoding="utf-8")
print(f"OK -> {OUT}  ({len(out):,} bytes)")
