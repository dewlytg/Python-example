#!/usr/bin/env python

"""
socket client for ftp
"""

import socket
import hashlib

client = socket.socket()
client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response:",server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        recevied_size = 0
        filename = cmd.split()[1]
        f = open(filename+".new","wb")
        m = hashlib.md5()
        while recevied_size != file_total_size:
            if file_total_size - recevied_size > 1024:
                size = 1024
            else: #最后一次，有多少接受多少，避免最后一次再次粘包
                size = file_total_size - recevied_size
            data = client.recv(size)
            recevied_size += len(data)
            m.update(data)
            f.write(data)
            print(file_total_size,recevied_size)
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done")
            f.close()
        server_file_md5 = client.recv(1024)
        print("server file md5:",server_file_md5)
        print("client file md5:",new_file_md5)
client.close()