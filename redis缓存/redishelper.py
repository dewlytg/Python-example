#!/usr/bin/env python

import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='localhost')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub() #打开收音机
        pub.subscribe(self.chan_sub) #调频道
        pub.parse_response() #准备接受
        return pub