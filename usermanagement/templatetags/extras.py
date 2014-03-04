from django import template

register = template.Library()


def joinby(value, arg):
    value = list(value)
    value = map(unicode, value)
    return arg.join(value)

register.filter('joinby', joinby)
