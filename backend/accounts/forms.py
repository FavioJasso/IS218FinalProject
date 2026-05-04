from django import forms
from backend.accounts.models import LogMessage
from backend.accounts.models import Product

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required
