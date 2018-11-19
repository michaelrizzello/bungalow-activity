# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Model definition for a ZillowDetails
class ZillowDetails(models.Model):
    zillow_details_id = models.AutoField(primary_key=True)
    zestimate_amount = models.IntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.IntegerField(null=True)
    link = models.CharField(max_length=255)