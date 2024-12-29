from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary using template filter"""
    return dictionary.get(key, '')
