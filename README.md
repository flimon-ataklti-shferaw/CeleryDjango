#CeleryDjango 
We will use Django + celery + RabbitMQ 
1. pip install -r requirement.txt
2. Download rabbitmq using (https://www.rabbitmq.com/download.html)
3. rabbitmqctl status
4. rabbitmqctl add_user test test
5. rabbitmqctl set_user_tags test administrator
6. rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
7. http://localhost:15672/
8. use test for username and password
=======================================================================
rabbitmq-server (to run rabbitmq)
celery -A CeleryDjango worker -l info
--- you will see the app, transport, tasks, ..... ---
rabbitmqctl shutdown (to shutdown rabbitmqctl)
celery -A CeleryDjango worker -l info
--- you will find errors ---
rabbitmq-server (start it again)
Python manage.py shell
From demo.tasks import add
add.delay(3,3)
check the result in (celery -A CeleryDjango worker -l info)
add.apply_async((3,2), countdown=5) (to delay it)
check the result in (celery -A CeleryDjango worker -l info)