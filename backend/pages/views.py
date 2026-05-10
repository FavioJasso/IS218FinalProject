# Imports page rendering tools
from django.shortcuts import render, get_object_or_404, redirect

# Imports Product model
from .models import Product

# Imports rating form
from .forms import RatingForm

def index(request):
	return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')


def catalog(request):
	return render(request, 'pages/catalog/catalog.html')


# Displays product detail page
def item_info(request, product_id):

    # Finds product using ID
    product = get_object_or_404(
        Product,
        id=product_id
    )

    # Checks if review form was submitted
    if request.method == 'POST':

        # Creates form using submitted data
        form = RatingForm(request.POST)

        # Checks if form is valid
        if form.is_valid():

            # Saves form temporarily
            rating = form.save(commit=False)

            # Connects review to product
            rating.product = product

            # Connects review to logged-in user
            rating.user = request.user

            # Saves review into database
            rating.save()

            # Reloads page after submission
            return redirect(
                'item_info',
                product_id=product.id
            )

    else:

        # Creates empty review form
        form = RatingForm()

    # Sends data to HTML template
    return render(
        request,
        'pages/catalog/item_info.html',
        {
            'product': product,
            'form': form
        }
    )
