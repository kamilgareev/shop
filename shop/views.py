from django.shortcuts import render, get_object_or_404
from .models import Item
from cart.forms import CartAddProductForm


def product_list(request):
    items = Item.objects.all()
    return render(request,
                  'shop/list.html',
                  {
                      'products': items
                  })


def product_detail(request, item_id):
    item = get_object_or_404(Item,
                             id=item_id)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/detail.html',
                  {
                      'product': item,
                      'cart_product_form': cart_product_form
                  })
