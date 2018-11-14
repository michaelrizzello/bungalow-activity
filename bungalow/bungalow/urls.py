from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from api.viewsets.property_address_viewset import PropertyAddressViewSet
from api.viewsets.property_viewset import PropertyViewSet
from api.viewsets.rental_details_viewset import RentalDetailsViewSet
from api.viewsets.zillow_details_viewset import ZillowDetailsViewSet

from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'property_addresses', PropertyAddressViewSet)
router.register(r'rental_details', RentalDetailsViewSet)
router.register(r'zillow_details', ZillowDetailsViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
