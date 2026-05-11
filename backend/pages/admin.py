# - Registers the VitaminReview model with Django Admin
# - Allows admins to view, edit, and delete vitamin reviews

from django.contrib import admin
from .models import VitaminReview, AdminFeedback


class AdminFeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'feedback_type', 'admin_user', 'created_at')
    list_filter = ('feedback_type', 'created_at')
    search_fields = ('title', 'description', 'admin_user__username')
    readonly_fields = ('admin_user', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:  # Only set admin_user on creation
            obj.admin_user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(VitaminReview)
admin.site.register(AdminFeedback, AdminFeedbackAdmin)