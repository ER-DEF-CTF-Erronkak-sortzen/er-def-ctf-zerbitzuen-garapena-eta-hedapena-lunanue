FROM ubuntu:latest
RUN apt update && apt install -y openssh-server

# Create user
RUN useradd -m blue && echo "blue:1234" | chpasswd

COPY rosesarered.txt /home/blue/rosesarered.txt

# Configure SSH
RUN mkdir /var/run/sshd

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]