from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    roles_choices = [
        ('HR', 'Hairdresser'),
        ('CL', 'Client'),
    ]
    role = models.CharField(max_length=2, choices=roles_choices, default='CL')
    token = models.CharField(max_length=256, default='')


class Service(models.Model):
    name = models.CharField(blank=False, max_length=100)
    approximate_time = models.IntegerField()
    price = models.IntegerField()
    notes = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{self.name}'


class Visit(models.Model):
    date = models.DateTimeField()
    service = models.ForeignKey(Service, related_name='services', on_delete=models.CASCADE)
    hairdresser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='hairdressers', on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='visits', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}, {self.client}'
