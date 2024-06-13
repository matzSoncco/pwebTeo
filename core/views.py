from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models.Product import Product
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def products(request):
    return render(request, 'core/products.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'core/products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

def exit(request):
    logout(request)
    return redirect('home')
