# Generated by Django 3.1.8 on 2021-05-05 14:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentspage',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
