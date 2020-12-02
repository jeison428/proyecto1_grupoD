from rest_framework import serializers
from knox.models import AuthToken
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'personal_id', 'username', 'email')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_proffessor', 'is_student', ]

    def create(self, validate_data):
        instance = User.objects.create(**validate_data)
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    type_id = serializers.IntegerField(required=False)
    personal_id = serializers.CharField(required=False)
    personal_code = serializers.CharField(required=False)
    photo = serializers.FileField(required=False)
    telephone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    is_proffessor = serializers.BooleanField(required=False)
    is_student = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_proffessor', 'is_student', ]


# class UserSerializer2(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     password = serializers.CharField()
#     email = serializers.EmailField()

#     type_id = serializers.IntegerField()
#     personal_id = serializers.CharField()
#     personal_code = serializers.CharField()
#     photo = serializers.FileField()
#     telephone = serializers.CharField()
#     address = serializers.CharField()

#     def create(self, validate_data):
#         instance = User()
#         instance.first_name = validate_data.get('first_name')
#         instance.last_name = validate_data.get('last_name')
#         instance.username = validate_data.get('username')
#         instance.set_password(validate_data.get('password'))
#         instance.email = validate_data.get('email')
#         instance.type_id = validate_data.get('type_id')
#         instance.personal_id = validate_data.get('personal_id')
#         instance.photo = validate_data.get('photo')
#         instance.telephone = validate_data.get('telephone')
#         instance.address = validate_data.get('address')
#         instance.save()
#         return instance