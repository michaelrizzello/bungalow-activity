from api.models import ZillowDetails
from rest_framework import serializers

# Serializers define the API representation.
class ZillowDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZillowDetails
        fields = ('zillow_details_id', 'zestimate_amount', 'zestimate_last_updated', 'zillow_id', 'link')
