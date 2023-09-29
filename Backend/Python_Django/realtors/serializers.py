from rest_framework import routers, serializers, viewsets
from .models import *


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields: '__all__'
