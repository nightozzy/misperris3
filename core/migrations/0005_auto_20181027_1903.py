# Generated by Django 2.1.2 on 2018-10-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181027_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.FileField(upload_to='media/'),
        ),
    ]