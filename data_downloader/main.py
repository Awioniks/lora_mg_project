#!/usr/bin/python3

from server import Server
from data_insert import Data_Insert


INFLUX_HOST = "172.18.0.3"
INFLUX_PORT = "8086"
INFLUX_DB = "TTN_GATEWAY"
MEASUREMENT = "radio_data"
INFLUX_USER = "PATRYK"
INFLUX_PASSWORD = "PATRYK"


if __name__ == "__main__":

    db = Data_Insert(db=INFLUX_DB, user=INFLUX_USER,
                password=INFLUX_PASSWORD, host=INFLUX_HOST,
                port=INFLUX_PORT, measurement=MEASUREMENT)
    serv = Server("0.0.0.0", 65432, db)
    serv.launch_server()
