#General
from django.urls import path, include

#Javier
from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CrearPaisAPI, CrearDepartamentoAPI, CrearCiudadAPI, CrearInstitucionAPI, CrearProfesorAPI,
                 CrearFacultadAPI, CrearDepartamentoUAPI, 
                 ConsultarPaisesAPI, ConsultarDepartamentos_paisAPI, ConsultarCiudades_departamentoAPI, 
                 ConsultarInstitucionesAPI, ConsultarInstitucion_idAPI, ConsultarFacultadesAPI, ConsultarFacultad_idAPI,
                 ConsultarDepartamentosUAPI,ConsultarDepartamentoU_idAPI,
                 crearAreaConocimientoAPI, crearGrupoInvestigacionAPI, crearLineaInvestigacionAPI, 
                 ConsultarGrupoInvestigacion_idAPI, ConsultarGrupoInvestigacion_institucionAPI)

urlpatterns = [
    #Javier
    path('api/1.0/crear_pais/', CrearPaisAPI.as_view()),
    path('api/1.0/crear_departamento/', CrearDepartamentoAPI.as_view()),
    path('api/1.0/crear_ciudad/', CrearCiudadAPI.as_view()),
    path('api/1.0/crear_institucion/', CrearInstitucionAPI.as_view()),
    path('api/1.0/crear_profesor/', CrearProfesorAPI.as_view()),
    path('api/1.0/crear_facultad/', CrearFacultadAPI.as_view()),
    path('api/1.0/crear_departamento_u/', CrearDepartamentoUAPI.as_view()),
    #----Consultar
    path('api/1.0/consultar_paises/', ConsultarPaisesAPI.as_view()),
    path('api/1.0/consultar_departamentos_pais/<int:id_pais>', ConsultarDepartamentos_paisAPI.as_view()),
    path('api/1.0/consultar_ciudades_departamento/<int:id_depto>', ConsultarCiudades_departamentoAPI.as_view()),
    path('api/1.0/consultar_instituciones/', ConsultarInstitucionesAPI.as_view()),
    path('api/1.0/consultar_institucion_id/<int:id>', ConsultarInstitucion_idAPI.as_view()),
    path('api/1.0/consultar_facultades/', ConsultarFacultadesAPI.as_view()),
    path('api/1.0/consultar_facultad_id/<int:id>', ConsultarFacultad_idAPI.as_view()),
    path('api/1.0/consultar_departamentosU/', ConsultarDepartamentosUAPI.as_view()),
    path('api/1.0/consultar_departamentoU_id/<int:id>', ConsultarDepartamentoU_idAPI.as_view()),
    #Jeison
    path('api/1.0/crear_grupo_investigacion/', crearGrupoInvestigacionAPI.as_view()),
    path('api/1.0/crear_area_conocimiento/', crearAreaConocimientoAPI.as_view()),
    path('api/1.0/crear_linea_investigacion/', crearLineaInvestigacionAPI.as_view()),
    path('api/1.0/consultar_gi_institucion/<int:id_ins>', ConsultarGrupoInvestigacion_institucionAPI.as_view()),
    path('api/1.0/consultar_gi_id/<int:id>', ConsultarGrupoInvestigacion_idAPI.as_view()),
    
]