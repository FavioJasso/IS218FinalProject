from django.db import models

# Imports Django's built-in user system
from django.contrib.auth.models import User


# Product model stores product information
class Product(models.Model):

    # Product name
    name = models.CharField(max_length=100)

    # Product description
    description = models.TextField()

    # Product price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Calculates average rating for the product
    def average_rating(self):

        # Gets all ratings connected to this product
        ratings = self.rating_set.all()

        # Returns 0 if there are no ratings
        if ratings.count() == 0:
            return 0

        # Adds all scores together
        total = sum(r.score for r in ratings)

        # Returns average rounded to 1 decimal
        return round(total / ratings.count(), 1)

    # Displays product name in admin panel
    def __str__(self):
        return self.name





# Rating model stores user reviews and scores
class Rating(models.Model):

    # Connects rating to a product
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Connects rating to a user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Stores rating score from 1–5
    score = models.IntegerField()

    # Stores written review
    comment = models.TextField(
        blank=True
    )

    # Automatically stores review creation date
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Displays readable review info
    def __str__(self):
        return f"{self.product.name} - {self.score}"

