from django.db import models


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description