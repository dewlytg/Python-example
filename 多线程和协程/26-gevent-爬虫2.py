#!/usr/bin/env python

from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all() #把当前程序的所有的io操作单独做上标记

def f(url):
    print("GET: %s" %url)
    resp = request.urlopen(url)
    data = resp.read()
    print("%d bytes recevied from %s." %(len(data),url))

urls = ['https://www.sohu.com/',
        'https://www.yahoo.com/',
        'https://github.com/' ]

time_start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,"https://www.sohu.com/"),
    gevent.spawn(f,"https://www.yahoo.com/"),
    gevent.spawn(f,"https://github.com/"),
])
print("异步cost",time.time() - async_time_start)