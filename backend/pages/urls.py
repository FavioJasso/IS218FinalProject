from django.urls import path
from backend.pages import views
from site_configurations import settings
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('catalog/', views.catalog, name='catalog'),
	path('catalog/item/<int:product_id>/', views.item_info, name='item_info'),
]

if settings.DEBUG:    
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	

