#!/usr/bin/env python

"""
发送者发送一条，接受者接受一条，类似单播
"""

import pika,time

#创建连接，声明管道
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue="hello",durable=True)

def callback(ch,method,properties,body):
    print("--->",ch,method,properties)
    #time.sleep(30)
    print("[x] Recevied %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag) #手动收到消息确认

channel.basic_qos(prefetch_count=1) #消费者一条一条处理，轮询机制
channel.basic_consume(callback,
                      queue="hello",
                      )
print("[*] Waiting for message. To exit press CTRL+C")
channel.start_consuming()