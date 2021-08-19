import re

class Data_Insert():
    def __init__(self, data_connection):
        self.data_connection = data_connection
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
        else:
            print(self.decoded_data, type(self.decoded_data ))

    def send_data(self, data):
        """
        Send data to Influxdb.
        """

        self.decode(data)
        pass
