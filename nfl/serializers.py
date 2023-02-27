from .models import Nfl
from rest_framework import serializers

# Our NflSerializer
class NflSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Nfl
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']