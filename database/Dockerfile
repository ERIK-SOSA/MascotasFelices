# Utilizamos la imagen oficial de PostgreSQL con la versión 12.18 y Alpine 3.18 como base
FROM postgres:15-alpine3.18

# Etiqueta de autor para identificar al creador del Dockerfile
LABEL maintainer="Erik <erik@email.com>"

# Definimos variables de entorno para configurar la base de datos
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mysecretpassword

# Exponemos el puerto 5432 para permitir conexiones externas a la base de datos
EXPOSE 5432

# Copiamos un script SQL personalizado al directorio de Docker-entrypoint-initdb.d
# Este script se ejecutará al inicializar la base de datos para realizar configuraciones adicionales si es necesario
COPY init.sql /docker-entrypoint-initdb.d/

# Cambiamos el usuario a 'postgres' para garantizar la ejecución de los comandos siguientes como usuario de PostgreSQL
USER postgres