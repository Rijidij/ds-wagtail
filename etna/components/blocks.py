from wagtail.core import blocks

from ..text_formats.blocks import BasicRichTextBlock
from ..quotes.blocks import QuoteBlock


class ComponentsStreamBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    quote = QuoteBlock()
