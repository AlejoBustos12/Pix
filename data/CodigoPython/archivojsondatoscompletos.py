# -*- coding: utf-8 -*-

import requests
import json

# Endpoint
url = "https://fakestoreapi.com/products"

# Hacer la solicitud GET
response = requests.get(url)
#Ruta Archivo a guardar
archivo=r"C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Input\productospython.json"
# Verificar si fue exitosa
if response.status_code == 200:
    productos = response.json()
    
    # Guardar en un archivo JSON
    with open(archivo, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)

    print("✅ Datos guardados en 'productos.json'")
else:
    print(f"❌ Error en la solicitud. Código de estado: {response.status_code}")
