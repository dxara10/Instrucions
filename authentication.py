from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registrar_usuario(username, email, password):
    return User.objects.create_user(username, email, password)

def fazer_login(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        return False

def fazer_logout(request):
    logout(request)
