from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STATUS = (
        ('standard', 'standard'),
        ('gold', 'gold'),
        ('platinum', 'platinum')
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField('Phone number', max_length=16, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='standard')
    about_general = models.TextField('About me', max_length=300, default='', blank=True)
    about_looking = models.TextField('Looking for', max_length=300, default='', blank=True)
    about_expectation = models.TextField('What I expect', max_length=300, default='', blank=True)

    def __str__(self):
        return self.email