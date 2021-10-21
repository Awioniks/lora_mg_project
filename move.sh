#!/bin/bash

mv ../lora_mgr_project /usr/local/bin
cp /usr/local/bin/lora.service /etc/systemd/system
chmod 777 etc/systemd/system/lora.service
systemctl deamon-reaload
systemctl start lora.service