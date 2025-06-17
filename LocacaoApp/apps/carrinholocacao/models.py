from django.db import models
from veiculo.models import Veiculo
from acessorio.models import Acessorio
from locacao.models import Locacao
from seguro.models import Seguro

class CarrinhoLocacao(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE, null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=True, blank=True)
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item do Carrinho"
        verbose_name_plural = "Itens do Carrinho"

    def __str__(self):
        if self.veiculo:
            return f"{self.quantidade}x {self.veiculo.modelo}"
        elif self.acessorio:
            return f"{self.quantidade}x {self.acessorio.nome}"
        return "Item não definido"