# Qu'est-ce que le FTP ?

## Définition

Le FTP (File Transfer Protocol) est un protocole réseau utilisé pour transférer des fichiers entre un client et un serveur sur un réseau informatique, généralement l'Internet. Il permet aux utilisateurs de télécharger, téléverser et gérer des fichiers stockés sur un serveur distant.

## Fonctionnement

Le FTP fonctionne selon un modèle client-serveur où :

1. **Client FTP** : Il s'agit de l'application utilisée par l'utilisateur pour se connecter au serveur FTP et effectuer des transferts de fichiers.
2. **Serveur FTP** : Héberge les fichiers et gère les connexions des clients.

Le FTP utilise généralement deux ports :
- **Port 21** : Pour établir la connexion et envoyer des commandes.
- **Port 20** : Pour le transfert des données.

## Modes de transfert

Le FTP propose deux modes de transfert de données :

1. **Mode actif** : Le serveur initie la connexion de données vers le client.
2. **Mode passif** : Le client initie la connexion de données vers le serveur, ce qui est souvent utilisé pour contourner les pare-feu.

## Sécurité du FTP

Le protocole FTP en lui-même ne chiffre pas les données, ce qui le rend vulnérable aux interceptions. Pour pallier cette limitation, plusieurs variantes sécurisées existent, telles que :

- **FTPS (FTP Secure)** : Utilise SSL/TLS pour sécuriser les connexions.
- **SFTP (SSH File Transfer Protocol)** : Utilise le protocole SSH pour assurer un transfert sécurisé.

## Commandes FTP courantes

Quelques commandes fréquemment utilisées en FTP incluent :

- `USER` : S'authentifier avec un nom d'utilisateur.
- `PASS` : Fournir le mot de passe.
- `LIST` : Lister les fichiers et répertoires.
- `PUT` : Envoyer un fichier vers le serveur.
- `GET` : Télécharger un fichier depuis le serveur.
- `QUIT` : Fermer la connexion.

## Utilisation du FTP

Le FTP est couramment utilisé pour :

- La gestion de sites web (envoi de fichiers vers un hébergement web).
- Le partage de fichiers volumineux.
- Les sauvegardes de données.

## Clients FTP populaires

Quelques clients FTP largement utilisés sont :

- **FileZilla** (open-source, multiplateforme)
- **WinSCP** (pour Windows)
- **Cyberduck** (pour macOS et Windows)
- **lftp** (en ligne de commande, pour Linux)

## Conclusion

Le FTP reste un outil essentiel pour le transfert de fichiers, bien que des solutions plus sécurisées comme SFTP ou FTPS soient souvent privilégiées pour des raisons de sécurité.

