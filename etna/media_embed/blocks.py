from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock

class MediaEmbedBlock(blocks.StructBlock):
    snippet = SnippetChooserBlock('media_embed.MediaEmbed', label='Media embed item')

    class Meta:
        label = 'Media embed block'
        icon = 'media'
        template = 'media_embed/blocks/media_embed_block.html'
