from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STATUS = (
        ('standard', 'standard'),
        ('gold', 'gold'),
        ('platinum', 'platinum')
    )
    LANGUAGES = (
        ('português', 'português'),
        ('inglês', 'inglês'),
        ('espanhol', 'espanhol'),
    )
    CATEGORY = (
        ('Serviços Domésticos', 'Serviços Domésticos'),
        ('TI e Programação', 'TI e Programação'),
        ('Moda e Beleza', 'Moda e Beleza'),
        ('Reforma e Reparos', 'Reforma e Reparos'),
        ('Saúde', 'Saúde'),
        ('Assistência Técnica', 'Assistência Técnica'),
        ('Tradução e Conteúdo', 'Tradução e Conteúdo'),
        ('Design e Multimedia', 'Design e Multimedia'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField('Phone number', max_length=16, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='standard')
    about_general = models.TextField('About me', max_length=300, default='', blank=True)
    about_looking = models.TextField('Looking for', max_length=300, default='', blank=True)
    about_expectation = models.TextField('What I expect', max_length=300, default='', blank=True)

    occupation = models.CharField('occupation', max_length=50, blank=True)
    about_professional = models.TextField('About my career', max_length=300, default='', blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY, default='')
    availability = models.TextField('Availability', max_length=70, default='', blank=True)
    #languages = models.CharField(max_length=15, choices=LANGUAGES, default=)

    def __str__(self):
        return self.email