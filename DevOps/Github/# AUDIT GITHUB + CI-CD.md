# AUDIT GITHUB + CI-CD

## Objectif 

Réaliser un audit de sécurité sur le dépôt GitHub du Backend de l'application .NET afin d'identifier les mauvaises pratiques et d'améliorer la sécurité. Ce rapport détaillera chaque étape de l’audit, en expliquant l’utilisation des outils spécifiques demandés.

### Analyse des données sensibles

Utilisation de **CodeQL** et **Dependabot**, deux outils intégré dans github. Il faudra les activés dans dans l'onglet **Security**

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/SecurityGitHub1.png)

### Ajout d'un fichier **.yml** pour exucuter une analyse avec le CI-CD.

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/securityGithub2.png)

### Utilisation du CI-CD

Dans l'onglet Action nous pouvons voir comment cela c'est déroulé.

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/SecurityGithub3.png)

### Vérification des scans

Dans l'onglet **Security** nous pouvons vérifier les alertes de vulnérabilités

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/SecurityGithub4.png)
