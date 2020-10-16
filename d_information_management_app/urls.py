#General
from django.urls import path, include

#Javier
from .views import consultarPais,crearDepartamento, crearCiudad,CrearPais

#Jeison
from .views import crearGrupoInvestigacion

urlpatterns = [
    #Javier
    path('crear_pais/', CrearPais.as_view(), name='crear_pais'),
    path('consultar_pais/', consultarPais, name='consultar_pais'),
    #path('consultar_pais/', consultarPais, name='consultar_pais'),
    path('crear_departamento/', crearDepartamento, name='crear_departamento'),
    path('crear_ciudad/', crearCiudad, name='crear_ciudad'),

    #Jeison
    #path('crear_grupo_inv/', crear_grupo_investigacion, name='crear_grupo_inv'),
    path('crear_grupo_inv/', crearGrupoInvestigacion.as_view(), name='crear_grupo_inv'),
    #path('crear_gi/', crear_gi, name='crear_gi'),
]

#http://localhost:8000/information/crear_gi/12/13/14/15/Grupo1/1999/algunacosa/cat1