from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class Post(models.Model):
    titulo = models.CharField(max_length=30, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    texto = models.CharField(max_length=500, null=True, blank=True)
    curtidas = models.IntegerField(null=True, blank=True, default=0)
    

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    curtidas = models.IntegerField(null=True, blank=True, default=0)
    texto = models.CharField(max_length=200, default="")
