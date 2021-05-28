# Generated by Django 3.1.8 on 2021-05-26 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, help_text='Your Twitter page URL')),
                ('youtube', models.URLField(blank=True, help_text='Your YouTube channel or user account URL')),
                ('linkedin', models.URLField(blank=True, help_text='Your LinkedIn page URL')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('instagram', models.URLField(blank=True, help_text='Your Instagram page URL')),
                ('rss', models.URLField(blank=True, help_text='Your RSS feed URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Social media links',
            },
        ),
    ]
