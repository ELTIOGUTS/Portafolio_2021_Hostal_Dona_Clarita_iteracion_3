# Generated by Django 3.2.4 on 2021-07-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0094_factura_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
    ]
