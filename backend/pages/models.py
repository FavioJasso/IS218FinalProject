from django.db import models
from django.contrib.auth.models import User


class VitaminReview(models.Model):
    STAR_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    vitamin_name = models.CharField(max_length=150)
    rating = models.IntegerField(choices=STAR_CHOICES)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vitamin_name} - {self.rating} Stars"


class AdminFeedback(models.Model):
    FEEDBACK_TYPES = [
        ('general', 'General'),
        ('bug', 'Bug Report'),
        ('feature_request', 'Feature Request'),
        ('improvement', 'Improvement Suggestion'),
    ]

    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES, default='general')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Admin Feedback"

    def __str__(self):
        return f"{self.title} ({self.get_feedback_type_display()}) - {self.admin_user.get_full_name() if self.admin_user else 'Anonymous'}"
