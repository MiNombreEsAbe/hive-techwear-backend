from django.shortcuts import render
from rest_framework import generics
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None