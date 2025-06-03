from django.db import models
from locacao.models import Locacao  

class Pagamento(models.Model):
    
    locacao = models.OneToOneField(Locacao, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=20, choices=[
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('PIX', 'PIX'),
        ('Dinheiro', 'Dinheiro'),
    ])
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora_pagamento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado')
    ])

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
        ordering = ['-data_hora_pagamento']

    def __str__(self):
        return f"Pagamento #{self.id} - {self.status} - R$ {self.valor}"