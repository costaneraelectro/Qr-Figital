# Generador de Código QR Figital · Banco Falabella (beta)

App web para generar **carnets con código QR** para asesores Banco Falabella,
listos para **imprimir y termolaminar**. Reproduce el diseño oficial de la
tarjeta (logos CMR · Débito · Seguros Falabella, "Pide tu CMR o Cuenta
Corriente · Banco Falabella 100% digital", flechas verdes y "Escanea el
Código QR") y le agrega el QR y el nombre del asesor.

## Modos

- **Individual:** un carnet **vertical** por PDF (~60 × 92 mm) para termolaminar.
  Cabe en la lámina 66 × 102 mm dejando borde.
- **Por hoja · 8 QR:** hasta **8 asesores** en una **hoja tamaño carta** con 8
  carnets para recortar.
- **Doble cara · 62 × 200 mm:** franja que **se dobla al medio** (a los 100 mm)
  y se termolamina, útil por ambos lados:
  - **Cara A:** QR para abrir CMR / Cuenta Corriente.
  - **Cara B:** venta de seguro — **códigos de barra Plan 1 y Plan 2**, **QR
    para aceptar condiciones**, **resumen de planes y coberturas**, y un
    **comparativo de las 3 tarjetas CMR** (Clásica / Premium / Elite).

> La cara B se imprime rotada 180° a propósito: al doblar la franja hacia atrás
> queda derecha.

## Cómo funciona el QR

El QR de apertura usa la URL de Banco Falabella reemplazando `utm_term` por el
**RUT del asesor sin guion pero con dígito verificador**
(ej: `12.345.678-9` → `utm_term=123456789`):

```
https://www.bancofalabella.cl/pre-landing?utm_source=Falabella&utm_medium=QRregional&utm_content=costanera-center-qr-unificado&utm_campaign=apertura-falabella&utm_term=<RUT+DV>&store_id=3660
```

El QR del seguro (cara B) apunta a la aceptación de condiciones
(`https://bit.ly/3HGuZdF`).

## Descargar / guardar el PDF

El botón usa la **hoja de compartir** del dispositivo:

- **iPhone / iPad:** abre *Compartir* → **Guardar en Archivos**, en Fotos o
  enviar por WhatsApp (soluciona que Safari solo mostraba el PDF).
- **Computador:** descarga directa.

## Impresión / termolaminado

- **Individual:** ~**60 × 92 mm** (cabe en lámina 66 × 102 mm con borde).
- **Por hoja:** carta **216 × 279 mm**, 8 carnets.
- **Doble cara:** **62 × 200 mm**; doblado queda **62 × 100 mm** (cabe en la
  lámina 66 × 102 mm).

## Uso

Un único archivo estático; funciona **sin internet** (librerías, logos y
gráficos van incrustados).

- **Local:** abre `index.html` (doble clic).
- **Publicado:** GitHub Pages (repo público) → Settings → Pages → `main` / root.

El RUT se valida con **módulo 11** (aviso, no bloqueante).

## Desarrollo

`index.html` es **generado**. Para editar modifica `src/app_template.html` y
reempaqueta:

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
    │   ├── logos3.png         # CMR + Débito + Seguros (tarjeta)
    │   ├── cmr.png            # logo CMR (header)
    │   └── umbrella.png       # logo Seguros Falabella (header)
    └── vendor/
        ├── jspdf.umd.min.js   # jsPDF 2.5.1
        ├── qrcode.min.js      # qrcode-generator 1.4.4
        └── jsbarcode.min.js   # JsBarcode 3.11.6
```

### Datos usados (cara B)

- Planes de **Seguro de Compra Protegida** (Plan 1 / Plan 2) y sus códigos de
  barra, tomados del folleto oficial.
- Comparativo de las **3 CMR** con valores/beneficios del comparador de Banco
  Falabella. Las imágenes de las tarjetas son **ilustrativas** (se pueden
  reemplazar por las oficiales).

## Créditos / librerías

- [jsPDF](https://github.com/parallax/jsPDF) — PDF.
- [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) — QR.
- [JsBarcode](https://github.com/lindell/JsBarcode) — códigos de barra.

---

> **Versión beta.** Carnet 100% digital para asesores Banco Falabella.
> Verifica el RUT antes de imprimir. Logos y marcas son propiedad de Falabella.
