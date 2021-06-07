from django.db import models
from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock

from ..text_formats.blocks import BasicRichTextBlock


class MediaSnippetBlock(blocks.StructBlock):
    snippet = SnippetChooserBlock('media_embed.MediaSnippet', label='Media snippet item')

    class Meta:
        label = 'Media snippet block'
        icon = 'media'
        template = 'media_embed/blocks/media_snippet_block.html'


class MediaEmbedBlock(blocks.StructBlock):
    title = blocks.TextBlock(max_length=255)
    intro = BasicRichTextBlock(required=False)
    media_embed = AbstractMediaChooserBlock()


    class Meta:
        label = 'Media embed block'
        icon = 'media'
        template = 'media_embed/blocks/media_embed_block.html'

