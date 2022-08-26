from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('orderdetails', Order_detailViewSet)
router.register('categorys', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls))
]

##############################################333