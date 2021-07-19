# Generated by Django 3.2.4 on 2021-06-05 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0010_auto_20210605_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('asunto', models.IntegerField(choices=[[0, 'Problema'], [1, 'Reservar'], [2, 'Solicitud'], [3, 'Cancelar']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id_familia_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nro_familia_producto', models.CharField(max_length=999)),
                ('familia_producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nro_tipo_producto', models.CharField(max_length=999)),
                ('tipo_producto', models.CharField(max_length=999)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='familia_producto',
            field=models.ForeignKey(blank=True, db_column='nro_familia_producto', null=True, on_delete=django.db.models.deletion.CASCADE, to='Web.familiaproducto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(blank=True, db_column='nro_tipo_producto', null=True, on_delete=django.db.models.deletion.CASCADE, to='Web.tipoproducto'),
        ),
    ]
