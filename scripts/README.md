
# 🧪 Scripts ETL y Simulación – Proyecto Smart City

Este módulo contiene los scripts Python utilizados para simular datos, extraer información desde CrateDB y almacenarla en distintos formatos como CSV o una base de datos PostgreSQL.

---

## 📤 `Generar datos.py`

Simula datos para tres sensores (`sensor001`, `sensor002`, `sensor003`) y los envía al **Orion Context Broker** utilizando peticiones HTTP. Cada sensor genera 400 registros espaciados entre marzo y abril de 2025.

- Sensor001: Temperatura, Humedad
- Sensor002: CO₂
- Sensor003: pH, Temperatura, Cloro

📌 Los valores generados están dentro de rangos realistas definidos para cada atributo.

---

## 📄 `ETLWarehouseCSV.py`

Este script extrae los datos históricos de CrateDB y genera un archivo CSV llamado `resumen_diario_sensores.csv` con el resumen diario por sensor y atributo.

- Conexión a CrateDB usando la librería `crate`.
- Agrupación por fecha y sensor.
- Cálculo de máximos, mínimos y promedios.
- El archivo se guarda en la carpeta `export_csv/`.

---

## 🛢️ `ETLWarehousePosgres.py`

Hace el mismo procesamiento que el script anterior pero **almacena los resultados directamente en una base de datos PostgreSQL** (`datawarehouse`).

- Se usa `sqlalchemy` para la conexión.
- Inserta datos en la tabla `resumen_diario_sensores`.
- Útil para análisis en Power BI u otros sistemas de BI conectados al DWH.

---

## ⚠️ Requisitos

```bash
pip install pandas requests crate sqlalchemy psycopg2
```

---

## 📂 Ubicación sugerida

```
scripts/
├── Generar datos.py
├── ETLWarehouseCSV.py
└── ETLWarehousePosgres.py
```

---

## 👨‍💻 Autor

Gabriel Rodriguez – *Estudiante de Inteligencia Artificial y Big Data en CIPFP Mislata*

