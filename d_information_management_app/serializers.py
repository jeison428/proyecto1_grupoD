from rest_framework import serializers
from .models import (Country, Department, City, Institution, Professor, Faculty, DepartmentU, AcademicTraining,
                    InvestigationGroup, KnowledgeArea, InvestigationLine, WorksDepartm, Drive, Directs, WorksInvestGroup)

# Create your serializers here.
# --------------------------------------------------Arias

class CountrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    def create(self, validate_data):
        instance = Country()
        instance.name = validate_data.get('name')
        instance.save()
        return instance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validate_data):
        instance = Department.objects.create(**validate_data)
        instance.save()
        return instance

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

    def create(self, validate_data):
        instance = City.objects.create(**validate_data)
        instance.save()
        return instance

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"

    def create(self, validate_data):
        instance = Institution.objects.create(**validate_data)
        instance.save()
        return instance

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

    def create(self, validate_data):
        instance = Professor.objects.create(**validate_data)
        instance.save()
        return instance

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

    def create(self, validate_data):
        instance = Faculty.objects.create(**validate_data)
        instance.save()
        return instance

class DepartmentUSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentU
        fields = "__all__"

    def create(self, validate_data):
        instance = DepartmentU.objects.create(**validate_data)
        instance.save()
        return instance

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


class InvestigationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationGroup
        fields = "__all__"# ['campo1','campo2']
    
    def create(self, validate_data):
        instance = InvestigationGroup.objects.create(**validate_data)
        instance.save()
        return instance

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

class InvestigationLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationLine
        fields = "__all__"

    def create(self, validate_data):
        instance = InvestigationLine.objects.create(**validate_data)
        instance.save()
        return instance

class WorksInvestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksInvestGroup
        fields = '__all__'

    def create(self, validate_data):
        instance = WorksInvestGroup.objects.create(**validate_data)
        instance.save()
        return instance

class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = '__all__'

    def create(self, validate_data):
        instance = Drive.objects.create(**validate_data)
        instance.save()
        return instance

class DirectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directs
        fields = '__all__'

    def create(self, validate_data):
        instance = Directs.objects.create(**validate_data)
        instance.save()
        return instance
