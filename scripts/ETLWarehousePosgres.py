from crate import client
import pandas as pd
from sqlalchemy import create_engine

# 📡 Conexión a CrateDB
crate_conn = client.connect("localhost:4200", error_trace=True)
cursor = crate_conn.cursor()

# 🏛️ Conexión a PostgreSQL (Data Warehouse)
dw_conn = create_engine('postgresql://gabriel:123456@localhost:5432/datawarehouse')

# 🔍 Tablas CrateDB y sus atributos a procesar
tablas = {
    "etsensortemperaturas": ["temperatura", "humidity"],
    "etsensorco2": ["co2"],
    "etsensorqualitywater": ["ph", "temperatura", "cloro"]
}

# 🔁 Procesamiento
for tabla, atributos in tablas.items():
    print(f"Procesando: {tabla}")
    for atributo in atributos:
        query = f"""
            SELECT DATE_TRUNC('day', time_index) AS fecha,
                   entity_id,
                   MAX({atributo}) AS max,
                   MIN({atributo}) AS min,
                   AVG({atributo}) AS avg
            FROM {tabla}
            GROUP BY fecha, entity_id
            ORDER BY fecha
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print(f"⚠️ No hay datos para {atributo} en {tabla}")
            continue

        # Crear DataFrame
        df = pd.DataFrame(rows, columns=["fecha", "entity_id", "max", "min", "avg"])

        # ✅ Convertir timestamp a fecha legible
        df["fecha"] = pd.to_datetime(df["fecha"], unit="ms")

        # 🏷️ Añadir metadatos
        df["sensor"] = tabla
        df["atributo"] = atributo

        # 🛢️ Guardar en PostgreSQL
        df.to_sql("resumen_diario_sensores", dw_conn, if_exists="append", index=False)
        print(f"✔️ {atributo} insertado correctamente.")
