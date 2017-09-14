#!/usr/bin/env python

"""
创建 TCP 客户端
创建 TCP 客户端相对服务器来说更为容易。与 TCP 服务器那段类似，我们也是先给出伪代码及其解释，然后再给出真正的代码。
cs = socket()           # 创建客户套接字
cs.connect()            # 尝试连接服务器
comm_loop:              # 通讯循环
cs.send()/cs.recv()     # 对话（发送／接收）
cs.close()              # 关闭客户套接字
"""

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input(">")
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()