from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    fields = ['user', 'customer_name', 'address', 'zip_code', 'building_type', 'city', 'state', 'total_price', 'total_quantity']
    list_filters =[]
    list_display = fields
    search_fields = ['user']