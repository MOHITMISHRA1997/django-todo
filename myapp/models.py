from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Task(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    your_task = models.CharField(max_length=150)
    priority = models.CharField(max_length=20)
    posted_date = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return f'{self.name} task'