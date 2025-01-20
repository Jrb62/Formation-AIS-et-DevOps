# TELNET

**TELNET** est un protocole réseau utilisé pour établir une connexion interactive à distance entre un client et un serveur via une ligne de commande. Il permet aux utilisateurs d'accéder et de gérer des dispositifs distants, généralement via le port **23**.

## Caractéristiques principales

- Fournit un accès distant en ligne de commande à un hôte distant.
- Fonctionne sur le modèle client-serveur.
- Transmet les données en texte clair, ce qui le rend vulnérable aux interceptions.
- Nécessite une authentification (nom d'utilisateur et mot de passe).
- Moins sécurisé que les protocoles modernes comme **SSH** (Secure Shell).

## Fonctionnement

1. L'utilisateur exécute une commande TELNET pour se connecter à un hôte distant.
2. Une session interactive est ouverte, permettant l'exécution de commandes à distance.
3. Toutes les données sont échangées en texte brut sans chiffrement.

## Commandes de base

- `telnet [adresse_IP] [port]` – Connexion à un serveur TELNET.
- `quit` – Déconnexion de la session TELNET.
- `help` – Afficher l'aide des commandes disponibles.

## Inconvénients

- Aucune sécurité native (pas de chiffrement des données).
- Vulnérable aux attaques par interception (sniffing).
- Obsolète pour les environnements sensibles à la sécurité.

## Alternatives recommandées

En raison de ses failles de sécurité, TELNET est souvent remplacé par des alternatives plus sûres, notamment :

- **SSH** – Protocole sécurisé pour l'accès distant.
- **RDP** – Accès à des interfaces graphiques à distance.
- **HTTPS** – Accès sécurisé aux services web.

## Conclusion

TELNET est un protocole ancien qui reste utilisé dans certains environnements spécifiques (réseaux fermés, équipements embarqués), mais son usage est déconseillé sur les réseaux publics en raison de son manque de sécurité.
