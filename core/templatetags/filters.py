from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    value.field.widget.attrs['class']= arg
    return value