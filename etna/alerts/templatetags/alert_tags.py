from django import template

from wagtail.core.models import Page

from ..models import Alert

# Alert snippets

register = template.Library()


def get_body_region_alert(page):
    """
    Get the body_region_alert field, if it exists.
    """
    alert = None
    try:
        alert = page.body_region_alert
    except AttributeError:
        pass

    if alert and alert.active:
        return alert
    else:
        return None


@register.inclusion_tag('alerts/tags/alerts.html', takes_context=True)
def alerts(context):
    """
    Return alerts from current page and those cascaded from ancestors.
    To begin with, I'm just trying the single "body_region_alert" field.
    """
    page = context['page']
    alerts = []

    # Get alert for current page, if any.
    alert = get_body_region_alert(page)
    if alert:
        alerts.insert(0, alert)

    # Get current page ancestors.
    branch = Page.objects.ancestor_of(page).specific()
    # Iterate backwards and if page has alert and "cascade" is true,
    # add to alerts list.
    for i in reversed(range(branch.count())):
        alert = get_body_region_alert(branch[i])
        if alert and alert.cascade:
            alerts.insert(0, alert)

    return {
        'alerts': alerts,
        'request': context['request'],
    }


@register.inclusion_tag('alerts/tags/all_alerts.html', takes_context=True)
def all_alerts(context):
    """
    Return all active alert snippets.
    Using this tag in the header template would be one way of displaying global alerts.
    If this method is used, an additional field would be required to filter non-global (section/page) alerts.
    """
    return {
        'alerts': Alert.objects.filter(active=True),
        'request': context['request'],
    }
