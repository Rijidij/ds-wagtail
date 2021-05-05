from wagtail.core import blocks

from ..text_formats.blocks import BasicRichTextBlock


class ComponentsStreamBlock(blocks.StreamBlock):
    paragraph = BasicRichTextBlock()
