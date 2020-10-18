#General
from django.urls import path, include

#Javier
from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CrearPaisAPI, CrearDepartamentoAPI, CrearCiudadAPI, CrearInstitucionAPI, CrearProfesorAPI,
                 ListarPaisesAPI, ListarDepartamentosAPI, ListarCiudadesAPI,
                 crearAreaConocimientoAPI, crearGrupoInvestigacionAPI, crearLineaInvestigacionAPI, 
                 ConsultarGrupoInvestigacion_idAPI, ConsultarGrupoInvestigacion_institucionAPI)

urlpatterns = [
    #Javier
    path('api/1.0/crear_pais/', CrearPaisAPI.as_view()),
    path('api/1.0/crear_departamento/', CrearDepartamentoAPI.as_view()),
    path('api/1.0/crear_ciudad/', CrearCiudadAPI.as_view()),
    path('api/1.0/crear_institucion/', CrearInstitucionAPI.as_view()),
    path('api/1.0/crear_profesor/', CrearProfesorAPI.as_view()),
    path('api/1.0/listar_paises/', ListarPaisesAPI.as_view()),
    path('api/1.0/listar_departamentos/', ListarDepartamentosAPI.as_view()),
    path('api/1.0/listar_ciudades/', ListarCiudadesAPI.as_view()),
    #Jeison
    path('api/1.0/crear_grupo_investigacion/', crearGrupoInvestigacionAPI.as_view()),
    path('api/1.0/crear_area_conocimiento/', crearAreaConocimientoAPI.as_view()),
    path('api/1.0/crear_linea_investigacion/', crearLineaInvestigacionAPI.as_view()),
    path('api/1.0/consultar_gi_institucion/<int:id_ins>', ConsultarGrupoInvestigacion_institucionAPI.as_view()),
    path('api/1.0/consultar_gi_id/<int:id>', ConsultarGrupoInvestigacion_idAPI.as_view()),
    
]