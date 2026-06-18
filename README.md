# UT5_TFU_Grupo2
Backend de Sistema Truck and Roll

## Requisitos

- Python 3.10 o superior

## Instalación

1. Clonar el repositorio y ubicarse en la carpeta del proyecto.
2. Crear y activar un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # En Windows: .venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de la API

Con el entorno virtual activado, ejecutar:

```bash
python run.py
```

La API quedará disponible en `http://127.0.0.1:5000`. La base de datos SQLite (`instance/pedidos.db`) se crea automáticamente, junto con datos de ejemplo, la primera vez que se inicia la aplicación.
