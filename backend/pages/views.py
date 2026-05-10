# - Handles displaying the vitamin review form
# - Saves new vitamin reviews to the database
# - Retrieves and displays all submitted reviews

from django.shortcuts import render, redirect
from .forms import VitaminReviewForm
from .models import VitaminReview

def home(request):
    if request.method == 'POST':
        form = VitaminReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VitaminReviewForm()

    reviews = VitaminReview.objects.all().order_by('-created_at')

    return render(request, 'pages/home.html', {
        'form': form,
        'reviews': reviews
    })