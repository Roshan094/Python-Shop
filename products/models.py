from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    #standard max length of urls


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
