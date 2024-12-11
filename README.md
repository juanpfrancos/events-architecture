# events-architecture




## Arquitectura

![Diagrama](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Diagram.webp)

## Microservicio de registro y autenticación

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Authorization%20Service.postman_collection.json)


## Microservicio de Gestión de Eventos (CRUD)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Event%20Management%20Service.postman_collection.json)

## Microservicio de Gestión de Eventos (CRUD)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Message%20Notification%20Service.postman_collection.json)


## Build microservicios

1. Inicializar :
   ```
    sudo docker-compose up --build
   ```
---

## Migraciones con Alembic

1. **Inicializar Alembic**:
   ```bash
   alembic init migrations

   ```

2. Configura el archivo `alembic.ini`:
   ```ini
   sqlalchemy.url = postgresql://user:password@localhost:5432/event_db
   ```

3. Genera una migración:
   ```bash
   alembic revision --autogenerate -m "Create events table"
   ```

4. Aplica la migración:
   ```bash
   alembic upgrade head
   
   ```

---
