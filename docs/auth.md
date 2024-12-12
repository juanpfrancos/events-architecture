# Documentación de la API de Servicio de Autenticación

## Descripción General
La **API de Servicio de Autenticación** permite registrar usuarios y gestionar la autenticación mediante JWT.

## URL Base
```
http://localhost:8009/
```

## Endpoints

### 1. Registrar Usuario
**Descripción:** Registra un nuevo usuario en el sistema.

- **Método:** `POST`
- **Endpoint:** `/auth/register`
- **Encabezados:**
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Cuerpo:**
  ```json
  {
    "username": "<string>",
    "email": "<email>",
    "first_name": "<string>",
    "last_name": "<string>",
    "phone_number": "<string>",
    "role": "<string>",
    "password": "<string>"
  }
  ```
  **Ejemplo:**
  ```json
  {
    "username": "Pedro",
    "email": "pedro@example.com",
    "first_name": "Fernandez",
    "last_name": "Pérez",
    "phone_number": "3211223399",
    "role": "Admin",
    "password": "QWSWQe23ed343455"
  }
  ```
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "username": "Pedro",
      "email": "pedro@example.com",
      "first_name": "Fernandez",
      "last_name": "Pérez",
      "phone_number": "3211223399",
      "role": "Admin",
      "id": 1
    }
    ```
  - **422 Unprocessable Entity:**
    ```json
    {
      "detail": [
        {
          "loc": ["body", "email"],
          "msg": "El correo electrónico ya está registrado",
          "type": "value_error"
        },
        {
          "loc": ["body", "password"],
          "msg": "La contraseña no cumple con los requisitos",
          "type": "value_error"
        }
      ]
    }
    ```

### 2. Iniciar Sesión
**Descripción:** Genera un token de acceso para un usuario autenticado.

- **Método:** `POST`
- **Endpoint:** `/auth/login`
- **Parámetros de Consulta:**
  - `username` (cadena, requerido): Nombre de usuario.
  - `password` (cadena, requerido): Contraseña.
- **Encabezados:**
  - `Accept: application/json`
- **Respuestas:**
  - **200 OK:**
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "token_type": "Bearer"
    }
    ```
  - **422 Unprocessable Entity:**
    ```json
    {
      "detail": [
        {
          "loc": ["query", "username"],
          "msg": "Usuario no encontrado",
          "type": "value_error"
        },
        {
          "loc": ["query", "password"],
          "msg": "Contraseña incorrecta",
          "type": "value_error"
        }
      ]
    }

## Ejemplo CURL

### Ejemplo de Registro de Usuario:
```bash
curl -X 'POST' \
  'http://localhost:8009/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "Pedro",
  "email": "pedro@example.com",
  "first_name": "Fernandez",
  "last_name": "Pérez",
  "phone_number": "3211223399",
  "role": "Admin",
  "password": "QWSWQe23ed343455"
}'
```

### Ejemplo de Inicio de Sesión:
```bash
curl -X 'POST' \
  'http://localhost:8009/auth/login?username=Pedro&password=QWSWQe23ed343455' \
  -H 'accept: application/json' \
  -d ''
