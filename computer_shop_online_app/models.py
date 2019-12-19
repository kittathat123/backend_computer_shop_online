# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django import forms

# Create your models here.


@python_2_unicode_compatible
class Product_on_promotion_page(models.Model):
    product_image = models.ImageField(default="default.png", blank=True, max_length=500)
    heading_brand_product = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    display = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_detail


@python_2_unicode_compatible
class New_arrival_product(models.Model):
    product_image = models.ImageField(
        upload_to="Image/new_arrival_product/",
        default="default.png",
        blank=True,
        max_length=500,
    )
    brand = models.CharField(max_length=30)
    product_detail = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_detail
