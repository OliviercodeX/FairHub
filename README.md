# FairHub

Aplicacion de escritorio en Python + Pygame para gestionar ventas, fiados y reportes de una feria de iglesia.

Desktop application built with Python + Pygame to manage sales, credit records, and reports for a church fair.

---

## ES - Descripcion

FairHub permite registrar ventas por chinamo (puesto), controlar fiados activos, consultar historial de movimientos y ver un resumen general del rendimiento de la feria.

## ES - Funcionalidades

- Gestion de chinamos: crear, renombrar, eliminar y administrar productos.
- Registro de ventas con carrito y separacion por tipo (`bought` o `fiado`).
- Registro de metodo de pago en compras (`efectivo` o `sinpe`) con nombre del titular para SINPE.
- Control de fiados activos por persona, con marcado de items pagados.
- Historial con vistas separadas: fiados, general, ventas y sinpes.
- Panel de resumen con totales globales y top de chinamos vendedores.

## ES - Tecnologias

- Python 3
- Pygame
- pygame-gui
- NumPy
- JSON para persistencia local

## ES - Estructura del proyecto

```text
FairHub/
|- main.py
|- requirements.txt
|- logic/
|  |- fair_manager.py
|  |- chinamo.py
|  |- sale.py
|- ui/
|  |- menu.py
|  |- screens.py
|  |- constants.py
|  |- credits_content.py
|- data/
   |- storage/
      |- chinamos.json
      |- sales_history.json
      |- fiados.json
      |- fair_data.json
```

## ES - Instalacion

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd FairHub
```

2. Crea y activa un entorno virtual (recomendado):

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

## ES - Ejecucion

```bash
python main.py
```

## ES - Persistencia de datos

La aplicacion guarda automaticamente la informacion en `data/storage/`:

- `chinamos.json`: catalogo de chinamos y productos.
- `sales_history.json`: historial de ventas registradas.
- `fiados.json`: fiados activos.
- `fair_data.json`: resumen consolidado y metricas generales.

---

## EN - Description

FairHub helps register sales by stand (`chinamo`), track active credit records (`fiados`), inspect transaction history, and view a global fair performance summary.

## EN - Features

- Stand management: create, rename, delete, and manage products.
- Cart-based sales flow with sale type classification (`bought` or `fiado`).
- Payment method tracking for purchases (`cash` or `sinpe`) with payer name for SINPE.
- Active credit tracking per person, including item-level payment marking.
- History module with separate views: credit, general, sales, and sinpe.
- Summary dashboard with global totals and top-performing stands.

## EN - Tech Stack

- Python 3
- Pygame
- pygame-gui
- NumPy
- JSON-based local persistence

## EN - Installation

1. Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd FairHub
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## EN - Run

```bash
python main.py
```

## EN - Data Persistence

The app automatically stores data in `data/storage/`:

- `chinamos.json`: stand catalog and products.
- `sales_history.json`: recorded sales history.
- `fiados.json`: active credit records.
- `fair_data.json`: consolidated metrics and global summary.

---

## Project Status

Active project under continuous improvement, focused on usability and reliable fair data management.

## Author

Developed by Mainor Martinez Sanchez Student of Instituto Tecnologico De Costa Rica.
