# Generated by Django 4.1.2 on 2022-12-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_professional_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_advertisement',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Advertisement desc'),
        ),
    ]
