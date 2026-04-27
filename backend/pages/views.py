from django.shortcuts import render


def index(request):
	return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')


def catalog(request):
	return render(request, 'pages/catalog/catalog.html')


def item_info(request):
	return render(request, 'pages/catalog/item_info.html')
