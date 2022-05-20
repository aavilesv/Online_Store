from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    identification = models.CharField(max_length=200, verbose_name="identification",default='')
    first_name = models.CharField(max_length=200,verbose_name="first_name",default='')
    last_name = models.CharField(max_length=200, verbose_name="last_name", default='')
    email = models.CharField(max_length=200,verbose_name="Email", default="")
    create_date = models.DateTimeField(default=timezone.now(), verbose_name="create_date", blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=200, default=" ")
    price = models.DecimalField(decimal_places=2, max_digits=19,default=0)
    create_date = models.DateTimeField(default=timezone.now(), blank=True)
    code = models.CharField(max_length=200, default=" ")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateTimeField(default=timezone.now(), blank=True)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
        ordering = ['id']

class Order_detail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, default=None)
    unit_price = models.DecimalField(decimal_places=2, max_digits=19, default=0)
    quantity =models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=19, default=0)



    class Meta:
        verbose_name = 'Order_detail'
        verbose_name_plural = 'Order_details'
        ordering = ['id']


