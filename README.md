# 📝 Mini App de Lista de Tareas con Flask

Este proyecto es una aplicación web sencilla desarrollada con **Flask** que permite gestionar una lista de tareas. 
El objetivo principal es comprender conceptos básicos de Flask como rutas, plantillas, formularios, manejo de 'session' y redirecciones.

---


## 🚀 Características

- Ver una lista de tareas.
- Agregar nuevas tareas.
- Eliminar tareas existentes.
- Persistencia de datos en memoria de usuario mediante 'session'.


---


## 📁 Estructura del proyecto
.
├── init.py # Aplicación principal Flask
├── templates/
│ ├── agregar.html # Formulario para agregar tareas
│ └── tareas.html # Vista de la lista de tareas


---

## ⚙️ Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/miniapp-flask-tareas.git
   cd miniapp-flask-tareas


2. Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate   # En Linux / Mac
venv\Scripts\activate      # En Windows


3. Instala Flask: 
pip install flask


4. Ejecuta la aplicación:
flask --app __init__.py run


4. Abre tu navegador en:
http://127.0.0.1:5000/tareas



📌 Rutas principales
- /tareas → Ver lista de tareas.
- /agregar → Formulario para añadir nuevas tareas.
- /eliminar/<indice> → Eliminar tarea según su índice.


📖 Aprendizaje clave
- Uso de Flask para definir rutas.
- Manejo de 'session' para almacenar datos temporales por usuario.
- Creación de formularios HTML con method="POST".
- Uso de 'redirect' y 'url_for' para aplicar el patrón Post/Redirect/Get.
- Renderizado de plantillas con Jinja2.


📜 Licencia
Este proyecto se desarrolla únicamente con fines de aprendizaje y práctica.
