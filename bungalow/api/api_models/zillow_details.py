# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

#Model definition for a ZillowDetails
class ZillowDetails(models.Model):
    zillow_details_id = models.AutoField(primary_key=True)
    zestimate_amount = models.IntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.IntegerField(null=True)
    link = models.CharField(max_length=255)

    def create_zillow_details(self, zestimate_amount, zestimate_last_updated, zillow_id, link):

        #Check if the zestimate_last_updated is empty, if not, convert it to a proper date for the database
        if len(zestimate_last_updated) == 0:
            formated_date = None
        else:
            formated_date = datetime.datetime.strptime(zestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

        #set default value for zestimate_amount
        if len(zestimate_amount) == 0:
           zestimate_amount = 0

        #set default value for zillow_id
        if len(zillow_id) == 0:
           zillow_id = 0

        zillow_details = ZillowDetails(zestimate_amount=zestimate_amount, zestimate_last_updated=formated_date,
                                        zillow_id=zillow_id, link=link)
        zillow_details.save()

        return zillow_details.zillow_details_id
