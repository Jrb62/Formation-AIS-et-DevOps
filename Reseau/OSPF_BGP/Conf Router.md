# *CONFIGURATION OSPF & BGP*

##### Router Bordure

````
R32# router bgp 300
R32# neighbor 192.168.42.1 remote-as 100
R32# neighbor 192.168.43.2 remote-as 200
R32# network 192.168.32.0
R32# network  192.168.38.0
R32# network 192.168.35.0 

R32# router ospf 1
R32# router-id 9.9.9.9
R32# redistribute bgp 300 match internal external
````

##### Router pas bordure

````
R31# router ospf 1
R31# router-id 10.10.10.10
R31# network 192.168.31.0 0.0.0.255 area 0
R31# network 192.168.38.0 0.0.0.255 area 0
R31# network 192.168.36.0 0.0.0.255 area 0

R31# router bgp 300
R31# redistribute ospf 1 match internal external
````

### Show BGP & OSPF

##### R31

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/BGP%2031.png)
![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/OSPF%2031.png)

##### R32

![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/bgp%2032.png)
![alt tag](https://github.com/Jrb62/Formation-AIS-et-DevOps/blob/main/screenshot/OSPF%2032.png)
