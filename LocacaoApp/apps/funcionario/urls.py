from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'funcionario' 

router = routers.DefaultRouter()
router.register('', views.FuncionarioViewSet, basename='funcionario')

urlpatterns = [
    path('', include(router.urls) )
]