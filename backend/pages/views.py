from django.shortcuts import render, get_object_or_404, redirect

from backend.accounts.models import Product

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'pages/catalog/catalog.html', {'products': products})

def item_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/catalog/item_info.html', {'product': product})

def display_image(request, supplement_id):
    item = get_object_or_404(Product, id=supplement_id)
    return render(request, 'pages/catalog/item_info.html', {'item': item})
