from django.contrib import admin

from .models import Inventory, LogComment, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'supplement_id',
        'product_name',
        'manufacturer',
        'product_type',
        'price',
        'is_fda_regulated',
    )
    list_filter = ('product_type', 'is_fda_regulated', 'manufacturer')
    search_fields = ('product_name', 'manufacturer', 'product_type', 'dosage_amount')
    ordering = ('product_name',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'product_name', 'quantity', 'expiration_date', 'cost')
    search_fields = ('product_name',)
    ordering = ('product_name',)


@admin.register(LogComment)
class LogCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'supplement', 'log_date', 'short_message')
    list_filter = ('log_date',)
    search_fields = ('message', 'user__username')
    date_hierarchy = 'log_date'

    @admin.display(description='Message')
    def short_message(self, obj):
        return (obj.message[:60] + '...') if len(obj.message) > 60 else obj.message
