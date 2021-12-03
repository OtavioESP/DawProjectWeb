from rest_framework import serializers
from loja import models

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = [
            'id',
            'username',
            'senha',
            'email'
        ]

class PostSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Post
        fields = [
            'usuario',
            'titulo',
            'texto',
            'curtidas'
        ]

class PostGetSerializer(serializers.ModelSerializer):
    nome_usuario = serializers.CharField(source='usuario.username')
    data_criacao = serializers.DateTimeField(format='%m/%d/%y %H:%M:%S')
    
    class Meta:
        model = models.Post
        fields = [
            'id',
            'nome_usuario',
            'titulo',
            'data_criacao',
            'texto',
            'curtidas'
        ]


class ComentarioSerializer(serializers.ModelSerializer):
    nome_usuario = serializers.CharField(source='usuario.username')

    class Meta:
        model = models.Comentario
        fields = [
            'nome_usuario',
            'post',
            'curtidas'
        ]

# class ItemSerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='category.name')

#     class Meta:
#         model = Item
#         fields = ('id', 'name', 'category_name')
