#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import (PaisSerializer, InstitucionSerializer, GrupoInvestigacionSerializer,
                            AreaConocimientoSerializer, LineaInvestigacionSerializer)
from rest_framework.views import APIView
from rest_framework import status
from .models import GrupoInvestigacion, AreaConocimiento, LineaInvestigacion

# Create your api's here.
# --------------------------------------------------Arias

class CrearPaisAPI(APIView):
    def post(self, request):
        serializer = PaisSerializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            prueba = Pais.objects.filter(nombre=request.data["nombre"])
            if not(prueba):
                pais = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListarPaisesAPI(APIView):
    #serializer_class = UpdateSerializer
    def get(self, request, *args, **kwargs):
        queryset = Pais.objects.all()
        return Response({"Paises": PaisSerializer(queryset, many=True).data })

class CrearInstitucionAPI(APIView):
    def post(self, request):
        request.data['ciudad']=[1,'Popayan',1]
        print("lo que llega: ",request.data)
        serializer = InstitucionSerializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            prueba = Institucion.objects.filter(nombre_ins=request.data["nombre_ins"])
            if not(prueba):
                institucion = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
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

class crearLineaInvestigacionAPI(generics.GenericAPIView):
    serializer_class = LineaInvestigacionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = LineaInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                lineaInvestigacion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)