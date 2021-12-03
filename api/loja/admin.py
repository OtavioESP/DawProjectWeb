from django.contrib import admin
from loja import models

# Register your models here.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'senha',
        'email'
    ]
    ordering = ['username']
    list_display = ['username']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'titulo',
        'usuario',
        'texto',
        'curtidas'
    ]
    ordering = ['usuario']


@admin.register(models.Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    fields = [
        'usuario',
        'post',
        'curtidas',
        'texto',
    ]
    list_filter = ['usuario', 'post', 'curtidas']
    ordering = ['usuario']
