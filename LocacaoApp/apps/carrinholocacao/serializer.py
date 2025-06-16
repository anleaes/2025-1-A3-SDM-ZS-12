from .models import CarrinhoLocacao
from rest_framework import serializers

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoLocacao
        fields = '__all__'