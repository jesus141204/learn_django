from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Gestionador de el modelo de usuario personalizado teniendo en cuenta que el campo username 
    es el fijo para la creacion y uso del login
    """
    def create_user(self,username,password,**extra_fields):
        #Creando el usuario normal
        """
        if not username:
            raise ValueError('El campo username es obligatorio.')
        if not cedula:
            raise ValueError('La cédula es obligatoria para crear el usuario.')
        if not primer_nombre:
            raise ValueError('El primer nombre es obligatorio para crear el usuario.')
        if not primer_apellido:
            raise ValueError('El primer apellido es obligatorio para crear el usuario.')

        #Importando aqui dentro para evitar importacion circular y se rompa django
        from .models import Persona
        #Obtenemos lo campos si se pasaron, sino se coloca por defecto None 
        segundo_nombre = extra_fields.pop('segundo_nombre', None)
        segundo_apellido = extra_fields.pop('segundo_apellido', None)
        telefono = extra_fields.pop('telefono', None)
        
        nueva_persona=Persona.objects.create(
            cedula=cedula,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            segundo_nombre=segundo_nombre,
            segundo_apellido=segundo_apellido,
            telefono=telefono
        )
        """
        #poner predeterminado o por defecto el activo
        extra_fields.setdefault('is_active',True)
        
        #Creacion del usuario
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser = True')
        #Redirigimos los datos al metodo de creacion de usuario que ya crea la persona
        return self.create_user(
            username=username,
            password=password,
            **extra_fields
        )