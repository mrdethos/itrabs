# Generated by Django 4.1.2 on 2022-12-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_customuser_professional_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='professional_history',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Professional history'),
        ),
    ]