from django import template
from ..models import Alert

register = template.Library()

# Alert snippets
@register.inclusion_tag('alerts/tags/alerts.html', takes_context=True)
def alerts(context):
    """
    Return all active alerts.
    """
    return {
        'alerts': Alert.objects.filter(active=True),
        'request': context['request'],
    }
