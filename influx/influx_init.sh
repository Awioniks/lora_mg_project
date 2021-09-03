#!/usr/bin/bash

influx_db="test_db"
influx_user="influx_user"
influx_password="influx_password"

influx_id=$(docker ps -f name="lora_mgr_project_influxdb_1" --format "{{.ID}}")

# POTENTIALLY NEED TO MAKE IT MANUALLY.
sudo docker exec -it $influx_id influx -execute influx -execute "CREATE USER $influx_user WITH PASSWORD '$influx_password' WITH ALL PRIVILEGES"
sudo docker exec -it $influx_id influx -execute influx -username $influx_user -password $influx_password -execute "CREATE DATABASE $influx_db"