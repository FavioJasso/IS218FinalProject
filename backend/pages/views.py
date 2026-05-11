from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from .forms import VitaminReviewForm, AdminFeedbackForm
from .models import VitaminReview, AdminFeedback


def is_admin_user(user):
    """Check if user is staff/admin."""
    return user.is_staff


def submit_rating(request):
    if request.method == 'POST':
        form = VitaminReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:vitamin_reviews')
    else:
        form = VitaminReviewForm()

    return render(request, 'pages/submit_ratings.html', {
        'form': form,
    })


def vitamin_reviews(request):
    reviews = VitaminReview.objects.all().order_by('-created_at')
    return render(request, 'pages/item_info.html', {
        'reviews': reviews,
    })


@user_passes_test(is_admin_user)
def submit_admin_feedback(request):
    if request.method == 'POST':
        form = AdminFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.admin_user = request.user
            feedback.save()
            return redirect('pages:admin_feedback_list')
    else:
        form = AdminFeedbackForm()

    return render(request, 'pages/submit_admin_feedback.html', {
        'form': form,
    })


@user_passes_test(is_admin_user)
def admin_feedback_list(request):
    feedback_list = AdminFeedback.objects.all()
    return render(request, 'pages/admin_feedback_list.html', {
        'feedback_list': feedback_list,
    })
