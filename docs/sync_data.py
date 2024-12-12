from sqlalchemy import create_engine, MetaData, Table
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = f"{os.getenv("DB_CNN")}"

# Configuración de Elasticsearch
ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "events"

# Conectar a PostgreSQL
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)  # Reflejar todas las tablas en la base de datos
events_table = metadata.tables.get("events")

if events_table is None:
    raise ValueError("La tabla 'events' no existe en la base de datos.")

# Conectar a Elasticsearch
es = Elasticsearch(ELASTICSEARCH_URL)


def fetch_events():
    """Obtiene los datos de la tabla 'events' desde PostgreSQL."""
    with engine.connect() as conn:
        query = events_table.select()
        result = conn.execute(query)
        for row in result.mappings():  # Usar .mappings() para convertir las filas en RowMappings
            event = dict(row)
            if "status" not in event:  # Validación
                raise ValueError(f"El campo 'status' no está presente en el evento: {event}")
            yield event


def index_events():
    """Sincroniza los datos desde PostgreSQL a Elasticsearch."""
    # Eliminar índice existente si estás reiniciando la sincronización
    es.indices.delete(index=INDEX_NAME, ignore=[400, 404])

    # Crear nuevo índice
    es.indices.create(index=INDEX_NAME, ignore=400)

    events = fetch_events()
    actions = []
    for event in events:
        actions.append({
            "_index": INDEX_NAME,
            "_id": event["id"],
            "_source": event
        })
    
    # Indexar en Elasticsearch usando helpers.bulk
    helpers.bulk(es, actions)
    print(f"Sincronización completa: {len(actions)} registros indexados.")

if __name__ == "__main__":
    index_events()
