# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

#Model definition for a PropertyAddess
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
