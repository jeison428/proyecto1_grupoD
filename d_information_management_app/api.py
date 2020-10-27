#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (CountrySerializer, DepartmentSerializer, CitySerializer, InstitutionSerializer, 
                        ProfessorSerializer, FacultySerializer, DepartmentUSerializer, AcademicTrainingSerializer,
                        InvestigationGroupSerializer, KnowledgeAreaSerializer, InvestigationLineSerializer, 
                        WorksInvestGroupSerializer, DriveSerializer, DirectsSerializer)

from .models import (Country, Department, City, Institution, Professor, Faculty, DepartmentU,
                    InvestigationGroup, KnowledgeArea, InvestigationLine#, WorksDepartm, Drive, Directs,
                    )

# Create your api's here.
# --------------------------------------------------Arias

class CreateCountryAPI(APIView):
    def post(self, request):
        serializer = CountrySerializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            test = Country.objects.filter(name=request.data["name"])
            if not(test):
                country = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateDepartmentAPI(generics.GenericAPIView):
    serializer_class = DepartmentSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Department.objects.filter(name=request.data['name'])
            if not(isElement):
                department = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateCityAPI(generics.GenericAPIView):
    serializer_class = CitySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = City.objects.filter(name=request.data['name'])
            if not(isElement):
                city = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateInstitutionAPI(generics.GenericAPIView):
    serializer_class = InstitutionSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Institution.objects.filter(name_inst=request.data['name_inst'])
            if not(isElement):
                institution = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateProfessorAPI(generics.GenericAPIView):# toca modificarlo a los cambios nuevos
    serializer_class = ProfessorSerializer
    
    def post(self, request):
        serializer = ProfessorSerializer(data = request.data) 
        if serializer.is_valid():
            test = Professor.objects.filter(user=request.data["user"])
            if not(test):
                professor = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateFacultyAPI(generics.GenericAPIView):
    serializer_class = FacultySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Faculty.objects.filter(name=request.data['name'])
            if not(isElement):
                faculty = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateDepartmentUAPI(generics.GenericAPIView):
    serializer_class = DepartmentUSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = DepartmentU.objects.filter(name=request.data['name'])
            if not(isElement):
                departmentU = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateAcademicTrainingAPI(generics.GenericAPIView):
    serializer_class = AcademicTrainingSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():#Toca arreglar el filtro. Att_:JAVIER
            isElement = AcademicTraining.objects.filter(professor=request.data['proffesor'],titulo=request.data['titulo'])
            if not(isElement):
                academicTraining = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ConsultCountryAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        return Response({"Countrys": CountrySerializer(queryset, many=True).data })

class ConsultDepartment_CountryAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.filter(country=kwargs["id_country"])
        return Response({"Departments": DepartmentSerializer(queryset, many=True).data })

class ConsultCity_DepartmentAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = City.objects.filter(department=kwargs["id_dep"])      
        return Response({"Citys": CitySerializer(queryset, many=True).data })

class ConsultInstitutionAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.all()
        return Response({"Institutions": InstitutionSerializer(queryset, many=True).data })

class ConsultInstitution_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.filter(id=kwargs["id"])  
        return Response({"Institution": InstitutionSerializer(queryset, many=True).data })

class ConsultProfessorAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.all()
        return Response({"Professors": ProfessorSerializer(queryset, many=True).data })

class ConsultProfessor_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.filter(user=kwargs["user"])  
        return Response({"Professors": ProfessorSerializer(queryset, many=True).data })

class ConsultFacultyAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.all()
        return Response({"Facultys": FacultySerializer(queryset, many=True).data })

class ConsultFaculty_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.filter(id=kwargs["id"])  
        return Response({"Faculty": FacultySerializer(queryset, many=True).data })

class ConsultDepartmentUAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = DepartamentoU.objects.all()
        return Response({"DepartamentosU": DepartamentoUSerializer(queryset, many=True).data })

class ConsultDepartmentU_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = DepartmentU.objects.filter(id=kwargs["id"])  
        return Response({"DepartmentU": DepartmentUSerializer(queryset, many=True).data })

# Create your api's here.
# --------------------------------------------------Jeison

class CreateInvestigationGroupAPI(generics.GenericAPIView):
    serializer_class = InvestigationGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationGroup.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateKnowledgeAreaAPI(APIView):
    def post(self, request):
        serializer = KnowledgeAreaSerializer(data = request.data)
        if serializer.is_valid():
            isElement = KnowledgeArea.objects.filter(name=request.data['name'])
            if not(isElement):
                knowledgeArea = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateInvestigationLineAPI(generics.GenericAPIView):
    serializer_class = InvestigationLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationLine.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationLine = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateWorksInvestGroupAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = WorksInvestGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            korksInvestGroup = WorksInvestGroup.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateDirectsAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = DirectsSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            directs = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateDriveAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = DriveSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            drive = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#consultar

class ConsultInvestigationGroup_DepartmentAPI(APIView):#si funciona
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(departmentU=kwargs['dep'])
        return Response({"Groups": InvestigationGroupSerializer(queryset, many=True).data })

class ConsultInvestigationGroup_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(id=kwargs['id'])
        return Response({"Group": InvestigationGroupSerializer(queryset, many=True).data })

class ConsultKnowledgeAreaAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.all()
        return Response({"Knowledges": KnowledgeAreaSerializer(queryset, many=True).data })

class ConsultKnowledgeArea_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(id=kwargs['id'])
        return Response({"Knowledge": KnowledgeAreaSerializer(queryset, many=True).data })

class ConsultInvestigationLine_knowledgeAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(know_area=kwargs['id_area'])
        return Response({"Lines": InvestigationLineSerializer(queryset, many=True).data })

class ConsultInvestigationLine_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(id=kwargs['id'])
        return Response({"Line": InvestigationLineSerializer(queryset, many=True).data })




