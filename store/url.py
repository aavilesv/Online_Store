from django.urls import path

from store.view_order import order
from store.view_product import product
from store.view_customer import customer
urlpatterns = [
    path('product/' ,product ,name='product'),
    path('Customer/' ,customer ,name='Customer'),
    path('order/' ,order ,name='order'),
]