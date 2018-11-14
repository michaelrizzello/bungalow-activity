# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Property(models.Model):
    area_unit = models.CharField(max_length=10)
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    #home_type = 
    last_sold_date = models.DateField()
    last_sold_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_size = models.IntegerField()
    tax_value = models.IntegerField()
    tax_year = models.IntegerField()
    year_built = models.CharField(max_length=5)

class RentalDetails(models.Model):
	rent_price = models.DecimalField(max_digits=10, decimal_places=2)
	rentzestimate_amount = models.DecimalField(max_digits=10, decimal_places=2)
	rentzestimate_last_updated = models.DateField()

class PropertyAddress(models.Model): 
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

class ZillowDetails(models.Model):
	zestimate_amount = models.DecimalField(max_digits=10, decimal_places=2)
	zestimate_last_updated = models.DateField()
	zillow_id = models.IntegerField()
	link = models.CharField(max_length=255)