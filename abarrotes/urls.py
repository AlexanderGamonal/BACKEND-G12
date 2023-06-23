"""
URL configuration for abarrotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
generadorSchema = get_schema_view(
    openapi.Info(
        title='Abarrotes API',
        default_version='v1',
        description='API de abarrotes con autenticacion',
        contact=openapi.Contact(name='Eduardo de Rivero', email='ederiveroman@gmail.com')
    ),
    # public > muestra todos los endpoint inclusive los que son accesibles solo con permisos determinados
    public=True
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/',include('gestion.urls')),
    path('documentacion/',generadorSchema.with_ui()),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
