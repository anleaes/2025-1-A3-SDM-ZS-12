from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'locacao' 

router = routers.DefaultRouter()
router.register('', views.LocacaoViewSet, basename='locacao')

urlpatterns = [
    path('', include(router.urls) )
]