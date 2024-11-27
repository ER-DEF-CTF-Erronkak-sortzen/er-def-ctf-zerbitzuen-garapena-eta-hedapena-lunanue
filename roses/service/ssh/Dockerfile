FROM ubuntu:latest
RUN apt update && apt install -y openssh-server

# Create user
RUN useradd -m blue && echo "blue:1234" | chpasswd

# Configure SSH
RUN mkdir /var/run/sshd

COPY rosesarered.txt /root/home/rosesarered.txt

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]