from django.db import models

class Acessorio(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    valor_adicional = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categoria = models.CharField(max_length=20, choices=[
    ("Segurança", "Segurança"),
    ("Conforto", "Conforto"),
    ("Entretenimento", "Entretenimento"),
    ("Utilitário", "Utilitário")
])

    class Meta:
        verbose_name = "Acessório"
        verbose_name_plural = "Acessórios"
        ordering = ['nome']

    def __str__(self):
        return self.nome