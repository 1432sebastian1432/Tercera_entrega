from django import forms
from .models import Profesor, Alumno, Curso

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class ProfesorModelForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['Nombre_y_Apellido', 'Materia']
    
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['Nombre_y_Apellido', 'Asignatura']
