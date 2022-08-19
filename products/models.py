from django.db import models
from django.core.exceptions import ValidationError
import os
from users.models import Profile


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    image = models.ImageField(upload_to='kudapizza')
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)


class Order_detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    price = models.CharField(max_length=25)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)