#!/usr/bin/env python
#coding:utf-8

##高级SocketServer用法，隐藏了之前复杂的定义
from SocketServer import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
     def handle(self):
          print '...connected from:', self.client_address
          self.wfile.write('[%s] %s' % (ctime(),
              self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()