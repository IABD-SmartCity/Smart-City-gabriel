import random
import requests
from datetime import datetime, timedelta
import time


ORION_URL = "http://localhost:1026/v2/entities"
HEADERS = {"Content-Type": "application/json"}


entities = {
   "sensor001": ["Temperatura", "humidity"],
   "sensor002": ["CO2"],
   "sensor003": ["Ph", "Temperatura", "cloro"]
}


start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 4, 30)
total_points = 400
interval = (end_date - start_date) / total_points


# Rango por atributo
attribute_ranges = {
   "Temperatura": (5, 30),
   "humidity": (20, 90),
   "CO2": (300, 800),
   "Ph": (6, 9),
   "cloro": (0.5, 2.0)
}


for entity_id, attributes in entities.items():
   timestamp = start_date
   for i in range(total_points):
       data = {}
       for attr in attributes:
           min_val, max_val = attribute_ranges.get(attr, (0, 30))
           value = round(random.uniform(min_val, max_val), 2)
           data[attr] = {
               "type": "Number",
               "value": value,
               "metadata": {
                   "timestamp": {
                       "type": "DateTime",
                       "value": timestamp.isoformat() + "Z"
                   }
               }
           }


       url = f"{ORION_URL}/{entity_id}/attrs"
       response = requests.post(url, headers=HEADERS, json=data)
       print(f"{entity_id} | Registro {i+1}/{total_points} | Status: {response.status_code}")


       time.sleep(2.5)
       timestamp += interval
