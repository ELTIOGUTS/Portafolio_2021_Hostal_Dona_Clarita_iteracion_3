# Generated by Django 3.2.4 on 2021-07-08 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0041_habitacion_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='habitacion',
        ),
        migrations.DeleteModel(
            name='Habitacion',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
