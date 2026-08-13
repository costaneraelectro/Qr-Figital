# Generador de QR Figital · Banco Falabella (beta)

App web para generar un **carnet vertical en PDF** con un **código QR
personalizado por asesor** y su **nombre y apellido**. Pensado para
**imprimir y termolaminar** (lámina 66 × 102 mm).

## Qué hace

1. El asesor ingresa su **RUT** (sin dígito verificador), el **dígito
   verificador / guion (DV)**, su **nombre** y **apellido**.
2. Genera un **código QR** con la URL de apertura de cuenta de Banco Falabella,
   reemplazando el parámetro `utm_term` por el **RUT sin guion pero con el
   dígito verificador** (ej: `12.345.678-9` → `utm_term=123456789`).
3. Dibuja la tarjeta vertical (logos CMR + Débito, texto promocional, QR con
   las pestañas verdes y el **nombre del asesor** bajo el QR).
4. **Descarga un PDF** listo para imprimir.

URL base del QR (se reemplaza `utm_term`):

```
https://www.bancofalabella.cl/pre-landing?utm_source=Falabella&utm_medium=QRregional&utm_content=costanera-center-qr-unificado&utm_campaign=apertura-falabella&utm_term=<RUT+DV>&store_id=3660
```

## Tamaño de impresión

La pieza se genera en **60 × 92 mm (vertical)**, **menor** que la lámina de
termolaminado de **66 × 102 mm**, dejando un **borde blanco** para poder
plastificar/sellar sin cortar el diseño.

## Uso

Es un único archivo estático. No requiere servidor ni conexión a internet
(las librerías y los logos van incrustados).

- **Local:** abre `index.html` en el navegador (doble clic).
- **Publicado:** sírvelo con GitHub Pages o cualquier hosting estático.

> **GitHub Pages:** el repositorio debe ser **público** (Pages gratis).
> Settings → Pages → Source: `Deploy from a branch` → `main` / `/ (root)`.

### Validación de RUT

El RUT se valida con **módulo 11** y muestra un aviso si el dígito verificador
no coincide (no bloquea, solo advierte).

## Desarrollo

`index.html` es un archivo **generado**. Para editar la app, modifica
`src/app_template.html` y vuelve a empaquetar:

```bash
python3 src/build.py
```

La tarjeta se dibuja completa con `canvas` (vectorial); el único recurso de
imagen incrustado son los **logos CMR + Débito** (`src/assets/logos.png`).

```
qr-figital/
├── index.html                 # app final autocontenida (generada)
├── README.md
└── src/
    ├── app_template.html      # HTML + estilos + lógica (editable)
    ├── build.py               # empaqueta todo en index.html
    ├── assets/logos.png       # logos CMR + Débito Falabella
    └── vendor/
        ├── jspdf.umd.min.js   # jsPDF 2.5.1
        └── qrcode.min.js      # qrcode-generator 1.4.4
```

## Créditos / librerías

- [jsPDF](https://github.com/parallax/jsPDF) — generación de PDF.
- [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) — código QR.

---

> **Versión beta.** Carnet 100% digital para asesores Banco Falabella.
> Verifica el RUT antes de imprimir. Logos y marcas son propiedad de Falabella.
