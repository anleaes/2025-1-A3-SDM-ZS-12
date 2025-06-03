from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    data_admissao = models.DateField()
    email_corporativo = models.EmailField()

    def __str__(self):
        return f"{self.nome} ({self.matricula})"