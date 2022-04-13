from django.shortcuts import render
import re
import json
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from apps.cart.serializers import CartSerializer, CartUpdateSerializer, CartListSerializer
from apps.products.models import Product
from .models import Cart
from apps.accounts.mixins import LoginRequired 
from apps.accounts.models import User
from config.helpers.errors import error_response

# Create your views here.

class CartList(LoginRequired, generics.ListAPIView):
    serializer_class = CartListSerializer
    pagination_class = None

    def get_queryset(self):
        authuser = json.loads(self.request.headers['Authorization'])
        return Cart.objects.filter(user = int(authuser['id']))

class CartAdd(LoginRequired, generics.CreateAPIView):
    querryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        authuser = json.loads(self.request.headers['Authorization'])
        user_id = int(authuser['id'])
        self.get_serializer_class().validate(self, request.data)

        product = Product.objects.filter(id=int(request.data['product'])).first()

        if (product is None):
            return error_response('product not found.', status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.filter(product_id=int(request.data['product']), user_id=user_id).first()

        if (cart is not None):
            return error_response('Cart already existed.', status.HTTP_400_BAD_REQUEST)

        new_cart = Cart.objects.create(
            user = User.objects.get(id=user_id),
            product = product,
            quantity = int( request.data['quantity'] )
        )

        # Convert Model to Serializer
        serializer = CartListSerializer(new_cart)

        # Response data as Dict
        return Response(serializer.data)

class CartUpdate(LoginRequired, generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        self.get_serializer_class().validate(self, request.data)
        quantity = int(request.data['quantity'])

        id = self.kwargs['id']
        cart = Cart.objects.filter(id=int(id))
        
        if cart.first() is None:
            return error_response('Cart not found.', status.HTTP_400_BAD_REQUEST)

        if quantity < 1:
            cart.delete()
            return Response({'message': 'Deleted successfully.'})

        cart.update(
            quantity = quantity
        )

        # Convert Model to Serializer
        serializer = CartListSerializer(cart[0])

        # Response data as Dict
        return Response(serializer.data)


