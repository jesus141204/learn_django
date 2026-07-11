from django.db import models
from base.models import ModeloBase

class Comunidad(ModeloBase):
    id_comunidad=models.CharField(primary_key=True,max_length=50)
    codigo_registro=models.CharField(max_length=50,null=False,blank=False)
    rif_consejo=models.CharField(max_length=50,null=False,blank=False)
    consejo_comunal=models.CharField(max_length=100,null=False,blank=False)
    comunidad=models.CharField(max_length=50,null=False,blank=False)
    registro_electoral=models.IntegerField(null=False,blank=False)
    codigo_parroquia=models.CharField(max_length=50,null=False,blank=False)
    codigo_comuna=models.ForeignKey(
    "comuna_app.Comuna",
    on_delete=models.CASCADE,
    related_name="comunidad",
    null=True,
    blank=True,
    db_column="codigo_comuna"
    )
    
    class Meta:
        db_table="comunidad"
    