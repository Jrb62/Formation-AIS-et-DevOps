# Déployer l'agent Wazuh pour Suricata (Ubuntu/Debian)

##### Après le déploiment de Wazuh nous pouvons aller sur l'interface graphique, il faudra alors créer un groupe d'agent.

![alt tab](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Wazuh1.png)

![alt tab](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Wazuh2.png)

##### Après avoir créé le groupe on va édit la config.

![alt tab](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Wazuh3.png)

##### Mettre cette config dans l'edit

````
<agent_config>
	<localfile>
		<log_format>json</log_format>
		<location>/var/log/suricata/eve.json</location>
	</localfile>
</agent_config>
````

##### Après avoir fait cela, il faudra créer un agent.

![alt tab](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/Wazuh4.png)

##### Dans la création de l'agent il faut bien choisir le groupe que nous venons de créer précédemment.

##### Une fois l'agent créé, il faudra copier le lien créé par Wazuh pour le télécharger sur la machine Suricata.

##### Une fois l'agent téléchargé entrez les commande suivante : 

````
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
````
