# Documentación de la API de Notificación de Mensajes

## Descripción General
La **API de Notificación de Mensajes** permite enviar mensajes de texto personalizados a whatsapp a través de un endpoint sencillo. A continuación, se detalla la documentación del servicio.

## URL Base
```
http://localhost:8007/
```

## Endpoints

### 1. Enviar Mensaje
**Descripción:** Envía un mensaje de texto a un número de whatsapp específico.

- **Método:** `POST`
- **Endpoint:** `/send_message/`
- **Encabezados:**
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Cuerpo:**
  ```json
  {
    "phone": "<string>",
    "message": "<string>"
  }
  ```
  **Ejemplo:**
  ```json
  {
    "phone": "3166245403",
    "message": "La hora de inicio del evento ha sido reprogramada para las 20:00"
  }
  ```
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "status": "Message sent successfully",
      "phone": "3166245103",
      "message": "La hora de inicio del evento ha sido reprogramada para las 20:00"
    }
    ```
  - **422 Unprocessable Entity:**
    ```json
    {
      "detail": [
        {
          "loc": ["body", "phone"],
          "msg": "Número de teléfono inválido",
          "type": "value_error"
        },
        {
          "loc": ["body", "message"],
          "msg": "El mensaje no puede estar vacío",
          "type": "value_error"
        }
      ]
    }
    ```

## Ejemplo CURL

### Ejemplo de Envío de Mensaje:
```bash
curl -X 'POST' \
  'http://localhost:8007/send_message/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone": "3166245103",
  "message": "La hora de inicio del evento ha sido reprogramada para las 20:00"
}'
```

## Notas
- El campo `phone` debe contener un número de teléfono válido en formato internacional o local.
- El campo `message` debe ser una cadena no vacía con el contenido del mensaje a enviar, puede incluir * o _ para dar formato al texto de whatsapp.
