from django.db import models
from base.models import ModeloBase

class ContactosInstitucionales(ModeloBase):
    #Definicion de choices para tipo contacto
    class tipos_contacto(models.TextChoices):
        Ministerio='Ministerio','Ministerio'
        Empresa_estado='Empresa Estado','Empresa del estado'
        Fundacion='Fundacion','Fundacion'
        Alcaldia='Alcaldia','Alcaldia'
        Gobernacion='Gobernacion', 'Gobernacion'
        
    id_contacto=models.AutoField(primary_key=True)
    rif_contacto=models.CharField(max_length=50,null=False,blank=False)
    nombre_contacto= models.CharField(max_length=100,null=False,blank=False)
    telefono_contacto=models.CharField(max_length=11,null=False,blank=False)    
    tipo_contacto=models.CharField(max_length=50,choices=tipos_contacto.choices,null=False,blank=False)
    
    class Meta:
        db_table="contactos_institucionales"
    
class ActoresInvolucrados(models.Model):
    id_actor=models.AutoField(primary_key=True)
    
    id_contacto=models.ForeignKey(
    ContactosInstitucionales,
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    related_name="Empleado_institucion",
    db_column="id_contacto",
    )
    
    id_persona=models.ForeignKey(
    "user_app.Persona",
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    related_name="actor_involucrado",
    db_column="id_persona"
    )
    
    class Meta:
        db_table="actores_institucionales"