from crate import client
import pandas as pd
import os

# 📡 Conexión a CrateDB
crate_conn = client.connect("localhost:4200", error_trace=True)
cursor = crate_conn.cursor()

# 📂 Directorio de salida y nombre del archivo
output_dir = "export_csv"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "resumen_diario_sensores.csv")

# 🔍 Tablas CrateDB y sus atributos a procesar
tablas = {
    "etsensortemperaturas": ["temperatura", "humidity"],
    "etsensorco2": ["co2"],
    "etsensorqualitywater": ["ph", "temperatura", "cloro"]
}

# 🔁 Procesamiento
all_dfs = []  # Lista para guardar todos los DataFrames y unirlos al final

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

        # Convertir fecha correctamente
        df["fecha"] = pd.to_datetime(df["fecha"], unit="ms")

        # Añadir columnas de contexto
        df["sensor"] = tabla
        df["atributo"] = atributo

        all_dfs.append(df)

# 📝 Unir todos los DataFrames y guardar en CSV
if all_dfs:
    df_final = pd.concat(all_dfs, ignore_index=True)
    df_final.to_csv(output_file, index=False)
    print(f"✔️ CSV exportado correctamente: {output_file}")
else:
    print("⚠️ No se encontraron datos para exportar.")
