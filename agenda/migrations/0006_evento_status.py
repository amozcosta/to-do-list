# Generated by Django 3.2.4 on 2021-06-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_evento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Finalizado'), (2, 'Executando'), (3, 'Aberto')], default=1),
            preserve_default=False,
        ),
    ]