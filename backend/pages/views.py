<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import RatingForm
>>>>>>> 7441771dde0d08e4e136dc00d05ba3eea2b09dc5

from backend.accounts.models import Product
from .models import MyModel

def item_info(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        form = RatingForm(request.POST)

        if form.is_valid():

            rating = form.save(commit=False)

<<<<<<< HEAD
def item_info(request):
	return render(request, 'pages/catalog/item_info.html')

def display_image(request, supplement_id):
	item = get_object_or_404(Product, supplement_id=supplement_id)
	return render(request, 'pages/catalog/item_info.html', {'item': item})
=======
            rating.product = product

            rating.user = request.user

            rating.save()

            return redirect('pages:item_info', product_id=product.id)

    else:
        form = RatingForm()

    return render(
        request,
        'pages/catalog/item_info.html',
        {
            'product': product,
            'form': form
        }
    )
>>>>>>> 7441771dde0d08e4e136dc00d05ba3eea2b09dc5
