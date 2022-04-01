from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from apps.accounts.mixins import LoginRequired
from .models import User
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer

# Create your views here.

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    querryset = User.objects.all()
    serializer_class = UserSignInSerializer

class UserProfile(LoginRequired, generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user], many = True)
        return Response(serializer.data[0])