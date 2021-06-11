from django import template

from bs4 import BeautifulSoup

from wagtail.embeds.embeds import get_embed
from wagtail.embeds.exceptions import EmbedException

register = template.Library()


@register.filter(name="embediframesrc")
def get_embed_iframe_src(url):
    """
    Get the src parameter from an Embed object so we can use a custom iframe.
    """
    try:
        embed = get_embed(url)
        soup = BeautifulSoup(embed.html, 'html.parser')
        return soup.iframe['src']
    except EmbedException:
        # Cannot find embed
        return None
