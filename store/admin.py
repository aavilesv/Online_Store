from django.contrib import admin

# Register your models here.
from store.models import Product,Order,Order_detail,Customer

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Customer)
