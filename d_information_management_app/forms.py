#General
from django import forms

#Javier
from .models import Pais, Departamento, Ciudad, GrupoInvestigacion

#Jeison


#Javier
class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['pais', 'nombre']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['pais','departamento','nombre']

#Jeison

class GrupoInvestigacionForm(forms.ModelForm):
    class Meta:
        model = GrupoInvestigacion 
        fields = ['id_institucion','nombre','categoria','email','fecha_fundacion']
        # fecha de fundacion hay que revisar si va