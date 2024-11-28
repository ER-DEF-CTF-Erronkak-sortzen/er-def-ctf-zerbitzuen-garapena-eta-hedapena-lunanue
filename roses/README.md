
################################################
#               ROSES ARE RED,                 #
#              BLUE IS THE SKY                 #
#            YOU WANT TO HACK ME,              #
#             I DON'T KNOW WHY                 #     
################################################

# Service definition:
- 3 dockers are deployed (and your mind will be destroyed ;): 
1. Ubuntu serving a web as a starting point. 
2. Ubuntu with a ssh service.
3. Ubuntu serving an apache-php web to enter a password, where flags are placed.

The attacker enters to the web of docker-1 where there is information about how to access trough ssh (docker-2). Once entered, the attacker will get the password to unlock docker-3.
The flags are stored in that last docker's file (docker-3) and attacker has to let them in his T-Submission machine. 

# Service implementation:
web docker is configured to take a copy of the rosesarered.png image and index.html file from the host machine, letting it in '/usr/local/apache2/htdocs/'. 
ssh docker is configured attending to the following tips:
  - It has openssh-server installed and started. 
  - It has a user called 'blue' whose password is '1234'.
www docker is configured to take a copy of php, html and txt files to the '/usr/local/apache2/htdocs/'.

 'blue' user's password will never be changed. Moreover, if a team changes it, it will be losing SLa points. 
 
-Flags: 
    Flags will be stored in 'roses_www_1' docker's '/usr/local/apache2/htdocs/dontlookhere.txt' file. 

# About exploting:
- The attacker has to inspect the rosesarered.png image showed in the index.html web page; the credentialas are stored inside the image (using steganography) as a message plain text. With those credentials, the attacker can log into roses_ssh docker. Once connected, he will get access to the rosesarered.txt, (at /home/blue/), where a poem of "Roses are red, Blue is the sky..." will be shown. 
The password you need for the next step is the result of applying the md5 to the poem file (rosesarered.txt).
The last step is to access the other web server and to use that hash as the password to enter the final webpage there the flags are being placed (at '/usr/local/apache2/htdocs/dontlookhere.txt').
- The defender should change 'blue' user's password. 
  
# Checker checks:
- Ports to reach dockers are open (WEB:80; SSH 2200; WWW:8888)
- SSH: User 'blue' exists in roses_ssh docker. 
- SSH: /etc/sshd_config file from roses_ssh docker has not been changed. 
- WEB: /usr/local/apache2/htdocs/index.html file's content from roses_web docker has not been changed.
- WWW: /usr/local/apache2/htdocs/index.html file's content from roses_www docker has not been changed.
- WWW: /usr/local/apache2/htdocs/flaggy.php file's content from roses_www docker has not been changed. 
- WWW: Permissions of the file 'usr/local/apache2/htdocs/rosesarered.txt' has not been changed.

# How to solve the vulnerability
 - Change the 'blue' user's password.
 - Change the owner of the rosesarered.txt to root user.
 - Change the image rosesarered.png in roses_web.

