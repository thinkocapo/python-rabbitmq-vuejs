#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(channel, method, properties, body):
    print(" [x] Received %r" % body)
    channel.basic_ack(delivery_tag = method.delivery_tag)


# auto_ack=True means RabbitMQ will mark it as delivered,
# but Worker fails to finish running the Task
channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()