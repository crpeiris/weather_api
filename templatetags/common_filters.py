from django import template

register = template.Library()

@register.filter
def underscore_to_space(value):
    """Replace underscores with spaces."""
    return value.replace('_', ' ')
