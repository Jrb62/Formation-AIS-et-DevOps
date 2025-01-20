# Spanning Tree Protocol (STP)

## Introduction
Le **Spanning Tree Protocol (STP)** est un protocole réseau de niveau 2 (couche liaison du modèle OSI) qui permet d'éviter les boucles dans les réseaux Ethernet commutés. Il a été défini dans la norme **IEEE 802.1D**.

## Objectifs du STP
STP vise à :
- Éviter les boucles réseau en désactivant dynamiquement certains chemins redondants.
- Assurer la disponibilité des chemins de secours en cas de défaillance d'un lien actif.
- Maintenir une topologie de réseau sans boucle tout en assurant la redondance.

## Fonctionnement
STP fonctionne en désignant un **pont racine (root bridge)** et en établissant une arborescence (spanning tree) sans boucle en procédant comme suit :

1. **Élection du pont racine (Root Bridge)**  
   - Le switch avec l'ID de pont le plus bas est élu comme "Root Bridge".
   
2. **Sélection des chemins les plus courts**  
   - Chaque switch calcule le chemin le plus court vers le root bridge en fonction du coût du chemin.

3. **Blocage des ports redondants**  
   - Les ports qui ne font pas partie du chemin le plus court sont mis en état "Blocking" pour éviter les boucles.

## États des ports STP
Un port STP peut être dans l'un des états suivants :

- **Blocking** : Ne relaie pas le trafic, écoute les BPDU (Bridge Protocol Data Units).
- **Listening** : Apprend la topologie sans envoyer de trafic.
- **Learning** : Commence à apprendre les adresses MAC sans encore transmettre de trafic utilisateur.
- **Forwarding** : Transmet le trafic utilisateur.
- **Disabled** : Le port est désactivé administrativement.

## Types de Spanning Tree Protocol
Il existe plusieurs variantes de STP, notamment :

- **STP (IEEE 802.1D)** : La version classique du protocole.
- **RSTP (IEEE 802.1w)** : Rapid Spanning Tree Protocol, qui permet une convergence plus rapide.
- **MSTP (IEEE 802.1s)** : Multiple Spanning Tree Protocol, permettant la gestion de plusieurs instances STP.

## Messages BPDU
STP utilise des messages appelés **BPDU (Bridge Protocol Data Units)** pour échanger des informations entre les switches et prendre des décisions sur la topologie réseau.

## Avantages de STP
- Prévient les boucles réseau.
- Permet la redondance tout en maintenant une topologie sans boucle.
- Offre une solution simple et efficace pour les réseaux commutés.

## Inconvénients de STP
- Temps de convergence relativement long dans la version classique (jusqu'à 50 secondes).
- Risque de lenteur pour les réseaux critiques nécessitant une disponibilité rapide.
- Nécessite une configuration et une surveillance adaptées.

## Conclusion
Le Spanning Tree Protocol est un mécanisme essentiel pour les réseaux commutés, garantissant un fonctionnement sans boucle tout en assurant la redondance et la résilience du réseau. Cependant, avec les exigences croissantes de rapidité et de flexibilité, des variantes plus avancées comme RSTP et MSTP sont souvent préférées dans les environnements modernes.

