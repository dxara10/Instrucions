from django.db import models

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil')
