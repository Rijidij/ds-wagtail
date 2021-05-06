from wagtail.core import blocks

from ..text_formats.blocks import BasicRichTextBlock

class QuoteBlock(blocks.StructBlock):
    """
    Quote streamfield component
    """
    title = blocks.CharBlock(max_length=100)
    quote = blocks.TextBlock(required=True)
    attribution = blocks.CharBlock(max_length=100)
    # ToDo: make this a link
    citation = blocks.CharBlock(max_length=100)
    # ToDo: add taxonomy field

    class Meta:
        icon = 'openquote'
        label = 'Quote'
        template = 'quote/blocks/quote.html'
