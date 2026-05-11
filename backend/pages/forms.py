from django import forms
from .models import VitaminReview, AdminFeedback


class VitaminReviewForm(forms.ModelForm):
    class Meta:
        model = VitaminReview
        fields = ['vitamin_name', 'rating', 'review_text']

class AdminFeedbackForm(forms.ModelForm):
    class Meta:
        model = AdminFeedback
        fields = ['feedback_type', 'title', 'description']
        widgets = {
            'feedback_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter feedback title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your feedback in detail'}),
        }