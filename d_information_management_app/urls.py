#General
from django.urls import path, include

#Javier
from .views import consultarPais,crearDepartamento, crearCiudad,CrearPais
from d_information_management_app.views import Home

#Jeison
from .views import crearGrupoInvestigacion
from d_information_management_app.api import PaisAPI, crearGrupoInvestigacionAPI
#from .api import UserAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    #Javier
    path('crear_pais/', CrearPais.as_view(), name='crear_pais'),
    path('consultar_pais/', consultarPais, name='consultar_pais'),
    #path('consultar_pais/', consultarPais, name='consultar_pais'),
    path('crear_departamento/', crearDepartamento, name='crear_departamento'),
    path('crear_ciudad/', crearCiudad, name='crear_ciudad'),
    path('home/', Home.as_view(), name='index'),
    path('api/1.0/crear_pais/', PaisAPI.as_view()),

    #Jeison
    #path('crear_grupo_inv/', crear_grupo_investigacion, name='crear_grupo_inv'),
    path('crear_grupo_inv/', crearGrupoInvestigacion.as_view(), name='crear_grupo_inv'),
    #path('crear_gi/', crear_gi, name='crear_gi'),
    path('api/1.0/crear_grupo_investigacion/', crearGrupoInvestigacionAPI.as_view(), name="api_crear_grupo_investigacion"),
    path('api/auth', include('knox.urls')),
    # path('api/auth/user', UserAPI.as_view()),
    # path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]