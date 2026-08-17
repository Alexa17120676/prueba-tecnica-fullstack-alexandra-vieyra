Prueba Técnica Full Stack

Alexandra Vieyra Xicohténcatl

Esta entrega contiene las soluciones de las cuatro secciones de la prueba técnica, además de algunas validaciones y una implementación funcional para facilitar la revisión.

Estructura

- seccion1.py
  - Problema A: agrupación de funciones por película.
  - Problema B: validación de horarios.

- tests/test_seccion1.py
  - Pruebas automáticas para validar los ejercicios de Python.

- seccion2.sql
  - Queries de PostgreSQL e índices propuestos.

- seccion3.md
  - Diseño del endpoint, análisis de errores y conceptos REST.

- seccion3_api/
  - Implementación funcional con FastAPI del endpoint propuesto.
  - Incluye Swagger y un endpoint adicional de semanas para integrar el frontend.

- seccion4/
  - Componente WeekSelector desarrollado con React y TypeScript.
  - Consume el endpoint de semanas de FastAPI.

- seccion4_problemaB.md
  - Identificación y corrección de los errores del Problema B de React.


Python

Ejecutar la solución:

python3 seccion1.py

Ejecutar pruebas:

python3 -m unittest discover -s tests -v


Backend - FastAPI

Entrar a la carpeta:

cd seccion3_api

Crear entorno virtual:

python3 -m venv .venv

Activarlo:

source .venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Levantar la API:

uvicorn main:app --reload

Swagger:

http://127.0.0.1:8000/docs


Frontend - React + TypeScript

En otra terminal:

cd seccion4

Instalar dependencias:

npm install

Levantar el frontend:

npm run dev

Abrir:

http://localhost:5173


Validaciones realizadas

- 5 pruebas de Python ejecutadas correctamente.
- Endpoint de cine probado con respuesta 200.
- Query param date probado correctamente.
- Cine inexistente probado con respuesta 404.
- Endpoint de semanas probado correctamente.
- React conectado con FastAPI.
- npm run build ejecutado correctamente.
- npm run lint ejecutado correctamente.