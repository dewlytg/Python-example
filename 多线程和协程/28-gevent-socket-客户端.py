#!/usr/bin/env python

import socket

HOST = "localhost"
PORT = 9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:"),encoding="utf-8")
    s.send(msg)
    data = s.recv(1024)
    print("Recevied",data)
s.close()