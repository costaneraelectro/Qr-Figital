# Generador de Código QR Figital · Banco Falabella (beta)

App web para generar **carnets con código QR** para asesores Banco Falabella,
listos para **imprimir y termolaminar**. Reproduce el diseño oficial de la
tarjeta (logos CMR · Débito · Seguros Falabella, flechas verdes y
"Escanea el Código QR") y le agrega el QR y el nombre del asesor.

## Qué hace

1. El asesor ingresa su **RUT** (sin dígito verificador), el **dígito
   verificador / guion (DV)**, su **nombre** y **apellido**.
2. Genera un **código QR** con la URL de apertura/contratación de Banco
   Falabella, reemplazando `utm_term` por el **RUT sin guion pero con el
   dígito verificador** (ej: `12.345.678-9` → `utm_term=123456789`).
3. Dibuja el carnet con el QR dentro del recuadro y el **nombre del asesor**
   al pie del QR (como el carnet real).
4. **Descarga un PDF** listo para imprimir.

### Dos modos

- **Individual:** un carnet por PDF (tamaño ~90 × 60 mm) para termolaminar.
  Cabe en la lámina de 66 × 102 mm dejando borde.
- **Por hoja · 8 QR:** carga hasta **8 asesores** y genera **una hoja tamaño
  carta con 8 carnets** para recortar (igual que el PDF oficial de ejemplo).

### Texto editable

El texto de la tarjeta es **editable** (una línea por renglón). Por defecto:

```
Abre conmigo tu CMR
o Cuenta Corriente
o contrata tu Seguro
```

URL base del QR (se reemplaza `utm_term`):

```
https://www.bancofalabella.cl/pre-landing?utm_source=Falabella&utm_medium=QRregional&utm_content=costanera-center-qr-unificado&utm_campaign=apertura-falabella&utm_term=<RUT+DV>&store_id=3660
```

## Impresión / termolaminado

- **Individual:** carnet ~**90 × 60 mm**, cabe en la lámina **66 × 102 mm**
  (orientado horizontal) dejando borde para sellar.
- **Por hoja:** **carta (216 × 279 mm)** con 8 carnets; recorta cada uno y
  termolamina.

## Uso

Es un único archivo estático; funciona **sin internet** (librerías, logos y
tarjeta van incrustados).

- **Local:** abre `index.html` (doble clic).
- **Publicado:** GitHub Pages o cualquier hosting estático.

> **GitHub Pages:** el repositorio debe ser **público**.
> Settings → Pages → Source: `Deploy from a branch` → `main` / `/ (root)`.

El RUT se valida con **módulo 11** (aviso, no bloqueante).

## Desarrollo

`index.html` es **generado**. Para editar la app modifica
`src/app_template.html` y vuelve a empaquetar:

```bash
python3 src/build.py
```

```
qr-figital/
├── index.html                 # app final autocontenida (generada)
├── README.md
└── src/
    ├── app_template.html      # HTML + estilos + lógica (editable)
    ├── build.py               # empaqueta todo en index.html
    ├── assets/
    │   ├── card-base.png      # tarjeta oficial sin el texto promocional
    │   └── umbrella.png       # logo Seguros Falabella (header)
    └── vendor/
        ├── jspdf.umd.min.js   # jsPDF 2.5.1
        └── qrcode.min.js      # qrcode-generator 1.4.4
```

La tarjeta base se extrajo del PDF oficial; el texto, el QR y el nombre se
dibujan encima con `canvas`.

## Créditos / librerías

- [jsPDF](https://github.com/parallax/jsPDF) — generación de PDF.
- [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) — código QR.

---

> **Versión beta.** Carnet 100% digital para asesores Banco Falabella.
> Verifica el RUT antes de imprimir. Logos y marcas son propiedad de Falabella.
