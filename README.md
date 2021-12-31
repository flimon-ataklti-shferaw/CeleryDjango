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
- when user fill the form and click send, automatic django will send automatic response and later celery will send the email
