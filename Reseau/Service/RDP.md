# Remote Desktop Protocol (RDP)

**Remote Desktop Protocol (RDP)** est un protocole de communication développé par Microsoft, permettant aux utilisateurs d'accéder à distance à un ordinateur ou un serveur via une interface graphique. Il est couramment utilisé pour l'administration système, le support technique et le travail à distance.

## Fonctionnalités principales

- **Accès à distance sécurisé** : Permet aux utilisateurs de se connecter à un ordinateur distant via un réseau local (LAN) ou Internet.
- **Transfert de données** : Prend en charge le transfert de fichiers et le partage du presse-papiers entre les machines locales et distantes.
- **Impression et audio à distance** : Permet de rediriger les périphériques locaux tels que les imprimantes et l'audio vers la session distante.
- **Cryptage des connexions** : Utilise des protocoles de sécurité tels que TLS (Transport Layer Security) pour protéger les données échangées.
- **Multiples sessions** : Supporte les connexions simultanées pour plusieurs utilisateurs sur les systèmes Windows Server.

## Ports et protocoles

- Par défaut, RDP utilise le **port 3389** (TCP/UDP).
- Le protocole repose sur une architecture client-serveur, où le client RDP se connecte à un serveur RDP hébergé sur la machine distante.

## Applications courantes

- Gestion de serveurs Windows dans un environnement professionnel.
- Accès à distance pour les télétravailleurs.
- Support technique et dépannage informatique.
- Accès aux applications d'entreprise depuis n'importe quel endroit.

## Outils RDP populaires

- **Microsoft Remote Desktop** (Windows, macOS, iOS, Android).
- **rdesktop** (Linux).
- **FreeRDP** (cross-platform).
- **Chrome Remote Desktop** (extension de navigateur).

## Sécurité et meilleures pratiques

Pour garantir la sécurité des connexions RDP, il est recommandé de :

1. Désactiver RDP lorsqu'il n'est pas utilisé.
2. Utiliser un VPN pour les connexions distantes.
3. Activer l'authentification multi-facteurs (MFA).
4. Limiter les adresses IP autorisées à se connecter.
5. Mettre régulièrement à jour le système pour corriger les vulnérabilités connues.

## Ressources supplémentaires

- [Documentation officielle Microsoft](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds)
- [Guide de configuration RDP sécurisé](https://www.microsoft.com/security/blog/)
