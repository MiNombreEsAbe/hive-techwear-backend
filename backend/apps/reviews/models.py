from django.db import models
from apps.products import Product
from cloudinary.models import CloudinaryField 
# Create your models here.

class Review(models.Model):
  class Meta(object):
    db_table = 'review'

  product = models.ForeignKey(
    Product, on_delete = models.CASCADE, db_index = True
  )

  name = models.CharField(
    'Name', blank = False, null = False, max_length = 50, db_index = True
  )

  description = models.TextField(
    'Description', blank = True, null = True, max_length = 255, db_index = True
  )

  image = CloudinaryField(
    "Product Image", blank = True, null = True
  )

  like_count = models.IntegerField(
    'Like Count', blank = False, null = False
  )

  created_at = models.DateTimeField(
    'Created Datetime', blank = True, auto_now_add = True
  )

  updated_at = models.DateTimeField(
    'Updated Datetime', blank = True, auto_now = True
  )