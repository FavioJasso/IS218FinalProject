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