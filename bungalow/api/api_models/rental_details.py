# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

#Model definition for a RentalDetails
class RentalDetails(models.Model):
    rental_details_id = models.AutoField(primary_key=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    rentzestimate_amount = models.IntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)

    def create_rental_details(self, rent_price, rentzestimate_amount, rentzestimate_last_updated):

        #Check if the rentzestimate_last_updated is empty, if not, convert it to a proper date for the database
        if len(rentzestimate_last_updated) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(rentzestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

        #set default value for rentzestimate_amount
        if len(rentzestimate_amount) == 0:
           rentzestimate_amount = 0

        #set default value for rent_price
        if len(rent_price) == 0:
           rent_price = 0

        rental_details = RentalDetails(rent_price=rent_price, rentzestimate_amount=rentzestimate_amount, rentzestimate_last_updated=formated_date)
        rental_details.save()

        return rental_details.rental_details_id
