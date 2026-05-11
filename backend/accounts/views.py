from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from backend.accounts.forms import LogCommentForm
from backend.accounts.models import LogComment
from backend.accounts.models import Inventory


#class HomeListView(ListView):
   # """Renders the home page, with a list of all messages."""
    #model = LogMessage

    #def get_context_data(self, **kwargs):
        #context = super(HomeListView, self).get_context_data(**kwargs)
        #return context

def home(request):
    return render(request, "pages/index.html")

def catalog(request):
    products = Inventory.objects.all()
    return render(request, "pages/catalog/catalog.html", {'products': products})

def item_info(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    comments = LogComment.objects.filter(supplement=inventory).order_by("-log_date")
    return render(request, "pages/catalog/item_info.html", {
        'inventory': inventory,
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