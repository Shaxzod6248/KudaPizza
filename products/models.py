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
    image = models.ImageField(upload_to='category', default="category/empty.webp")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='kudapizza')
    name_uz = models.CharField(max_length=50, null=True)
    name_en = models.CharField(max_length=50, null=True)
    name_ru = models.CharField(max_length=50, null=True)
    definition_uz = models.TextField(blank=True, null=True)
    definition_en = models.TextField(blank=True, null=True)
    definition_ru = models.TextField(blank=True, null=True)
    price = models.FloatField()


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)


class Order_detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    price = models.CharField(max_length=25)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)