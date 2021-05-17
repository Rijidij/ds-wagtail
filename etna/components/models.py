from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey

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
        SnippetChooserPanel('body_region_alert'),
        InlinePanel('alert_placements', label="Alerts"),
    ]


class ComponentsPageAlertsPlacement(Orderable, models.Model):
    page = ParentalKey('components.ComponentsPage', on_delete=models.CASCADE, related_name='alert_placements')
    alert = models.ForeignKey('alerts.Alert', on_delete=models.CASCADE, related_name='+')

    class Meta(Orderable.Meta):
        verbose_name = "alert placement"
        verbose_name_plural = "alert placements"

    panels = [
        SnippetChooserPanel('alert'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.alert.title
