# Usar la imagen base oficial de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de configuración de Poetry y las dependencias
COPY pyproject.toml poetry.lock /app/

# Instalar Poetry
RUN pip install --no-cache-dir poetry

# Instalar las dependencias del proyecto
RUN poetry install --no-dev --no-root

# Copiar el código fuente al contenedor
COPY . /app

# Exponer el puerto donde corre FastAPI
EXPOSE 8007

# Comando para ejecutar el servidor de FastAPI
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8007"]
