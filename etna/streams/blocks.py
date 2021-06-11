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


class YouTubeBlock(blocks.StructBlock):
    """ Embed a YouTube video player."""

    share = EmbedBlock(label="YouTube share link")
    title = blocks.TextBlock(required=False, max_length=100)
    description = BasicRichTextBlock(required=False)

    class Meta:
        template = "streams/blocks/stream-embed-block.html"
        icon = "media"
        label = "YouTube video"


class SoundCloudBlock(blocks.StructBlock):
    """ Embed a SoundCloud audio player. """

    share = EmbedBlock(label="SoundCloud share link")
    title = blocks.TextBlock(required=False, max_length=100)
    description = BasicRichTextBlock(required=False)

    class Meta:
        template = "streams/blocks/stream-embed-block.html"
        icon = "media"
        label = "SoundCloud audio"
