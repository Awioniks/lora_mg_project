import socket
import selectors
import types

class Server():

    def __init__(self, host, port, data_insert):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.data_insert = data_insert

    def launch_server(self):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((self.host, self.port))
        lsock.listen()
        print(f"listening on {self.host} {self.port}")
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.accept_wrapper(key.fileobj)
                else:
                    data = self.service_connection(key, mask)
                    if mask & selectors.EVENT_READ:
                        self.data_insert.send_data(data)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print(f"Accpeted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print(f"Closing connection to {data.addr}")
                self.sel.unregister(sock)
                sock.close()
            return data.outb

        if mask & selectors.EVENT_WRITE:
            if data.outb:
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]
