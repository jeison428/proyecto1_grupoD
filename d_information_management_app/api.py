#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework.response import Response
from .serializers import PaisSerializer, GrupoInvestigacionSerializer#, LoginSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from .models import GrupoInvestigacion

class PaisAPI(APIView):
    def post(self, request):
        print(request)
        serializer = PaisSerializer(data = request.data)
        if serializer.is_valid():
            pais = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GrupoInvestigacionAPI(APIView):
    def post(self, request):
        serializer = GrupoInvestigacionSerializer(data = request.data)
        if serializer.is_valid():
            hayElemento = GrupoInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                grupoInvestigacion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response({
#             "user":
#             UserSerializer(user, context=self.get_serializer_context()).data,
#             "token":
#             AuthToken.objects.create(user)[1]
#         })

# class UserAPI(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user