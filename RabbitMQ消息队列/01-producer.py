#!/usr/bin/env python

"""
发送者发送一条，接受者接受一条，类似单播
"""

import pika

#创建连接，声明管道
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#声明queue
channel.queue_declare(queue="hello",durable=True) #队列持久化，通过rabbitmqctl list_queues 可以查看队列 消息条数是否持久化，重启后查看

#an RabbitMQ a message can never be sent directly to the queue,it always need to go through an exchange.
channel.basic_publish(exchange="",
                      routing_key="hello",
                      body="Hello World!",
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent #消息持久化
                      ))
print("[x] Sent Hello World!")
connection.close()