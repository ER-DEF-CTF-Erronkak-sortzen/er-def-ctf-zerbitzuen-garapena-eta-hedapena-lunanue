#!/usr/bin/env python3

from ctf_gameserver import checkerlib
import logging
import http.client
import socket
import paramiko
import hashlib
PORT_WEB = 80
PORT_SSH = 2200
PORT_WWW = 8888
def ssh_connect():
    def decorator(func):
        def wrapper(*args, **kwargs):
            # SSH connection setup
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            rsa_key = paramiko.RSAKey.from_private_key_file(f'/keys/team{args[0].team}-sshkey')
            client.connect(args[0].ip, username = 'root', pkey=rsa_key)

            # Call the decorated function with the client parameter
            args[0].client = client
            result = func(*args, **kwargs)

            # SSH connection cleanup
            client.close()
            return result
        return wrapper
    return decorator

class MyChecker(checkerlib.BaseChecker):

    def __init__(self, ip, team):
        checkerlib.BaseChecker.__init__(self, ip, team)
        self._baseurl = f'http://[{self.ip}]:{PORT_WEB}'
        logging.info(f"URL: {self._baseurl}")

    @ssh_connect()
    def place_flag(self, tick):
        flag = checkerlib.get_flag(tick)
        creds = self._add_new_flag(self.client, flag)
        if not creds:
            return checkerlib.CheckResult.FAULTY
        logging.info('created')
        checkerlib.store_state(str(tick), creds)
        checkerlib.set_flagid(str(tick))
        return checkerlib.CheckResult.OK

    def check_service(self):
        # check if ports are open
        if not self._check_port_web(self.ip, PORT_WEB) or not self._check_port_ssh(self.ip, PORT_SSH) or not self._check_port_web(self.ip, PORT_WWW):
            return checkerlib.CheckResult.DOWN
        #else
        # check if server is Apache 2.4.50 only for docker-3 (roses_www)
        if not self._check_apache_version():
            return checkerlib.CheckResult.FAULTY
        # check if blue user exists in roses_ssh docker
        if not self._check_ssh_user('blue'):
            return checkerlib.CheckResult.FAULTY
        file_path_web = '/var/www/html/index.html'
        # check if index.hmtl from roses_web has been changed by comparing its hash with the hash of the original file
        if not self._check_web_integrity(file_path_web):
            return checkerlib.CheckResult.FAULTY
        #file_path_web = '/var/www/html/rosesarered.png'
        # check if rosesarered.png image from roses_web has been changed by comparing its hash with the hash of the original file
        #if not self._check_web_integrity(file_path_web):
        #    return checkerlib.CheckResult.FAULTY
        file_path_ssh = '/etc/ssh/sshd_config'
        # check if /etc/sshd_config from roses_ssh has been changed by comparing its hash with the hash of the original file
        if not self._check_ssh_integrity(file_path_ssh):
            return checkerlib.CheckResult.FAULTY            
        file_path_web = '/var/www/html/index.html'
        # check if index.hmtl from roses_www has been changed by comparing its hash with the hash of the original file
        if not self._check_www_integrity(file_path_web):
            return checkerlib.CheckResult.FAULTY  
        file_path_web = '/var/www/html/flaggy.php'
        # check if index.hmtl from roses_www has been changed by comparing its hash with the hash of the original file
        if not self._check_www_integrity(file_path_web):
            return checkerlib.CheckResult.FAULTY
        file_path_web = '/var/www/html/dontlookhere.txt'
        # check if the permissions of the file dontlookhere.txt (where flags are placed) from roses_www has been changed 
        if not self._check_www_permissions(file_path_web):
            return checkerlib.CheckResult.FAULTY  
        return checkerlib.CheckResult.OK     
    
    def check_flag(self, tick):
        if not self.check_service():
            return checkerlib.CheckResult.DOWN
        flag = checkerlib.get_flag(tick)
        #creds = checkerlib.load_state("flag_" + str(tick))
        # if not creds:
        #     logging.error(f"Cannot find creds for tick {tick}")
        #     return checkerlib.CheckResult.FLAG_NOT_FOUND
        flag_present = self._check_flag_present(flag)
        if not flag_present:
            return checkerlib.CheckResult.FLAG_NOT_FOUND
        return checkerlib.CheckResult.OK
        
    @ssh_connect()
    #Function to check if an user exists
    def _check_ssh_user(self, username):
        ssh_session = self.client
        command = f"docker exec roses_ssh_1 sh -c 'id {username}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        print("CHECK SSH USER")
        if stderr.channel.recv_exit_status() != 0:
            return False
        return True
    
    @ssh_connect()
    def _check_web_integrity(self, path):
        ssh_session = self.client
        command = f"docker exec roses_web_1 sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        print("CHECK WEB INTEGRITY")
        print(path)
        if stderr.channel.recv_exit_status() != 0:
            return False
        output = stdout.read().decode().strip()
        print(hashlib.md5(output.encode()).hexdigest())
        return hashlib.md5(output.encode()).hexdigest() == 'cf7dd307bdfefb3b07fdee7cb886405b' or '9b6deaf36a9ba3e6df246047d8c3bcc3' or 'e0581dbe8e7a5dcdcf63c2a1d1576bdf'
    
    @ssh_connect()
    def _check_ssh_integrity(self, path):
        ssh_session = self.client
        command = f"docker exec roses_ssh_1 sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        print("CHECK SSH INTEGRITY")
        if stderr.channel.recv_exit_status() != 0:
            return False
        output = stdout.read().decode().strip()
        print (hashlib.md5(output.encode()).hexdigest())

        return hashlib.md5(output.encode()).hexdigest() in ['51acad5071aab26de09e45c6c5516c58','ba55c65e08e320f1225c76f810f1328b']
    
    @ssh_connect()
    def _check_www_integrity(self, path):
        ssh_session = self.client
        command = f"docker exec roses_www_1 sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        print("HELLO")
        if stderr.channel.recv_exit_status() != 0:
            print(stderr)
            return False
        output = stdout.read().decode().strip()
        print (hashlib.md5(output.encode()).hexdigest())

        return hashlib.md5(output.encode()).hexdigest() in ['732019deb1c69bf126754ca4ec1cde6b','536fd85ce834bb2e0fddc0a4bb7bc47f','6b5b06919f4320b1ce40155c35cc13e1','f4a41ea12bd3bd034c989f09160b45ab']
    
    @ssh_connect()
    def _check_www_permissions(self, path):
        ssh_session = self.client
        command = f"docker exec roses_www_1 sh -c 'chmod 644 {path} -v | grep retained'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if not "retained" in stdout.read().decode():
            return False
        return True
    
    # Private Funcs - Return False if error  --- HOR GAINEAN DAGOAN SSH_CONNECT HORI EZ DA PASAPASAN AGERTZEN ????
    def _add_new_flag(self, ssh_session, flag):
        # Execute the file creation command in the container
        command = f"docker exec roses_www_1 sh -c 'echo {flag} >> /var/www/html/dontlookhere.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)

        # Check if the command executed successfully
        if stderr.channel.recv_exit_status() != 0:
            return False
        
        # Return the result
        return {'flag': flag}

    @ssh_connect()
    def _check_flag_present(self, flag):
        ssh_session = self.client
        command = f"docker exec roses_www_1 sh -c 'grep {flag} /var/www/html/dontlookhere.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False

        output = stdout.read().decode().strip()
        return flag == output

    def _check_port_web(self, ip, port):
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5)
            conn.request("GET", "/")
            response = conn.getresponse()
            return response.status == 200
        except (http.client.HTTPException, socket.error) as e:
            print(f"Exception: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def _check_port_ssh(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            return result == 0
        except socket.error as e:
            print(f"Exception: {e}")
            return False
        finally:
            sock.close()

    @ssh_connect()
    def _check_apache_version(self):
        ssh_session = self.client
        command = f"docker exec roses_www_1 sh -c 'httpd -v | grep \"Apache/2.4.50\'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        print("CHECK APACHE VERSION")
        if stdout:
            return True
        else:
            return False
  
if __name__ == '__main__':
    checkerlib.run_check(MyChecker)




