from django.contrib import admin

# Register your models here.

from .models.Product import Product

admin.site.register(Product)