#!/usr/bin/env python
import pika


# Pika to Queue
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
import time


# Task or computation
def callback(ch, method, properties, body):
    print(method)
    print(" [x] Received %r" % properties)
    print body

    # import pdb
    # pdb.set_trace()
    time.sleep(body.count(b'.'))
    # sio.emit('my event', {'data': 'foobar'})
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(queue='hello', on_message_callback=callback)

# channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


# When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to. Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.