# Installation de Wazuh avec docker

## Pré-requis avant de déployer Wazuh

Debian à jours / Docker installé.

Commençons par ajuster le mappage de la mémoire en éditant le fichier *sysctl.conf*

`` nano /etc/sysctl.conf ``

A la fin du fichier ajouter la ligne suivante : 

`` vm.max_map_count=262144 ``

Redémarrer la machine pour le prise en compte.

## Déploiment de Wazuh

###### Utilisation du dépôt officiel de Wazuh avec un fichier *docker-compose.yml*

Pour commencer, il faudra créer un dossier wazuh-docker qui sera l'emplacement ou le conteneur sera stocké.

Nous allons créer aussi un dossier Wazuh qui viendra cloner le dépôt en utilisant la dernière branche stable.


*Création des fichiers* (Pour la procédure je vais tout faire depuis le répertoire utilisateur)

`` cd /home/utilisateur `` 
``  mkdir wazuh-docker ``
``  mkdir wazuh ``

En suite il faudra ce placer dans le dossier wazuh

`` cd /home/utilisateur/wazuh ``

Maintenant on va cloner le dépôt en utilisant la dernière branche stable

``  git clone https://github.com/wazuh/wazuh-docker.git -b v4.7.3 `` 

Nous allons copier les fichiers dans le répertoire wazuh-docker

``  mv wazuh-docker/single-node/* /home/utilisateur/wazuh-docker ``

Déplaçons nous maintenant dans ce dossier 

``  cd /home/utilisateur/wazuh-docker ``

Il faudra édite le fichier docker-compose.yml et modifier la variable *INDEX_PASSWORD* qui correspond au mot de passe du compote admin par défaut.

``  nano docker-compose.yml ``

Ensuite nous allons générer les certificats.

`` docker compose -f generate-indexer-certs.yml run --rm generator ``

Télécharger les images du conteneurs 

``  docker compose pull `` 

Démarrer les conteneurs 

``  docker compose up -d ``

Vérifions les logs pour voir si tout démarre bien

`` docker compose logs -f `` 


[Commencer à utiliser Wazuh](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/aa25c361f5e57ae7ec536041b75e1c0c1901bffe/DevOps/Docker/WazuhxSuricata/Commencer-Wazuh)