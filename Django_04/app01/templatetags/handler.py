#!/usr/bin/env python
from django import template

register = template.Library()

@register.simple_tag
def zhangsan(arg1,arg2):
    return arg1 + arg2

@register.filter
def lisi(arg1,arg2):
    return arg1 + arg2