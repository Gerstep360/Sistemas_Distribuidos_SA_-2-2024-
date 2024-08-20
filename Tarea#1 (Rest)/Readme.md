# Proyecto de Servicio REST con Flask

Este proyecto implementa un simple servicio REST utilizando Flask, que incluye dos rutas principales para manejar solicitudes `GET` y `POST`. La aplicación web tiene una interfaz básica construida en HTML y CSS.

## Archivos del Proyecto

- **`metodo rest.py`**: Este es el archivo principal de la aplicación Flask. Contiene la lógica para manejar las solicitudes y para obtener la dirección IP local.
- **`index.html`**: Este archivo contiene la interfaz web que permite al usuario interactuar con el servicio REST. Utiliza JavaScript para enviar solicitudes `GET` y `POST` a las rutas del servidor.

## Requisitos

- Python 3.x
- Flask (`pip install flask`)

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local.

   ```bash
   git clone https://github.com/Gerstep360/Sistemas_Distribuidos_SA_-2-2024-.git
2. Navega al directorio del proyecto.

   ```bash
   cd Tarea#1 (Rest)
3. Instala las dependencias necesarias.

   ```bash
   pip install flask
4. Ejecuta la aplicación Flask.

   ```bash
   python metodo_rest.py
5. Abre tu navegador y navega a `http://[localhost]:5000` para acceder a la interfaz web.

## Uso de la Aplicación

### 1. Solicitud GET

- La aplicación permite enviar una solicitud GET al servidor haciendo clic en el botón "Obtener Mensaje" en la interfaz web.
- Esto enviará una solicitud a la ruta `/hello`, que devolverá un mensaje JSON con el texto "Hello, World!".

### 2. Solicitud POST

- La aplicación también permite enviar una solicitud POST al servidor introduciendo datos en el campo de texto y haciendo clic en "Enviar Datos".
- Los datos se envían a la ruta `/echo`, que devuelve un JSON con el mensaje enviado.