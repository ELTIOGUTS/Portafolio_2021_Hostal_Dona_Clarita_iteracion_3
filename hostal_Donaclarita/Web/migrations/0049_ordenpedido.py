# Generated by Django 3.2.4 on 2021-07-11 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0048_alter_reserva_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=50)),
                ('detalle_del_pedido', models.TextField()),
                ('familia_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.familiaproducto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Web.proveedor')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.tipoproducto')),
            ],
        ),
    ]
