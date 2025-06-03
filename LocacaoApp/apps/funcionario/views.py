from django.shortcuts import render
from .models import Funcionario
from .serializer import FuncionarioSerializer
from rest_framework import viewsets

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer