from django.core.management.base import BaseCommand, CommandError
import csv
from api.models import Property, PropertyAddress, RentalDetails, ZillowDetails
import datetime

class Command(BaseCommand):

    #add an argument to get the name of the csv_file you want to load
    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            #opens the csv file
            with open(csv_file, newline='') as csvfile:
                dataReader = csv.DictReader(csvfile)
                for row in dataReader:

                    # maps all the fields in the csv file to a variable
                    area_unit = row['area_unit']
                    bathrooms = row['bathrooms']
                    bedrooms = row['bedrooms']
                    home_size = row['home_size']
                    home_type = row['home_type']
                    last_sold_date = row['last_sold_date']
                    last_sold_price = row['last_sold_price']
                    link = row['link']
                    price = row['price']
                    property_size = row['property_size']
                    rent_price = row['rent_price']
                    rentzestimate_amount = row['rentzestimate_amount']
                    rentzestimate_last_updated = row['rentzestimate_last_updated']
                    tax_value = row['tax_value']
                    tax_year = row['tax_year']
                    year_built = row['year_built']
                    zestimate_amount = row['zestimate_amount']
                    zestimate_last_updated = row['zestimate_last_updated']
                    zillow_id = row['zillow_id']
                    address = row['address']
                    city = row['city']
                    state = row['state']
                    zipcode = row['zipcode']

                    #Check if the last_sold_date is empty, if not, convert it to a proper date for the database
                    if len(last_sold_date) == 0:
                        last_sold_date = None
                    else:
                        last_sold_date = datetime.datetime.strptime(last_sold_date, "%m/%d/%Y").strftime("%Y-%m-%d")

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

                    #Check if the rentzestimate_last_updated is empty, if not, convert it to a proper date for the database
                    if len(rentzestimate_last_updated) == 0:
                        rentzestimate_last_updated = None
                    else:
                        rentzestimate_last_updated = datetime.datetime.strptime(rentzestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

                    #set default value for rentzestimate_amount
                    if len(rentzestimate_amount) == 0:
                       rentzestimate_amount = 0

                    #set default value for rent_price
                    if len(rent_price) == 0:
                       rent_price = 0

                    #Check if the zestimate_last_updated is empty, if not, convert it to a proper date for the database
                    if len(zestimate_last_updated) == 0:
                        zestimate_last_updated = None
                    else:
                        zestimate_last_updated = datetime.datetime.strptime(zestimate_last_updated, "%m/%d/%Y").strftime("%Y-%m-%d")

                    #set default value for zestimate_amount
                    if len(zestimate_amount) == 0:
                       zestimate_amount = 0

                    #set default value for zillow_id
                    if len(zillow_id) == 0:
                       zillow_id = 0

                    #creates a PropertyAddress object
                    property_address = PropertyAddress(street_address=address, city=city, state=state, zipcode=zipcode)
                    property_address.save()

                    #creates a ZillowDetails object
                    zillow_details = ZillowDetails(zestimate_amount=zestimate_amount, zestimate_last_updated=zestimate_last_updated, zillow_id=zillow_id, link=link)
                    zillow_details.save()
                    
                    #creates a RentalDetails object
                    rental_details = RentalDetails(rent_price=rent_price, rentzestimate_amount=rentzestimate_amount, rentzestimate_last_updated=rentzestimate_last_updated)
                    rental_details.save()
                    
                    #creates a Property object
                    property = Property(area_unit=area_unit, bathrooms=bathrooms, home_type=home_type, last_sold_date=last_sold_date,
                                                        price=price, property_size=property_size, tax_value=tax_value, year_built=year_built,
                                                        property_address_id=property_address.property_address_id,
                                                        zillow_details_id=zillow_details.zillow_details_id,
                                                        rental_details_id=rental_details.rental_details_id)
                    property.save()
                    