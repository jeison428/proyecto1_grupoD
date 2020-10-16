from rest_framework import serializers
from .models import Pais, GrupoInvestigacion
from knox.models import AuthToken
from django.contrib.auth import authenticate



class PaisSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()

    def create(self, validate_data):
        instance = Pais()
        instance.nombre = validate_data.get('nombre')
        instance.save()
        return instance
    
    """def validate_username(self, data):
        paises = Pais.objects.filter(nombre = data)
        if len(paises) != 0:
            raise serializers.ValidationError("Este nombre de pais ya existe, Ingrese uno nuevo")
        else:
            return data"""

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

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Credenciales incorrectas")

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('personal_id', 'cellphone')


