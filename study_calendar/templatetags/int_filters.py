from django import template

register = template.Library()

@register.filter
def mod(value, arg):
    return (int(value)) % arg
