from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'CategoriaVeiculo'

router = routers.DefaultRouter()
router.register('', views.CategoriaVeiculoViewSet, basename='CategoriaVeiculo')

urlpatterns = [
    path('', include(router.urls) )
]