from django.contrib import admin
from .models import Imagen, Categoria, Producto, Usuario

class ImagenAdmin(admin.ModelAdmin):
    # clase para agregar algunos filtros al panel administrativo
    list_display = ['id','nombre', 'nombre_tag']
    # modifica el ordenamiento predeterminado
    ordering = ['-id']
    # sirve para indicar que se muestren los campos que no son editables
    readonly_fields = ['id', 'nombre_tag']
    # habilita un input de busqueda indicando que columnas tiene que buscar
    # ^ > inicia con # LIKE 'texto%'
    # = > que respete mayus y minus
    # @ > que haga la busqueda (es como si no le pusiesemos nada)
    # Nada > que no respete mayus ni minus
    search_fields = ['nombre']

# para poder visualizar el modelo en el panel administrativo
admin.site.register(Imagen, ImagenAdmin)