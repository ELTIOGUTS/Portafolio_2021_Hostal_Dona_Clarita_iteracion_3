# Generated by Django 3.2.4 on 2021-07-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0047_alter_reserva_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('APROBADA', 'Aprobada'), ('CANCELADA', 'Cancelada')], default='APROBADA', max_length=150),
        ),
    ]
