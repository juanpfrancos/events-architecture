from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")
"""
   Create index 'events' with their mappings
"""
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
        print(f"Índice '{index_name}' creado correctamente.")
    else:
        print(f"El índice '{index_name}' ya existe.")

if __name__ == "__main__":
    create_events_index()
