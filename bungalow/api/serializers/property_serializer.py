from api.models import Property
from rest_framework import serializers

from api.serializers.property_address_serializer import PropertyAddressSerializer
from api.serializers.rental_details_serializer import RentalDetailsSerializer
from api.serializers.zillow_details_serializer import ZillowDetailsSerializer

# Serializers define the API representation.
class PropertySerializer(serializers.ModelSerializer):
    property_address = PropertyAddressSerializer(many=False, read_only=True)
    rental_details = RentalDetailsSerializer(many=False, read_only=True)
    zillow_details = ZillowDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = Property
        fields = ('__all__')
