#!/usr/bin/env python

"""
发布者发送消息，所有接受者都接受，类似广播
"""

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type="fanout")

message = "".join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange="logs",
                      routing_key="",
                      body=message)
print("[x] Sent %r" % message)
connection.close()