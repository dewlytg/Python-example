#!/usr/bin/env python

import redis

pool = redis.ConnectionPool(host="localhost",port=6379)

r = redis.Redis(connection_pool=pool)
r.set("foo","Bar")
print(r.get("foo"))