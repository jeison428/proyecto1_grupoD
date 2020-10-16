from rest_framework import serializers
from .models import *

# Create your serializers here.
# --------------------------------------------------Arias

class PaisSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()

    def create(self, validate_data):
        instance = Pais()
        instance.nombre = validate_data.get('nombre')
        instance.save()
        return instance


# Create your serializers here.
# --------------------------------------------------Jeison

class GrupoInvestigacionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    id_institucion = serializers.IntegerField()
    nombre = serializers.CharField()
    categoria = serializers.CharField()
    email = serializers.EmailField()
    fecha_fundacion = serializers.DateField()

    def create(self, validate_data):
        instance = GrupoInvestigacion()
        instance.id_institucion = validate_data.get('id_institucion')
        instance.nombre = validate_data.get('nombre')
        instance.categoria = validate_data.get('categoria')
        instance.email = validate_data.get('email')
        instance.fecha_fundacion = validate_data.get('fecha_fundacion')
        instance.save()
        return instance

class AreaConocimientoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()
    descripcion = serializers.CharField()

    def create(self, validate_data):
        instance = AreaConocimiento()
        instance.nombre = validate_data.get('nombre')
        instance.descripcion = validate_data.get('descripcion')
        instance.save()
        return instance

class LineaInvestigacionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    id_area_con = serializers.IntegerField()
    nombre = serializers.CharField()
    descripcion = serializers.CharField()

    def create(self, validate_data):
        instance = LineaInvestigacion()
        instance.id_area_con = validate_data.get('id_area_con')
        instance.nombre = validate_data.get('nombre')
        instance.descripcion = validate_data.get('descripcion')
        instance.save()
        return instance


