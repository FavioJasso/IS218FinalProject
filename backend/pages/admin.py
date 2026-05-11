from django.contrib import admin

from .models import AdminFeedback, ProductReview, VitaminReview


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'rating', 'author_label', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'display_name', 'user__username')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)


@admin.register(VitaminReview)
class VitaminReviewAdmin(admin.ModelAdmin):
    list_display = ('vitamin_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('vitamin_name', 'review_text')


@admin.register(AdminFeedback)
class AdminFeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'feedback_type', 'admin_user', 'created_at')
    list_filter = ('feedback_type', 'created_at')
    search_fields = ('title', 'description', 'admin_user__username')
    readonly_fields = ('admin_user', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.admin_user = request.user
        super().save_model(request, obj, form, change)
