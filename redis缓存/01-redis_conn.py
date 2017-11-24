#!/usr/bin/env python

import redis
#每次客户端请求都需要建立一个连接
r = redis.Redis(host="localhost",port=6379)
r.set("foo","Bar")
print(r.get("foo"))