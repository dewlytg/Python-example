#!/usr/bin/env python

"""
socket client for ssh
"""

import socket

client = socket.socket()
client.connect(("localhost",9999))

while True:
    #支持客户端循环发送数据到服务端
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode()) #python3中必须把字符串转换为bytes类型，这里可以理解字符串类型是utf-8
    cmd_res_size = client.recv(1024)
    print("命令结果大小:",cmd_res_size)
    client.send("please input somthing in order to packet splicing".encode()) #把代码放到Linux执行会发生粘包错误，这个可以避免错误发生
    received_size = 0
    received_data = b''
    while received_size != int(cmd_res_size.decode()): #cmd_res_size是bytes类型的数据，需要使用decode转换为字符串
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
client.close()