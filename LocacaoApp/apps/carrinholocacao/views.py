from django.shortcuts import render
from .models import CarrinhoLocacao
from .serializer import CarrinhoLocacaoSerializer
from rest_framework import viewsets

class CarrinhoLocacaoViewSet(viewsets.ModelViewSet):
    queryset = CarrinhoLocacao.objects.all()
    serializer_class = CarrinhoLocacaoSerializer