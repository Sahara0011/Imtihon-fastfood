from django.contrib import admin
from menu.models import ProductType, Product

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductType)
