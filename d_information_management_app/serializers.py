from rest_framework import serializers
from .models import (Country, State, City, Institution, Professor, Faculty, Department, InvestigationGroup, 
                    KnowledgeArea, InvestigationLine, WorksDepartm, ManageInvestLine, ManageInvestGroup, 
                    WorksInvestGroup, AcademicTraining, IsMember)

# Create your serializers here.
# --------------------------------------------------Arias

#País
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

    def create(self, validate_data):
        instance = Country.objects.create(**validate_data)
        instance.save()
        return instance

#Estado o Departamento
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

    def create(self, validate_data):
        instance = State.objects.create(**validate_data)
        #instance.save()
        print("Serializer en state: ",instance)
        return instance

#Ciudad
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

    def create(self, validate_data):
        instance = City.objects.create(**validate_data)
        instance.save()
        return instance

#Institución
class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"

    def create(self, validate_data):
        instance = Institution.objects.create(**validate_data)
        instance.save()
        return instance

#Profesor
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

    def create(self, validate_data):
        instance = Professor.objects.create(**validate_data)
        instance.save()
        return instance

#Facultad
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

    def create(self, validate_data):
        instance = Faculty.objects.create(**validate_data)
        instance.save()
        return instance

#Departamento 
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validate_data):
        instance = Department.objects.create(**validate_data)
        instance.save()
        return instance
#Formación Academica
class AcademicTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicTraining
        fields = "__all__"

    def create(self, validate_data):
        instance = AcademicTraining.objects.create(**validate_data)
        instance.save()
        return instance

# Create your serializers here.
# --------------------------------------------------Jeison

#Grupo de investigacion
class InvestigationGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    foundation_date = serializers.DateField(required=False)
    category = serializers.CharField(required=False)
    class Meta:
        model = InvestigationGroup
        fields = "__all__"# ['campo1','campo2']
    
    def create(self, validate_data):
        instance = InvestigationGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Area del conocimiento
class KnowledgeAreaSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validate_data):
        instance = KnowledgeArea()
        instance.name = validate_data.get('name')
        instance.description = validate_data.get('description')
        instance.save()
        return instance

#Linea de investigacion
class InvestigationLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationLine
        fields = "__all__"

    def create(self, validate_data):
        instance = InvestigationLine.objects.create(**validate_data)
        instance.save()
        return instance

#Trabaja
class WorksInvestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksInvestGroup
        fields = '__all__'

    def create(self, validate_data):
        instance = WorksInvestGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Maneja
class ManageInvestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvestLine
        fields = '__all__'

    def create(self, validate_data):
        instance = ManageInvestLine.objects.create(**validate_data)
        instance.save()
        return instance

#Dirige
class ManageInvestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvestGroup
        fields = '__all__'

    def create(self, validate_data):
        instance = ManageInvestGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Es miembro
class IsMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsMember
        fields = '__all__'

    def create(self, validate_data):
        instance = IsMember.objects.create(**validate_data)
        instance.save()
        return instance

