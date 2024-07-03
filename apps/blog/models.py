from django.db import models

# Create your models here.
class Recipe (models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="uploads")
    ingredients=models.TextField()
    utensils=models.TextField()
    nutrutionperserving=models.TextField()
    preparationsteps=models.TextField()
