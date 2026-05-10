from django.urls import path
from .views import submit_rating, item_info

urlpatterns = [
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
