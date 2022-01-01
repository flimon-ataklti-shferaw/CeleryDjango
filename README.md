#CeleryDjango 
We will use Django + celery + RabbitMQ 
1. pip install -r requirement.txt
2. Download rabbitmq using (https://www.rabbitmq.com/download.html)
3. rabbitmqctl status
4. rabbitmqctl add_user test test
5. rabbitmqctl set_user_tags test administratord
6. rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
7. http://localhost:15672/
8. use test for username and password
=======================================================================
- celery -A CeleryDjango worker -l info
- Inside shell
- from demo.tasks import add, mul, xsum
- add(22,23)
- mul(32,22)
- xsum([2,4,3])
- add.delay(2,2)
- mul.delay(23232,2323232)
- create periodic task from admin page
- celery -A CeleryDjango beat -l info --->(for scheduled tasks)