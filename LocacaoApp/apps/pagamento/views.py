from django.shortcuts import render
from .models import Pagamento
from .serializer import PagamentoSerializer
from rest_framework import viewsets

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer