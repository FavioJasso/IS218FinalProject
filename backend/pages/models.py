from django.db import models
from django.contrib.auth.models import User


class ProductReview(models.Model):
    """A user-submitted rating + comment for a specific product.

    `product_id` is a plain integer because `accounts.Product` is `managed=False`
    with a non-default primary key column (`Supplement_ID`), which makes a
    standard ForeignKey awkward. Lookups happen via `Product.objects.get(pk=...)`.
    """

    STAR_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    product_id = models.IntegerField(db_index=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_reviews'
    )
    display_name = models.CharField(max_length=80, blank=True)
    rating = models.IntegerField(choices=STAR_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Product #{self.product_id} - {self.rating} stars by {self.author_label}"

    @property
    def author_label(self):
        if self.user_id and self.user is not None:
            return self.user.get_full_name() or self.user.username
        return self.display_name or 'Anonymous'


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
