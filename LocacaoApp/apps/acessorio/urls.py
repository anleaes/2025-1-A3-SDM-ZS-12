from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'acessorio'

router = routers.DefaultRouter()
router.register('', views.AcessorioViewSet, basename='acessorio')

urlpatterns = [
    path('', include(router.urls) )
]