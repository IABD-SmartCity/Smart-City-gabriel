## 📊 Visualización de Datos con Grafana

A continuación se muestran las visualizaciones generadas con Grafana para analizar los valores medios diarios capturados por los sensores de la Smart City. Las consultas SQL se ejecutan sobre CrateDB y permiten agrupar los datos por día.

---

### 🌡️ Temperatura diaria promedio

**Consulta SQL:**
```sql
SELECT
  DATE_TRUNC('day', time_index) AS "time",
  AVG(temperatura) AS avg_temperatura
FROM etsensortemperaturas
WHERE entity_id = '$SensorTemperatura'
GROUP BY DATE_TRUNC('day', time_index)
ORDER BY "time"
![GraficaPH](https://github.com/user-attachments/assets/8be77142-6f3e-44b9-be80-92140e4507b1)

