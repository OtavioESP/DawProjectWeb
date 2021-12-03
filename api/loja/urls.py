from django.urls import path, include
from rest_framework import routers
from loja import views

router = routers.DefaultRouter()

router.register('posts', views.PostView, basename='posts')
router.register('usuarios', views.UsuarioView, basename='usuarios')



urlpatterns = [
    path('', include(router.urls)),
]
