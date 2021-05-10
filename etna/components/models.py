from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

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

    # Alert to be displayed in the body region of the page.
    # Additional fields could be added for the header and footer regions.
    body_region_alert = models.ForeignKey(
        'alerts.Alert',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        SnippetChooserPanel('body_region_alert')
    ]
