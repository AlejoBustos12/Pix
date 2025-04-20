# -*- coding: utf-8 -*-

import json
import psycopg2

#ruta=rf'C:\Users\Usuario\Documents\codigospython\PIXRPA\Productos_2025-04-11.json'
ruta=rf'C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Input\productospython.json'
# Leer el archivo JSON
with open(ruta, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Conexión a PostgreSQL
conn = psycopg2.connect(host='20.232.11.10',user='postgres',password='123',database='CamaraComercio')
cur = conn.cursor()

# Insertar registros
for item in data:
    # Verificar si el producto ya existe
    cur.execute("SELECT 1 FROM productos WHERE id = %s", (item['id'],))
    existe = cur.fetchone()
    #print("EXISTE: ", existe)
    if not existe:
        cur.execute("""
            INSERT INTO productos (id, title, price, category, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            item['id'],
            item['title'],
            item['price'],
            item['category'],
            item['description']
        ))
    #     print(f"✅ Insertado producto ID {item['id']}")
    # else:
    #     print(f"⚠️ Ya existe producto ID {item['id']} — se omitió")

conn.commit()
cur.close()
conn.close()

#print("✅ JSON cargado exitosamente en PostgreSQL.")
