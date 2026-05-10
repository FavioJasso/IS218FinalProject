from django.contrib.auth.models import User

from backend.accounts import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='supplement_images/')

    def __str__(self):
        return self.name
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='supplement_images/')

    def __str__(self):
        return self.name

# Rating system for products (vitamins)
class Rating(models.Model):

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.IntegerField()  # 1 to 5 stars

    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.score} stars"
