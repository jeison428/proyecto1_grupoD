from rest_framework import serializers
from .models import (Pais, Departamento, Ciudad, Institucion, Profesor, Facultad, DepartamentoU,
                    Trabaja, Maneja, Dirige,
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
        instance = Departamento.objects.create(**validate_data)
        instance.save()
        return instance

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"

    def create(self, validate_data):
        instance = Ciudad.objects.create(**validate_data)
        instance.save()
        return instance

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"

    def create(self, validate_data):
        instance = Institucion.objects.create(**validate_data)
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

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = "__all__"

    def create(self, validate_data):
        instance = Facultad.objects.create(**validate_data)
        instance.save()
        return instance

class DepartamentoUSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoU
        fields = "__all__"

    def create(self, validate_data):
        instance = DepartamentoU.objects.create(**validate_data)
        instance.save()
        return instance

# Create your serializers here.
# --------------------------------------------------Jeison


class GrupoInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoInvestigacion
        fields = "__all__"# ['campo1','campo2']
    
    def create(self, validate_data):
        instance = GrupoInvestigacion.objects.create(**validate_data)
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

class LineaInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaInvestigacion
        fields = "__all__"

    def create(self, validate_data):
        instance = LineaInvestigacion.objects.create(**validate_data)
        instance.save()
        return instance

class TrabajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabaja
        fields = '__all__'

    def create(self, validate_data):
        instance = Trabaja.objects.create(**validate_data)
        instance.save()
        return instance

class ManejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maneja
        fields = ['linea_inv', 'profesor', 'estado_analisis']

    def create(self, validate_data):
        instance = Maneja.objects.create(**validate_data)
        instance.save()
        return instance

class DirigeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dirige
        fields = ['grupo_inv', 'profesor', 'estado_direccion']

    def create(self, validate_data):
        instance = Dirige.objects.create(**validate_data)
        instance.save()
        return instance
