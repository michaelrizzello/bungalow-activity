from api.models import PropertyAddress
from rest_framework import viewsets
from api.serializers.property_address_serializer import PropertyAddressSerializer

# ViewSets define the view behavior.
class PropertyAddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    serializer_class = PropertyAddressSerializer
