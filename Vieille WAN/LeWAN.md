# **LE WAN**

## *Performances, Latence, Redondance, Sécurité, Bande Passante*


• Performances : Mesurées en termes de débit et de latence. Dépend de la qualité des liaisons et de la technologie utilisée.

• Latence : Le délai de transmission des données. Critique pour les applications temps réel.

• Redondance : Multiplicité des chemins pour éviter les pannes. Topologies mesh et redondance de liens sont couramment utilisées.

• Sécurité : Protocoles de chiffrement, pare-feu, et segmentation du réseau.

• Bande Passante : Quantité de données pouvant être transmises sur une connexion donnée. Les technologies modernes comme le FTTH offrent des bandes passantes élevées.


## *Technologies d'accès au WAN Publics*

• FTTH (Fiber to the Home) / FTTE (Fiber to the Exchange) : Fournit des connexions à haut débit via la fibre optique.

• DSL (Digital Subscriber Line) : Utilise les lignes téléphoniques existantes pour fournir un accès internet.

• PPP (Point-to-Point Protocol) : Utilisé pour établir des connexions directes sur des lignes téléphoniques, y compris sur DSL.

• DOCSIS (Data Over Cable Service Interface Specification) : Norme pour la transmission de données sur les réseaux de télévision par câble.


## *Technologies d'accès au WAN Privés*

• Lignes Louées : Connexions privées dédiées entre deux points, souvent utilisées pour des communications sécurisées.

• Metro Ethernet : Réseau Ethernet déployé dans une zone métropolitaine pour connecter des sites d'une même entreprise.

• MPLS (Multiprotocol Label Switching) : Technologie pour acheminer efficacement les données sur des réseaux étendus.

• VPN (Virtual Private Network) : Crée des tunnels sécurisés sur internet pour les communications privées.

• RNIS (Réseau Numérique à Intégration de Services) : Fournit des lignes téléphoniques numériques et des connexions de données.

• RTPC (Réseau Téléphonique Public Commuté) : Réseau téléphonique traditionnel pour les connexions vocales.

• Frame Relay : Ancienne technologie pour les communications de données, remplacée par MPLS et d'autres technologies modernes.

• ATM (Asynchronous Transfer Mode) : Utilisé pour le transport de voix, vidéo et données, remplacé par des technologies plus modernes.

## *Interconnexion de Secours (Mono/Multifournisseur d’Accès à Internet)*

• Mono FAI : Utilisation d'un seul fournisseur d'accès à Internet. Moins coûteux mais vulnérable aux pannes du fournisseur.

• Multi FAI : Utilisation de plusieurs fournisseurs pour assurer la redondance et la résilience.

## *SD-WAN*

• Définition : Technologie qui virtualise les réseaux WAN pour améliorer l'agilité et réduire les coûts.

• Avantages : Flexibilité, gestion centralisée, optimisation des performances, sécurité intégrée.

• Cas d'utilisation : Adaptation dynamique aux conditions du réseau, priorisation des applications critiques, intégration facile avec les services cloud.


## *Protocoles de Routage (Rôles : Redondance, Équilibrage de Charge, Multiplicité des Chemins)*


• Redondance : Assure la continuité du service en cas de défaillance d'un lien.

• Équilibrage de Charge : Répartit le trafic entre plusieurs liens pour optimiser l'utilisation des ressources.

• Multiplicité des Chemins : Utilisation de plusieurs routes pour acheminer les données, assurant flexibilité et résilience.


## *Protocoles de Routage (Détection de Panne et Basculement : État de Liens, Mécanismes de Timers, Basculement Automatique)*


• Détection de Panne : Protocoles comme BFD (Bidirectional Forwarding Detection) surveillent l'état des liens pour détecter les pannes rapidement.

• Mécanismes de Timers : Protocoles utilisent des timers pour déterminer quand un lien est considéré comme inactif.

• Basculement Automatique : Les routes sont mises à jour automatiquement pour utiliser des chemins alternatifs en cas de panne.


## *Protocoles de Routage (Quels sont les Protocoles de Routage Utilisés dans les WAN)*


• RIP (Routing Information Protocol) : Protocole de routage basé sur la distance, simple mais limité en termes d'échelle.

• OSPF (Open Shortest Path First) : Protocole de routage à état de liens, très utilisé dans les réseaux de grande taille.

• EIGRP (Enhanced Interior Gateway Routing Protocol) : Protocole de routage hybride développé par Cisco.

• BGP (Border Gateway Protocol) : Principal protocole de routage utilisé pour l'interconnexion des réseaux sur internet.
