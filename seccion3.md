Sección 3 — FastAPI y REST

# Problema A — Diseñar un endpoint

1. El path y método HTTP

GET /api/v1/cines/{id_cine}

2. Los query params

date (opcional): fecha de las funciones en formato YYYY-MM-DD.
Si no se envía, se utiliza la fecha actual.

3. El response schema (estructura JSON)
```json
{
  "id_cine": 15,
  "name": "Perisur",
  "brand": "VIP",
  "city": "CDMX",
  "date": "2026-08-13",
  "rooms": [
    {
      "id_room": 1,
      "name": "Sala 1",
      "showtimes": [
        {
          "id_showtime": 101,
          "id_movie": 1,
          "movie": "Inside Out 3",
          "show_time": "14:30"
        }
      ]
    }
  ]
}
```
4. Los posibles códigos de error
404: el cine solicitado no existe.
422: alguno de los parámetros enviados tiene un formato incorrecto.
500: ocurrió un error inesperado en el servidor.

# Problema B — Corregir errores
```python
@router.post("/movies")
async def create_movie(data: dict):
    movie = Movie(
        title=data["title"],
        release_date=data["release_date"],
        distributor=data["distributor"],
    )
    db.add(movie)
    db.commit()
    return movie
```

1. Validación del input: data se recibe como un dict genérico. Usaría un modelo de Pydantic para validar los campos antes de crear la película.
2. Base de datos: se usa db, pero no se define ni se recibe. Lo inyectaría con Depends(get_db).
3. async/sync: el endpoint es async, pero las operaciones de base de datos son síncronas. Usaría def o una sesión asíncrona con await, según corresponda.
4. Manejo de errores: falta controlar qué pasa si falla el guardado. Agregaría try/except y rollback() en caso de error.

# Problema C — ¿Cuál es la diferencia?

1. GET vs POST

GET: se usa para consultar u obtener información del servidor sin modificarla.
POST: se usa para enviar información al servidor, normalmente para crear un nuevo recurso.

2. Status code 400 vs 422 vs 500

400: la solicitud es incorrecta o está mal formada.
422: la solicitud llegó correctamente, pero alguno de los datos no cumple con la validación esperada.
500: ocurrió un error inesperado del lado del servidor.

3. Path param (/movies/{id}) vs query param (/movies?format=IMAX)

Path param: identifica un recurso específico dentro de la ruta.
Query param: se utiliza para filtrar o modificar una consulta.