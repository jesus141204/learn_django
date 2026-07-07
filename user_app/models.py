from django.db import models
from base.models import ModeloBase
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

#Departamento al cual pertenece la persona 
class Departamento(ModeloBase):
    id_departamento=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,null=True,blank=True)
    descripcion=models.TextField(null=True,blank=True)
    
    class Meta:
        db_table="departamento"    

#Modelo para contener todos los datos de las personas puede ser tanto usuario,vocero, etc...
class Persona(ModeloBase):
    id_persona=models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=8,null=True,unique=True,blank=True)
    primer_nombre=models.CharField(max_length=100,null=False)
    segundo_nombre=models.CharField(max_length=100,null=True,blank=True)
    primer_apellido=models.CharField(max_length=100,null=False)
    segundo_apellido=models.CharField(max_length=100,null=True,blank=True)
    telefono=models.CharField(max_length=12,null=True,blank=True)
    id_departamento=models.ForeignKey(Departamento,
    on_delete=models.CASCADE,
    related_name="persona_departamento",
    db_column="id_departamento",                                       
    null=True,
    blank=True
    )    
    class Meta:
        db_table="persona"
        
#Declaracion de tabla usuario personalizada 
class CustomUser(AbstractBaseUser,PermissionsMixin):
    id_user=models.AutoField(primary_key=True)
    username=models.CharField(max_length=150,unique=True)
    id_persona=models.OneToOneField(Persona,on_delete=models.CASCADE,
    related_name="dato_usuario",
    null=True,
    blank=True,
    db_column="id_persona"                                    
    )
    #Campos de estado de control
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=True,blank=True)
    #Enlace al manager que esta en el archivo manager.py
    objects=CustomUserManager()
    #Configracion de Autenticacion
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Cuenta de:{self.id_persona.primer_nombre}"
    
    class Meta():
        db_table="auth_user"

#Tabla que se encargara del registro de historial de las tablas que sean necesarios tener una bitacora

class AuditLog(models.Model):
    #Definiendo las opciones  de las acciones que se realizaran
    class actions(models.TextChoices):
        CREAR= 'INSERT','Creacion'
        EDITAR= 'UPDATE','Modificacion'
        ELIMINAR= 'DELETE','Eliminacion'
    
    id_log=models.AutoField(primary_key=True)
    new_data=models.TextField(null=False,blank=False)
    old_data=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    action=models.CharField(
        max_length=50,
        choices=actions.choices,
        default=actions.CREAR
    )
    table_name=models.CharField(max_length=100,null=False,blank=False)
    object_id=models.IntegerField(null=True,blank=True)
    id_user=models.ForeignKey(
    CustomUser,
    null=False,
    blank=False,
    related_name="historial_usuario",
    db_column="id_user",
    on_delete=models.CASCADE
    )
    class Meta:
        db_table="audit_log"