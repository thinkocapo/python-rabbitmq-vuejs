# thinkocapo/python-rabbitmq-vue
rabbitmq-python-vue


## Setup - Run RabbitMQ
1. `rabbitmq-server start`
2. enable the rabbitmq 'web stomp' plugin `rabbitmq-plugins enable rabbitmq_web_stomp`

## Know the Protocools

*This project's browser integration uses STOMP*

There are 3 protocools, AMQP, MQTT and STOMP  
[AMPQP MQTT vs STOMP](https://blogs.vmware.com/vfabric/2013/02/choosing-your-messaging-protocol-amqp-mqtt-or-stomp.html)
STOMP was used because the Browser side javascript can directly consume Messages from RabbitMQ. The library stompjs wraps around a websocket to do this.

other modules considered, pika.py but couldn't open a socket/websocket back to browser. Rabbitmq channel seemed blocking/listening, so code for socket would never execute - and vice versa if socket connection formed first.
flaskSocketIO had same/similar issue.

Flask Sockets and Flask Pika
Browser Javascript > Sockets > Flask > Pika > RabbitMQ
Flask Pika - could not get to work https://github.com/wdtinc/flask-pika, low popularity and support
Flask Sockets - even if work with Javascript Sockets then still needs access to AMQP RabbitMQ

### AMQP
Optional, for testing
1. `cd amqp`
1. `python receive.py` (terminal1) then `python send.py` (terminal2)
or
2. `python worker.py` (terminal`) then `python new_task.py` (terminal2)

### STOMP
Makefile for this?
1. `rabbitmq-server start` (terminal1)
2. Chrome > File > Open > index.html
3. `python stomp.py` (terminal2)
4. Chrome > it logs in index.html console that message was received



### The Official Rabbitmq Example Apps
- `git clone` it from https://github.com/rabbitmq/rabbitmq-web-stomp-examples
- I ran its `make` command, different log activity each time. hung, or ended. unsure if this way necessary / what it does.
- https://www.rabbitmq.com/web-stomp.html mentions these examples
- access them on http://127.0.0.1:15670/, http://127.0.0.1:15670/web-stomp-examples/echo.html
- thinkocapo/run-rabbit-pythons-are-rabbitmq-ing


## Notes
Note on worker.py
Experimenting with sockets, flask plus open channel failed. blocking thread i/o, program execution wouldn't reach the second tool instantiation.

for x in range(6): publish...
then open 6 worker.py's and see each gets assigned 1
or   open 3 worker.py's and see each gets assigned 3, and the execution speed is indiscernable to the eye, even though 3workers technically is slower
but add a Task(1000milliseconds) [async] and it takes noticeably longer


```
rabbitmqctl start_app

rabbitmqctl stop_app
or
ps aux | grep rabbit
kill <pid>
```


https://github.com/jasonrbriggs/stomp.py/wiki/Simple-Example didn't work


https://pythonhosted.org/stompclient/usage.html?