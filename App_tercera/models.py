from django.db import models
from django.contrib.auth.models import User

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
    
class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)

    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"
    
