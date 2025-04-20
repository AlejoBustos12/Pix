# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from datetime import datetime
import os

# Asegurar que el directorio exista
os.makedirs("PIXRPA", exist_ok=True)

# Conexión a la base de datos
conn = psycopg2.connect(
    host='20.232.11.10',
    database='CamaraComercio',
    user='postgres',
    password='1234'
)

# Consulta
df = pd.read_sql("SELECT * FROM productos", conn)

# Nombre del archivo
fecha_actual = datetime.now().strftime('%Y-%m-%d')
#nombre_reporte = rf"C:\Users\Usuario\Documents\codigospython\PIXRPA\Reporte_{fecha_actual}.xlsx"
nombre_reporte = rf"C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Output\Reporte_{fecha_actual}.xlsx"
#C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Output
# Resumen
resumen = {
    "Total de productos": [df.shape[0]],
    "Precio promedio general": [df['price'].mean()]
}
df_resumen = pd.DataFrame(resumen)

# Agrupaciones
precio_categoria = df.groupby('category')['price'].mean().reset_index()
precio_categoria.columns = ['Categoría', 'Precio Promedio']

cantidad_categoria = df['category'].value_counts().reset_index()
cantidad_categoria.columns = ['Categoría', 'Cantidad de Productos']

# Escritura a Excel
with pd.ExcelWriter(nombre_reporte, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Productos', index=False)
    df_resumen.to_excel(writer, sheet_name='Resumen', index=False, startrow=0)
    precio_categoria.to_excel(writer, sheet_name='Resumen', index=False, startrow=4)
    cantidad_categoria.to_excel(writer, sheet_name='Resumen', index=False, startrow=8)

# Cerrar conexión
conn.close()

print(f"✅ Reporte generado exitosamente: {nombre_reporte}")
