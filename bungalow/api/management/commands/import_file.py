from django.core.management.base import BaseCommand, CommandError
import csv
from api.models import Property, PropertyAddress, RentalDetails, ZillowDetails

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in dataReader:

                area_unit = row[0]
                bathrooms = row[1]
                bedrooms = row[2]
                home_size = row[3]
                home_type = row[4]
                last_sold_date = row[5]
                last_sold_price = row[6]
                link = row[7]
                price = row[8]
                property_size = row[9]
                rent_price = row[10]
                rentzestimate_amount = row[11]
                rentzestimate_last_updated = row[12]
                tax_value = row[13]
                tax_year = row[14]
                year_built = row[15]
                zestimate_amount = row[16]
                zestimate_last_updated = row[17]
                zillow_id = row[18]
                address = row[19]
                city = row[20]
                state = row[21]
                zipcode = row[22]

                property_address = PropertyAddress()
                property_address_id = property_address.create_property_address(address, city, state, zipcode)

                zillow_details = ZillowDetails()
                zillow_details_id = zillow_details.create_zillow_details(zestimate_amount, zestimate_last_updated, zillow_id, link)

                rental_details = RentalDetails()
                rental_details_id = rental_details.create_rental_details(rent_price, rentzestimate_amount, rentzestimate_last_updated)

                property = Property()
                property.create_property(area_unit, bathrooms, home_type, last_sold_date, last_sold_price,
                                         price, property_size, tax_value, tax_year, year_built,
                                         property_address_id,
                                         zillow_details_id,
                                         rental_details_id)
