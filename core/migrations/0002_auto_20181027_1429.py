# Generated by Django 2.1.2 on 2018-10-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='genero',
            field=models.BinaryField(),
        ),
    ]