from django import template

register = template.Library()

@register.filter
def filterC(product, category):
   return product.filter(category=category).values()
