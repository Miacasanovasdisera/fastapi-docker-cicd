# Usamos una versión de Python optimizada para contenedores
FROM python:3.10-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Primero copiamos los requirements para aprovechar el caché de Docker
COPY requirements.txt .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de nuestro código
COPY . .

# Exponemos el puerto 8000 que es donde corre FastAPI
EXPOSE 8000

# Comando para ejecutar nuestra aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]