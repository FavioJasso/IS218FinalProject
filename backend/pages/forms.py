from django import forms
from .models import VitaminReview, AdminFeedback, ProductReview


class VitaminReviewForm(forms.ModelForm):
    class Meta:
        model = VitaminReview
        fields = ['vitamin_name', 'rating', 'review_text']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['display_name', 'rating', 'comment']
        widgets = {
            'display_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name (optional)',
            }),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience with this supplement...',
            }),
        }
        labels = {
            'display_name': 'Display name',
            'rating': 'Rating',
            'comment': 'Your review',
        }

class AdminFeedbackForm(forms.ModelForm):
    class Meta:
        model = AdminFeedback
        fields = ['feedback_type', 'title', 'description']
        widgets = {
            'feedback_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter feedback title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your feedback in detail'}),
        }