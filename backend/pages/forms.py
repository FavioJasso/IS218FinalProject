# - This form is used by users to submit vitamin ratings and reviews
# - Automatically creates form fields from the VitaminReview model
# - Widgets control how inputs appear on the page

from django import forms
from .models import VitaminReview

class VitaminReviewForm(forms.ModelForm):
    class Meta:
        model = VitaminReview
        fields = ['vitamin_name', 'rating', 'review_text']

        widgets = {
            'vitamin_name': forms.TextInput(attrs={
                'placeholder': 'Enter vitamin product name'
            }),
            'review_text': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your review here'
            }),
        }