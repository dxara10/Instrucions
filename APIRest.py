# Instale o Django REST Framework
pip install djangorestframework

# No arquivo serializers.py
from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade', 'email']

# No arquivo views.py
from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

# No arquivo urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pessoas', views.PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
