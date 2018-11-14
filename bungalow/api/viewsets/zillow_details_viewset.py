from api.models import ZillowDetails
from rest_framework import viewsets
from api.serializers.zillow_details_serializer import ZillowDetailsSerializer

# ViewSets define the view behavior.
class ZillowDetailsViewSet(viewsets.ModelViewSet):
    queryset = ZillowDetails.objects.all()
    serializer_class = ZillowDetailsSerializer
