# Définition du SSH

## Qu'est-ce que le SSH ?

SSH est un protocole réseau cryptographique qui permet d'établir une connexion sécurisée entre un client et un serveur sur un réseau non sécurisé. Il est principalement utilisé pour l'administration à distance des systèmes et le transfert sécurisé de fichiers.

## Fonctionnalités principales

- **Authentification sécurisée :** SSH permet l'authentification via des mots de passe, des clés publiques/privées, ou d'autres méthodes comme Kerberos.
- **Chiffrement des communications :** Les données échangées sont chiffrées, garantissant la confidentialité et l'intégrité.
- **Redirection de ports :** SSH peut être utilisé pour établir des tunnels sécurisés vers d'autres services.
- **Transfert de fichiers sécurisé :** Protocole SCP (Secure Copy Protocol) et SFTP (SSH File Transfer Protocol).
- **Exécution de commandes distantes :** Permet d'exécuter des commandes sur un serveur distant sans ouvrir une session interactive.

## Fonctionnement du SSH

SSH fonctionne selon un modèle client-serveur, où :

1. Le client SSH initie une connexion vers le serveur en utilisant une adresse IP et un port (généralement le port 22).
2. Le serveur répond en présentant sa clé publique pour établir une connexion sécurisée.
3. Une fois l'authentification réussie, la session est établie de manière sécurisée.

## Les composants de SSH

- **sshd (démon SSH) :** Processus serveur qui écoute les connexions entrantes.
- **ssh (client SSH) :** Programme permettant de se connecter à un serveur SSH.
- **ssh-keygen :** Outil pour générer des paires de clés publiques/privées.
- **ssh-agent :** Utilitaire qui gère les clés d'authentification.
- **scp/sftp :** Outils de transfert sécurisé de fichiers.

## Exemples d'utilisation

- Connexion à un serveur distant :
  ```bash
  ssh utilisateur@serveur.com
  ```
- Copie de fichiers sécurisée avec SCP :
  ```bash
  scp fichier.txt utilisateur@serveur.com:/chemin/destination
  ```
- Création d'une paire de clés SSH :
  ```bash
  ssh-keygen -t rsa -b 4096
  ```

## Avantages du SSH

- Sécurité renforcée par rapport aux protocoles non chiffrés comme Telnet ou FTP.
- Facilité d'automatisation via des scripts.
- Compatibilité multi-plateformes (Linux, macOS, Windows via OpenSSH).

## Conclusion

SSH est un outil essentiel pour la gestion sécurisée des systèmes informatiques à distance, offrant une solution robuste pour l'administration et le transfert de données en toute sécurité.

