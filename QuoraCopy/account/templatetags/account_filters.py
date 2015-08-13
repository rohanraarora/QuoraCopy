from django import template
import json

register = template.Library()

@register.filter(name="addAttributes")
def addAttributes(value, arg):
    data = json.loads(arg)
    if data is None:
        return False
    else:
        return value.as_widget(attrs=data)
