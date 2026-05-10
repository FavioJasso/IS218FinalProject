from django.db import models

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