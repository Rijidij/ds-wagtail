from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

from ..text_formats.blocks import BasicRichTextBlock


class StreamEmbedBlock(blocks.StructBlock):
    """ Embed a streaming media player (YouTube, Soundcloud, etc."""

    share = EmbedBlock(label="Share link")
    title = blocks.TextBlock(required=False, max_length=100)
    description = BasicRichTextBlock(required=False)

    class Meta:
        template = "streams/blocks/stream-embed-block.html"
        icon = "media"
        label = "Streaming media player"
