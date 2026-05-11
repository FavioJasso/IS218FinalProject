from django.urls import path

from backend.accounts import views
from .views import submit_rating, item_info, submit_admin_feedback, admin_feedback_list

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/item/<int:pk>/', views.item_info, name='item_info'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_reviews/<int:supplement_id>/', views.log_comment, name='submit_reviews'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('delete/', views.delete_account_view, name='delete_account'),
    path('log/', views.feedback, name='log'),
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('', item_info, name='item_info'),
    path('admin/feedback/submit/', submit_admin_feedback, name='submit_admin_feedback'),
    path('admin/feedback/', admin_feedback_list, name='admin_feedback_list'),
]