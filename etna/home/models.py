from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from ..media_embed.blocks import MediaSnippetBlock, MediaEmbedBlock


class HomePage(Page):
    content = StreamField(
        [
            ('media_snippet_block', MediaSnippetBlock()),
            ('media_embed_block', MediaEmbedBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

