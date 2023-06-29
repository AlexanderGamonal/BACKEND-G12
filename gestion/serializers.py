from rest_framework import serializers
from .models import *

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # O usamos el 'fields' o el 'exclude' pero nunca los dos a la vez
        # fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions']
    

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField()
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoSegundoMetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class UploadImageSerializer(serializers.Serializer):
    imagen = serializers.ImageField()