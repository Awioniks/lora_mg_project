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
        self.data_type = [
            "rssi", "lsnr", "freq", "modul"
        ]
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
            freq_obj = re.search(r'\"freq\":\d+.\d+', self.decoded_data)
            modul_obj = re.search(r'\"modu\":\"[a-zA-Z]+\"', self.decoded_data)

            data_list = [rssi_obj, lsnr_obj, freq_obj, modul_obj]

            for data_, data_type in zip(data_list, self.data_type):
                self.set_current_data(data_, data_type)

            return True
        return False

    def set_current_data(self, data, data_type):
        """
        Set current data structrure
        """

        if data:
            data_el = data.group()
            data_el = data_el.replace("\"", "").split(":")
            self.db_d[data_type] = data_el[-1]

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
                        "sensor": "gateway_jozek"
                    },
                    "fields": {
                        key: val
                            for key, val in self.db_d.items()
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
