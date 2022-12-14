from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    STATUS = (
        ('standard', 'standard'),
        ('gold', 'gold'),
        ('platinum', 'platinum')
    )
    LANGUAGES = (
        ('Português', 'Português'),
        ('Inglês', 'Inglês'),
        ('Espanhol', 'Espanhol'),
    )
    CATEGORY = (
        ('Não especificado', 'Não especificado'),
        ('Serviços Domésticos', 'Serviços Domésticos'),
        ('TI e Programação', 'TI e Programação'),
        ('Moda e Beleza', 'Moda e Beleza'),
        ('Reforma e Reparos', 'Reforma e Reparos'),
        ('Saúde', 'Saúde'),
        ('Assistência Técnica', 'Assistência Técnica'),
        ('Tradução e Conteúdo', 'Tradução e Conteúdo'),
        ('Design e Multimedia', 'Design e Multimedia'),
    )
    CURRENCY = (
        ('BRL', 'BRL'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField('Phone number', max_length=16, default='(0) 0 0000-0000')
    status = models.CharField(choices=STATUS, max_length=10, default='standard')
    about_general = models.TextField('About me', max_length=300, default='', blank=True)
    about_looking = models.TextField('Looking for', max_length=300, default='', blank=True)
    about_expectation = models.TextField('What I expect', max_length=300, default='', blank=True)

    occupation = models.CharField('Occupation', max_length=50, blank=True)
    professional_history = models.TextField('Professional history', max_length=300, default='', blank=True)
    about_professional = models.TextField('About my career', max_length=300, default='', blank=True)
    about_advertisement = models.TextField('Descrição do Anúncio:', max_length=300, default='', blank=True)
    category = models.CharField('Categoria', choices=CATEGORY, max_length=30, default='Não especificado')
    availability = models.TextField('Disponibilidade', max_length=70, default='', blank=True)
    currency =  models.CharField('Moeda', max_length=3, choices=CURRENCY, default='BRL')
    currency_amount = models.DecimalField('Preço por hora', max_digits=10, decimal_places=2, default=0)

    languages = MultiSelectField('Idiomas', max_length=30, choices=LANGUAGES, default='Português')

    def __str__(self):
        return self.email