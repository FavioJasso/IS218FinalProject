from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from pathlib import Path
from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment, Inventory
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
    products = Inventory.objects.all()
    return render(request, "pages/catalog/catalog.html", {'products': products})

def item_info(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    image_filenames = _supplement_image_filenames()
    image_url = _image_url_for_product(inventory.supplement, image_filenames)
    comments = LogComment.objects.filter(supplement=inventory).order_by("-log_date")
    return render(request, "pages/catalog/item_info.html", {
        'inventory': inventory,
        'image_url': image_url,
        "comments": comments,
    })

def feedback(request):
    return HttpResponse("")

@login_required
def log_comment(request, supplement_id):
    inventory = get_object_or_404(Inventory, pk=supplement_id)
    form = LogCommentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = timezone.now()
        message.supplement = inventory
        message.user_id = request.user.id
        message.save()
        return redirect('accounts:item_info', pk=inventory.pk)

    return render(request, "accounts/ratings/submit_review.html", {"form": form, "inventory": inventory})


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def delete_account_view(request):
    return render(request, "accounts/delete_account.html")