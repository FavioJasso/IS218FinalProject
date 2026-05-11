from django.urls import path

from backend.accounts import views as accounts_views
from .views import (
    submit_rating,
    vitamin_reviews,
    submit_admin_feedback,
    admin_feedback_list,
)

app_name = 'pages'

urlpatterns = [
    path('', accounts_views.home, name='home'),
    path('catalog/', accounts_views.catalog, name='catalog'),
    path('catalog/item/<int:pk>/', accounts_views.item_info, name='item_info'),
    path('feedback/', accounts_views.feedback, name='feedback'),
    path('submit_reviews/<int:supplement_id>/', accounts_views.log_comment, name='submit_reviews'),
    path('login/', accounts_views.login_view, name='login'),
    path('register/', accounts_views.register_view, name='register'),
    path('delete/', accounts_views.delete_account_view, name='delete_account'),
    path('log/', accounts_views.feedback, name='log'),
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('reviews/', vitamin_reviews, name='vitamin_reviews'),
    path('admin/feedback/submit/', submit_admin_feedback, name='submit_admin_feedback'),
    path('admin/feedback/', admin_feedback_list, name='admin_feedback_list'),
]
