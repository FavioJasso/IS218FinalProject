from django.urls import path
from .views import submit_rating, item_info

urlpatterns = [
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('', item_info, name='item_info'),
]