from wagtail.core import blocks

from ..quotes.blocks import QuoteBlock


class JumplinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80)
    anchor = blocks.CharBlock(required=False, max_length=80)

    class Meta:
        icon = 'arrows-up-down'
        label = 'Jumplink'
        template = 'jumplinks/blocks/jumplink.html'


class JumplinkQuoteBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80, label='Jumplink label')
    anchor = blocks.CharBlock(required=False, max_length=80, label='Jumplink anchor')
    block = QuoteBlock()

    class Meta:
        icon = 'openquote'
        label = 'Jumplink Quote'
        template = 'jumplinks/blocks/jumplink.html'


class JumplinkParagraphBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80, label='Jumplink label')
    anchor = blocks.CharBlock(required=False, max_length=80, label='Jumplink anchor')
    block = blocks.RichTextBlock(label='Paragraph')

    class Meta:
        icon = 'paragraph'
        label = 'Jumplink Paragraph'
        template = 'jumplinks/blocks/jumplink.html'
