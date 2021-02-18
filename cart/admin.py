from django.contrib import admin

# Register your models here.
from .models import OrderItem, Order
from product.models import Product

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)