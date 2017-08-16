#coding:utf-8

import socket
import struct
ip = "8.8.8.8"
num_ip=socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])
print num_ip

import socket
import struct
num_ip = 134744072
ip = socket.inet_ntoa(struct.pack('I',socket.htonl(num_ip)))
print ip