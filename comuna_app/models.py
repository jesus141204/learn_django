from base.models import ModeloBase
from django.db import models

class Comuna(ModeloBase):
    id_comuna=models.AutoField(primary_key=True)
    codigo_comuna=models.CharField(max_length=50,null=False)
    nombre_comuna=models.CharField(max_length=100,null=False)
    rif_comuna=models.CharField(max_length=50,null=False)
    fecha_fundacion=models.DateField(null=False)
    
    class Meta:
        db_table="comuna"