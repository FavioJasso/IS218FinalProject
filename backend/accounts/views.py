from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment
=======
from django.utils import timezone
from pathlib import Path
from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment, LogMessage
from backend.accounts.models import Product
>>>>>>> 3eac805865107092558baddb2a603eba752dfd35
from backend.accounts.models import Inventory
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


# class HomeListView(ListView):
#    """Renders the home page, with a list of all messages."""
#    model = LogMessage
#    def get_context_data(self, **kwargs):
#        context = super(HomeListView, self).get_context_data(**kwargs)
#        return context

def home(request):
    return render(request, "pages/index.html")

def catalog(request):
<<<<<<< HEAD
    products = Inventory.objects.all()
    return render(request, "pages/catalog/catalog.html", {'products': products})

def item_info(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    comments = LogComment.objects.filter(supplement=inventory).order_by("-log_date")
=======
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

def item_info(request, pk):
    product = Product.objects.get(pk=pk)
    inventory = Inventory.objects.filter(supplement=product).first()
    comments = LogComment.objects.filter(supplement=product).order_by("-log_date")
    image_url = _image_url_for_product(product, _supplement_image_filenames())
>>>>>>> 3eac805865107092558baddb2a603eba752dfd35
    return render(request, "pages/catalog/item_info.html", {
        'inventory': inventory,
        'image_url': image_url,
        "comments": comments,
    })

def feedback(request):
    return HttpResponse("")

@login_required
def log_comment(request, supplement_id):
<<<<<<< HEAD
    inventory = get_object_or_404(Inventory, pk=supplement_id)
    form = LogCommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = timezone.now()
        message.supplement = inventory
        message.user_id = request.user.id
        message.save()
        return redirect('accounts:item_info', pk=inventory.pk)
=======
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    product = get_object_or_404(Product, pk=supplement_id)
    form = LogCommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        if hasattr(message, "product"):
            message.product = product
        message.log_date = timezone.now()
        message.supplement = product
        message.user_id = request.user.id
        message.save()
        return redirect('accounts:item_info', pk=product.pk)
>>>>>>> 3eac805865107092558baddb2a603eba752dfd35

    return render(request, "accounts/ratings/submit_review.html", {"form": form, "inventory": inventory})


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def delete_account_view(request):
    return render(request, "accounts/delete_account.html")