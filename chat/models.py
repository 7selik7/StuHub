from django.db import models
from profiles.models import Profile


class Chat(models.Model):
    name = models.CharField(max_length=100)
    user1_id = models.IntegerField(default=0)
    user2_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender_name} in {self.chat}"
