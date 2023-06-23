from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('login',TokenObtainPairView.as_view()),
    path('registro', RegistroUsuarioController.as_view()),
    path('categorias', CategoriasController.as_view()),
]