
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

#Modelo para contener todos los datos de las personas puede ser tanto usuario,vocero, etc...
class Persona(models.Model):

    id_persona=models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=8,null=True)
    primer_nombre=models.CharField(max_length=100,null=False)
    segundo_nombre=models.CharField(max_length=100,null=True,blank=True)
    primer_apellido=models.CharField(max_length=100,null=False)
    segundo_apellido=models.CharField(max_length=100,null=True,blank=True)
    telefono=models.CharField(max_length=12)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True) 

#Modelo para gestionar la creacion del modelo de usuario 
class User_Manager(BaseUserManager):
    pass

#Declaracion de tabla usuario personalizada 
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=150,unique=True,)
    id_persona=models.OneToOneField(Persona,on_delete=models.CASCADE,
    related_name="dato_usuario",
    null=True,
    blank=True,
    db_column="id_persona"                                    
    )
    
    #Campos de estado de control
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    #Configracion de Autenticacion
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Cuenta de:{self.id_persona.primer_nombre}"
    
    class Meta():
        db_table="auth_user"
    