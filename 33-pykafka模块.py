#coding:utf-8

from pykafka import KafkaClient

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
    client = KafkaClient(hosts=hosts)
    topic = client.topics[mytopic]
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            #yield message.offset, message.value
            yield '{0} {1}'.format(message.offset, message.value)