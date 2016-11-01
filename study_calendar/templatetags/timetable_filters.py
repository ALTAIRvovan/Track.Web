from django import template
from ..models import TimeTable

register = template.Library()

@register.filter
def has_user(value, arg):
    return isinstance(value, TimeTable) and value.user_set.filter(pk=arg.id).exists()