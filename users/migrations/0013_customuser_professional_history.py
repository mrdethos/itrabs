# Generated by Django 4.1.2 on 2022-12-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_customuser_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='professional_history',
            field=models.TextField(blank=True, max_length=300, verbose_name='Professional history'),
        ),
    ]
