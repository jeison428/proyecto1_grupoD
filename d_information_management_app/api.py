#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (CountrySerializer, StateSerializer, CitySerializer, InstitutionSerializer, 
                        ProfessorSerializer, FacultySerializer, DepartmentSerializer, InvestigationGroupSerializer,
                        KnowledgeAreaSerializer, InvestigationLineSerializer, WorksInvestGroupSerializer, 
                        ManageInvestLineSerializer, ManageInvestGroupSerializer, AcademicTrainingSerializer,
                        IsMemberSerializer)

from .models import (Country, State, City, Institution, Professor, Faculty, Department, AcademicTraining,
                    InvestigationGroup, KnowledgeArea, InvestigationLine, WorksInvestGroup, ManageInvestGroup,
                    ManageInvestLine, IsMember)

# Create your api's here.
# --------------------------------------------------Arias

#region Create

class CreateCountryAPI(generics.GenericAPIView):
    serializer_class = CountrySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            test = Country.objects.filter(name=request.data["name"])
            if not(test):
                country = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateStateAPI(generics.GenericAPIView):
    serializer_class = StateSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = State.objects.filter(name=request.data['name'])
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
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            # test = Professor.objects.filter(name=request.data["name"])
            # if not(test):
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
#endregion
#region Consult

class ConsultCountryAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        return Response({"Countrys": CountrySerializer(queryset, many=True).data })

class ConsultCountry_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.filter(id=kwargs["id_country"])
        returned = CountrySerializer(queryset, many=True).data
        if returned:
            return Response({"Country": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Country.objects.get(id=request.data['id'])
        except Country.DoesNotExist:
            return Response(f"No existe el País en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = CountrySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ConsultState_CountryAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = State.objects.filter(country=kwargs["id_country"])
        returned = StateSerializer(queryset, many=True).data
        if returned:
            return Response({"States": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Departamentos con ese País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = State.objects.get(id=request.data['id'])
        except State.DoesNotExist:
            return Response(f"No existe ese Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        serializer = StateSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ConsultCity_StateAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = City.objects.filter(state=kwargs["id_dep"])
        returned = CitySerializer(queryset, many=True).data
        if returned:
            return Response({"Cities": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Ciudades con ese Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = City.objects.get(id=request.data['id'])
        except City.DoesNotExist:
            return Response(f"No existe esa Ciudad en la base de datos", status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        serializer = CitySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultInstitutionAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.all()
        return Response({"Institutions": InstitutionSerializer(queryset, many=True).data })

class ConsultInstitution_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.filter(id=kwargs["id"]) 
        returned = InstitutionSerializer(queryset, many=True).data
        if returned:
            return Response({"Institution": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Instituto en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Institution.objects.get(id=request.data['id'])
        except Institution.DoesNotExist:
            return Response(f"No existe Instituto en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = InstitutionSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ConsultFacultyAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.all()
        return Response({"Facultys": FacultySerializer(queryset, many=True).data })

class ConsultFaculty_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.filter(id=kwargs["id"])  
        returned = FacultySerializer(queryset, many=True).data
        if returned:
            return Response({"Faculty": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Facultad en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Faculty.objects.get(id=request.data['id'])
        except Faculty.DoesNotExist:
            return Response(f"No existe Facultad en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = FacultySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ConsultDepartmentAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.all()
        return Response({"Departments": DepartmentSerializer(queryset, many=True).data })

class ConsultDepartment_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.filter(id=kwargs["id"])  
        returned = DepartmentSerializer(queryset, many=True).data
        if returned:
            return Response({"Department": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Department.objects.get(id=request.data['id'])
        except Department.DoesNotExist:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CreateAcademicTrainingAPI(generics.GenericAPIView):
    serializer_class = AcademicTrainingSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():#Toca arreglar el filtro. Att_:JAVIER
            isElement = AcademicTraining.objects.filter(professor=request.data['professor'],degree=request.data['degree'])
            if not(isElement):
                academicTraining = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#endregion

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

# Trabaja entre GI y AC
class CreateWorksInvestGroupAPI(generics.GenericAPIView): # (Faltan pruebas)
    serializer_class = WorksInvestGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = WorksInvestGroup.objects.filter(
                inv_group=request.data['inv_group'], know_area=request.data['know_area']
            )
            if not(isElement):
                korksInvestGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Dirige entre profesor y GI
class CreateManageInvestGroupAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = ManageInvestGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = ManageInvestGroup.objects.filter(
                inv_group=request.data['inv_group'], professor=request.data['professor']
            )
            if not(isElement):
                directs = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Es miembro entre profesor y GI (falta)
class CreateIsMemberAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = IsMemberSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = IsMember.objects.filter(
                inv_group=request.data['inv_group'], professor=request.data['professor']
            )
            if not(isElement):
                is_member = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateManageInvestLineAPI(generics.GenericAPIView): # Falta validar que no hayan 2 registros iguales
    serializer_class = ManageInvestLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            drive = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#consultar

class ConsultInvestigationGroup_DepartmentAPI(APIView):#si funciona
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(department=kwargs['dep'])
        return Response({"Groups": InvestigationGroupSerializer(queryset, many=True).data })

class ConsultInvestigationGroup_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(id=kwargs['id'])
        
        returned = InvestigationGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Group": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = InvestigationGroup.objects.get(id=kwargs['id'])
        except InvestigationGroup.DoesNotExist:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = InvestigationGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultProfessorAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.all()
        return Response({"Professors": ProfessorSerializer(queryset, many=True).data })

class ConsultProfessor_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.filter(user=kwargs['id'])

        returned = ProfessorSerializer(queryset, many=True).data
        if returned:
            return Response({"Professor": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Professor.objects.get(user=kwargs['id'])
        except Professor.DoesNotExist:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = ProfessorSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

# class IsMemberAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         queryset = IsMember.objects.filter(inv_group=)


