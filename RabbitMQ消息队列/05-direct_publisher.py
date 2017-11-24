#!/usr/bin/env python

"""
定向发布消息，定向收消息，类似多播
"""

import pika
import sys

#先执行,"python 05-direct_publisher.py info 内容",或者"python 05-direct_publisher.py warnning 内容" "python 05-direct_publisher.py error 内容"
connection = pika.BlockingConnection (pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

severity = sys.argv[1] if len (sys.argv) > 1 else 'info'
message = ' '.join (sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                       routing_key=severity,
                       body=message)
print ("[x] Sent %r:%r" % (severity, message))
connection.close()