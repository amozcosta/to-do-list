# Generated by Django 3.2.4 on 2021-06-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
    ]
