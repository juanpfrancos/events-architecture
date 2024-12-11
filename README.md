# events-architecture




## Arquitectura

![Diagrama](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Diagram.webp)

## Microservicio de Gestión de Eventos

## Migraciones con Alembic

1. Inicializar :
   ```
    sudo docker-compose up --build
   ```

2. Hacer build:
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
   
   from model import Base 
   target_metadata = Base.metadata
   
   sqlalchemy.url = postgresql+psycopg2://testuser:P4ssw0rd1234@localhost:5433/events_db
   
   ```

---
