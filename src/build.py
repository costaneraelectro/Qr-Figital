#!/usr/bin/env python3
"""
Empaqueta la app en un unico archivo `index.html` autocontenido (funciona offline).

Inyecta dentro de `app_template.html`:
  - vendor/jspdf.umd.min.js   -> generador de PDF
  - vendor/qrcode.min.js      -> generador de codigo QR
  - assets/logos.png          -> logos CMR + Debito Falabella (base64)

La tarjeta se dibuja por completo con canvas (vectorial), asi que el unico
recurso de imagen incrustado son los logos.

Uso:
    python3 src/build.py
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent          # .../src
OUT  = ROOT.parent / "index.html"                        # .../index.html

tpl   = (ROOT / "app_template.html").read_text(encoding="utf-8")
jspdf = (ROOT / "vendor" / "jspdf.umd.min.js").read_text(encoding="utf-8")
qrlib = (ROOT / "vendor" / "qrcode.min.js").read_text(encoding="utf-8")
logo  = base64.b64encode((ROOT / "assets" / "logos.png").read_bytes()).decode()

out = (tpl
       .replace("<!--__LIB_JSPDF__-->",  "<script>\n" + jspdf + "\n</script>")
       .replace("<!--__LIB_QRCODE__-->", "<script>\n" + qrlib + "\n</script>")
       .replace("__LOGO_B64__", "data:image/png;base64," + logo))

OUT.write_text(out, encoding="utf-8")
print(f"OK -> {OUT}  ({len(out):,} bytes)")
