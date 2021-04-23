# --------------------------------[edit 21/04/15 김인웅]-------------------------------- #
from django import template

register = template.Library()

@register.filter()
def sub(value, arg):
    return value - arg