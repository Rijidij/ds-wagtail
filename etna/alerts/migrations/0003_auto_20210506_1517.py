# Generated by Django 3.1.8 on 2021-05-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_alert_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='name',
            new_name='title',
        ),
    ]
