from django import forms
from .models import VitaminReview

class VitaminReviewForm(forms.ModelForm):
    class Meta:
        model = VitaminReview
        fields = ['vitamin_name', 'rating', 'review_text']