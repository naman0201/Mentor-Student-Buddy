from django import template
 

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[0]

@register.filter(name='times') 
def times(number):
    return range(number)

    
    
@register.filter(name='addjoin') 
def addjoin(value,key):
    return value
