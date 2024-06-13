from django.contrib import admin
from django.db import models
import uuid
# Register your models here.

from core.models.Product import Product
from core.models.Ingredient import Ingredient
from core.models.product_storage import ProductStorage
from core.models.Storage import Storage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'modified']

admin.site.register(Product, CategoryAdmin)

#class ProductAdmin(admin.ModelAdmin):
#    list_display = ['name', 'price']

#admin.site.register(Product,ProductAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'stack', 'price']
    search_fields = ['name']
    
admin.site.register(Ingredient,IngredientAdmin)

class StorageAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    
admin.site.register(Storage,StorageAdmin)

#admin.site.register(University)