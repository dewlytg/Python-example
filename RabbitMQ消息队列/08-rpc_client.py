#!/usr/bin/env python

"""
客户端先生产消息，后消费消息
"""

import pika
import uuid

class FibonacciRpcClient (object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id: #接受服务端返回的uuid，来判断是否为指定的进程，可能存在多个进程同时执行，但是返回结果时间不确定，通过这个可以avoid
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue', #此queue用于存放要执行的内容
                                   properties=pika.BasicProperties(
                                        reply_to=self.callback_queue, #客户端把随机生成的queue-id传递给服务端，用来接受服务端的返回结果
                                        correlation_id=self.corr_id, #客户端通过uuid随机生成一个id来确定每次执行过程唯一
                                    ),
                                    body=str(n))
        while self.response is None:
            self.connection.process_data_events() #使用非阻塞模式来接受消息，代替了start_consuming()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print("[x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print ("[.] Got %r" % response)