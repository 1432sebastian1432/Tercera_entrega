from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"
    
class Profesor(models.Model):
    Nombre_y_Apellido = models.CharField(max_length=100)
    Materia = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre_y_Apellido
    
class Alumno(models.Model):

    Nombre_y_Apellido = models.CharField(max_length=40)
    Asignatura= models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.Nombre_y_Apellido}"
    
