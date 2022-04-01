from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('signin/', views.UserSignIn.as_view(), name = 'user_sign_in'),
    path('signup/', views.UserSignUp.as_view(), name = 'user_sign_up'),
    path('profile/', views.UserProfile.as_view(), name = 'user_profile'),
]