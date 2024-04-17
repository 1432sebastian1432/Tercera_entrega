from App_tercera.models import Curso
from django.http import HttpResponse
from django.template import loader
from .forms import curso_formulario
from .models import Profesor
from django.shortcuts import render, redirect
from .models import Profesor, Alumno
from django.http import JsonResponse
from .forms import AlumnoForm
from .forms import ProfesorModelForm

def inicio(request):
    return render( request , "padre.html")

#def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()  # Aquí corregimos el nombre de la variable
    dicc = {"alumnos": alumnos}  # Corregimos el nombre de la clave del diccionario
    plantilla = loader.get_template("lista_alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request , "alumnos.html")

def curso_formulario_view(request):  
    if request.method == "POST":
        mi_formulario = curso_formulario(request.POST)  
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

def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})
        
     
    else:
        mi_formulario = curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

#def lista_profesores(request):
    # Recuperar la lista de profesores desde la base de datos
    profesores = Profesor.objects.all()

    # Convertir la lista de profesores en un diccionario serializable
    data = {
        'profesores': list(profesores.values())
    }

    # Devolver los datos en formato JSON
    return JsonResponse(data)

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

def elimina_alumno(request, id):
    # Buscar el alumno por su ID
    alumno = Alumno.objects.get(id=id)
    
    # Eliminar el alumno
    alumno.delete()
    
    # Redirigir a una página que muestre la lista actualizada de alumnos
    return redirect('ver_alumnos')

#def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        formulario = AlumnoForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            alumnos = Alumno.objects.all()
            return render(request, "lista_alumnos.html", {"alumnos": alumnos})

    formulario = AlumnoForm(instance=alumno)
    return render(request, "editar_alumno.html", {"mi_formulario": formulario, "alumno": alumno})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        formulario = AlumnoForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_alumnos')  # Redirigir a la página de lista de alumnos después de editar

    formulario = AlumnoForm(instance=alumno)
    return render(request, "editar_alumno.html", {"mi_formulario": formulario, "alumno": alumno})

def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'ver_profesores.html', {'profesores': profesores})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_profesores')
    else:
        form = ProfesorModelForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        form = ProfesorModelForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('ver_profesores')
    else:
        form = ProfesorModelForm(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('ver_profesores')
    return render(request, 'confirmar_eliminar_profesor.html', {'profesor': profesor})

def profesor_formulario_view(request):  
    if request.method == "POST":
        mi_formulario = ProfesorModelForm(request.POST) 
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Profesor(nombre_y_apellido=datos["nombre_y_apellido"], materia=datos["materia"])
            curso.save()
            return render(request, "formulario.html")
    return render(request, "Resultado_busqueda_profesor.html")