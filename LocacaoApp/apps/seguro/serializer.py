from .models import Seguro
from rest_framework import serializers


class SeguroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguro
        fields = '__all__'