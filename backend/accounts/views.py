from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from backend.accounts.forms import LogMessageForm
from backend.accounts.models import LogMessage
from django.views.generic import ListView

def hello_there(request, name):
    return HttpResponse(f"Hello there, {name}!")


def home(request):
    return render(request, "pages/index.html")
#class HomeListView(ListView):
   # """Renders the home page, with a list of all messages."""
    #model = LogMessage

    #def get_context_data(self, **kwargs):
        #context = super(HomeListView, self).get_context_data(**kwargs)
        #return context

def catalog(request):
    return render(request, "pages/catalog/catalog.html")

def feedback(request):
    return HttpResponse(request,"")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("accounts:home")

    return render(request, "accounts/ratings/submit_review.html", {"form": form})


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def delete_account_view(request):
    return render(request, "accounts/delete_account.html")