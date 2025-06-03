from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'CategoriaVeiculo'

router = routers.DefaultRouter()
router.register('', views.VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('', include(router.urls) )
]