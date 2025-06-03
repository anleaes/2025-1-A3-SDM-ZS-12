from .models import Locacao
from rest_framework import serializers

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
        fields = '__all__'