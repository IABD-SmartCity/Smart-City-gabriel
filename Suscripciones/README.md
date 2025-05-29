# 📡 Smart City - Gestión de Sensores con FIWARE

Este proyecto registra y monitoriza sensores de temperatura, humedad, CO2 y calidad del agua usando **FIWARE Orion Context Broker** como gestor de contexto y **QuantumLeap** para el almacenamiento histórico de datos en CrateDB.

## 🧱 Arquitectura

- **Orion Context Broker**: Recibe entidades NGSIv2.
- **QuantumLeap**: Recibe notificaciones y almacena los datos históricos.
- **CrateDB**: Base de datos de series temporales.
- **Docker**: Contenedores para cada componente (opcional).

---

## 📌 Entidades Registradas

### 🌡️ SensorTemperaturas (`sensor001`)
```json
{
  "id": "sensor001",
  "type": "SensorTemperaturas",
  "humidity": {
    "value": 55,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  },
  "Temperatura": {
    "value": 30,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  }
}
```

### 🫁 SensorCO2 (`sensor002`)
```json
{
  "id": "sensor002",
  "type": "SensorCO2",
  "CO2": {
    "value": 55,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  }
}
```

### 💧 SensorQualityWater (`sensor003`)
```json
{
  "id": "sensor003",
  "type": "SensorQualityWater",
  "Ph": {
    "value": 20,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  },
  "Temperatura": {
    "value": 55,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  },
  "cloro": {
    "value": 31,
    "type": "Number",
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2025-03-01T13:00:00Z"
      }
    }
  }
}
```

---

## 📬 Suscripciones a Notificaciones

Cada sensor está suscrito a **QuantumLeap** para recibir notificaciones de cambio de atributos y su timestamp.

### SensorTemperaturas (`sensor001`)
- Atributos: `Temperatura`, `humidity`
- Metadata: `timestamp`
- URL: `http://quantumleap:8668/v2/notify`

### SensorCO2 (`sensor002`)
- Atributo: `CO2`
- Metadata: `timestamp`

### SensorQualityWater (`sensor003`)
- Atributos: `Temperatura`, `Ph`, `cloro`
- Metadata: `timestamp`

---

## 🚀 Comandos `curl` para cargar sensores y suscripciones

Ejecutar los siguientes comandos en orden:


```bash
# Crear suscripción para sensor001
curl -X POST http://localhost:1026/v2/subscriptions -H "Content-Type: application/json" -d '{
  "description": "Suscripción a sensores con metadata.timestamp",
  "subject": {
    "entities": [
      { "idPattern": "sensor001", "type": "SensorTemperaturas" }
    ]
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": ["Temperatura", "humidity"],
    "metadata": ["timestamp"]
  },
  "throttling": 1
}'

# Crear suscripción para sensor002
curl -X POST http://localhost:1026/v2/subscriptions -H "Content-Type: application/json" -d '{
  "description": "Suscripción a sensores con metadata.timestamp",
  "subject": {
    "entities": [
      { "idPattern": "sensor002", "type": "SensorCO2" }
    ]
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": ["CO2"],
    "metadata": ["timestamp"]
  },
  "throttling": 1
}'

# Crear suscripción para sensor003
curl -X POST http://localhost:1026/v2/subscriptions -H "Content-Type: application/json" -d '{
  "description": "Suscripción a sensores con metadata.timestamp",
  "subject": {
    "entities": [
      { "idPattern": "sensor003", "type": "SensorQualityWater" }
    ]
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": ["Temperatura", "Ph", "cloro"],
    "metadata": ["timestamp"]
  },
  "throttling": 1
}'
```


⚠️ **Nota**: Asegúrate de tener levantados los servicios `orion`, `quantumleap` y `crate` mediante Docker Compose u otro sistema antes de ejecutar estos comandos.

---

## 🛠️ Requisitos

- Docker y Docker Compose
- FIWARE Orion Context Broker
- QuantumLeap y CrateDB
- curl

---

## 📈 Visualización

Puedes conectar **Grafana** a **CrateDB** para visualizar las series temporales de los sensores.

---
## 👨‍💻 Autor

Gabriel Rodriguez – *Estudiante de Inteligencia Artificial y Big Data en CIPFP Mislata*
