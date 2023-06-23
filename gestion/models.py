from django.db import models
# PermissionsMixin > modulo de permissions 
# AbstractBaseUser > me sirve para modificar mi auth_user en su totalidad
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.html import mark_safe

class Imagen(models.Model):
    nombre = models.ImageField()

    def __str__(self):
        # sirve para indicar como se mostrar la instancia al moment de ser solicitada
        return self.nombre
    
    def nombre_tag(self):
        # return mark_safe('<img src="/imagenes/%s" width="150" height="150" />' % (self.ubicacion))
        return mark_safe('<img src="/imagenes/{}" width="150" height="150" />'.format(self.nombre))
    
    # sirve para indicar el nombre de este 'atributo'
    nombre_tag.short_description = 'Figura de la imagen'

    class Meta:
        db_table = 'imagenes'
        # sirve para indicar como sera el nombre pluralizado en el panel administrativo
        verbose_name_plural = 'Imagenes'


class Categoria(models.Model):
    nombre = models.TextField(unique=True)
    imagen = models.OneToOneField(to=Imagen, on_delete=models.RESTRICT, db_column='imagen_id', related_name='categoria')

    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.TextField()
    fechaVencimiento = models.DateField(db_column='fecha_vencimiento')
    lote = models.TextField(null=False)
    precio = models.FloatField(null=False)
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id', related_name='productos')
    imagen = models.OneToOneField(to=Imagen, on_delete=models.RESTRICT, db_column='imagen_id', related_name='producto')

    class Meta:
        db_table = 'productos'
        # si queremos que vaya de manera ASC no es necesario hacer nada
        # si queremos que vaya de manera DESC se le coloca el '-' al comienzo
        # primero ordenara los productos alfabeticamente (A-Z) y luego de manera DESC las fechas vencimiento 
        ordering = ['nombre', '-fechaVencimiento']

class ManejoUsuario(BaseUserManager):
    # para poder utilizar los metodos para obtener la data y utilizar el modelo pero ademas para modificar cierta funcionabilidad
    def create_superuser(self, nombre, apellido, email, password, tipo):
        # metodo que se manda a llamar cuando en la terminal creamos un super usuario
        if not email:
            raise ValueError('El correo es obligatorio')
        # quita caracteres especiales como tildes, mayusculas y otros para que el correo no se guarde de esa manera
        emailNormalizado = self.normalize_email(email)
        nuevoUsuario = self.model(email = emailNormalizado, nombre = nombre, tipo = tipo, apellido = apellido)
        # generar el hash de la contrasena
        # set_password > metodo propio del auth_user que sirve para generar el hash de la contrasena usando los mismos principios que la libreria bcrypt
        nuevoUsuario.set_password(password)

        nuevoUsuario.save()



class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.TextField(null=False)
    apellido = models.TextField()
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    tipo = models.TextField(choices=[('ADMIN', 'ADMIN'), ('CAJERO', 'CAJERO')])
    is_staff = models.BooleanField(default=False, db_column='is_staff')

    # sirve para indicarle que campo utilizara para encontrar al usuario por el panel administrativo
    USERNAME_FIELD = 'email'

    # campos que son requeridos al usar el comando para crear un superusuario en la consola, es indiferente si le colocamos null=False
    REQUIRED_FIELDS = ['nombre','apellido','tipo']

    objects = ManejoUsuario()

    class Meta:
        db_table = 'usuarios'

