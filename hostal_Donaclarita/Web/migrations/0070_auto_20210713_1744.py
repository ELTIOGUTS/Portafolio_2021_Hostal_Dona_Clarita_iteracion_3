# Generated by Django 3.2.4 on 2021-07-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0069_alter_habitacion_estado_habitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='estado_habitacion',
            field=models.IntegerField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible'), ('Rechazado', '')]),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
