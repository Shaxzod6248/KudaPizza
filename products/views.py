from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_detailViewSet(viewsets.ModelViewSet):
    queryset = Order_detail.objects.all()
    serializer_class = OrderDetailSerializer