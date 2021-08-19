#!/usr/bin/python3

from server import Server
from data_insert import Data_Insert

if __name__ == "__main__":
    db = Data_Insert("trololo")
    serv = Server("127.0.0.1", 65432, db)
    serv.launch_server()
