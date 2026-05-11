from django.urls import path

from backend.accounts import views
from .views import submit_rating, item_info, submit_admin_feedback, admin_feedback_list

app_name = 'pages'

urlpatterns = [
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('catalog/', views.catalog, name='catalog'),
	path('catalog/item/<int:product_id>/', views.item_info, name='item_info'),
]

if settings.DEBUG:    
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	

=======
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('', item_info, name='item_info'),
]
>>>>>>> e5dd19e1b0815e96019b830e419b32a5d421414b
=======
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('', item_info, name='item_info'),
]
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
=======
    path('submit-rating/', submit_rating, name='submit_rating'),
    path('', item_info, name='item_info'),
]
>>>>>>> 73a9d3768026108b42abfa745faca235a61cc334
>>>>>>> 3eac805865107092558baddb2a603eba752dfd35
