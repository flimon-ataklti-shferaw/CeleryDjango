from django.db import models

class Demo(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{total}".format(total=self.total)