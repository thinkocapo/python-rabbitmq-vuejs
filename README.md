#Instructions
1. start RabbitMQ server
rabbitmq-server
2. send.py receive.py
3. new_task.py 


for x in range(6): publish...
then open 6 worker.py's and see each gets assigned 1
or   open 3 worker.py's and see each gets assigned 3, and the execution speed is indiscernable to the eye, even though 3workers technically is slower


but add a Task(1000milliseconds) [async] and it takes noticeably longer



rabbitmqctl start_app
rabbitmqctl stop_app