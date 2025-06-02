from django.shortcuts import render
from .models import Cliente
from .serializer import ClienteSerializer
from rest_framework import viewsets

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer