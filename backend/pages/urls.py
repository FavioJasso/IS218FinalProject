from django.urls import path
from backend.pages import views

app_name = 'pages'

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('catalog/', views.catalog, name='catalog'),

	# Updated to support product ratings and dynamic product pages
	path('catalog/item/<int:product_id>/', views.item_info, name='item_info'),
]
