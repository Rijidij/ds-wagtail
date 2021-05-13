from wagtail.core import blocks

from ..text_formats.blocks import BasicRichTextBlock
from ..quotes.blocks import QuoteBlock
from ..jumplinks import blocks as JumplinkBlocks


class ComponentsStreamBlock(blocks.StreamBlock):
    jumplink = JumplinkBlocks.JumplinkBlock()
    paragraph = blocks.RichTextBlock()
    jumplink_paragraph = JumplinkBlocks.JumplinkParagraphBlock()
    quote = QuoteBlock()
    jumplink_quote = JumplinkBlocks.JumplinkQuoteBlock()
