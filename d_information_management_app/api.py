#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (PaisSerializer, DepartamentoSerializer, CiudadSerializer, InstitucionSerializer, ProfesorSerializer,
                         GrupoInvestigacionSerializer,AreaConocimientoSerializer, LineaInvestigacionSerializer)

from .models import (Pais, Departamento, Ciudad, Institucion, Profesor, 
                    GrupoInvestigacion, AreaConocimiento, LineaInvestigacion)

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

class CrearDepartamentoAPI(generics.GenericAPIView):
    serializer_class = DepartamentoSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = Departamento.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                departamento = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CrearCiudadAPI(generics.GenericAPIView):
    serializer_class = CiudadSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = Ciudad.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                ciudad = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CrearInstitucionAPI(generics.GenericAPIView):
    serializer_class = InstitucionSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = Institucion.objects.filter(nombre_ins=request.data['nombre_ins'])
            if not(hayElemento):
                institucion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CrearProfesorAPI(APIView):
    def post(self, request):
        serializer = ProfesorSerializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            prueba = Profesor.objects.filter(nombre=request.data["nombre"])
            if not(prueba):
                profesor = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListarPaisesAPI(APIView):
    #serializer_class = UpdateSerializer
    def get(self, request, *args, **kwargs):
        queryset = Pais.objects.all()
        return Response({"Paises": PaisSerializer(queryset, many=True).data })

class ListarDepartamentosAPI(APIView):#NO VALIDAN NADA, ESTAN HECHOS A LO MALDITA SEA
    def post(self, request, *args, **kwargs):
        queryset = Departamento.objects.filter(pais=request.data["pais"])
        return Response({"Departamentos": DepartamentoSerializer(queryset, many=True).data })

class ListarCiudadesAPI(APIView):#INCOMPLETO
    def post(self, request, *args, **kwargs):
        #queryset = Ciudad.objects.filter(SELECT * FROM Ciudad )        
        return Response({"Ciudades": CiudadSerializer(queryset, many=True).data })

# Create your api's here.
# --------------------------------------------------Jeison

class crearGrupoInvestigacionAPI(generics.GenericAPIView):
    serializer_class = GrupoInvestigacionSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = GrupoInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                grupoInvestigacion = serializer.save()
                print(">>>>>>>>>>>>>222    ",(grupoInvestigacion))
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

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            hayElemento = LineaInvestigacion.objects.filter(nombre=request.data['nombre'])
            if not(hayElemento):
                lineaInvestigacion = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ConsultarGrupoInvestigacion_institucionAPI2(APIView):#no funciona
    def get(self, request, *args, **kwargs):
        queryset = GrupoInvestigacion.objects.filter(institucion=request.data['institucion'])
        return Response({"Grupos": GrupoInvestigacionSerializer(queryset, many=True).data })

class ConsultarGrupoInvestigacion_institucionAPI(APIView):#si funciona
    def get(self, request, *args, **kwargs):
        queryset = GrupoInvestigacion.objects.filter(institucion=kwargs['id_ins'])
        return Response({"Grupos": GrupoInvestigacionSerializer(queryset, many=True).data })
    #serializer_class = GrupoInvestigacionSerializer
    # def get_queryset(self, request, *args, **kwargs):
    #     print(">>>>>>>>>>>>>>>>1        ",self.request.data)
    #     queryset = GrupoInvestigacion.objects.all()
    #     id_inst = self.request.query_params.get('id_inst')
    #     print(">>>>>>>>>>>>>>>>2         ",id_inst)
    #     if id_inst is not None:
    #         queryset = queryset.filter(institucion=id_inst)
    #     return queryset

class ConsultarGrupoInvestigacion_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        print(">>>>>>>>>>>aca",(kwargs))
        queryset = GrupoInvestigacion.objects.filter(id=kwargs['id'])
        return Response({"Grupo": GrupoInvestigacionSerializer(queryset, many=True).data })