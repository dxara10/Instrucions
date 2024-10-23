# No arquivo views.py dentro do aplicativo
from django.shortcuts import render
from .models import MeuModelo

def minha_view(request):
    objetos = MeuModelo.objects.all()
    return render(request, 'meu_app/minha_template.html', {'objetos': objetos})
