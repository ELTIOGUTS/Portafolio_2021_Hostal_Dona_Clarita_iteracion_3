# Generated by Django 3.2.4 on 2021-07-15 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0075_alter_ordencompra_tipo_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordencompra',
            name='comentarios',
        ),
    ]
