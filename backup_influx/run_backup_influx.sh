#!/bin/bash

docker run -p 8086:8086 -p 8088:8088 -d --name influx_backup \
      -v influxdb:/var/lib/influxdb \
      -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf \
      -v $PWD/backups:/tmp/backups  \
      influxdb:1.8
