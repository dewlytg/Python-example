#!/usr/bin/env python

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    with open("index.html","rb") as fd:
        data = fd.read()
    client.send(data)

def main():
    sock  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("0.0.0.0",8000))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__  == "__main__":
    main()