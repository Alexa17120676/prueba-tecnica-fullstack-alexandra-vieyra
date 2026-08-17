Sección 3 - FastAPI

Esta carpeta contiene una implementación funcional del endpoint propuesto en el Problema A de la Sección 3.

Endpoint:

GET /api/v1/cines/{id_cine}

Query param opcional:

date=YYYY-MM-DD

Si no se envía una fecha, se utiliza la fecha actual.

La API incluye:

- Path param para identificar el cine.
- Query param para consultar una fecha específica.
- Modelos de respuesta con Pydantic.
- Validación automática de parámetros.
- Respuesta 404 cuando el cine no existe.
- Documentación automática con Swagger.

Instalación:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Ejecución:

uvicorn main:app --reload

Swagger:

http://127.0.0.1:8000/docs

Ejemplos:

GET /api/v1/cines/15

GET /api/v1/cines/15?date=2026-08-17

GET /api/v1/cines/999