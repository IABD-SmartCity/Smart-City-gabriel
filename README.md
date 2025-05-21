# 🌆 Proyecto Smart City con FIWARE

Bienvenido al repositorio del **Proyecto Smart City**, una simulación completa del funcionamiento de una ciudad inteligente utilizando la arquitectura FIWARE y tecnologías de visualización de datos.

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
  - 🗃️ *PosgresSQL* – Almacenamiento estructurado para análisis posterior.

---

## 🧩 Fases del Proyecto

1. **Fase 1 – Simulación base:**
   - Definición de entidades como sensores de temperatura, CO₂ y calidad del agua.
   - Ingesta de datos mediante Orion y almacenamiento en CrateDB.
   - Visualización básica con Grafana.

---

## 📦 Estructura del repositorio
```bash
proyecto-smart-city/
│
├── docker-compose.yml       # Orquestación de contenedores FIWARE
├── README.md                # Documentación del proyecto
│
├── docs/                    # Documentación adicional (especificaciones, notas técnicas)
│
├── context-data/            # Entidades NGSI y datos simulados (JSON/CSV)
│
├── grafana/                 # Configuración de dashboards en Grafana (datasource y dashboards)
│
├── crate-init/              # Scripts SQL de inicialización para CrateDB
│
├── powerbi/                 # Informes Power BI
│ └── SmartCity.pbix         # Archivo del informe interactivo de Power BI
│
└── scripts/                 # Scripts útiles para automatizar el flujo de datos
├── Generar datos.py         # Envía datos simulados al Context Broker (Orion)
├── ETLWarehouseCSV.py       # Extrae datos de CrateDB y guarda en CSV para Power BI
└── ETLWarehousePosgres.py   # Extrae y almacena datos en PostgreSQL (Data Warehouse)
```
