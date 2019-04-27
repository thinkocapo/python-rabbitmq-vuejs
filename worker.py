#!/usr/bin/env python
import time
import pika


# SOCKET IO
# import socketio
# create a Socket.IO server
# sio = socketio.Server()
# wrap with a WSGI application
# app = socketio.WSGIApp(sio)



# Pika to Queue
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


# Task or computation
def callback(ch, method, properties, body):
    print(method)
    print(" [x] Received %r" % properties)
    time.sleep(body.count(b'.'))
    # sio.emit('my event', {'data': 'foobar'})
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(
    queue='hello',
    on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
