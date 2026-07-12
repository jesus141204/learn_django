from django.db import models
from base.models import ModeloBase

class TipoTransformaciones(models.IntegerChoices):
    Economica=1,"Economica"
    Indp_cult_c_t=2,"Independencia, cultura, ciencia y tecnología"
    Seguridad_ciu_def=3,"Seguridad ciudadana y defensa"
    Social=4,"Social"
    Politica=5,"Política" 
    Ecosocialismo=6,"Ecosocialismo"
    Geopolitica=7,"Geopolítica"
    
class PlanPatria(models.Model):
    id_patria=models.IntegerField(primary_key=True,choices=TipoTransformaciones.choices)
    area=models.TextField(null=False,blank=False)
    
    class Meta:
        db_table="Plan_patria"  
    
class AgendaConcretaAccion(ModeloBase):
    id_agenda=models.AutoField(primary_key=True)
    
    id_comite=models.ForeignKey(
    "vocero_app.Comite",
    on_delete=models.CASCADE,
    db_column="id_comite"
    )
    
    id_comunidad=models.ForeignKey(
    "comunidad_app.Comunidad",
    on_delete=models.CASCADE,
    db_column="id_comunidad",
    )
    
    class Meta:
        db_table="Agenda_concreta_accion"
    
class Nudo(ModeloBase):
    #definiendo los choices que son opciones de los campos de la tabla
    class TipoPrioridad(models.IntegerChoices):
        Alta=1,"Alta"
        Media=2,"Media"    
        Baja=3,"Baja"
    
    class MetodoGestion(models.TextChoices):
        Autogestion="autogestion","Autogestion"
        Cogestion="cogestion","Cogestion"
        Gobierno_obedecional="gobierno obedecional","Gobierno Obedecional"
    
    class TipoEstatus(models.IntegerChoices):
        Sin_Iniciar=1,"Sin iniciar"
        En_pausa=2,"En pausa"
        En_Ejecucion=3,"En ejecucion"
        Resuelto=4,"Resuelto"
    
    #definiendo los atributos
    id_nudo=models.AutoField(primary_key=True)
    problema=models.TextField(null=False,blank=False)
    localizacion=models.TextField(null=False,blank=False)
    potencialidades=models.TextField(null=False,blank=False)
    recursos=models.TextField(null=False,blank=False)
    solucion=models.TextField(null=False,blank=False)
    prioridad=models.IntegerField(choices=TipoPrioridad.choices,null=False,blank=False)
    fecha_inicio=models.DateField(null=True,blank=True)
    metodo_gestion=models.CharField(max_length=50,choices=MetodoGestion.choices,null=False,blank=False)
    status=models.IntegerField(choices=TipoEstatus.choices,null=False,blank=False)
    
    id_patria=models.ForeignKey(
    PlanPatria,
    on_delete=models.CASCADE,
    db_column="id_patria",
    null=False,
    blank=False
    )
    class Meta:
        db_table="Nudo"

class ContactoNudo(models.Model):
    id_contacto_nudo=models.AutoField(primary_key=True)
    
    id_nudo=models.ForeignKey(
    Nudo,                      
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    db_column="id_nudo",
    )
    
    id_contacto=models.ForeignKey(
    "contactos_app.ContactosInstitucionales",
    on_delete=models.CASCADE,
    null=False,
    blank=False,
    db_column="id_contacto"
    )
    
    class Meta:
        db_table="contacto_nudo"