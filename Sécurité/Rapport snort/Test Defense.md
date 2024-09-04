# Utilisation de snort pour voir le traffic

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Capture%20d'%C3%A9cran%202024-09-04%20135406.png)

### Bloquer les tentatives avec Fail2ban

````
sudo apt instal fail2ban
````

##### Configuration de Fail2ban

````
sudo nano /etc/fail2ban/jail.local
````

##### Mettre ce fichier dans le fichier

````
[sshd]
enabled = true
port = ssh
logpath = %(sshd_log)s 
maxretry = 10  (le nombre maximum de tentatives de connexion autorisées avant que l'IP soit bannie.)
findtime = 60 (la période pendant laquelle maxretry tentatives sont comptabilisées (en secondes). Dans cet exemple, c'est 60 secondes donc 1 minute)
bantime = 600 (la durée pendant laquelle l'IP sera bannie après avoir dépassé maxretry tentatives. Ici, 600 secondes donc 10 minutes.)
````

````
sudo systemctl restart fail2ban
````

##### Vérifier le bon fonctionnement spécifiquement pour sshd

````
sudo fail2ban-client status sshd
````

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Capture%20d'%C3%A9cran%202024-09-04%20154603.png)