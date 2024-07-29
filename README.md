# Python Flask Webservice

Este es un servicio web desarrollado en Python utilizando Flask. Proporciona una API para gestionar entidades en una base de datos MySQL.

## Requisitos

- Python 3.9 o superior
- MySQL

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tuusuario/python_flask_webservice.git
    cd python_flask_webservice
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\\Scripts\\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta los valores según tu configuración):
    ```env
    DATABASE_URI=mysql+mysqlconnector://usuario:contraseña@localhost/nombre_base_datos
    ```

2. Asegúrate de tener configurado correctamente el archivo `config.py` en el directorio `config/` para leer las variables de entorno.

## Configuración de la base de datos

1. Ejecuta el script SQL para migrar la base de datos que se encuentra en el archivo `entidades.sql`:

    ```sh
    mysql -u usuario -p nombre_base_datos < entidades.sql
    ```

## Ejecución

### Opción 1: Usar Docker

1. Construir la imagen Docker:
    ```sh
    docker build -t bnka_api_1 .
    ```

2. Ejecutar el contenedor:
    ```sh
    docker run -p 5000:5000 bnka_api_1
    ```

### Opción 2: Usar Flask directamente (más eficiente para depurar)

1. Asegúrate de que tu base de datos MySQL está en funcionamiento y accesible.
2. Ejecuta la aplicación:
    ```sh
    python3 app.py
    ```

## Uso

### Rutas de la API

- **GET /api/entidades**: Obtiene todas las entidades.
- **POST /api/entidades**: Crea una nueva entidad.

#### Ejemplo de solicitud POST

Para crear una nueva entidad, puedes usar Postman o cualquier otra herramienta para enviar una solicitud POST a `http://127.0.0.1:5000/api/entidades` con el siguiente cuerpo JSON:

```json
{
    "NUMERO_PROSA": 372.0,
    "TIE_NUMERO": 1,
    "DESCRIPCION": "PRODUCTOS INTEGRALES",
    "NUMERO_FIID": "B372",
    "NUMERO_TSYS_EMI": null,
    "NUMERO_TSYS_ADQ": null,
    "DESC_VENTAS": "",
    "DESC_PAGOS": "",
    "NUMERO_LN": "PRO1",
    "GCO_NUMERO": 12.0,
    "ID_UNICO_CARNET": null,
    "TRANSCOD": null,
    "CAMARA": 1,
    "ID_BANXICO": 0.0,
    "ENV_BANXICO": 1.0,
    "RED_MCD_ID_01": null,
    "RED_MCD_ID_02": null,
    "RED_VSA_ID_01": null,
    "AMEX_CAP": null,
    "IND_COLLECTION": null
}
```

#### Postman

Para probar la API, puedes importar la colección de Postman `API PRODUCTS BD.postman_collection` que se encuentra en el proyecto.

1. Abre Postman.
2. Haz clic en el botón "Importar" en la esquina superior izquierda.
3. Selecciona la pestaña "Import File".
4. Selecciona el archivo `API PRODUCTS BD.postman_collection.json` y haz clic en "Open".
