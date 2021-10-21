#!/usr/bin/python3

import yaml

from server import Server
from data_insert import Data_Insert


if __name__ == "__main__":

    with open("config.yaml", 'r') as file_handler:
        data = yaml.full_load(file_handler)

    db = Data_Insert(db=data["INFLUX_DB"], user=data["INFLUX_USER"],
                password=data["INFLUX_PASSWORD"], host=data["INFLUX_HOST"],   
                port=data["INFLUX_PORT"], measurement=data["MEASUREMENT"])
    
    serv = Server(data["HTTP_IP"], data["PORT"], db)
    serv.launch_server()
