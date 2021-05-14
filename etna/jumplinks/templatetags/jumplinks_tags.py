from django import template

from wagtail.core.models import Page

register = template.Library()


def get_jumplink_from_struct_value(struct_value):
    jumplink = None

    if bool(struct_value['label']):
        jumplink = {
            'label': struct_value['label'],
            'anchor': struct_value['anchor'],
        }

    return jumplink


def get_jumplink_from_block(block):
    if block.block_type == "jumplink":
        jumplink = get_jumplink_from_struct_value(block.value)
    else:
        jumplink = get_jumplink_from_struct_value(block.value['jumplink'])

    return jumplink


@register.inclusion_tag('jumplinks/tags/jumplinks.html')
def jumplinks(page):
    """
    Return jumplinks from current page.
    """
    jumplinks = []
    for block in page.content:
        if block.block_type.startswith("jumplink"):
            jumplink = get_jumplink_from_block(block)
            if jumplink:
                jumplinks.append(jumplink)

    return {
        "page": page,
        "jumplinks": jumplinks,
    }
