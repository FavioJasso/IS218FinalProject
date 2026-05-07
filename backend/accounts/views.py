from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment
from backend.accounts.models import Product


#class HomeListView(ListView):
   # """Renders the home page, with a list of all messages."""
    #model = LogMessage

    #def get_context_data(self, **kwargs):
        #context = super(HomeListView, self).get_context_data(**kwargs)
        #return context

def home(request):
    return render(request, "pages/index.html")

def catalog(request):
    products = Product.objects.all()
    return render(request, "pages/catalog/catalog.html", {'products': products})

def item_info(request, pk):
    product = Product.objects.get(pk=pk)
    comments = LogComment.objects.filter(supplement=product).order_by("-log_date")
    return render(request, "pages/catalog/item_info.html", {'product': product, "comments": comments,})

def feedback(request):
    return HttpResponse("")

def log_comment(request, supplement_id):
    product = get_object_or_404(Product, pk=supplement_id)
    form = LogCommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        if hasattr(message, "product"):
            message.product = product
        message.log_date = datetime.now()
        message.supplement = product
        message.username = request.user.username
        message.save()
        return redirect('item_info', pk=product.pk)

    return render(request, "accounts/ratings/submit_review.html", {"form": form, "product": product})


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def delete_account_view(request):
    return render(request, "accounts/delete_account.html")