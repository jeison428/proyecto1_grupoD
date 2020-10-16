from rest_framework import serializers
from knox.models import AuthToken
from django.contrib.auth import authenticate
from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('personal_id', 'cellphone')