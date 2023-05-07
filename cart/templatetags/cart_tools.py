from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
# calculate subtotal, price times quantity
def calc_subtotal(price, quantity):
    return price * quantity