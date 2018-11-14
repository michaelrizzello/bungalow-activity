from api.models import RentalDetails
from rest_framework import viewsets
from api.serializers.rental_details_serializer import RentalDetailsSerializer

# ViewSets define the view behavior.
class RentalDetailsViewSet(viewsets.ModelViewSet):
    queryset = RentalDetails.objects.all()
    serializer_class = RentalDetailsSerializer
