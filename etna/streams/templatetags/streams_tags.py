from django import template
from django.utils.safestring import mark_safe

from bs4 import BeautifulSoup

from wagtail.embeds import embeds
from wagtail.embeds.exceptions import EmbedException


register = template.Library()


@register.inclusion_tag(filename='streams/tags/streamembed.html', takes_context=True, name='streamembed')
def embed_tag(context):
    try:
        url = context['self']['share'].url
        embed = embeds.get_embed(url)
        soup = BeautifulSoup(embed.html, 'html.parser')

        return {
            # the whole embed object
            'embed': embed,
            # the src attribute of the iframe
            'embediframesrc': soup.iframe['src'],
            # optional title
            'title': context['self']['title'],
            # optional description
            'summary': context['self']['summary'],
        }
    except EmbedException:
        return None
