from .models import CarrinhoLocacao
from rest_framework import serializers

class CarrinhoLocacaoSerializer(serializers.ModelSerializer):
    marca_veiculo = serializers.CharField(source='veiculo.marca', read_only=True)
    seguro_nome = serializers.CharField(source='seguro.tipo', read_only=True)
    nome_cliente = serializers.CharField(source='locacao.cliente.nome', read_only=True)

    class Meta:
        model = CarrinhoLocacao
        fields = '__all__'