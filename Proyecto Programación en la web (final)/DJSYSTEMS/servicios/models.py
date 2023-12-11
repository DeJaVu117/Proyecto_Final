from django.db import models

# Create your models here.
class Servicio(models.Model):

    servicio = models.CharField(max_length=30000)
    calificacion = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo