from django import template
from ..models import Alert

register = template.Library()

# Alert snippets
@register.inclusion_tag('alerts/tags/alerts.html', takes_context=True)
def alerts(context):
    """
    Return all active alert snippets.
    Using this tag in the header template would be one way of displaying global alerts.
    If this method is used, an additional field would be required to filter non-global (section/page) alerts.
    """
    return {
        'alerts': Alert.objects.filter(active=True),
        'request': context['request'],
    }
