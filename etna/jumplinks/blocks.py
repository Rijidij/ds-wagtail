from wagtail.core import blocks

from ..quotes.blocks import QuoteBlock


class JumplinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80)
    anchor = blocks.CharBlock(required=False, max_length=80)

    class Meta:
        icon = 'arrows-up-down'
        label = 'Jumplink'
        template = 'jumplinks/blocks/jumplink.html'


# Create "wrappers" for streamfield blocks with a jumplink.

class JumplinkQuoteBlock(blocks.StructBlock):
    block = QuoteBlock()
    jumplink = JumplinkBlock()

    class Meta:
        icon = 'openquote'
        label = 'Jumplink Quote'
        template = 'jumplinks/blocks/jumplink_wrapper.html'


class JumplinkParagraphBlock(blocks.StructBlock):
    block = blocks.RichTextBlock(label='Paragraph')
    jumplink = JumplinkBlock()

    class Meta:
        icon = 'pilcrow'
        label = 'Jumplink Paragraph'
        template = 'jumplinks/blocks/jumplink_wrapper.html'
