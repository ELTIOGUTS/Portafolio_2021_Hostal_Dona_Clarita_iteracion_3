# Generated by Django 3.2.4 on 2021-07-08 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0045_auto_20210708_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='empresa',
        ),
    ]
