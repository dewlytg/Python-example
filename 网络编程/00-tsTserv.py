#!/usr/bin/env python
#coding:utf-8

"""
创建一个 TCP 服务器

我们首先将给出一个关于如何创建一个通用的 TCP 服务器的伪代码，然后解释我们都做了些什么。要注意的是，这只是设计服务器的一种方法，当你对服务器的设计有了一定的了解之后，你就能用你所希望的方式来修改这段伪代码：
ss = socket()           # 创建服务器套接字
ss.bind()               # 把地址绑定到套接字上
ss.listen()             # 监听连接
inf_loop:               # 服务器无限循环
cs = ss.accept()        # 接受客户的连接
comm_loop:              # 通讯循环
cs.recv()/cs.send()     # 对话（接收与发送）
cs.close()              # 关闭客户套接字
ss.close()              # 关闭服务器套接字（可选）
"""

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "waiting for connection..."
    ##建立连接
    tcpCliSock,addr = tcpSerSock.accept()
    print "...connected from:",addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send("[%s] %s" %(ctime(),data))

tcpCliSock.close()
tcpSerSock.close()