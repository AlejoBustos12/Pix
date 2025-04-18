# Proyecto RPA - Prueba Técnica

Este proyecto es una **prueba técnica** que automatiza una serie de tareas usando **tecnología RPA (Automatización Robótica de Procesos)**, ejecutado desde la plataforma **Pix** y desarrollado con **Python 3**.

## 📝 Descripción del Proyecto

El proceso RPA desarrollado realiza las siguientes tareas:

1. **Obtiene productos desde una API pública.**
2. **Guarda los datos originales y estructurados.**
3. **Almacena la información en una base de datos.**
4. **Genera un reporte en formato Excel** con estadísticas relevantes sobre los productos obtenidos.
5. **Sube automáticamente el reporte a OneDrive** mediante integración con Microsoft Graph.
6. **Envía el reporte a través de un formulario web** previamente definido.
7. **Registra evidencias del proceso**, incluyendo logs, capturas y respuestas del sistema.

Este flujo fue diseñado para demostrar habilidades en automatización, manipulación de datos, integración de APIs y generación de reportes automatizados.

---

## ▶️ Pasos para la Ejecución

1. **Clonar o descargar este repositorio.**
2. **Configurar las variables necesarias:**
   - Credenciales para la API pública (si aplica).
   - Parámetros de conexión a la base de datos.
   - Token de acceso para Microsoft Graph (OneDrive).
   - URL del formulario web.
3. **Instalar las dependencias (ver sección siguiente).**
4. **Ejecutar el proceso desde la plataforma Pix** o localmente con:
   ```bash
   python main.py
