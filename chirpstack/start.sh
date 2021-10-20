#!/bin/bash

# Install Bridge.
if [[ $1 == "bridge" ]]; then
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
    sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list
    sudo apt update
    sudo apt install chirpstack-gateway-bridge
    sudo systemctl start chirpstack-gateway-bridge
fi

# Install Network Server.
if [[ $1 == "net" ]]; then
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
    sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list
    sudo apt update
    sudo apt install chirpstack-network-server
    sudo systemctl start chirpstack-network-server
fi

# Install Application Server.
if [[ $1 == "app" ]]; then
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
    sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list
    sudo apt-get update
    sudo apt-get install chirpstack-application-server
    sudo systemctl start chirpstack-application-server
fi

# Install requirements.
if [[ $1 == "req" ]]; then
    sudo apt install mosquitto
    sudo apt install postgresql
    sudo apt install redis-server
fi