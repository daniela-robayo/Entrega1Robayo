from django.db import models

# Create your models here.
class Equipo(models.Model):
    name = models.CharField(max_length=20)
    numeroIntegrantes = models.IntegerField()
    deporte = models.CharField(max_length=20)
    fechaFundacion = models.DateField()

class Integrante(models.Model):
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=20)

class Facilidad(models.Model):
    name = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()
