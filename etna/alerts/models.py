from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

from ..text_formats.fields import BasicRichTextField


@register_snippet
class Alert(models.Model):
    title = models.CharField(max_length=100)
    message = BasicRichTextField()
    active = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('message'),
        FieldPanel('active')
    ]

    def __str__(self):
        return self.title
