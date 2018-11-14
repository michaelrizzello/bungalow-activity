# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

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

    def create_property(self, area_unit, bathrooms, home_type, last_sold_date, last_sold_price,
                        price, property_size, tax_value, tax_year, year_built, property_address_id,
                        rental_details_id, zillow_details_id):

        #Check if the last_sold_date is empty, if not, convert it to a proper date for the database
        if len(last_sold_date) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(last_sold_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        #set default value for last_sold_price
        if len(last_sold_price) == 0:
           last_sold_price = 0

        #set default value for property_size
        if len(property_size) == 0:
           property_size = 0

        #set default value for tax_year
        if len(tax_year) == 0:
           tax_year = 0

        #set default value for tax_value
        if len(tax_value) == 0:
           tax_value = 0

        property = Property(area_unit=area_unit, bathrooms=bathrooms, home_type=home_type,
                            last_sold_date=formated_date, last_sold_price=last_sold_price, price=price,
                            property_size=property_size, tax_value=tax_value, tax_year=tax_year, year_built=year_built,
                            property_address_id=property_address_id, rental_details_id=rental_details_id, zillow_details_id=zillow_details_id)
        property.save()

        return property.property_id
