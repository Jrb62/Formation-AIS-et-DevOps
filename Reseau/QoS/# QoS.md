# QoS 

### *Sans QoS*

##### Quels débits avez-vous relevé ?

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/transfert.png)

##### Les deux débits sont-ils identiques ? Pourquoi ?

*Les débits sont indentiques car il n'y a pas de priorisation*

### QoS Activé en fonction de l'interface source

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/image.png)

###### Quels débits avez-vous relevé ?

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/transfert%201.png)

##### Les deux débits sont-ils identiques ? Pourquoi ?

*On vois une différence de débit car il envoie en priorité les paquets a l'interface du routeur qui est priorisé*

###### En mode "simulation", à partir du poste H1, retrouver le code DSCP correspondant au paquet arrivant dans le routeur par le port Fa1/0 et sortant par le port Fa0/1

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/trasnfert%203.png)

###### Idem pour les paquets arrivant par le port Fa0/0 depuis le poste G1 et sortant par le port Fa0/1

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/trasnfert%204.png)


Ce travail a était effectué en collaboration avec [@Zennael](https://github.com/Zennael/AIS) [@NicolasW-7](https://github.com/NicolasW-7/AIS-Brief-et-TIPS) [@Ariyu-M](https://github.com/Ariyu-M/Formation_AIS_DevOps)