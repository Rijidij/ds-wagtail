from wagtail.core import blocks

class JumplinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80)
    anchor = blocks.CharBlock(required=False, max_length=80)

    class Meta:
        icon = 'arrows-up-down'
        label = 'Jumplink'
        template = 'jumplinks/blocks/jumplink.html'
