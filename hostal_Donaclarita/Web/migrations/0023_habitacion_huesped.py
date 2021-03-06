# Generated by Django 3.2.4 on 2021-06-29 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0022_auto_20210629_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_habitacion', models.CharField(max_length=50)),
                ('tipo_habitacion', models.CharField(max_length=100)),
                ('precio_por_noche', models.IntegerField()),
                ('cantidad_camas', models.CharField(max_length=50)),
                ('cantidad_baños', models.CharField(max_length=50)),
                ('tipo_cama', models.CharField(max_length=100)),
                ('tipo_baño', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='habitaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=250)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('cantidad_personas', models.IntegerField()),
                ('fecha_llegada', models.DateField()),
                ('fecha_ida', models.DateField()),
                ('empresa', models.CharField(max_length=50)),
                ('rut_empresa', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=100)),
                ('telefono_empresa', models.CharField(max_length=50)),
                ('correo_empresa', models.CharField(max_length=50)),
                ('direccion_empresa', models.TextField()),
                ('Habitacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Web.habitacion')),
            ],
        ),
    ]
