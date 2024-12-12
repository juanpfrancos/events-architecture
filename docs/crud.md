# Documentación de la API de Gestión de Eventos

## Descripción General
La **API de Gestión de Eventos** permite crear, administrar y buscar eventos. A continuación, se detalla la documentación de los endpoints disponibles.

## URL Base
```
http://localhost:8008/
```

## Endpoints

### 1. Obtener Evento por ID
**Descripción:** Recupera los detalles de un evento específico.

- **Método:** `GET`
- **Endpoint:** `/events/:event_id`
- **Parámetros de Ruta:**
  - `event_id` (entero, requerido): ID del evento.
- **Encabezados:**
  - `Accept: application/json`
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "title": "Concierto",
      "location": "Bogotá",
      "start_time": "2024-12-15T19:00:00.000Z",
      "end_time": "2024-12-15T22:00:00.000Z",
      "capacity": 500,
      "id": 101,
      "attendees_registered": 450,
      "status": "confirmed",
      "created_at": "2024-11-01T12:00:00.000Z",
      "updated_at": "2024-11-05T10:00:00.000Z",
      "description": "Un evento musical en vivo."
    }
    ```
  - **422 Unprocessable Entity:**
    ```json
    {
      "detail": [
        {
          "loc": ["body", "event_id"],
          "msg": "ID inválido",
          "type": "value_error"
        }
      ]
    }
    ```

### 2. Actualizar Evento
**Descripción:** Actualiza los detalles de un evento específico.

- **Método:** `PUT`
- **Endpoint:** `/events/:event_id`
- **Parámetros de Ruta:**
  - `event_id` (entero, requerido): ID del evento.
- **Encabezados:**
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Cuerpo:**
  ```json
  {
    "title": "Nuevo Evento",
    "description": "Descripción actualizada",
    "location": "Medellín",
    "start_time": "2024-12-20T18:00:00.000Z",
    "end_time": "2024-12-20T21:00:00.000Z",
    "capacity": 600,
    "status": "cancelled"
  }
  ```
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "title": "Nuevo Evento",
      "location": "Medellín",
      "start_time": "2024-12-20T18:00:00.000Z",
      "end_time": "2024-12-20T21:00:00.000Z",
      "capacity": 600,
      "id": 5101,
      "attendees_registered": 300,
      "status": "cancelled",
      "created_at": "2024-11-10T12:00:00.000Z",
      "updated_at": "2024-11-15T14:00:00.000Z",
      "description": "Descripción actualizada"
    }
    ```
  - **422 Unprocessable Entity:** Mismo formato que en "Obtener Evento por ID".

### 3. Eliminar Evento
**Descripción:** Elimina un evento específico.

- **Método:** `DELETE`
- **Endpoint:** `/events/:event_id`
- **Parámetros de Ruta:**
  - `event_id` (entero, requerido): ID del evento.
- **Encabezados:**
  - `Accept: application/json`
- **Respuestas:**
  - **204 No Content:** Sin cuerpo.
  - **422 Unprocessable Entity:** Mismo formato que en "Obtener Evento por ID".

### 4. Obtener Todos los Eventos
**Descripción:** Recupera una lista de todos los eventos.

- **Método:** `GET`
- **Endpoint:** `/events/`
- **Encabezados:**
  - `Accept: application/json`
- **Respuestas:**
  - **200 OK:**
    ```json
    [
      {
        "title": "Conferencia de Tecnología",
        "location": "Cali",
        "start_time": "2024-12-10T09:00:00.000Z",
        "end_time": "2024-12-10T17:00:00.000Z",
        "capacity": 300,
        "id": 102,
        "attendees_registered": 250,
        "status": "confirmed",
        "created_at": "2024-10-01T12:00:00.000Z",
        "updated_at": "2024-11-01T10:00:00.000Z",
        "description": "Evento enfocado en tendencias tecnológicas."
      }
    ]
    ```

### 5. Crear Evento
**Descripción:** Crea un nuevo evento.

- **Método:** `POST`
- **Endpoint:** `/events/`
- **Encabezados:**
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Cuerpo:**
  ```json
  {
    "title": "Nuevo Evento",
    "description": "Descripción del evento",
    "location": "Pereira",
    "start_time": "2024-12-12T15:12:44.838Z",
    "end_time": "2024-12-12T18:12:44.838Z",
    "capacity": 600
  }
  ```
- **Respuestas:**
  - **200 OK:** Mismo formato que "Obtener Evento por ID".
  - **422 Unprocessable Entity:** Mismo formato que "Obtener Evento por ID".

#### Ejemplo CURL:
```bash
curl -X 'POST' \
  'http://localhost:8008/events/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Nuevo Evento",
  "description": "Descripción del evento",
  "location": "Pereira",
  "start_time": "2024-12-12T15:12:44.838Z",
  "end_time": "2024-12-12T18:12:44.838Z",
  "capacity": 600
}'
```

### 6. Búsqueda de Texto Completo
**Descripción:** Busca eventos utilizando una consulta de texto.

- **Método:** `GET`
- **Endpoint:** `/events/search/full-text`
- **Parámetros de Consulta:**
  - `query` (cadena, requerido): Término de búsqueda.
- **Encabezados:**
  - `Accept: application/json`
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "results": [
        {
          "title": "Evento de Prueba",
          "location": "Manizales",
          "start_time": "2024-12-11T14:00:00.000Z",
          "end_time": "2024-12-11T16:00:00.000Z",
          "id": 103
        }
      ]
    }
    ```
  - **422 Unprocessable Entity:** Mismo formato que "Obtener Evento por ID".
