from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from pathlib import Path

from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment, Inventory, Product
from site_configurations import settings


def _supplement_image_filenames():
    image_dir = Path(settings.MEDIA_ROOT) / "supplement_images"
    if not image_dir.exists():
        return []

    valid_exts = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    return sorted(
        file_path.name
        for file_path in image_dir.iterdir()
        if file_path.is_file() and file_path.suffix.lower() in valid_exts
    )


def _image_url_for_product(product, image_filenames):
    if not image_filenames:
        return None

    normalized_product_name = "".join(
        ch for ch in (product.product_name or "").lower() if ch.isalnum()
    )
    for filename in image_filenames:
        normalized_filename = "".join(ch for ch in filename.lower() if ch.isalnum())
        if normalized_product_name and normalized_product_name in normalized_filename:
            return f"{settings.MEDIA_URL}supplement_images/{filename}"

    product_index = (product.pk - 1) % len(image_filenames)
    fallback_filename = image_filenames[product_index]
    return f"{settings.MEDIA_URL}supplement_images/{fallback_filename}"


def home(request):
    return render(request, "pages/index.html")


def catalog(request):
    products = Product.objects.all()
    image_filenames = _supplement_image_filenames()
    product_cards = [
        {
            "product": product,
            "image_url": _image_url_for_product(product, image_filenames),
        }
        for product in products
    ]
    return render(request, "pages/catalog/catalog.html", {"product_cards": product_cards})


def _build_product_description(product):
    """Compose a human-readable description from the available Product fields."""
    parts = []
    if product.product_type:
        parts.append(product.product_type)
    if product.dosage_amount:
        parts.append(f"Dosage: {product.dosage_amount}")
    if product.formula_type:
        parts.append(f"Formula: {product.formula_type}")
    if product.manufacturer:
        parts.append(f"By {product.manufacturer}")
    if not parts:
        return f"{product.product_name} is a quality supplement in our catalog."
    return " \u2022 ".join(parts)


def item_info(request, pk):
    from django.db.models import Avg
    from backend.pages.forms import ProductReviewForm
    from backend.pages.models import ProductReview

    product = get_object_or_404(Product, pk=pk)
    inventory = Inventory.objects.filter(supplement=product).first()
    comments = (
        LogComment.objects.filter(supplement=inventory).order_by("-log_date")
        if inventory
        else []
    )
    image_url = _image_url_for_product(product, _supplement_image_filenames())

    reviews_qs = ProductReview.objects.filter(product_id=product.pk).order_by('-created_at')
    rating_summary = reviews_qs.aggregate(avg=Avg('rating'))

    return render(request, "pages/catalog/item_info.html", {
        "product": product,
        "inventory": inventory,
        "image_url": image_url,
        "description": _build_product_description(product),
        "comments": comments,
        "reviews": reviews_qs,
        "review_count": reviews_qs.count(),
        "average_rating": rating_summary['avg'],
        "review_form": ProductReviewForm(),
    })


def feedback(request):
    return HttpResponse("")


@login_required
def log_comment(request, supplement_id):
    product = get_object_or_404(Product, pk=supplement_id)
    inventory = Inventory.objects.filter(supplement=product).first()
    form = LogCommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid() and inventory is not None:
        message = form.save(commit=False)
        message.log_date = timezone.now()
        message.supplement = inventory
        message.user_id = request.user.id
        message.save()
        return redirect('accounts:item_info', pk=product.pk)

    return render(request, "accounts/ratings/submit_review.html", {
        "form": form,
        "inventory": inventory,
        "product": product,
    })


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def delete_account_view(request):
    return render(request, "accounts/delete_account.html")
