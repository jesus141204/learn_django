from django.db import models
from base.models import ModeloBase

class Comite(models.Model):
    id_comite=models.AutoField(primary_key=True)
    nombre_comite=models.CharField(max_length=100,null=False,blank=False)
    
    class Meta:
        db_table="comite"

class Eleccion(ModeloBase):
    id_eleccion=models.AutoField(primary_key=True)
    fecha_expedicion=models.DateField(null=False,blank=False)
    fecha_expiracion=models.DateField(null=True,blank=True)
    # Relaciones 
    codigo_comunidad=models.ForeignKey(
    "comunidad_app.Comunidad",
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    related_name="eleccion",
    db_column="codigo_comunidad"
    )
    #id_vocero=pass
    
    class Meta:
        db_table="eleccion"

class Vocero(models.Model):
    #Definiendo la clase de opciones para la condicion de el vocero
    class Condicion_Vocero(models.IntegerChoices):
        Principal=1, "Principal"
        Suplente=2, "Suplente"
    
    id_vocero=models.AutoField(primary_key=True)
    condicion=models.PositiveSmallIntegerField(
    choices=Condicion_Vocero.choices,
    default=Condicion_Vocero.Principal,
    help_text="indica si el vocero actua como principal o suplente"
    )
    
    id_eleccion=models.ForeignKey(
    Eleccion,
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    related_name="vocero_electo",
    db_column="id_eleccion"
    )
    
    id_persona=models.ForeignKey(
    "user_app.Persona",
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    related_name="dato_vocero",
    db_column="id_persona"
    )
    
    id_comite=models.ForeignKey(
    Comite,
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    db_column="id_comite"
    )
    
    class Meta:
        db_table="vocero"