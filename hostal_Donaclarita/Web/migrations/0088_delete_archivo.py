# Generated by Django 3.2.4 on 2021-07-18 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0087_rename_documento_archivo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Archivo',
        ),
    ]