from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=5)
    description = models.TextField()
    deadline = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    TYPE_CHOICES = [
        ('Лабораторная', 'Лабораторная'),
        ('Тест', 'Тест'),
        ('РГР', 'РГР'),
        ('Іспит', 'Іспит'),
        ('курсова робота', 'курсова робота'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    user_id = models.IntegerField()
    dev_id = models.IntegerField()
    status = models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')], default=0)

    def __str__(self):
        return self.subject
    '''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_placed')
    dev_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_assigned')
    '''

