#!/bin/bash

# Launch data downloader
python3 ./data_downloader/main.py


# Launch lora packet forwarder
./ttn-gateway/packet_forwarder/poly_pkt_fwd/poly_pkt_fwd