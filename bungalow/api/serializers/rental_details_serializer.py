from api.models import RentalDetails
from rest_framework import serializers

# Serializers define the API representation.
class RentalDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalDetails
        fields = ('rental_details_id', 'rent_price', 'rentzestimate_last_updated', 'rentzestimate_amount')
