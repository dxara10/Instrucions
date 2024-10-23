# No terminal, execute:
django-admin startproject meu_projeto

# No arquivo views.py dentro da pasta do aplicativo:
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo! Você está na página inicial.")

# No arquivo urls.py dentro da pasta do aplicativo:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# No arquivo urls.py do projeto principal:
from django.urls import path, include

urlpatterns = [
    path('', include('meu_app.urls')),
]

# Execute o servidor Django
python manage.py runserver
