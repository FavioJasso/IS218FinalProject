from django.urls import path
from backend.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('delete/', views.delete_account_view, name='delete_account'),
    path('log/', views.log_message, name='log'),
]


