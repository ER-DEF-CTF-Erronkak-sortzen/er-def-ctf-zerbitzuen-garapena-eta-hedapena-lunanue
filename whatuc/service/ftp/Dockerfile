# Usa una imagen base de Debian o Ubuntu
FROM ubuntu:latest

# Instala vsftpd
RUN apt-get update && apt-get install -y vsftpd

# Copia el archivo de configuración personalizado de vsftpd (si tienes uno)
COPY vsftpd.conf /etc/vsftpd.conf

# Crea una carpeta para los archivos FTP
RUN mkdir -p /home/blue/ftp/files

COPY rosesarered.txt /home/blue/ftp/files/rosesarered.txt

# Da permisos y crea el usuario de FTP
RUN useradd -m blue && echo "blue:1234" | chpasswd && \
    chown blue:blue /home/blue/ftp -R

# Expone el puerto 21 para FTP
EXPOSE 21

# Ejecuta el servicio vsftpd en segundo plano
CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]