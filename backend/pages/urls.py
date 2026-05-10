# - Defines URL routes for the pages app
# - The home page displays the vitamin rating system

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]