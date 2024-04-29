from django import forms
from .models import Profesor, Alumno, Curso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}