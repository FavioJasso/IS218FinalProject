# - This model represents a single user review of a vitamin product
# - Each review includes the vitamin name, a star rating, written feedback,
#   and the date the review was submitted
# - One database row = one vitamin product review

from django.db import models

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
