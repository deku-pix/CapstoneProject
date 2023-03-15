from django.db import models
from django import forms
# Create your models here.

import uuid
from datetime import datetime
# Create your models here.

#agencias_nombre = ()
#tipo_ref = (('DEL', 'Delegada'), ('EXE', 'Exenta'))

"""type_choice = (

    ('1.', 'Estatal'),
    ('2.', 'Federal')
)"""

class Compra(models.Model):

    agencia_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    id_agencia = models.CharField(max_length=30, blank=False)
    metodo = models.CharField(max_length=60, blank=False)
    objeto = models.CharField(
        max_length=30, blank=False)
    num_licitador = models.CharField(max_length=1000, blank=False)
    comentarios = models.CharField(max_length=1000, blank=False)
    comprador = models.CharField(max_length=1000, blank=False)
    num_compra = models.CharField(max_length=1000, blank=False)
    concepto = models.CharField(max_length=1000, blank=False)
    cantidad = models.CharField(max_length=1000, blank=False)
    fondos = models.CharField(max_length=1000, blank=False)
    descripcion = models.CharField(max_length=1000, blank=False)
    id_comprador = models.CharField(max_length=1000, blank=False)
    #num_reporte = models.CharField(max_length=1000, blank=False)
    asignacion = models.CharField(max_length=1000, blank=False)
    procedencia = models.CharField(max_length=1000, blank=False)
    proveedor = models.CharField(max_length=1000, blank=False)
    cuenta = models.CharField(max_length=255, blank=False)
    alerta = models.BooleanField(blank=False, default='False')
    alerta = models.BooleanField(blank=False, default='False')
    fecha_reporte = models.DateField(blank=True)
    #fecha_adjudicacion = models.DateField(blank=False)
    fecha_recibo = models.DateField(blank=True)
    
    def __str__(self):
        return self.num_compra

    #numero_compras = models.SlugField(primary_key=True, max_length=30, default='')
