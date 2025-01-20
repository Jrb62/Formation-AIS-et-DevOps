# HTTP et HTTPS

## Qu'est-ce que HTTP ?
**HTTP** (HyperText Transfer Protocol) est un protocole de communication utilisé sur le Web pour transférer des données entre un client (navigateur web) et un serveur web. Il fonctionne selon un modèle requête-réponse, où le client envoie une requête au serveur et celui-ci répond avec les ressources demandées (pages web, images, fichiers, etc.).

### Caractéristiques de HTTP :
- Fonctionne principalement sur le port **80**.
- Protocole sans état (chaque requête est traitée indépendamment des autres).
- Texte en clair, ce qui signifie que les données transmises ne sont pas chiffrées.

## Qu'est-ce que HTTPS ?
**HTTPS** (HyperText Transfer Protocol Secure) est la version sécurisée de HTTP, qui utilise un protocole de chiffrement (TLS/SSL) pour assurer la confidentialité et l'intégrité des données transmises entre le client et le serveur.

### Caractéristiques de HTTPS :
- Fonctionne principalement sur le port **443**.
- Assure la sécurité des échanges grâce au chiffrement des données.
- Protège contre les attaques de type "man-in-the-middle".
- Utilise des certificats SSL/TLS pour authentifier les sites web et garantir leur identité.

## Différences entre HTTP et HTTPS
| Critère       | HTTP                          | HTTPS                           |
|---------------|-------------------------------|---------------------------------|
| Port          | 80                            | 443                             |
| Sécurité      | Pas de chiffrement            | Chiffrement via SSL/TLS         |
| Performance   | Plus rapide                   | Un peu plus lent                |
| Utilisation   | Sites non sensibles           | Transactions, login, e-commerce |

## Pourquoi utiliser HTTPS ?
1. **Protection des données sensibles** : empêche les tiers malveillants d'intercepter des informations sensibles.
2. **Confiance des utilisateurs** : la présence du cadenas dans la barre d'adresse rassure les visiteurs.
3. **Amélioration du référencement** : les moteurs de recherche favorisent les sites utilisant HTTPS.
4. **Intégrité des données** : prévient les altérations de contenu en transit.

---

En conclusion, HTTPS est essentiel pour garantir la sécurité et la confidentialité des données en ligne, et il est fortement recommandé d'utiliser HTTPS plutôt que HTTP pour toute application web moderne.

