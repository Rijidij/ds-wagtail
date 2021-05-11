from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

from ..text_formats.fields import BasicRichTextField


@register_snippet
class Alert(models.Model):
    title = models.CharField(max_length=100)
    message = BasicRichTextField()
    active = models.BooleanField(default=False)
    cascade = models.BooleanField(default=False, verbose_name='Display on child pages')

    panels = [
        FieldPanel('title'),
        FieldPanel('message'),
        FieldPanel('active'),
        FieldPanel('cascade'),
    ]

    def __str__(self):
        return self.title
