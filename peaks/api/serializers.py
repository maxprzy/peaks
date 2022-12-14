from rest_framework.serializers import ModelSerializer
from .models import MountainPeak


class MountainPeakSerializer(ModelSerializer):
    class Meta:
        model = MountainPeak
        fields = [
            'id',
            'name',
            'altitude',
            'lat',
            'long'
        ]