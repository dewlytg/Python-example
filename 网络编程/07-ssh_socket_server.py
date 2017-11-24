#!/usr/bin/env python

"""
socket server for ssh
"""

import socket,os,time

server = socket.socket()
server.bind(("localhost",9999))
server.listen()

while True:
    #支持多个连接，所以使用while循环
    conn,addr = server.accept()
    print("new addr",addr)
    #支持从客户端一直接受数据
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read()
        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has not output"
        conn.send(str(len(cmd_res.encode())).encode())
        recevied_ack = conn.recv(1024) #把代码放到Linux执行会发生粘包错误，这个可以避免错误发生
        conn.send(cmd_res.encode())
        print("send done")
server.close()