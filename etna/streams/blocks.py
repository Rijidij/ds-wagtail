from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock


class YouTubeBlock(blocks.StructBlock):
    """ Embed a YouTube video player."""

    share = EmbedBlock(label="YouTube share link")

    class Meta:
        template = "streams/blocks/stream-embed.html"
        icon = "media"
        label = "YouTube video"


class SoundCloudBlock(blocks.StructBlock):
    """ Embed a SoundCloud audio player. """

    share = EmbedBlock(label="SoundCloud share link")

    class Meta:
        template = "streams/blocks/stream-embed.html"
        icon = "media"
        label = "SoundCloud audio"
