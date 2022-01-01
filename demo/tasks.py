from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task

from .models import Demo

@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x, y):
    number1 = x
    number2 = (y * random.randint(3, 100))
    total = number1 * number2
    new_obj = Demo.objects.create(
        name='some item',
        number1=number1,
        number2=number2,
        total=total
    )
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)

@shared_task()
def xsum2(numbers):
    return sum(numbers)
