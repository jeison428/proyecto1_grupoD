#General
from django.shortcuts import render, redirect

#Jeison
from django.http import HttpResponse
from django.shortcuts import render

#Javier
from .forms import PaisForm, DepartamentoForm, CiudadForm
from .models import Pais
from django.views.generic import TemplateView,CreateView, ListView, UpdateView,FormView
from django.urls import reverse_lazy


# Create your views here.


#--------------------------------------------JAVIER
class Home(TemplateView):
    template_name = 'index.html'

class CrearPais(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/crear_pais.html'


"""    
def home(request):
    return render(request,'index.html')

def crearPais(request):
    if request.method == 'POST':
        pais_form = PaisForm(request.POST)
        if pais_form.is_valid():
            pais = pais_form.cleaned_data['nombre']
            pais_form.save()
        return redirect('index')
    else:
        pais_form = PaisForm()
    return render(request, 'pais/crear_pais.html',{'pais_form':pais_form})
"""

def consultarPais(request):
    autor_form = None
    error = None
    paises = None
    if request.method == 'POST':
        pais_form = PaisForm(request.POST)
        if pais_form.is_valid():
            nombre = pais_form.cleaned_data['nombre']
            paises = Pais.objects.filter(nombre__iexact = nombre)
    else:
        pais_form = PaisForm()
    return render(request, 'pais/consultar_pais.html',{'pais_form':pais_form, 'paises':paises, 'error':error})
        

def crearDepartamento(request):
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento = departamento_form.cleaned_data['nombre']
            departamento_form.save()
        return redirect('index')
    else:
        departamento_form = DepartamentoForm()
    return render(request, 'departamento/crear_departamento.html',{'departamento_form':departamento_form})


def crearCiudad(request):
    if request.method == 'POST':
        ciudad_form = CiudadForm(request.POST)
        if ciudad_form.is_valid():
            ciudad = ciudad_form.cleaned_data['nombre']
            ciudad_form.save()
        return redirect('index')
    else:
        ciudad_form = CiudadForm()
    return render(request, 'ciudad/crear_ciudad.html',{'ciudad_form':ciudad_form})


#--------------------------------------------JEISON
# Metodo para la creacion de un objeto de la clase Grupo de Investigacion
