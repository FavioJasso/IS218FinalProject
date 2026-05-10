# - Registers the VitaminReview model with Django Admin
# - Allows admins to view, edit, and delete vitamin reviews

from django.contrib import admin
from .models import VitaminReview

admin.site.register(VitaminReview)