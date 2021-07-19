# Generated by Django 3.2.4 on 2021-07-15 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0077_delete_ordencompra'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion', models.CharField(max_length=100)),
                ('detalle_de_la_compra', models.CharField(max_length=100)),
                ('estado_orden_compra', models.CharField(choices=[('En espera', 'En espera'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='En espera', max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Web.huesped')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Web.comedor')),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Web.servicio')),
            ],
        ),
    ]