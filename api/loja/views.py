from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from loja import models, serializers
from rest_framework.response import Response


class UsuarioView(viewsets.ModelViewSet):


    def get_queryset(self):
        print("QUERYSET")
        usuarios = models.Usuario.objects.all()
        return usuarios


    def get_serializer_class(self):
        print("SERIALIZER")
        return serializers.UsuarioSerializer

    def get(self, request):
        print("GEEEEET")
        usuarios = self.get_queryset()
        serializer = get_serializer_class(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POOOOOOST")
        obj = get_serializer_class(data=request.data, many=True)
        if obj.is_valid():
            obj.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class PostView(mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
# ):
class PostView(viewsets.ModelViewSet):
    # queryset = models.Post.objects.all()


    def get_queryset(self):
        posts = models.Post.objects.all().order_by('-data_criacao')
        return posts

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostGetSerializer
        return serializers.PostSerializer

    def get(self, request):
        obj = serializers.PostSerializer(data=request.data, many=True)
        if obj.is_valid():
            obj.save()
            return Response("Objeto criado com sucesso !", status=status.HTTP_201_CREATED)
        else:
            return Response("Objeto nao pode ser criado !",status=status.HTTP_406_NOT_ACCEPTABLE)

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = serializers.PostGetSerializer(posts, many=True)
        return Response(serializer.data)
