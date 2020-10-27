#General
from django.urls import path, include

#Javier
# from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
# from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CreateCountryAPI, CreateDepartmentAPI, CreateCityAPI, CreateInstitutionAPI, CreateProfessorAPI,
                 CreateFacultyAPI, CreateDepartmentUAPI, CreateWorksInvestGroupAPI, CreateDriveAPI, CreateDirectsAPI,
                 ConsultCountryAPI, ConsultDepartment_CountryAPI, ConsultCity_DepartmentAPI, 
                 ConsultInstitutionAPI, ConsultInstitution_idAPI, ConsultFacultyAPI, ConsultFaculty_idAPI,
                 ConsultDepartmentUAPI,ConsultDepartmentU_idAPI,
                 CreateKnowledgeAreaAPI, CreateInvestigationGroupAPI, CreateInvestigationLineAPI, 
                 ConsultInvestigationGroup_idAPI, ConsultInvestigationGroup_DepartmentAPI, 
                 ConsultKnowledgeAreaAPI, ConsultKnowledgeArea_idAPI, ConsultInvestigationLine_knowledgeAPI,
                 ConsultInvestigationLine_idAPI)

urlpatterns = [
    #Javier
    path('api/1.0/crear_pais/', CreateCountryAPI.as_view()),
    path('api/1.0/crear_departamento/', CreateDepartmentAPI.as_view()),
    path('api/1.0/crear_ciudad/', CreateCityAPI.as_view()),
    path('api/1.0/crear_institucion/', CreateInstitutionAPI.as_view()),
    path('api/1.0/crear_profesor/', CreateProfessorAPI.as_view()),
    path('api/1.0/crear_facultad/', CreateFacultyAPI.as_view()),
    path('api/1.0/crear_departamento_u/', CreateDepartmentUAPI.as_view()),
    #----Consultar
    path('api/1.0/consultar_paise/', ConsultCountryAPI.as_view()),
    path('api/1.0/consultar_departamento_pais/<int:id_pais>', ConsultDepartment_CountryAPI.as_view()),
    path('api/1.0/consultar_ciudad_departamento/<int:id_depto>', ConsultCity_DepartmentAPI.as_view()),
    path('api/1.0/consultar_institucion/', ConsultInstitutionAPI.as_view()),
    path('api/1.0/consultar_institucion_id/<int:id>', ConsultInstitution_idAPI.as_view()),
    path('api/1.0/consultar_facultad/', ConsultFacultyAPI.as_view()),
    path('api/1.0/consultar_facultad_id/<int:id>', ConsultFaculty_idAPI.as_view()),
    path('api/1.0/consultar_departamentoU/', ConsultDepartmentUAPI.as_view()),
    path('api/1.0/consultar_departamentoU_id/<int:id>', ConsultDepartmentU_idAPI.as_view()),
    #Jeison
    #Crear
    path('api/1.0/crear_grupo_investigacion/', CreateInvestigationGroupAPI.as_view()),
    path('api/1.0/crear_area_conocimiento/', CreateKnowledgeAreaAPI.as_view()),
    path('api/1.0/crear_linea_investigacion/', CreateInvestigationLineAPI.as_view()),
    path('api/1.0/crear_trabaja/', CreateWorksInvestGroupAPI.as_view()),
    path('api/1.0/crear_dirige/', CreateDirectsAPI.as_view()),
    path('api/1.0/crear_maneja/', CreateDriveAPI.as_view()),
    #Consultar
    path('api/1.0/consultar_gi_dep/<int:dep>', ConsultInvestigationGroup_DepartmentAPI.as_view()),
    path('api/1.0/consultar_gi_id/<int:id>', ConsultInvestigationGroup_idAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/', ConsultKnowledgeAreaAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/<int:id>', ConsultKnowledgeArea_idAPI.as_view()),
    path('api/1.0/consultar_li_area/<int:id_area>', ConsultInvestigationLine_knowledgeAPI.as_view()),
    path('api/1.0/consultar_li_id/<int:id>', ConsultInvestigationLine_idAPI.as_view()),
    
]