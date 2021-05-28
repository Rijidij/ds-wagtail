from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock

class AudioEmbedBlock(blocks.StructBlock):
    snippet = SnippetChooserBlock('media_embed.AudioEmbed')

    class Meta:
        label = 'Audio embed block'
        icon = 'media'
        template = 'audio_embed/blocks/audio_embed_block.html'
