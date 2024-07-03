# Installation de Docker 

### Configurer le dépôt de docker : 
````
apt-get update

apt-get install ca-certificates curl gnupg

install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

chmod a+r /etc/apt/keyrings/docker.gpg
````
### On ajoute ensuite le dépôt à la sources “apt” : 
````
echo \"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \

 "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \

 sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
````
### Une fois cela fait, on installe les paquets nécessaire au fonctionnement de Docker: 
````
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin 
````
### On vérifie le bon fonctionnement de docker avec la commande : 
````
systemctl status docker 
````
 

### Si il est bien en "active (running)", activez le service Docker pour qu'il démarre automatiquement après le redémarrage de la machine:
````
systemctl enable docker 
````