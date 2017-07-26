#!/usr/bin/env python
#coding:utf-8
__author__="dewly_tg"

"""
    redis module operation
"""

import redis

pool = redis.ConnectionPool(host="192.168.2.41", port="6379")
r = redis.Redis(connection_pool=pool)

r.set('foo','Bar',ex=3)
print r.get('foo')

r.set('u1','tg',px=3)
print r.get('u1')

r.mset(k1='v1', k2='v2')
print r.mget("k1","k2")

r.getset('foo',"new")
print r.get('foo')

r.set("foo1","武汉市")
print r.getrange("foo1",0,2)

r.set("foo1","bar_new")
print r.getrange("foo1",0,2)

r.setrange("foo1",1,"aaa")
print r.get("foo1")
print r.strlen("foo1")

r.set("foo",123)
r.incr("foo",amount=1)
print r.get("foo")

r.set("foo1","123.0")
r.incrbyfloat("foo1",amount=2.0)
print r.get("foo1")

r.append("foo","abc")
print r.get("foo")

r.lpush("l1",'a','b','c','d')
print r.lrange('l1',0,-1)
r.rpush('l2','a','b','c','d')
print r.lrange('l2',0,-1)


