# Generated by Django 4.1.2 on 2022-12-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_customuser_about_advertisement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='category',
            field=models.CharField(choices=[('Não especificado', 'Não especificado'), ('Serviços Domésticos', 'Serviços Domésticos'), ('TI e Programação', 'TI e Programação'), ('Moda e Beleza', 'Moda e Beleza'), ('Reforma e Reparos', 'Reforma e Reparos'), ('Saúde', 'Saúde'), ('Assistência Técnica', 'Assistência Técnica'), ('Tradução e Conteúdo', 'Tradução e Conteúdo'), ('Design e Multimedia', 'Design e Multimedia')], default='Não especificado', max_length=30, verbose_name='Categoria'),
        ),
    ]