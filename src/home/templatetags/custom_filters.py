from django import template

register = template.Library()

@register.filter
def batch(iterable, n):
    """
    Splits an iterable into sublists of size n.
    """
    return [iterable[i:i + n] for i in range(0, len(iterable), n)]
