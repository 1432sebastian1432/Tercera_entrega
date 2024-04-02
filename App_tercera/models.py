from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.CharField(max_length=100) 

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


