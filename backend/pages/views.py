from collections import defaultdict

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render

from backend.accounts.models import LogComment, Product

from .forms import (
    AdminFeedbackForm,
    ProductReviewForm,
    VitaminReviewForm,
)
from .models import AdminFeedback, ProductReview, VitaminReview


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


def submit_product_review(request, pk):
    """Public form: anyone can leave a rating + comment for a product."""
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product.pk
            if request.user.is_authenticated:
                review.user = request.user
                if not review.display_name:
                    review.display_name = request.user.get_full_name() or request.user.username
            review.save()
            return redirect('accounts:item_info', pk=product.pk)
    else:
        form = ProductReviewForm()

    return render(request, 'pages/submit_product_review.html', {
        'form': form,
        'product': product,
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


@staff_member_required
def feedback_report(request):
    """Admin-only aggregated report of every piece of user feedback."""
    products_by_id = {p.pk: p for p in Product.objects.all()}

    review_stats = (
        ProductReview.objects.values('product_id')
        .annotate(avg=Avg('rating'), count=Count('id'))
    )
    stats_by_product = {row['product_id']: row for row in review_stats}

    reviews_by_product = defaultdict(list)
    for review in ProductReview.objects.all().order_by('-created_at'):
        reviews_by_product[review.product_id].append(review)

    comments_by_product = defaultdict(list)
    for comment in (
        LogComment.objects.select_related('supplement').order_by('-log_date')
    ):
        if comment.supplement_id is None:
            continue
        comments_by_product[comment.supplement.supplement_id].append(comment)

    product_rows = []
    referenced_ids = set(reviews_by_product) | set(comments_by_product) | set(products_by_id)
    for product_id in sorted(referenced_ids):
        product = products_by_id.get(product_id)
        stats = stats_by_product.get(product_id, {'avg': None, 'count': 0})
        product_rows.append({
            'product': product,
            'product_id': product_id,
            'avg_rating': stats['avg'],
            'review_count': stats['count'],
            'reviews': reviews_by_product.get(product_id, []),
            'comments': comments_by_product.get(product_id, []),
        })

    totals = {
        'reviews': ProductReview.objects.count(),
        'comments': LogComment.objects.count(),
        'vitamin_reviews': VitaminReview.objects.count(),
        'overall_avg': ProductReview.objects.aggregate(avg=Avg('rating'))['avg'],
    }

    return render(request, 'pages/feedback_report.html', {
        'product_rows': product_rows,
        'totals': totals,
        'standalone_vitamin_reviews': VitaminReview.objects.all().order_by('-created_at'),
    })
