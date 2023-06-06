from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_placed')
    dev_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_assigned')
    status = models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')], default=0)

    def __str__(self):
        return self.subject
