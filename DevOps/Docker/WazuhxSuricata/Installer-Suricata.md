# Installation de Suricata (Ubuntu/Debian)

##### Pour installer Suricata c'est très simple.

##### Il faudra mettre à jour le système (Il est toujours recommandé de mettre à jour les paquets avant d'installer un nouveau logiciel) 

````
sudo apt update
sudo apt upgrade
```` 

##### Installer Suricata depuis les dépôts officiels : Ubuntu/Debian ont Suricata dans leurs dépôts officiels, donc vous pouvez l'installer avec *apt*

````
sudo apt install suricata
````

##### Une fois l'installation terminée, vous pouvez vérifier que Suricata est correctement installé en vérifiant sa version.

````
suricata --version
````

##### Vous pouvez maintenant configurer Suricata selon vos besoins. Le fichier de configuration principal se trouve à :

````
/etc/suricata/suricata.yaml

````

##### Pour démarrer Suricata

````
sudo systemctl start suricata
````

##### Pour vérifier que Suricata fonctionne correctement

````
sudo systemctl status suricata
````