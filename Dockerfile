# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias 
RUN pip install Flask mysql-connector-python

# Copia el archivo de la aplicación a la imagen
COPY app.py .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]