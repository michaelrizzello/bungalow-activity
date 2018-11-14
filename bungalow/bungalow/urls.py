from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from api.models import Property, PropertyAddress, RentalDetails, ZillowDetails
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PropertyAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = ('property_address_id', 'street_address', 'city', 'state', 'zipcode')

# ViewSets define the view behavior.
class PropertyAddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    serializer_class = PropertyAddressSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'property_addresses', PropertyAddressViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
