from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('login',TokenObtainPairView.as_view()),
    path('registro', RegistroUsuarioController.as_view()),
    path('categorias', CategoriasController.as_view()),
    path('productos', ProductosController.as_view()),
    path('productos-segundo-metodo', ProductosSegundoMetodoController.as_view()),
    path('upload-image', UploadImageController.as_view()),
]