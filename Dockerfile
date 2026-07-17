#Usamos una versión de Python optimizada para contenedores

FROM python:3.10-slim

#Definimos el directorio de trabajo dentro del contenedor

WORKDIR /app

#Primero copiamos los requirements para aprovechar el caché de Docker

COPY requirements.txt .

#Instalamos las librerías

RUN pip install --no-cache-dir -r requirements.txt

#Copiamos el resto de nuestro código

COPY . .

#Exponemos el puerto 8000 (solo como referencia documental)

EXPOSE 8000

#Usamos formato 'shell' para que pueda leer la variable de entorno PORT que inyecta Render

#Si PORT no existe (como en tu compu local), usa el 8000 por defecto.

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}