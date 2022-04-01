from django.db import models
from apps.accounts.models import User
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    class Meta(object):
        db_table = 'order'

    user = models.ForeignKey(
        User, related_name = 'relates_order_user', on_delete = models.CASCADE
    )

    customer_name = models.CharField(
        'Customer Name', blank = False, null = False, max_length = 200
    )

    customer_number = models.CharField(
        'Customer Number', blank = False, null = False, max_length = 25
    )

    address = models.CharField(
        'Address', blank = False, null = False, max_length = 200
    )

    zip_code = models.CharField(
        'Zip Code', blank = False, null = False, max_length = 50
    )

    building_type = models.CharField(
        'Building Type', blank = True, null = True, max_length = 200
    )

    city = models.CharField(
        'City', blank = False, null = False, max_length = 200
    )

    state = models.CharField(
        'State', blank = False, null = False, max_length = 200
    )

    total_price = models.FloatField(
        'Total Price', blank = False, null = False
    )

    total_quantity = models.IntegerField(
        'Total Quantity', blank = False, null = False
    )

    created_at = models.DateTimeField(
        'Creation Date', blank = True, default = timezone.now
    )

    @property 
    def order_items(self):
        return self.related_order.all()