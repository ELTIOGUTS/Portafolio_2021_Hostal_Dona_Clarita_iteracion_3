# Generated by Django 3.2.4 on 2021-07-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0028_alter_habitacion_estado_habitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='estado_habitacion',
            field=models.CharField(choices=[[0, 'Disponible '], [1, 'Disponible, Temporalmente'], [2, 'No Disponible, Reservada a empresa'], [3, 'No Disponible, En Mantenimiento'], [4, 'Fuera de servicio']], max_length=100),
        ),
    ]
