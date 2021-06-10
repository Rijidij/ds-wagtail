import re
from django import template

register = template.Library()

@register.filter(name="youtubeembedurl")
def get_youtube_embed_url_with_parameters(url, params="rel=0"):
    """
    Gets a YouTube embed URL from a watch or share link.
    Adapted from: https://danielms.site/blog/wagtail-embedurl-youtube-tags/
    """

    if "youtube.com" in url or "youtu.be" in url:
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"  # Get video id from URL
        embed_url = re.sub(
            regex, r"https://www.youtube.com/embed/\1", url
        )  # Append video id to desired URL
        embed_url_with_parameters = embed_url + "?" + params  # Add additional parameters
        return embed_url_with_parameters
    else:
        return None
