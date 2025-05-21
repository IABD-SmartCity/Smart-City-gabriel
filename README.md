
# 🌆 Proyecto Smart City con FIWARE

Bienvenido al repositorio del **Proyecto Smart City**, una simulación completa del funcionamiento de una ciudad inteligente utilizando la arquitectura FIWARE y tecnologías de visualización de datos.

---

## 🧠 ¿De qué trata este proyecto?

Este proyecto tiene como objetivo modelar una ciudad inteligente capaz de recopilar, almacenar y visualizar datos en tiempo real a través de sensores simulados. Utilizando la arquitectura modular de FIWARE, se implementan distintas fases que permiten ampliar progresivamente la funcionalidad del sistema.

---

## 🏗️ Tecnologías utilizadas

- **FIWARE Components:**
  - 🔵 *Orion Context Broker* – Gestión del contexto y entidades.
  - 🔵 *QuantumLeap* – Persistencia temporal de datos para visualización.
  - 🔵 *CrateDB* – Base de datos para datos históricos.
  - 🔵 *Grafana* – Paneles de visualización en tiempo real.

- **Contenedores:**
  - 🐳 *Docker & Docker Compose* – Orquestación de los servicios.

- **Otras herramientas:**
  - 📊 *Power BI* – Visualización avanzada de datos históricos.
  - 🗃️ *PostgreSQL* – Almacenamiento estructurado para análisis posterior.

---

## 🧩 Fases del Proyecto

1. **Fase 1 – Simulación base:**
   - Definición de entidades como sensores de temperatura, CO₂ y calidad del agua.
   - Ingesta de datos mediante Orion y almacenamiento en CrateDB.
   - Visualización básica con Grafana.

2. **Fase 2 – Procesamiento y almacenamiento:**
   - Scripts de extracción, transformación y carga (ETL) para CSV y PostgreSQL.
   - Generación automática de resúmenes diarios.

3. **Fase 3 – Visualización avanzada:**
   - Dashboard interactivo en Power BI con comparativas, promedios, distribución y filtros por sensor, atributo y fecha.

---

## 📦 Estructura del repositorio

```bash
proyecto-smart-city/
│
├── docker-compose.yml       # Orquestación de contenedores FIWARE
├── README.md                # Documentación del proyecto
│
├── context-data/            # Entidades NGSI y datos simulados
│   ├── resumen_diario_sensores.csv
│   └── README.md
│
├── grafana/                 # Configuración de dashboards en Grafana
│   ├── Paneles, variables y SQL
│   └── README.md
│
├── crateDB/                 # Consultas SQL, tablas y ejemplos de CrateDB
│   ├── TablasCrateDB.png
│   └── README.md
│
├── powerbi/                 # Informe en Power BI
│   ├── SmartCity.pbix
│   └── README.md
│
└── scripts/                 # Scripts para simulación y ETL
    ├── Generar datos.py         # Envía datos simulados al Context Broker
    ├── ETLWarehouseCSV.py       # Extrae datos de CrateDB y guarda en CSV
    ├── ETLWarehousePosgres.py   # Inserta los datos en PostgreSQL
    └── README.md
```

---

## 📷 Ejemplo de interfaz

![Interfaz general del sistema](./92b50904-722f-4dab-8714-db99bc4c4fe8.png)

---

## 👨‍💻 Autor

Gabriel Rodriguez – *Estudiante de Inteligencia Artificial y Big Data en CIPFP Mislata*
