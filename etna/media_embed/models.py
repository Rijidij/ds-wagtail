from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtailmedia.edit_handlers import MediaChooserPanel

from ..text_formats.fields import BasicRichTextField


@register_snippet
class AudioEmbed(models.Model):
    title = models.CharField(max_length=255)
    intro = BasicRichTextField(blank=True)
    audio_media = models.ForeignKey(
        'wagtailmedia.Media',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        limit_choices_to={'type': 'audio'}
    )

    panels = [
        FieldPanel('title'),
        RichTextFieldPanel('intro'),
        MediaChooserPanel('audio_media'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Audio embeds'
