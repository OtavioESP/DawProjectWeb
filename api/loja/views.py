from django.shortcuts import render
from rest_framework import viewsets
from loja import models, serializers
from rest_framework.response import Response


class UsuarioView(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class PostView(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()

    def get_queryset(self):
        posts = models.Post.objects.all().order_by('-data_criacao')
        return posts

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostGetSerializer
        return serializers.PostSerializer

    def post(self, request):
        print(request)
        obj = get_serializer_class(data=request.data,many=True)
        if obj.is_valid():
            obj.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = get_serializer_class(post, many=True)
        return Response(serializer.data)

class ComentarioView(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentarioSerializer
