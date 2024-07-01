# **Topologie Répandues dans les WAN**

## Star Topology

````
Description : Chaque site distant est connecté à un site central (le nœud central).

Avantages : Facile à déployer et à gérer, centralisation des ressources.

Inconvénients : Si le nœud central tombe en panne, tous les sites distants sont isolés.
````

## Ring Topology

````
Description : Chaque site est connecté à deux autres sites, formant un anneau.

Avantages : Redondance (les données peuvent circuler dans les deux sens), résistance aux pannes de liaisons simples.

Inconvénients : La complexité de gestion et les délais de latence peuvent augmenter avec la taille de l'anneau.
````

## Full Mesh Topology

````
Description : Chaque site est connecté directement à tous les autres sites.

Avantages : Haut niveau de redondance et de résilience, faible latence.

Inconvénients : Coûts élevés, complexité accrue à mesure que le nombre de sites augmente.
````

## Partial Mesh Topology

````
Description : Certains sites sont connectés directement à d'autres, mais pas tous.

Avantages : Compromis entre la redondance et les coûts, plus flexible que le maillage complet.

Inconvénients : Peut nécessiter une gestion plus complexe que la topologie en étoile.
````

## Point-to-Point Topology

```
`Description : Une connexion directe entre deux sites.

Avantages : Simplicité et fiabilité, faible latence.

Inconvénients : Pas de redondance, limitation de l'extensibilité.
````

## Hierarchical Topology

````
Description : Ressemble à une topologie en étoile, mais avec plusieurs niveaux de nœuds centraux.

Avantages : Extensibilité, permet de gérer de grands réseaux.

Inconvénients : Complexité de gestion, potentiel de points de défaillance aux nœuds centraux.
````

## Hybrid Topology 

````
Description : Combinaison de plusieurs topologies, par exemple une étoile avec des segments en maillage partiel.

Avantages : Très flexible, peut être optimisé pour différents segments du réseau.

Inconvénients : Peut être complexe à concevoir et à maintenir.
````

#### Chaque topologie présente des avantages et des inconvénients spécifiques qui doivent être évalués en fonction des besoins du réseau WAN, des ressources disponibles, et des objectifs de l'organisation.