#!/bin/bash

# Launch lora packet forwarder

cd /usr/local/bin/lora_mgr_project
sudo docker-compose up -d
sleep 60
cd /usr/local/bin/lora_mgr_project/ttn-gateway/packet_forwarder/poly_pkt_fwd
./poly_pkt_fwd
