class Data_Insert():
    def __init__(self, data_connection):
        self.data_connection = data_connection
        self.decoded_data = None

    def decode(self, data):
        """
        Decode to human and db format
        """

        print(str(data))
        print(data, "\n")
        self.decoded_data = data
    
    def send_data(self, data):
        """
        Send data to influxdb.
        """
        self.decode(data)
        pass
