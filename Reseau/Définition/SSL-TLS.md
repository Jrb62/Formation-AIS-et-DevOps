# Définition de SSL/TLS

## Introduction
SSL (Secure Sockets Layer) et TLS (Transport Layer Security) sont des protocoles cryptographiques conçus pour assurer la sécurité des communications sur un réseau informatique, en particulier sur Internet. TLS est l'évolution de SSL et offre des fonctionnalités de sécurité améliorées.

## Historique
- **SSL 1.0** : Jamais publié en raison de failles de sécurité.
- **SSL 2.0 (1995)** : Première version publique, mais rapidement remplacée en raison de vulnérabilités.
- **SSL 3.0 (1996)** : Améliorations importantes, mais vulnérable à certaines attaques (ex. POODLE).
- **TLS 1.0 (1999)** : Successeur de SSL 3.0 avec des améliorations de sécurité.
- **TLS 1.1 (2006)** et **TLS 1.2 (2008)** : Renforcement des algorithmes cryptographiques.
- **TLS 1.3 (2018)** : Simplification et sécurisation accrue du protocole.

## Fonctionnalités principales
1. **Confidentialité** : Le chiffrement empêche les tiers d'accéder aux données transmises.
2. **Intégrité** : Vérification de l'absence de modification des données pendant le transfert.
3. **Authentification** : Assure que les parties communicantes sont bien celles qu'elles prétendent être.

## Comment fonctionne SSL/TLS ?
1. **Handshake (poignée de main)** :
   - Négociation des paramètres de sécurité (algorithmes de chiffrement, clés).
   - Authentification à l'aide de certificats.
2. **Chiffrement des données** :
   - Une clé symétrique est utilisée pour chiffrer la communication.
3. **Vérification de l'intégrité** :
   - Des codes d'authentification de message (MAC) garantissent que les données n'ont pas été altérées.

## Différences entre SSL et TLS
- TLS offre des algorithmes de chiffrement plus sûrs et des mécanismes de négociation améliorés par rapport à SSL.
- SSL est considéré comme obsolète et non sécurisé.
- TLS est actuellement le standard utilisé pour les communications sécurisées.

## Applications courantes de TLS
- Navigation web sécurisée (HTTPS).
- E-mails (SMTP, IMAP, POP3 avec TLS).
- VPN (Virtual Private Networks).
- Messagerie instantanée.

## Conclusion
SSL/TLS est essentiel pour assurer la sécurité des communications sur Internet en garantissant la confidentialité, l'intégrité et l'authentification des données transmises. Il est recommandé d'utiliser la dernière version de TLS (1.3) pour bénéficier des meilleures garanties de sécurité.

