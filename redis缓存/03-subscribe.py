#!/usr/bin/env python

"""
redis 消息订阅
"""

from redishelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)