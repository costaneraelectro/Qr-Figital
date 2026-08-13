# Generador de Código QR Figital · Banco Falabella (beta)

App web para generar **carnets doble cara con código QR** para asesores Banco
Falabella, listos para **imprimir, doblar y termolaminar**. Todos los carnets
son **doble cara** (franja **62 × 200 mm** que se dobla al medio → 62 × 100 mm).

## Modos

- **Múltiples · doble cara:** carga varios asesores → hoja(s) tamaño carta con
  **3 franjas por hoja** para recortar.
- **Individual · doble cara:** un asesor → una franja 62 × 200 mm.

### Las dos caras

- **Cara A** (QR de apertura): tarjeta oficial vertical (logos CMR · Débito ·
  Seguros, *"Pide tu CMR o Cuenta Corriente · Banco Falabella 100% digital"*,
  flechas verdes, "Escanea el Código QR") con el **QR** y el **nombre del asesor**.
- **Cara B** (venta de seguro + comparador), impresa a 180° para que al doblar
  quede derecha:
  - Logo **Seguro Compra Protegida**.
  - **Códigos de barra Plan 1 y Plan 2** (venta en caja) con precio mensual.
  - **QR para aceptar las condiciones** del seguro.
  - **Tabla de planes/coberturas** (suma asegurada, precio mínimo, muerte
    accidental, precio mensual).
  - **Comparativo de las 3 tarjetas CMR** (Clásica / Premium / Elite) con
    imagen real, valor UF + $ aprox/año, **duración de puntos** y beneficios.

## Valores

Los pesos son **aproximados según la UF del 01-08-2026 ($40.845)**:

| | Plan 1 | Plan 2 |
|---|---|---|
| Precio mensual | $5.700 | $8.600 |
| Suma asegurada | $2.042.200 | $4.084.500 |
| Muerte accidental | $4.084.500 | $4.084.500 |

Tarjetas CMR (comisión anual aprox): Clásica $5.500 · Premium $9.000 · Elite $14.300.
Duración de CMR Puntos: Clásica 1 año · Premium y Elite 2 años.

## Cómo funciona el QR

- **Apertura** (cara A): URL de Banco Falabella reemplazando `utm_term` por el
  **RUT del asesor sin guion pero con dígito verificador**
  (`12.345.678-9` → `utm_term=123456789`).
- **Seguro** (cara B): `https://bit.ly/3HGuZdF` (aceptar condiciones).

## Descargar / guardar el PDF

El botón usa la **hoja de compartir** del dispositivo:

- **iPhone / iPad:** *Compartir* → **Guardar en Archivos**, Fotos o WhatsApp.
- **Computador:** descarga directa.

## Impresión / termolaminado

Cada franja mide **62 × 200 mm**; doblada al medio queda **62 × 100 mm** y cabe
en la lámina **66 × 102 mm** dejando borde. El RUT se valida con módulo 11.

## Uso

Un único archivo estático; funciona **sin internet**.

- **Local:** abre `index.html` (doble clic).
- **Publicado:** GitHub Pages (repo público) → Settings → Pages → `main` / root.

## Desarrollo

`index.html` es **generado**. Edita `src/app_template.html` y reempaqueta:

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
    │   ├── cmr.png, umbrella.png            # header
    │   ├── seg-logo.png       # Seguro Compra Protegida (cara B)
    │   └── card-green/gray/black.png        # 3 CMR (comparador)
    └── vendor/
        ├── jspdf.umd.min.js   · qrcode.min.js · jsbarcode.min.js
```

### Fuentes de datos (cara B)

- Planes y códigos de barra del folleto oficial de **Seguro de Compra Protegida**.
- Comparativo, beneficios y duración de puntos del **comparador de CMR** de
  Banco Falabella. Imágenes de tarjetas oficiales.

## Créditos / librerías

- [jsPDF](https://github.com/parallax/jsPDF) · [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) · [JsBarcode](https://github.com/lindell/JsBarcode)

---

> **Versión beta.** Carnet 100% digital para asesores Banco Falabella.
> Verifica el RUT antes de imprimir. Logos y marcas son propiedad de Falabella.
