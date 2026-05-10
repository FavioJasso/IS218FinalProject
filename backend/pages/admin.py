# Imports Django admin tools
from django.contrib import admin

# Imports Product and Rating models
from .models import Product, Rating


# Registers Product model in admin dashboard
admin.site.register(Product)

# Registers Rating model in admin dashboard
admin.site.register(Rating)
