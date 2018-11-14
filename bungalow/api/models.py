# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.
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

    def create_property(self, area_unit, bathrooms, home_type, last_sold_date, last_sold_price,
                        price, property_size, tax_value, tax_year, year_built, property_address_id,
                        rental_details_id, zillow_details_id):

        if len(last_sold_date) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(last_sold_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        if len(last_sold_price) == 0:
           last_sold_price = 0

        if len(property_size) == 0:
           property_size = 0

        if len(tax_year) == 0:
           tax_year = 0

        if len(tax_value) == 0:
           tax_value = 0

        property = Property(area_unit=area_unit, bathrooms=bathrooms, home_type=home_type,
                            last_sold_date=formated_date, last_sold_price=last_sold_price, price=price,
                            property_size=property_size, tax_value=tax_value, tax_year=tax_year, year_built=year_built,
                            property_address_id=property_address_id, rental_details_id=rental_details_id, zillow_details_id=zillow_details_id)
        property.save()

        return property.property_id

class RentalDetails(models.Model):
    rental_details_id = models.AutoField(primary_key=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    rentzestimate_amount = models.IntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)

    def create_rental_details(self, rent_price, rentzestimate_amount, rentzestimate_last_updated):

        if len(rentzestimate_last_updated) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(rentzestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

        if len(rentzestimate_amount) == 0:
           rentzestimate_amount = 0

        if len(rent_price) == 0:
           rent_price = 0

        rental_details = RentalDetails(rent_price=rent_price, rentzestimate_amount=rentzestimate_amount, rentzestimate_last_updated=formated_date)
        rental_details.save()

        return rental_details.rental_details_id

class PropertyAddress(models.Model):
    property_address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def create_property_address(self, street_address, city, state, zipcode):
        property_address = PropertyAddress(street_address=street_address, city=city, state=state, zipcode=zipcode)
        property_address.save()

        return property_address.property_address_id

class ZillowDetails(models.Model):
    zillow_details_id = models.AutoField(primary_key=True)
    zestimate_amount = models.IntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.IntegerField(null=True)
    link = models.CharField(max_length=255)

    def create_zillow_details(self, zestimate_amount, zestimate_last_updated, zillow_id, link):

        if len(zestimate_last_updated) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(zestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

        if len(zestimate_amount) == 0:
           zestimate_amount = 0

        if len(zillow_id) == 0:
           zillow_id = 0

        zillow_details = ZillowDetails(zestimate_amount=zestimate_amount, zestimate_last_updated=formated_date,
                                        zillow_id=zillow_id, link=link)
        zillow_details.save()
        
        return zillow_details.zillow_details_id
