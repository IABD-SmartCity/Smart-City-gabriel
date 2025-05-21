# 📄 resumen_diario_sensores.csv

Este archivo contiene un **resumen diario de los valores registrados por los sensores** desplegados en la simulación de la Smart City. Es útil para análisis estadísticos, visualización en Power BI o exportación a otros sistemas.

---

## 🧾 Descripción de columnas

| Columna     | Descripción                                                                 |
|-------------|-----------------------------------------------------------------------------|
| `fecha`     | Fecha de la medición (formato YYYY-MM-DD)                                   |
| `entity_id` | Identificador único del sensor (por ejemplo: sensor001)                     |
| `max`       | Valor máximo registrado por el sensor en ese día                            |
| `min`       | Valor mínimo registrado por el sensor en ese día                            |
| `avg`       | Promedio diario del valor registrado por el sensor                          |
| `sensor`    | Nombre de la tabla o tipo de sensor en FIWARE/CrateDB                       |
| `atributo`  | Variable medida por el sensor (temperatura, co2, humedad, ph, etc.)         |

---

## 📊 Uso típico

Este archivo puede ser utilizado para:
- Visualización en Power BI o Grafana.
- Cálculo de tendencias, outliers y estacionalidades.
- Comparación entre sensores o atributos a lo largo del tiempo.
- ETL hacia bases de datos estructuradas (MySQL, PostgreSQL, etc.)

---

## 📁 Ubicación en el proyecto

Se recomienda ubicar este archivo en la carpeta `/data` o `/scripts/output/`, dependiendo del flujo de trabajo.

---

## 🧠 Ejemplo de uso en Python

```python
import pandas as pd

df = pd.read_csv("resumen_diario_sensores.csv")
df[df["atributo"] == "temperatura"].groupby("fecha")["avg"].mean().plot()
```
## 👨‍💻 Autor

- Gabriel Rodriguez – *Estudiante de Inteligencia Artificial y Big Data en CIPFP Mislata*
