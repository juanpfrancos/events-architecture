# Events App


## Preparar entorno

1. Clonar repositorio :
   ```
   git clone https://github.com/juanpfrancos/events-architecture.git
   ```
2. Agregar variables de entorno :
   Se debe crear un archivo .env en el directorio raíz y pegar dentro de él las variables de entorno adjuntas en el email.   
   
   ### Estructura directorio
   ![Estructura](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs//Structure.PNG)

---
## Build microservicios

1. Inicializar :
   ```
    sudo docker-compose up --build
   ```
---

## Generar eventos con data de prueba

1. Generar eventos :
   
   [generate_events.py](https://github.com/juanpfrancos/events-architecture/blob/main/docs/generate_events.py)

2. Sincronizar data existente :
   
   [sync_data.py](https://github.com/juanpfrancos/events-architecture/blob/main/docs/sync_data.py)

---





## Arquitectura

![Diagrama](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Diagram.webp)

## Microservicio de registro y autenticación

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Authorization%20Service.postman_collection.json)


## Microservicio de Gestión de Eventos (CRUD)

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Event%20Management%20Service.postman_collection.json)

## Microservicio de Notificaciones

[Postman Collection](https://raw.githubusercontent.com/juanpfrancos/events-architecture/refs/heads/main/docs/Message%20Notification%20Service.postman_collection.json)

