# Generated by Django 3.1.8 on 2021-05-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_auto_20210507_1545'),
        ('components', '0004_auto_20210506_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentspage',
            name='body_region_alert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='alerts.alert'),
        ),
    ]
