# Events App


## 1. Preparar entorno

1. Clonar repositorio :
   ```
   git clone https://github.com/juanpfrancos/events-architecture.git
   ```
2. Agregar variables de entorno :
   Se debe crear un archivo .env en el directorio raíz y pegar dentro de él las variables de entorno adjuntas en el email.   
   
   ### Estructura directorio
   ![Estructura](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs//Structure.PNG)

---
## 2. Build microservicios

1. Inicializar :
   ```
    sudo docker-compose up --build
   ```
---

## Generar eventos con data de prueba

1. Generar eventos :
   
   He añadido un script con el propósito de crear eventos de forma automatizada con datos de prueba.
   Lo ideal es ejecutarlo apenas todos los microservicios estén inicializados.

   [generate_events.py](https://github.com/juanpfrancos/events-architecture/blob/main/docs/generate_events.py)

2. Sincronizar data existente :
   
   Si ya existen datos en la db o se han agregado regstros desde otra fuente diferente a la api, lo ideal es ejecutar este script para sincronizar la data de la db a Elasticsearch.

   [sync_data.py](https://github.com/juanpfrancos/events-architecture/blob/main/docs/sync_data.py)

---





## Arquitectura

![Diagrama](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Diagram.webp)

Mientras los microservicios están revantados se puede acceder a la documentación de las apis a través de  `swagger`y `redoc` .

## Microservicio de registro y autenticación

[Documentación Markdown](https://github.com/juanpfrancos/events-architecture/blob/main/docs/auth.md)

[Redoc](http://localhost:8009/redoc)

[Swagger](http://localhost:8009/docs)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Authorization%20Service.postman_collection.json)


## Microservicio de Gestión de Eventos (CRUD)
[Documentación Markdown](https://github.com/juanpfrancos/events-architecture/blob/main/docs/crud.md)

[Redoc](http://localhost:8008/redoc)

[Swagger](http://localhost:8008/docs)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Event%20Management%20Service.postman_collection.json)

## Microservicio de Notificaciones
[Documentación Markdown](https://github.com/juanpfrancos/events-architecture/blob/main/docs/messages.md)

[Redoc](http://localhost:8007/redoc)

[Swagger](http://localhost:8007/docs)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Message%20Notification%20Service.postman_collection.json)

### **API Gateway**

#### **Probar las operaciones GraphQL**
Se puede ingresar al playgraund de Graphql y Strawberry desde el navegador en `http://localhost:8005/graphql`. Y realizar las consultas y mutaciones. 
##### **Query: Obtener todos los eventos**
```graphql
query {
  events {
    id
    title
    location
    start_time
    end_time
  }
}
```

##### **Query: Buscar evento por ID**
```graphql
query {
  event(eventId: 1) {
    title
    description
    location
  }
}
```

##### **Query: Búsqueda full-text**
```graphql
query {
  fullTextSearch(query: "conference") {
    id
    title
    description
  }
}
```

##### **Mutation: Crear un evento**
```graphql
mutation {
  createEvent(
    title: "Nuevo evento"
    description: "Detalle del evento"
    location: "Online"
    startTime: "2024-12-20T10:00:00"
    endTime: "2024-12-20T12:00:00"
    capacity: 100
  ) {
    id
    title
    status
  }
}
```

##### **Mutation: Enviar una notificación**
```graphql
mutation {
  sendNotification(phone: "3166234530", message: "Recordatorio de evento") 
}
```

---

### **Documentación de parámetros**

| **Operación**         | **Tipo**  | **Parámetro**           | **Tipo de Dato** | **Descripción**                                   |
|-----------------------|-----------|-------------------------|------------------|--------------------------------------------------|
| `events`             | Query     | -                       | -                | Devuelve todos los eventos disponibles.          |
| `event`              | Query     | `eventId`               | `int`            | ID del evento que se desea obtener.             |
| `fullTextSearch`     | Query     | `query`                 | `str`            | Texto a buscar en los eventos.                  |
| `createEvent`        | Mutation  | `title`, `description`, `location`, `startTime`, `endTime`, `capacity` | Varios | Crea un nuevo evento con la información proporcionada. |
| `updateEvent`        | Mutation  | `eventId`, `title`, `description`, `location`, `startTime`, `endTime`, `capacity`, `status` | Varios | Actualiza un evento existente.                  |
| `deleteEvent`        | Mutation  | `eventId`               | `int`            | Elimina un evento por su ID.                    |
| `sendNotification`   | Mutation  | `phone`, `message`      | `str`, `str`     | Envía una notificación a un número de teléfono. |


# Documentación Elasticsearch 

## Índice: `events`

## Propósito
El índice `events` se utiliza para almacenar información de eventos sincronizados desde la base de datos PostgreSQL. Permite realizar búsquedas full-text y aplicar filtros avanzados basados en fechas, ubicación, capacidad, y estado.

---

## Configuración del Índice
El índice se crea con los siguientes parámetros:

```json
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "standard"
      },
      "description": {
        "type": "text",
        "analyzer": "standard"
      },
      "location": {
        "type": "keyword"
      },
      "start_time": {
        "type": "date"
      },
      "end_time": {
        "type": "date"
      },
      "capacity": {
        "type": "integer"
      },
      "attendees_registered": {
        "type": "integer"
      },
      "status": {
        "type": "keyword"
      },
      "created_at": {
        "type": "date"
      },
      "updated_at": {
        "type": "date"
      }
    }
  }
}
```

---

## Estructura de los Campos

### Campos Principales:

| Campo                 | Tipo     | Descripción                                                        |
|-----------------------|----------|----------------------------------------------------------------------|
| `title`               | `text`   | Título del evento. Soporta búsqueda full-text.                     |
| `description`         | `text`   | Descripción del evento. Soporta búsqueda full-text.                 |
| `location`            | `keyword`| Ubicación del evento. Ideal para filtros exactos.                   |
| `start_time`          | `date`   | Fecha y hora de inicio del evento.                                   |
| `end_time`            | `date`   | Fecha y hora de finalización del evento.                            |
| `capacity`            | `integer`| Capacidad máxima de asistentes al evento.                           |
| `attendees_registered`| `integer`| Cantidad actual de asistentes registrados.                          |
| `status`              | `keyword`| Estado del evento: `planned`, `ongoing`, `completed`, `cancelled`.  |
| `created_at`          | `date`   | Fecha de creación del registro.                                     |
| `updated_at`          | `date`   | Fecha de la última actualización del registro.                      |

---

## Ejemplo de Documento
Un documento almacenado en el índice `events` se vería de la siguiente forma:

```json
{
  "title": "Conferencia de Tecnología 2024",
  "description": "Una conferencia sobre avances en inteligencia artificial.",
  "location": "Bogotá",
  "start_time": "2024-12-15T09:00:00+00:00",
  "end_time": "2024-12-15T17:00:00+00:00",
  "capacity": 500,
  "attendees_registered": 120,
  "status": "planned",
  "created_at": "2024-12-01T12:34:56+00:00",
  "updated_at": "2024-12-05T14:45:30+00:00"
}
```

---

## Creación del Índice
El índice puede ser creado mediante el siguiente script:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch()

def create_events_index():
    index_name = "events"
    if not es.indices.exists(index=index_name):
        mappings = {
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "description": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "location": {
                        "type": "keyword"
                    },
                    "start_time": {
                        "type": "date"
                    },
                    "end_time": {
                        "type": "date"
                    },
                    "capacity": {
                        "type": "integer"
                    },
                    "attendees_registered": {
                        "type": "integer"
                    },
                    "status": {
                        "type": "keyword"
                    },
                    "created_at": {
                        "type": "date"
                    },
                    "updated_at": {
                        "type": "date"
                    },
                }
            }
        }
        es.indices.create(index=index_name, body=mappings)
        print(f"indice '{index_name}' creado correctamente.")
    else:
        print(f"El indice '{index_name}' ya existe.")

create_events_index()
```

---

## Uso de Kibana (Opcional)
Si desea tener mayor control de las búsquedas, ejecutar casos de prueba puede hacerlo desde Kibana agregando estas lineas dentro de `docker-compose.yaml` detenga los microservicios y vuelva a levantarlos con el paso `2. Build microservicios`:

```
      kibana:
    image: docker.elastic.co/kibana/kibana:8.10.1
    ports:
      - "5601:5601"
    depends_on:
      elasticsearch:
        condition: service_healthy
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    networks:
      - backend
    restart: unless-stopped

```

## Migraciones con Alembic
También se realizaron migraciones con Alembic en los microservicios `events_service` y `auth_service` Siguiento los pasos:

1. **Inicializar Alembic**:

```
    alembic init migrations
```

2. Configura el archivo con la cadena de conexión a DB `alembic.ini`:

```
    sqlalchemy.url = postgresql://user:password@localhost:5432/event_db
```

3. Genera una migración:
```
    alembic revision --autogenerate -m "Migration description"
```


4. Aplica la migración:
```
    alembic upgrade head
```
  
Si se van a realizar cambios en el modelo, después de realizar los cambios solo es necesario ejecutar el paso `3` y `4`. Con esto quedará lista la nueva migración