from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    fields = ['name', 'description', 'type', 'image', 'category', 'price']
    list_filter = []
    list_display = fields
    search_fields = ['name', 'description']