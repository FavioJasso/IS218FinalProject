from django import forms
from backend.accounts.models import LogComment

class LogCommentForm(forms.ModelForm):
    class Meta:
        model = LogComment
        fields = ("message",)   # NOTE: the trailing comma is required
