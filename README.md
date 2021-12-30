#CeleryDjango 
We will use Django + celery + RabbitMQ 
1. pip install -r requirement.txt
2. Follow (https://www.rabbitmq.com/download.html) 
3. brew install rabbitmq (FOR MAC), [for Windows follow https://www.rabbitmq.com/download.html]
4. brew install python-tk@3.9; (FOR MAC)
5. export PATH=$PATH:/usr/local/opt/rabbitmq/sbin
6. rabbitmqctl status
7. rabbitmqctl add_user test test
8. rabbitmqctl set_user_tags test administrator
9. rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
10. http://localhost:15672/
11. use test for username and password



Django Documenattion - (https://docs.djangoproject.com/en/3.2/)
Celery documentation - (https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
Rabbitmq documentation - (https://www.rabbitmq.com/documentation.html)