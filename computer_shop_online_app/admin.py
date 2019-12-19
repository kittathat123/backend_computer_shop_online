# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product_on_promotion_page, New_arrival_product

# Register your models here.
admin.site.register(Product_on_promotion_page)
admin.site.register(New_arrival_product)
