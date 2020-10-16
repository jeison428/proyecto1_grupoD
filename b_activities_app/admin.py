from django.contrib import admin
from .models import *

# Register your models here.

'''
class ponenciaCongresoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class publicacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class cursoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class exposicionResultadosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class estanciaInvestigacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class parcipacionProyectoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

'''




admin.site.register(ponenciaCongreso)
admin.site.register(publicacion)
admin.site.register(curso)
admin.site.register(exposicionResultados)
admin.site.register(estanciaInvestigacion)
admin.site.register(parcipacionProyecto)