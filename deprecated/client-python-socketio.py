import socketio
sio = socketio.Client()
sio.connect('http://localhost:5000')
print "YOYOYO"

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('message')
def on_message(data):
    print('I received a message!')


@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')
