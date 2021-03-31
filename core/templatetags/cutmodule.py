from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def cut_words(value, words):
    for word in words.split():
        value = value.replace(word, "")
    return value