#Overview

THERE ARE 2 protocools, AMQP and STOMP

## Setup - Run RabbitMQ
1. `rabbitmq-server start`


[AMPQP MQTT vs STOMP](https://blogs.vmware.com/vfabric/2013/02/choosing-your-messaging-protocol-amqp-mqtt-or-stomp.html)

## AMQP
Optional, for testing
1. `cd amqp`
1. receive.py, send.py
or
2. worker.py, new_task.py

## STOMP
Makefile for this?
1. rabbitmq-server start (terminal1)
2. File > Open > index.html
3. pythong stomp.py *(terminal2)
4. Expected Result - logs in index.html console





3. RabbitMQ Web Stomp Plugin

// OLD
- ran `make` some log activity, it hung, or is designed to do that. then stopped it
- `rabbitmq-plugins enable rabbitmq_web_stomp` from https://www.rabbitmq.com/web-stomp.html
- http://127.0.0.1:15670/ for echo, bunny
- http://127.0.0.1:15670/web-stomp-examples/echo.html


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