#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from .models import GrupoInvestigacion, AreaConocimiento, LineaInvestigacion

# Create your api's here.
# --------------------------------------------------Arias

class PaisAPI(APIView):
    def post(self, request):
        print(request)
        serializer = PaisSerializer(data = request.data)
        if serializer.is_valid():
            pais = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your api's here.
# --------------------------------------------------Jeison

class crearGrupoInvestigacionAPI(APIView):
    def post(self, request):
        serializer = GrupoInvestigacionSerializer(data = request.data)
        if serializer.is_valid():
            hayElemento = GrupoInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                grupoInvestigacion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class crearAreaConocimientoAPI(APIView):
    def post(self, request):
        serializer = AreaConocimientoSerializer(data = request.data)
        if serializer.is_valid():
            hayElemento = AreaConocimiento.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                areaConocimiento = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class crearLineaInvestigacionAPI(APIView):
    def post(self, request):
        serializer = LineaInvestigacionSerializer(data = request.data)
        if serializer.is_valid():
            hayElemento = LineaInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                lineaInvestigacion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)