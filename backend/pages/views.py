<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
=======
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import VitaminReviewForm, AdminFeedbackForm
from .models import VitaminReview, AdminFeedback


def is_admin_user(user):
    """Check if user is staff/admin"""
    return user.is_staff


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
<<<<<<< HEAD
    })

# Admin-only: Submit feedback
@user_passes_test(is_admin_user)
def submit_admin_feedback(request):
    if request.method == 'POST':
        form = AdminFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.admin_user = request.user
            feedback.save()
            return redirect('admin_feedback_list')
    else:
        form = AdminFeedbackForm()

    return render(request, 'pages/submit_admin_feedback.html', {
        'form': form
    })


# Admin-only: View all feedback
@user_passes_test(is_admin_user)
def admin_feedback_list(request):
    feedback_list = AdminFeedback.objects.all()
    
    return render(request, 'pages/admin_feedback_list.html', {
        'feedback_list': feedback_list
    })
=======
<<<<<<< HEAD
<<<<<<< HEAD
    })
>>>>>>> e5dd19e1b0815e96019b830e419b32a5d421414b
=======
    })
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
=======
    })
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
>>>>>>> 3eac805865107092558baddb2a603eba752dfd35
