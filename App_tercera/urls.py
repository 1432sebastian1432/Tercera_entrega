from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="home"),
    path('profesores', views.lista_profesores, name='profesores'),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name="Alumnos"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("alta_curso", views.curso_formulario_view),
    path("buscar_curso", views.buscar_curso, name="buscar curso"),
    path('buscar_curso1', views.buscar_curso1, name='buscar_curso1'),
    path('buscar_profesor', views.buscar_profesor, name='buscar_profesor'),
    path("buscar_profesor1", views.buscar_profesor1, name="buscar_profesor1"),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"),
    path("buscar_alumno1", views.buscar_alumno1, name="buscar_alumno1"),
    path('alumno_formulario/', views.alumno_formulario, name='alumno formulario'),
    path('eliminar_alumno/<int:id>/', views.elimina_alumno, name='eliminar_alumno'),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("ver_alumnos/", views.ver_alumnos, name="ver_alumnos"),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor"),
    path('ver_profesores/', views.ver_profesores, name='ver_profesores'),
    path('profesor_formulario/', views.profesor_formulario_view, name='profesor_formulario'),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editar_perfil , name="editar_perfil"),
    path('ver_alumnos/alta_alumno', views.alta_alumno, name='alta_alumno'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('guardar_alumno/', views.agregar_alumno, name='guardar_alumno'),
    path('guardar_curso/', views.guardar_curso, name='guardar_curso'),
    path('ver_cursos/', views.ver_cursos, name='ver_cursos'),
    path('editar_profesor/<int:id>/', views.editar_profesor, name='editar_profesor'),


    ]
