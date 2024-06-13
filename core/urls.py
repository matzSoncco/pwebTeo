from django.urls import path
from .views import home, products, exit
from .views import products, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('core/products/', products, name='products'),
    path('core/products/<int:product_id>/', product_detail, name='product_detail'),
    path('logout/', exit, name='exit'),
]