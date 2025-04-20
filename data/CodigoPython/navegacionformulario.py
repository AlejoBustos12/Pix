# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

fecha_actual = datetime.now().strftime('%Y-%m-%d')
# Nombre del archivo
rutaimagenpdf=rf"C:\Users\Usuario\Documents\codigospython\PIXRPA\examinar.png"
ruta=rf"C:\Users\Usuario\Documents\codigospython\PIXRPA\ruta.png"
evidencia_path = rf"C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Output\formulario_confirmacion.png"

options = webdriver.ChromeOptions()

# Usa tu perfil de Chrome para mantener la sesión iniciada
options.add_argument(r"user-data-dir=C:\Users\Usuario\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Default")  # Estás usando 'Default'

# Inicia el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abre el formulario
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScNC4UzDZ2sLyQBxgyEnvIGnVI6MLjbItu7E8e9F8-qEdq7oA/viewform?usp=dialog")
print("salida")


time.sleep(7)
# ✅ Maximizar la ventana
driver.maximize_window()

nombre="Jonathan bustos mejia"
input_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
input_field.send_keys(nombre)

fecha="01/01/2025"
input_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
input_field.send_keys(fecha)

comentarios="ninguno"
input_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
input_field.send_keys(comentarios)

time.sleep(2)
#BOTON SIGUIENTE
search_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/span/span[2]')
search_button.click()

time.sleep(4)
#CLIC EN IMAGEN DESACRAGR PDF
pos2 = pyautogui.locateCenterOnScreen(rutaimagenpdf, confidence=0.8)
if pos2 :
#if pos is not None:
    pyautogui.click(pos2)

# Espera unos segundos para que la ventana se cargue
time.sleep(7)

# Busca la ubicación de la imagen en la pantalla
campo_pos = pyautogui.locateOnScreen(ruta, confidence=0.8)
#campo_pos = pyautogui.locateOnScreen(ruta)

if campo_pos:
    # Obtén el centro del campo de entrada
    campo_center = pyautogui.center(campo_pos)

    # Mueve el cursor a la posición del campo de entrada y hace clic
    pyautogui.click(campo_center)
    archivo=rf"C:\Users\Usuario\Documents\PIXRPA\Prueba Tecnica\data\Output\Reporte_{fecha_actual}.xlsx"
    # Escribe el texto en el campo de entrada
    pyautogui.write(archivo, interval=0.1)
    # Presionar Enter
    pyautogui.press('enter')
else:
    print("No se encontró el campo de entrada.")


time.sleep(4)
#BOTON SIGUIENTE
search_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
search_button.click()

time.sleep(4)
# Captura de pantalla de la confirmación
driver.save_screenshot(evidencia_path)
print(f"Evidencia guardada en: {evidencia_path}")


# #driver.quit()
#input("Presiona Enter para cerrar el navegador...")











