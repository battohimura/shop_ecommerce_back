# SHOP ECOMMERCE BACK

Backend para proyecto personal de Fernanda Avello.

## Instrucciones de instalación

1. Crear entorno virtual
    `virtualenv -p python3.10 .venv`

2. Activar entorno virtual (WSL/Linux)
    `source .venv/bin/activate`

3. Correr migraciones
    `python manage.py migrate`

4. Crear superuser
    `python manage.py createsuperuser`

5. Correr backend
    `python manage.py runserver`

Backend debería estar corriendo en puerto 8000
