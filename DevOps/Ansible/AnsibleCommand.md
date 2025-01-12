# Commandes Ansible pour GitHub

Ce document liste des commandes utiles pour travailler avec Ansible dans le cadre d'un projet. 

## 1. Vérification de la syntaxe des playbooks

````
 ansible-playbook --syntax-check <playbook.yml>
````

## 2. Exécution d'un playbook

````
 ansible-playbook -i <inventory_file> <playbook.yml>
````
#### Exemple avec des variables
````
 ansible-playbook -i inventory/hosts.yml playbook.yml --extra-vars "ansible_connection=local"
````

## 3. Lister les tâches d'un playbook
````
 ansible-playbook --list-tasks <playbook.yml>
````
#### Affiche la liste des tâches définies dans un playbook sans les exécuter.

## 4. Lister les hôtes ciblés
````
 ansible-playbook --list-hosts -i <inventory_file> <playbook.yml>
````
#### Affiches les hôtes sur lesquels un playbook sera appliqué.

## 5. Ping des hôtes dans l'inventaire
````
 ansible -i <inventory_file> all -m ping
````
#### Testez la connectivité SSH avec tout les hôtes définis dans un inventaire.

## 6. Exécution d'une commande ad hoc
````
 ansible -i <inventory_file> all -m command -a "uptime"
````
#### Exécute une commande rapidemant sur les hôtes sans passer par un playbook

## 7. Simulation d'exécution dry-run
````
 ansible-playbook -i <inventory_file> <playbook.yml> --check
````
#### Testez un playbook sans appliquer de modification réelles.

## 8. Installation des dépendances avec Ansible Galaxy
````
 ansible-galaxy install -r requirements.yml
````
#### Installe les rôles ou collections définis dans un fichier requirements.yml