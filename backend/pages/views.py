<<<<<<< HEAD
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
=======
from django.shortcuts import render, redirect
from .forms import VitaminReviewForm
from .models import VitaminReview

# Page to submit a rating
def submit_rating(request):
    if request.method == 'POST':
        form = VitaminReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_info')
    else:
        form = VitaminReviewForm()

    return render(request, 'pages/submit_ratings.html', {
        'form': form
    })


# Page to display ratings like comments
def item_info(request):
    reviews = VitaminReview.objects.all().order_by('-created_at')

    return render(request, 'pages/item_info.html', {
        'reviews': reviews
    })
>>>>>>> e5dd19e1b0815e96019b830e419b32a5d421414b
