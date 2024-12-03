# Usa la imagen oficial de MySQL
FROM mysql:latest

# Establece una contraseña para el usuario root 
ENV MYSQL_ROOT_PASSWORD=rootpass

# Copia el script SQL que creará la base de datos y la tabla
COPY init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto 3306 (el puerto predeterminado de MySQL)
EXPOSE 3306
