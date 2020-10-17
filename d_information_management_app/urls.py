#General
from django.urls import path, include

#Javier
from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CrearInstitucionAPI, ListarPaisesAPI, CrearPaisAPI, crearAreaConocimientoAPI, 
                    crearGrupoInvestigacionAPI, crearLineaInvestigacionAPI)

urlpatterns = [
    #Javier
    path('crear_pais/', CrearPais.as_view(), name='crear_pais'),
    path('consultar_pais/', consultarPais, name='consultar_pais'),
    path('crear_departamento/', crearDepartamento, name='crear_departamento'),
    path('crear_ciudad/', crearCiudad, name='crear_ciudad'),
    path('home/', Home.as_view(), name='index'),
    #Javier
    path('api/1.0/crear_pais/', CrearPaisAPI.as_view()),
    path('api/1.0/listar_paises/', ListarPaisesAPI.as_view()),
    path('api/1.0/crear_institucion/', CrearInstitucionAPI.as_view()),
    #Jeison
    path('api/1.0/crear_grupo_investigacion/', crearGrupoInvestigacionAPI.as_view(), name="api_crear_grupo_investigacion"),
    path('api/1.0/crear_area_conocimiento/', crearAreaConocimientoAPI.as_view(), name="api_crear_area_conocimiento"),
    path('api/1.0/crear_linea_investigacion/', crearLineaInvestigacionAPI.as_view(), name="api_crear_linea_investigacion"),
    
]