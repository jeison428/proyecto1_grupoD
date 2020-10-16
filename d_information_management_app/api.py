#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework.response import Response
from .serializers import PaisSerializer, GrupoInvestigacionSerializer
from rest_framework.views import APIView
from rest_framework import status

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
            grupoInvestigacion = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)