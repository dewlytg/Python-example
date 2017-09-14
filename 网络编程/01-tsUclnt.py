#!/usr/bin/env python

"""
cs = socket()              # 创建客户套接字
comm_loop:                 # 通讯循环
cs.sendto()/cs.recvfrom()  # 对话（发送／接收）
cs.close()                 # 关闭客户套接字
"""

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input(">")
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()