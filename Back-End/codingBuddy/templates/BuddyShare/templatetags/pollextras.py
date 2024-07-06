from django import template
 

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return "ritik"
    #return value.split(key)[0]
    