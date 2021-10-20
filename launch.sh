#!/bin/bash

# Launch data downloader
sudo docker-compose restart data_downloader
sudo docker-compose up -d data_downloader

# Launch lora packet forwarder
sleep 15
cd ttn-gateway/packet_forwarder/poly_pkt_fwd
./poly_pkt_fwd 1> /dev/null  &
