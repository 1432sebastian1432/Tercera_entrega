from App_tercera.models import Curso, Avatar
from django.http import HttpResponse
from django.template import loader
from .forms import CursoForm , UserEditForm
from .models import Profesor
from django.shortcuts import render, redirect
from .models import Profesor, Alumno
from django.http import JsonResponse
from .forms import AlumnoForm
from .forms import ProfesorModelForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
import logging
from django.contrib.auth.models import User 


def inicio(request):
    return render( request , "padre.html")

def alta_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        camada = request.POST.get('camada')
        nuevo_curso = Curso(nombre=nombre, camada=camada)
        nuevo_curso.save()
        texto = f"Se guardó en la BD el curso: {nuevo_curso.nombre}, Camada: {nuevo_curso.camada}"
        return HttpResponse(texto)
    else:
        return render(request, 'alta_curso.html')
    
def alta_alumno(request):
    if request.method == 'POST':
        Nombre_y_Apellido = request.POST.get('Nombre_y_Apellido')
        Asignatura = request.POST.get('Asignatura')
        
        if Nombre_y_Apellido and Asignatura:  
            Alumno.objects.create(Nombre_y_Apellido=Nombre_y_Apellido, Asignatura=Asignatura)
            return redirect('ver_alumnos')  

    return render(request, 'alta_alumnos.html')  

def ver_cursos(request):
    cursos = Curso.objects.all()
    avatares = None
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
    return render(request, 'cursos.html', {'cursos': cursos, 'avatares': avatares})

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    avatares = None
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
    return render(request, 'Lista_alumnos.html', {'alumnos': alumnos, 'avatares': avatares})



def alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "alumnos.html", {"url":avatares[0].imagen.url})

def curso_formulario_view(request):  
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)  
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")
    return render(request, "formulario.html")

def alumno_formulario(request):
    if request.method == "POST":
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(Nombre_y_Apellido=datos["Nombre_y_Apellido"], Asignatura=datos["Asignatura"])
            alumno.save()
            return render(request, "formulario_alumno.html")
    else:
        formulario = AlumnoForm()
    return render(request, "Lista_alumnos.html", {"formulario": formulario}) 

def buscar_curso(request):

    return render(request, "buscar_curso.html")

def buscar_curso1(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

def buscar_profesor(request):

    return render(request, "buscar_curso.html")

def buscar_profesor1(request):
    nombre = request.GET.get("nombre_y_apellido")

    if nombre:
        profesores = Profesor.objects.filter(Nombre_y_Apellido__icontains=nombre)
        return render(request, "resultado_busqueda_profesor.html", {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor a buscar")

def buscar_alumnno(request):
    return render (request, "buscar_curso.html")

def buscar_alumno1(request):
    nombre_alumno = request.GET.get("nombre_alumno", "")
    asignatura = request.GET.get("asignatura", "")

    alumnos = Alumno.objects.filter(Nombre_y_Apellido__icontains=nombre_alumno, Asignatura__icontains=asignatura)

    return render(request, "Resultado_de_la_busqueda_alumno.html", {"alumnos": alumnos})
    
def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        camada = request.POST.get('camada')
        
        # Actualizar los campos del curso
        curso.nombre = nombre
        curso.camada = camada
        curso.save()

        messages.success(request, 'El curso se ha actualizado correctamente.')
        return redirect('ver_cursos')
    else:
        # Si la solicitud es GET, mostrar el formulario con los datos del curso
        return render(request, 'editar_curso.html', {'curso': curso})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

def elimina_alumno(request, id):
    
    alumno = Alumno.objects.get(id=id)
    
   
    alumno.delete()
    
    
    return redirect('ver_alumnos')

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        formulario = AlumnoForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver_alumnos')  
            
            return render(request, "editar_alumno.html", {"mi_formulario": formulario, "alumno": alumno})
    else:
        formulario = AlumnoForm(instance=alumno)
    
    return render(request, "editar_alumno.html", {"mi_formulario": formulario, "alumno": alumno})




def ver_profesores(request):
    profesores = Profesor.objects.all()
    avatares = None
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
    return render(request, 'ver_profesores.html', {'profesores': profesores, 'avatares': avatares})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            Nombre_y_Apellido = form.cleaned_data['Nombre_y_Apellido']
            Asignatura = form.cleaned_data['Asignatura']
            Alumno.objects.create(Nombre_y_Apellido=Nombre_y_Apellido, Asignatura=Asignatura)
            return redirect('ver_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def eliminar_profesor(request, id):
    
    profesor = Profesor.objects.get(id=id)
    
    
    profesor.delete()
    
    
    return redirect('ver_profesores')

def profesor_formulario_view(request):  
    if request.method == "POST":
        mi_formulario = ProfesorModelForm(request.POST) 
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Profesor(nombre_y_apellido=datos["nombre_y_apellido"], materia=datos["materia"])
            curso.save()
            return render(request, "formulario.html")
    return render(request, "Resultado_busqueda_profesor.html")

logger = logging.getLogger(__name__)

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" )
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})


def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

def editar_perfil(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})
def agregar_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        camada = request.POST.get('camada')
        Curso.objects.create(nombre=nombre, camada=camada)
        return redirect('ver_cursos')
    return render(request, 'agregar_curso.html')

def agregar_profesor(request):
    if request.method == 'POST':
        nombre_apellido = request.POST.get('Nombre_y_Apellido')
        materia = request.POST.get('Materia')
        
        if nombre_apellido and materia:
            Profesor.objects.create(Nombre_y_Apellido=nombre_apellido, Materia=materia)
            return redirect('ver_profesores')
        else:
            
            error_message = "Por favor, ingrese el nombre y apellido del profesor y la materia que enseña."
            return render(request, 'agregar_profesor.html', {'error_message': error_message})
    
    return render(request, 'agregar_profesor.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def guardar_curso(request, curso_id=None):
    if curso_id:
        curso = get_object_or_404(Curso, id=curso_id)
    else:
        curso = None

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos')  
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'formulario_curso.html', {'form': form})

def editar_profesor(request, id):
    
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        
        formulario = ProfesorModelForm(request.POST, instance=profesor)
        if formulario.is_valid():
            
            formulario.save()
            return redirect('ver_profesores')  
        else:
            
            return render(request, "editar_profesor.html", {"formulario": formulario, "profesor": profesor})
    else:
        
        formulario = ProfesorModelForm(instance=profesor)
    
    return render(request, "editar_profesor.html", {"formulario": formulario, "profesor": profesor})