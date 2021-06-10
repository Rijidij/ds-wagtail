from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock


class YouTubeBlock(blocks.StructBlock):
    """ Embed a YouTube video player."""

    video = EmbedBlock()

    class Meta:
        template = "streams/blocks/youtube-block.html"
        icon = "media"
        label = "Embed YouTube video"
