#!/bin/bash

rm -r /usr/local/bin/lora_mgr_project
cp -r ../lora_mgr_project /usr/local/bin
cp /usr/local/bin/lora_mgr_project/lora.service /etc/systemd/system
chmod 777 /etc/systemd/system/lora.service
systemctl daemon-reload
systemctl start lora.service
