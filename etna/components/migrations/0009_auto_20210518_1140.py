# Generated by Django 3.1.8 on 2021-05-18 11:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0008_auto_20210513_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentspage',
            name='content',
            field=wagtail.core.fields.StreamField([('jumplink', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=80, required=False)), ('anchor', wagtail.core.blocks.CharBlock(max_length=80, required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('jumplink_paragraph', wagtail.core.blocks.StructBlock([('block', wagtail.core.blocks.RichTextBlock(label='Paragraph')), ('jumplink', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=80, required=False)), ('anchor', wagtail.core.blocks.CharBlock(max_length=80, required=False))]))])), ('quote', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100)), ('quote', wagtail.core.blocks.TextBlock(required=True)), ('attribution', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('citation', wagtail.core.blocks.CharBlock(max_length=100, required=False))])), ('jumplink_quote', wagtail.core.blocks.StructBlock([('block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100)), ('quote', wagtail.core.blocks.TextBlock(required=True)), ('attribution', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('citation', wagtail.core.blocks.CharBlock(max_length=100, required=False))])), ('jumplink', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=80, required=False)), ('anchor', wagtail.core.blocks.CharBlock(max_length=80, required=False))]))]))], blank=True, null=True),
        ),
    ]
