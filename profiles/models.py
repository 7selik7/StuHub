from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50)
    registration_time = models.DateTimeField(default=timezone.now)
    completed_orders = models.IntegerField(default=0)
    made_orders = models.IntegerField(default=0)

    def __str__(self):
        return self.email
