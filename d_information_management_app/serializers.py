from rest_framework import serializers
from .models import (Pais, Departamento, Ciudad, Institucion, Profesor,
                     GrupoInvestigacion, AreaConocimiento, LineaInvestigacion)

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

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"

    def create(self, validate_data):
        instance = Departamento.objects.crearDepartamento(validate_data)
        instance.save()
        return instance

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"

    def create(self, validate_data):
        instance = Ciudad.objects.crearCiudad(validate_data)
        instance.save()
        return instance

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"

    def create(self, validate_data):
        instance = Institucion.objects.crearInstitucion(validate_data)
        instance.save()
        return instance

class ProfesorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    cedula = serializers.IntegerField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    es_interno = serializers.IntegerField()

    def create(self, validate_data):
        instance = Profesor()
        instance.cedula = validate_data.get('cedula')
        instance.nombre = validate_data.get('nombre')
        instance.apellido = validate_data.get('apellido')
        instance.es_interno = validate_data.get('es_interno')
        instance.save()
        return instance

# Create your serializers here.
# --------------------------------------------------Jeison

class GrupoInvestigacionSerializer2(serializers.Serializer):
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

class GrupoInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoInvestigacion
        fields = "__all__"
    
    def create(self, validate_data):
        instance = GrupoInvestigacion.objects.create_grupo_investigacion(validate_data)
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

class LineaInvestigacionSerializer2(serializers.Serializer):
    id = serializers.ReadOnlyField()
    id_area_con = serializers.IntegerField()
    nombre = serializers.CharField()
    descripcion = serializers.CharField()

    def create(self, validate_data):
        instance = LineaInvestigacion()
        instance.area_con_id = validate_data.get('area_con_id')
        instance.nombre = validate_data.get('nombre')
        instance.descripcion = validate_data.get('descripcion')
        instance.save()
        return instance

class LineaInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaInvestigacion
        fields = "__all__"

    def create(self, validate_data):
        instance = LineaInvestigacion.objects.create_linea_investigacion(validate_data)
        instance.save()
        return instance


