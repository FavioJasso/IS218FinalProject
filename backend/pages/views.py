from django.shortcuts import render, get_object_or_404

from backend.accounts.models import Product
from .models import MyModel

def index(request):
	return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')


def catalog(request):
	return render(request, 'pages/catalog/catalog.html')


def item_info(request):
	return render(request, 'pages/catalog/item_info.html')

def display_image(request, supplement_id):
	item = get_object_or_404(Product, supplement_id=supplement_id)
	return render(request, 'pages/catalog/item_info.html', {'item': item})