#!/usr/bin/env python
# coding:utf-8
from pykafka import KafkaClient

__author__ = "dewly_tg"

"""
kafka producer and cosumer for python

斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。1 2 3 5 8……
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

"""


def product(mytopic, hosts, content):
    ## 如果kafka配置文件里配置的是主机名称，请配置成client = KafkaClient(hosts="kafka01:9092,kafka02:9092,kafka03:9092")
    client = KafkaClient(hosts=hosts)
    topic = client.topics[mytopic]
    producer = topic.get_producer()
    for i in range(4):
        print i
        producer.produce(content)
    producer.stop()


def consum(mytopic, hosts):
    # type: (object, object) -> object
    client = KafkaClient(hosts=hosts)
    topic = client.topics[mytopic]
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            #yield message.offset, message.value
            yield '{0} {1}'.format(message.offset, message.value)