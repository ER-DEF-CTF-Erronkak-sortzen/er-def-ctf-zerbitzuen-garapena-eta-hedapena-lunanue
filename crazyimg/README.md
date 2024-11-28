
################################################
#   ONE IMAGE, ONE THOUSAND WORDS  - Cr4zY!mG  #     
################################################

# Service definition:
- 2 dockers are deployed: 
1. Mysql database. 
2. Ubuntu with a ssh service.









///TO BE MODIFIED


The attacker enters to the web of docker-1 where there is information about how to access trough ssh (docker-2). Once entered, the attacker will get the password to unlock docker-3.
The flags are stored in that last docker's file (docker-3) and attacker has to let them in his T-Submission machine. 

# Service implementation:
web docker is configured to take a copy of the rosesarered.png image and index.html file from the host machine, letting it in '/var/www/html/'. 
ssh docker is configured attending to the following tips:
  - It has openssh-server installed and started. 
  - It has a user called 'blue' whose password is '1234'.
www docker is configured to take a copy of php, html and txt files to the '/var/www/html/'.


 
-Flags: 
    Flags will be stored in 'roses_www_1' docker's '/var/www/html/dontlookhere.txt' file. 

# About exploting:
- The attacker has to inspect the rosesarered.png image showed in the index.html web page; the credentialas are stored inside the image (using steganography) as a message plain text. With those credentials, the attacker can log into roses_ssh docker. Once connected, he will get access to the rosesarered.txt, (at /home/blue/), where a poem of "Roses are red, Blue is the sky..." will be shown: 

*Roses are red,
blue is the sky,
you want to hack me
and I don't know why,
you have to be brave
don't be shy,
the password you need is
the md5 of this file.*

The password you need for the next step is the result of applying the md5 to the poem file (rosesarered.txt).
The last step is to access the other web server and to use that hash as the password to enter the final webpage there the flags are being placed (at '/var/www/html/dontlookhere.txt').
- The defender should change 'blue' user's password. 
  
# Checker checks:
- Ports to reach dockers are open (WEB:80; SSH 2200; WWW:8888)
- SSH: User 'blue' exists in roses_ssh docker. 
- SSH: /etc/sshd_config file from roses_ssh docker has not been changed. 
- WEB: /var/www/html/index.html file's content from roses_web docker has not been changed.
- WWW: /var/www/html/index.html file's content from roses_www docker has not been changed.
- WWW: /var/www/html/flaggy.php file's content from roses_www docker has not been changed. 
- WWW: Permissions of the file 'var/www/html/rosesarered.txt' has not been changed.

# How to solve the vulnerability
 - Change the 'blue' user's password.
 - Change the owner of the rosesarered.txt to root user.
 - Change the image rosesarered.png in roses_web.

