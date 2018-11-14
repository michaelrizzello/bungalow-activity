from api.models import PropertyAddress
from rest_framework import serializers

# Serializers define the API representation.
class PropertyAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = ('property_address_id', 'street_address', 'city', 'state', 'zipcode')
