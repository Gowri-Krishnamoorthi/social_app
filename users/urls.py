from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import redirect
from .views import user_login, user_logout, home

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect /users/ to /users/login/
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]
