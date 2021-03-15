from django.db import models


class Compradores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    estado_geo = models.CharField(max_length=200)

    def __int__(self):
        return self.id
