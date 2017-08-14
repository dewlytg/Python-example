#coding:utf-8

##第三方模块
import netifaces as ni
ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print ip

##非第三方模块
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('eth0')