from django.db import models

class Seguro(models.Model):
    tipo = models.CharField(max_length=50)  # Ex: "Básico", "Completo", "Roubo e Incêndio"
    cobertura = models.TextField()  # Descrição das coberturas
    valor_diario = models.DecimalField(max_digits=10, decimal_places=2)
    franquia = models.DecimalField(max_digits=10, decimal_places=2)
    seguradora = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Seguro"
        verbose_name_plural = "Seguros"
        ordering = ['tipo']

    def __str__(self):
        return f"{self.tipo} - R${self.valor_diario}/dia"
