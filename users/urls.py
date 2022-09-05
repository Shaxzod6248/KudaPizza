from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('login/', login_user),
    path('logout/', logout_user),
    path('register/', register_user)
]