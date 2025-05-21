# 📊 Paneles de sensores en Grafana – Proyecto Smart City

En esta sección se documentan las visualizaciones desarrolladas con **Grafana** para los sensores de la ciudad inteligente. Se muestran los paneles con promedios diarios y las consultas SQL usadas para obtener los datos desde **CrateDB**.

---

## 🌡️ Temperatura diaria promedio

**Consulta SQL:**

```sql
SELECT
  DATE_TRUNC('day', time_index) AS "time",
  AVG(temperatura) AS avg_temperatura
FROM etsensortemperaturas
WHERE entity_id = '$SensorTemperatura'
GROUP BY DATE_TRUNC('day', time_index)
ORDER BY "time"
```
![grafiaSensorTemperatura](https://github.com/user-attachments/assets/6e3d9e56-02cb-4e57-95be-f74771f6bb66)

## 🌬️ CO₂ diario promedio

**Consulta SQL:**

```sql
SELECT
  DATE_TRUNC('day', time_index) AS "time",
  AVG(co2) AS avg_co2
FROM etsensorco2
WHERE entity_id = '$SensorCO2'
GROUP BY DATE_TRUNC('day', time_index)
ORDER BY "time"
```

![GraficaCO2](https://github.com/user-attachments/assets/8c6c3025-2632-460c-8387-615f58632f2a)


## 💧 Humedad diaria promedio

**Consulta SQL:**

```sql
SELECT
  DATE_TRUNC('day', time_index) AS "time",
  AVG(humidity) AS avg_humidity
FROM etsensortemperaturas
WHERE entity_id = '$SensorHumedad'
GROUP BY DATE_TRUNC('day', time_index)
ORDER BY "time"
```

![GraficaHumedad](https://github.com/user-attachments/assets/f31b9ac6-d987-43d8-a9f5-9e5599f0023b)

## 🧪 Nivel de pH del agua diario promedio****

**Consulta SQL:**

```sql
SELECT
  DATE_TRUNC('day', time_index) AS "time",
  AVG(ph) AS avg_ph
FROM etsensorqualitywater
WHERE entity_id = '$SensorPH'
GROUP BY DATE_TRUNC('day', time_index)
ORDER BY "time"
```

![GraficaPH](https://github.com/user-attachments/assets/2c036c8d-ce17-436e-b6e1-16585b2ac51a)

## 👨‍💻 Autor

- Gabriel Rodriguez – *Estudiante de Inteligencia Artificial y Big Data en CIPFP Mislata*
