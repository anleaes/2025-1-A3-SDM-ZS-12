from django.db import models
from carrinholocacao.models import CarrinhoLocacao 

class Pagamento(models.Model):

    carrinho_locacao = models.ForeignKey(CarrinhoLocacao, on_delete=models.CASCADE, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=20, choices=[
        ('Pix', 'Pix'),
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito'),
        ('Dinheiro', 'Dinheiro'),
    ])
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_hora_pagamento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado')
    ])

    def save(self, *args, **kwargs):
        if not self.valor and self.locacao:
            self.valor = self.locacao.valor_total_previsto or 0
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
        ordering = ['-data_hora_pagamento']

    def __str__(self):
        return f"Pagamento #{self.id} - {self.status} - R$ {self.valor}"