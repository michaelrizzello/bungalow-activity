# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Model definition for a RentalDetails
class RentalDetails(models.Model):
    rental_details_id = models.AutoField(primary_key=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    rentzestimate_amount = models.IntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)