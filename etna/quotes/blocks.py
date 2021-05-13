from wagtail.core import blocks

from ..text_formats.blocks import BasicRichTextBlock
from ..jumplinks.blocks import JumplinkBlock

class QuoteBlock(blocks.StructBlock):
    """
    Quote streamfield component
    """
    title = blocks.CharBlock(max_length=100)
    quote = blocks.TextBlock(required=True)
    attribution = blocks.CharBlock(required=False, max_length=100)
    # ToDo: make this a link
    citation = blocks.CharBlock(required=False, max_length=100)
    # ToDo: add taxonomy field

    jumplink = JumplinkBlock()

    class Meta:
        icon = 'openquote'
        label = 'Quote'
        template = 'quotes/blocks/quote.html'
