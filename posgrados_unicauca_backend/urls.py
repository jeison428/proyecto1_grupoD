"""posgrados_unicauca_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from d_information_management_app.views import Home
from d_information_management_app.api import PaisAPI, GrupoInvestigacionAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_projects_app.urls')),
    path('', include('a_students_app.urls')),
    path('', include('all_reports_app.urls')),
    path('', include('b_activities_app.urls')),
    path('', include('c_tracking_app.urls')),
    path('', include('d_accounts_app.urls')),
    path('information/', include(('d_information_management_app.urls','information'))),
    path('home/', Home.as_view(), name='index'),
    path('api/1.0/crear_pais/', PaisAPI.as_view(), name="api_crear_pais"),
    path('api/1.0/crear_grupo_investigacion/', GrupoInvestigacionAPI.as_view(), name="api_crear_grupo_investigacion")
]
