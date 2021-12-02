from django.urls import path, include
from rest_framework import routers
from loja import views

router = routers.DefaultRouter()

router.register('posts', views.PostView)
router.register('comentarios', views.ComentarioView)


urlpatterns = [
    path('', include(router.urls)),
]
