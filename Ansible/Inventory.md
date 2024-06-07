# **Inventaire Windows et Linux pour le playbook**

## **Inventaire Windows**

````
[windows]
192.168.10.10 (*ip du serveur*)

[windows:vars]
ansible_user= *user@localdomaincom*
ansible_password= *Password*
ansible_connection=winrm
ansible_port=5985
ansible_winrm_scheme=http
ansible_winrm_transport=basic

````

## **Inventaire localhost**

````
all:
  hosts:
    localhost:
      ansible_host: 127.0.0.1
      ansible_connection: local

````

## **Inventaire Linux**

````
all:
  hosts:
    *Nom de la machine Linux*
    vm-web-staging-01:
      ansible_host: *XXX.XXX.XXX.XXX*
      ansible_user: *Utilisateur*

````      
