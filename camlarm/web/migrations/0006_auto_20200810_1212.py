# Generated by Django 3.0.8 on 2020-08-10 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200810_1207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detections',
            new_name='Detection',
        ),
    ]