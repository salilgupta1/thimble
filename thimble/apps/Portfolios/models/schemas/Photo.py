from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
  image = CloudinaryField('image')