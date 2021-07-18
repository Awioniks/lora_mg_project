#!/usr/bin/python3

import socket
import sys
import selectors
import types

HOST = '127.0.0.1'
PORT = 65432

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"Accpeted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
        return data.outb
    
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]
    
sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"listening on {HOST} {PORT}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            data = service_connection(key, mask)
            if mask & selectors.EVENT_READ:
                print(data, " data to display")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     while True:
#         try:
#             conn, addr = s.accept()
#             with conn:
#                 print('Connected by', addr)
#                 while True:
#                     data = conn.recv(1024)
#                     if data:
#                         conn.sendall(data)
#                     else:
#                         break
#         except KeyboardInterrupt:
#             sys.exit("Bye !")
