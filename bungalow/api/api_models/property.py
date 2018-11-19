# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Model definition for a Property
class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_address = models.OneToOneField(
        'PropertyAddress',
        on_delete=models.CASCADE,
        null=True
    )
    rental_details = models.OneToOneField(
        'RentalDetails',
        on_delete=models.CASCADE,
        null=True
    )
    zillow_details = models.OneToOneField(
        'ZillowDetails',
        on_delete=models.CASCADE,
        null=True
    )

    area_unit = models.CharField(max_length=10)
    bathrooms = models.CharField(max_length=5)
    bedrooms = models.CharField(max_length=5)
    home_type = models.CharField(max_length=40)
    last_sold_date = models.DateField(null=True)
    last_sold_price = models.IntegerField(null=True)
    price = models.CharField(max_length=10)
    property_size = models.IntegerField(null=True)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2)
    tax_year = models.IntegerField(null=True)
    year_built = models.CharField(max_length=5)