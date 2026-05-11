from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('item-info/', views.item_info, name='item_info'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
    path('admin/feedback/submit/', views.submit_admin_feedback, name='submit_admin_feedback'),
    path('admin/feedback/', views.admin_feedback_list, name='admin_feedback_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
