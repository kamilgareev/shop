from django.urls import path
from .views import product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('items', product_list, name='product_list'),
    path('item/<int:item_id>', product_detail, name='product_detail'),
]