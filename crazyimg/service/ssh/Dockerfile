FROM ubuntu:latest
RUN apt update && apt install -y openssh-server steghide

# Create user
RUN useradd -m oneimg && echo "oneimg:1000w3rd5" | chpasswd

COPY crazyimg.jpeg /tmp/crazyimg.jpeg

# Configure SSH
RUN mkdir /var/run/sshd

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]