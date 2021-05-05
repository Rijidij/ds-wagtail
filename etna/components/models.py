from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from .blocks import ComponentsStreamBlock


class ComponentsPage(Page):
    """
    Experimental page to test component options.
    No required fields, search fields, or parent/child restrictions applied.
    """
    content = StreamField(
        ComponentsStreamBlock,
        blank = True,
        null = True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
