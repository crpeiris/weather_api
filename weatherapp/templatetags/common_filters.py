from django import template

register = template.Library()

@register.filter(name='underscore_to_space')
def underscore_to_space(value):
    """Replace underscores with spaces."""
    if value is None:
        return ''
    return str(value).replace('_', ' ')
