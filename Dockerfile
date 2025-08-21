# Dockerfile

# Etapa 1: Imagen base
FROM python:3.11-slim-bookworm

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema si fueran necesarias (para este proyecto no se necesitan)
# RUN apt-get update && apt-get install -y ...

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto al contenedor
COPY . .

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer el puerto en el que Gunicorn se ejecutará
EXPOSE 8000

# Comando para iniciar la aplicación en producción
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]