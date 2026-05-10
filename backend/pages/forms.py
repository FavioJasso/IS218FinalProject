# Imports Django form tools
from django import forms

# Imports Rating model
from .models import Rating


# Creates review form from Rating model
class RatingForm(forms.ModelForm):

    class Meta:

        # Uses Rating model
        model = Rating

        # Fields shown in form
        fields = ['score', 'comment']
