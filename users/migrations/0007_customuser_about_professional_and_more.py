# Generated by Django 4.1.2 on 2022-12-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_about_expectation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_professional',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='About my career'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='availability',
            field=models.TextField(blank=True, default='', max_length=70, verbose_name='Availability'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='category',
            field=models.CharField(choices=[('domestic_services', 'Serviços Domésticos'), ('it', 'TI e Programação'), ('fashion', 'Moda e Beleza'), ('repairs', 'Reforma e Reparos'), ('health', 'Saúde'), ('technical_assistance', 'Assistência Técnica'), ('translate', 'Tradução e Conteúdo'), ('design', 'Design e Multimedia')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, verbose_name='occupation'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about_expectation',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='What I expect'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about_general',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='About me'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about_looking',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Looking for'),
        ),
    ]