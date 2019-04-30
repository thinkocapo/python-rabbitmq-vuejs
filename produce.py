import time
import sys

import stomp

# class MyListener(stomp.ConnectionListener):
#     def on_error(self, headers, message):
#         print('received an error "%s"' % message)
#     def on_message(self, headers, message):
#         print('received a message "%s"' % message)

# conn = stomp.Connection()
# conn.set_listener('', MyListener())
# conn.start()
# conn.connect('admin', 'password', wait=True)

# conn.subscribe(destination='/queue/test', id=1, ack='auto')

# conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')

# time.sleep(2)
# conn.disconnect()


#!python
import threading
import logging
import time
import requests
import argparse

logging.basicConfig(level=logging.DEBUG)

from stompclient import PublishSubscribeClient

# Parse the message sent as argument
parser = argparse.ArgumentParser()
parser.add_argument("msg", help="pass your s3cret")
args = parser.parse_args()
psst = args.msg 

# works if you keep produce.py connected (don't .disconnect()) 
def frame_received(frame):
    # Do something with the frame!
    print "----Received Frame----\n%s\n-----" % frame

client = PublishSubscribeClient('127.0.0.1', 61613) # 15670 # 61613
listener = threading.Thread(target=client.listen_forever)
listener.start()

# For our example, we want to wait until the server is actually listening
client.listening_event.wait()

client.connect()
client.subscribe("/topic/test", frame_received)
client.send("/topic/test", psst)
# client.send("/topic/test", '{"key": "Another 1frame example."}') # JSON PARSE this

# AUTO DISCONNECT
# time.sleep(5) # Inject some sleep so the frames all get picked up before we fire a disconnect message.
client.disconnect()