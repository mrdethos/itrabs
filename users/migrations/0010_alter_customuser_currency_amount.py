# Generated by Django 4.1.2 on 2022-12-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_currency_customuser_currency_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='currency_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Amount of currency'),
        ),
    ]
