# Generated by Django 3.2.4 on 2021-06-05 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_evento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]