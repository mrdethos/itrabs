from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STATUS = (
        ('standard', 'standard'),
        ('gold', 'gold'),
        ('platinum', 'platinum')
    )
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='standard')
    description = models.TextField('Description', max_length=600, default='', blank=True)
    def __str__(self):
        return self.username