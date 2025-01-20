# Définition d'un VLAN (Virtual Local Area Network)

Un **VLAN** (Virtual Local Area Network) est une technologie utilisée pour segmenter un réseau physique en plusieurs réseaux logiques distincts. Cette segmentation permet aux administrateurs de regrouper des appareils en fonction de critères comme leur rôle, leur département ou leur emplacement géographique, indépendamment de leur connexion physique au réseau.

## Avantages des VLANs

- **Isolation des données** : Les données de chaque VLAN sont isolées des autres VLANs, ce qui améliore la sécurité.
- **Optimisation du réseau** : Réduit la congestion en limitant les diffusions de données à chaque VLAN.
- **Flexibilité** : Les appareils d’un même VLAN peuvent être dispersés géographiquement tout en restant connectés logiquement.
- **Facilité de gestion** : Simplifie la gestion réseau en regroupant les appareils par fonction ou besoin.

---

## Exemple d’utilisation : Réseau d’entreprise

Imaginez une entreprise avec trois départements : **Comptabilité**, **Ressources humaines** et **Informatique**.

- Le réseau physique contient 50 ordinateurs connectés à plusieurs commutateurs (switchs).
- En configurant trois VLANs :
  - **VLAN 10 : Comptabilité**
  - **VLAN 20 : Ressources humaines**
  - **VLAN 30 : Informatique**

Les ordinateurs de chaque département peuvent communiquer entre eux dans leur VLAN respectif, mais pas avec les autres VLANs, sauf si un routeur ou une configuration spécifique (comme un routeur inter-VLAN) est utilisé.

### Avantage dans ce contexte :
- Les données sensibles de la comptabilité restent isolées des autres départements.
- Réduction des broadcasts inutiles dans l’ensemble du réseau.
- Meilleure sécurité et performance.

---

## Schéma simplifié

```
Switch
| VLAN 10    | VLAN 20    | VLAN 30
|------------|------------|--------
Comptabilité       RH      Informatique
```

En résumé, un VLAN optimise la gestion, la sécurité et les performances d’un réseau en segmentant un réseau physique en plusieurs réseaux logiques adaptés aux besoins.

