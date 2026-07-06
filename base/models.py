from django.db import models

"""Modelo Base donde tendra en comun los campos que se necesite en comun
los datos de creacion  y actualizacion y si esta eliminado logicamente"""

class ModeloBase(models.Model):
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True) 
    
    class Meta:
        abstract=True