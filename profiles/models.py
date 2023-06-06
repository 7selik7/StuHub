from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.email
