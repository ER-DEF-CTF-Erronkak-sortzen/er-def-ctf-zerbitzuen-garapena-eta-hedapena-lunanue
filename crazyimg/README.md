
################################################
#   ONE IMAGE, ONE THOUSAND WORDS  - Cr4zY!mG  #     
################################################

# Service definition:
- 2 dockers are deployed: 
1. Mysql database. 
2. Ubuntu with a ssh service.


The attacker enters the mysql-docker and dumps the database located there. In one of the tables (table = crazyusers) there are some credentials to access the ssh service.

Once he gains access through SSH, the attacker will be lead to an stenographed image, where the flags are being placed.


# Service implementation:

The db-docker is configured to create and insert data into a table called "crazyusers". The data is some credentials to access the following ssh-docker (user: 'oneimg' ; password: '1000w3rd5').
The ssh-docker is configured with the previous user (oneimg/1000w3rd5) and an image (called "crazyimg.jpeg") is uploaded into /tmp directory.
 
-Flags: 
    Flags will be stored in a stenographed message in the /tmp/crazyimg.jpeg file. 

# About exploting:
- The attacker has to inspect the database located in the crazyimg_db docker; the credentialas are stored inside the database, inside a table in plain text. With those credentials, the attacker can log into crazyimg_ssh docker. Once connected, he will get access to the crazyimg.jpeg, (at /tmp/), where the flags are hiddenly stored.

  
# Checker checks:
- Ports to reach dockers are open (DB:3306; SSH 2222)
- SSH: User 'oneimg' exists in crazyimg_ssh docker. 
- SSH: /etc/sshd_config file from crazyimg_ssh docker has not been changed.
- SSH: /tmp/crazyimg.jpeg exists in crazyimg_ssh_docker. 
- DB: Table 'crazyusers' exists.

# How to solve the vulnerability
 - Change the 'oneimg' user's password in the database.
 - Change the image crazyimg.jpeg storaged in /tmp/ directory.

