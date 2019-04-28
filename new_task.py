#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


for x in range(1):
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print(" [x] Sent %r" % message)