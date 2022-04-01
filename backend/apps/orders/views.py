from django.shortcuts import render
from rest_framework import generics
from apps.accounts.mixins import LoginRequired
from .serializers import OrderListSerializer, OrderSerializer
from .models import Order

# Create your views here.

class OrderList(LoginRequired, generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.order_by('-id').filter(user = request.login_user.id)
        return self.list(request, *args, **kwargs)

class OrderAdd(LoginRequired, generics.ListAPIView):
    querryset = Order.objects.all()
    serialzer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id 
        return super().reate(request, *args, **kwargs)