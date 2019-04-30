#!/usr/bin/env python
import sys
import pika

#python 2.7
import requests
import argparse

import pdb # pdb.set_trace()

# Open a blocked channel from Python to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Exchange and Queue declaration
channel.queue_declare(queue='hello')
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# Number of messages to send is passed by command line
# parser = argparse.ArgumentParser()
# parser.add_argument("quantity", help="number of messages to send")
# args = parser.parse_args()
# quantity = args.quantity 

quantity = sys.argv[1:]
pdb.set_trace()
for x in range(int(quantity[0])):
    # or send through a string '' like '{ k1: v1 }' and parse it
    message = ' '.join(sys.argv[2:]) or "Hello World!"
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print(" [x] Sent %r" % message)


# TODO write python so you can keep the interpreter open and continue sending more messages
# wold need a helper function for `channel.basic_publish(...)`