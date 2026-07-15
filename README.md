-> Weather API - Cloud & DevOps Pipeline

¡Hola! Soy estudiante de Ingeniería en Informática en la UNMDP. Este proyecto forma parte de mi portfolio profesional y tiene como objetivo demostrar la implementación de buenas prácticas de DevOps, automatización de CI/CD y despliegue de software mediante contenedores.

-> Arquitectura y Enfoque

Más que una simple API REST, este proyecto sirve como sandbox para explorar la paridad de entornos (Dev vs Prod) y la automatización de flujos de trabajo.

Backend: Desarrollado en Python con FastAPI.

Containerización: Empaquetado con Docker para garantizar consistencia entre entornos.

CI/CD: Pipeline automatizado con GitHub Actions. Cada commit a main valida la integridad del build y la construcción de la imagen de Docker.

-> Stack Tecnológico

Backend: Python 3.10+, FastAPI, Uvicorn, httpx.

Infraestructura: Docker (Dockerfile).

Automatización: GitHub Actions (CI Pipeline).

Cloud: Despliegue automatizado.

-> Guía de inicio rápido

Ejecución Local con Docker

Clonar el repositorio:

git clone https://github.com/Miacasanovasdisera/fastapi-docker-cicd.git
cd fastapi-docker-cicd


Construir y correr:

docker build -t weather-api .
docker run -d -p 8000:8000 weather-api


La documentación interactiva (Swagger UI) estará disponible en: http://localhost:8000/docs

Autor

Mia Casanovas Di Sera - Estudiante de Ingeniería en Informática (UNMDP)

https://www.linkedin.com/in/mia-casanovas-di-sera-b1b865296/?skipRedirect=true