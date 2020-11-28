from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import LoginSerializer, UserSerializer, CreateUserSerializer
from .models import User

from d_information_management_app.models import Professor
from c_tracking_app.models import ActivityProfessor
from a_students_app.models import Student, StudentProfessor

#region loguin
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
#endregion

#region usuarios
class CreateUserAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ConsultUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        return Response({"Users": CreateUserSerializer(queryset, many=True).data })

class ConsultUser_PersonalAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(personal_id=kwargs['id'])
        return Response({"Users": CreateUserSerializer(queryset, many=True).data })

class ConsultUser_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=kwargs['id'])
        return Response({"Users": CreateUserSerializer(queryset, many=True).data })
#endregion

#region autenticacion usuarios
class AuthUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            Professor.objects.get(user=kwargs['id'])
            return Response(f"profesor")
        except Professor.DoesNotExist:
            try:
                StudentProfessor.objects.get(professor__user=kwargs['id'])
                return Response(f"director")
            except StudentProfessor.DoesNotExist:
                try:
                    ActivityProfessor.objects.get(professor__user=kwargs['id'])
                    return Response(f"coordinador")
                except ActivityProfessor.DoesNotExist:
                    try:
                        Student.objects.get(user=kwargs['id'])
                        return Response(f"estudiante")
                    except Student.DoesNotExist:
                        return Response(f"Usuario sin rol")


#endregion

