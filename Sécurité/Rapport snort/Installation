# SNORT3 INSTALLATION

[from @YaKnowThisIs](https://github.com/YaKnowThisIs/Snort-3/blob/main/Installation.md)

### Installation des dépendances

````
 apt update && apt upgrade
apt install build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex git cmake libdaq2 libdaq-dev  libhwloc-dev luajit libluajit-5.1-dev libssl-dev zlib1g-dev liblzma-dev gawk libcmocka-dev && apt install hwloc 

````

### Installation LibDAQ

````
cd
git clone https://github.com/snort3/libdaq.git
cd libdaq
./bootstrap
./configure
make install
ldconfig 

````

### Installation Snort3

````
cd
git clone https://github.com/snort3/snort3.git
cd snort3
export my_path=/
./configure_cmake.sh --prefix=$my_path
cd build
make -j $(nproc)
make install

````
### TEST DE FONCTIONNEMENT 

```` 

snort -V

````
