# Generated by Django 3.1.3 on 2020-11-03 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trabajador',
            new_name='worker',
        ),
    ]
