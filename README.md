# Práctica Formativa Obligatoria N 2

## Instrucciones

1. Clonar el repositorio:
2. Construir y levantar los contenedores:

docker-compose up --build

3. Abrir la aplicación en el navegador:
   http://localhost:5000

## Servicios

Web (Flask): puerto 5000 → contenedor corre en 80

MySQL: puerto 3306, base de datos docker_db

## Notas

Las credenciales se configuran mediante el archivo .env

Los contenedores están definidos en docker-compose.yml

## Imagen Docker

- La imagen de este proyecto está subida a Docker Hub y se puede descargar con:

docker pull rosinaer/pfo_2_devops:latest

- Luego se puede levantar con:

docker run -p 5000:80 rosinaer/pfo_2_devops:latest
