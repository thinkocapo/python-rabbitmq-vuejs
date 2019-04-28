








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
    time.sleep(body.count(b'.'))
    # sio.emit('my event', {'data': 'foobar'})
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()





from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)