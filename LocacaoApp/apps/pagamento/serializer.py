from .models import Pagamento
from rest_framework import serializers

class PagamentoSerializer(serializers.ModelSerializer):
    nome_cliente = serializers.CharField(source='carrinho_locacao.locacao.cliente.nome', read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'