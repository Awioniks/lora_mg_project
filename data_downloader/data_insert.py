import re

from influxdb import InfluxDBClient


class Data_Insert():
    def __init__(self, *args, **kwargs):

        # Influx credentials.
        self.measurement = kwargs['measurement']
        self.db = kwargs['db']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.host = kwargs['host']
        self.port = kwargs['port']

        # Data structures.
        self.db_d = {}
        self.decoded_data = None

    def decode(self, data):
        """
        Decode to human and db format
        """

        self.decoded_data = data.decode(
            'utf8', errors="ignore")
        match_obj = re.search(
            r'data\"', self.decoded_data)
        if match_obj:
            rssi_obj = re.search(r'\"rssi\":-\d+', self.decoded_data)
            lsnr_obj = re.search(r'\"lsnr\":\d+.\d+', self.decoded_data)

            if rssi_obj:
                print(rssi_obj.group(), "RSSI")
                self.db_d["RSSI"] = rssi_obj.group()

            if lsnr_obj:
                print(lsnr_obj.group(), "LSNR")
                self.db_d["LSNR"] = rssi_obj.group()

            return True
        return False

    def send_data(self, data):
        """
        Prepeare data from gateway,
        send data to influx.
        """

        if self.decode(data):
            measurement = [
                {
                    "measurement": "radio_data",
                    "tags": {
                        "sensor": "nr_1"
                    },
                    "fields": {
                        "rssi": self.db_d["RSSI"],
                        "lsnr": self.db_d["LSNR"]
                    }
                }
            ]
            self.send_to_influx(measurement)

    def send_to_influx(self, measurement):
        """
        Send data to influx database.
        """

        influx_client =  InfluxDBClient(
                host=self.host, port=self.port, username="PATRYK",
                password="PATRYK", database=self.db)
        influx_client.write_points(measurement)
