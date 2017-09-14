#!/usr/bin/env python
#coding:utf-8

"""
UDP 和 TCP 服务器的另一个重要的区别是，由于数据报套接字是无连接的，所以无法把客户的连
接交给另外的套接字进行后续的通讯。这些服务器只是接受消息，需要的话，给客户返回一个结果
就可以了。
创建一个 UDP 服务器
由于 UDP 服务器不是面向连接的，所以不用像 TCP 服务器那样做那么多设置工作。事实上，并不用设置什么东西，直接等待进来的连接就好了。
ss = socket()                   # 创建一个服务器套接字
ss.bind()                       # 绑定服务器套接字
inf_loop:                       # 服务器无限循环
cs = ss.recvfrom()/ss.sendto()  # 对话（接收与发送）
ss.close()                      # 关闭服务器套接字

"""
from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print "waiting for message..."
    ##无连接，直接接受客户端数据，然后发送数据给客户端
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto("[%s] %s" %(ctime(),data),addr)
    print "...recevied from and return to:",addr

udpSerSock.close()