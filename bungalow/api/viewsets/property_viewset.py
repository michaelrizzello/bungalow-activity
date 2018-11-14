from api.models import Property
from rest_framework import viewsets
from api.serializers.property_serializer import PropertySerializer

# ViewSets define the view behavior.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
