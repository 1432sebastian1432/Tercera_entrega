from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio , name="home"),
    path("profesores/", views.lista_profesores, name="lista_profesores"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar)
    
]