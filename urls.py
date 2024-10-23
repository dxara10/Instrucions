# No arquivo urls.py dentro do aplicativo
from django.urls import path
from . import views

urlpatterns = [
    path('', views.minha_view, name='minha_view'),
]
