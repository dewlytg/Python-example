#!/usr/bin/env python

"""
redis 消息发布
"""

from redishelper import RedisHelper

obj = RedisHelper()
obj.public('hello')
