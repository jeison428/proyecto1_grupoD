from django.db import models
from django.contrib.auth.models import BaseUserManager

import datetime

# Create your models here.
# --------------------------------------------------Arias

class CiudadManager(BaseUserManager):
    def crearCiudad(self, validated_data):
        ciudad = Ciudad(**validated_data)
        ciudad.save()
        return ciudad

class InstitucionManager(BaseUserManager):
    def crearInstitucion(self, validated_data):
        institucion = Institucion(**validated_data)
        institucion.save()
        return institucion

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False, null=False)

    objects = CiudadManager()

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_ins = models.CharField(max_length=30, blank=False, null=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=False, null=False)

    objects = InstitucionManager()

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
    
    def __str__(self):
        return self.nombre_ins

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    es_interno = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return self.nombre

# Create your models here.
# -------------------------------------------Jeison

# modelos
class GrupoInvestigacion(models.Model):
    id= models.AutoField(primary_key=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_fundacion = models.DateField()

    class Meta:
        verbose_name = 'Grupo de investigación'
        verbose_name_plural = 'Grupos de investigación'

    def __str__(self):
        return self.nombre

class AreaConocimiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Area del conocimiento'
        verbose_name_plural = 'Areas del conocimiento'

    def __str__(self):
        return self.nombre

class LineaInvestigacion(models.Model):
    id = models.AutoField(primary_key=True)
    area_con = models.ForeignKey(AreaConocimiento, on_delete=models.CASCADE, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Linea de investigación'
        verbose_name_plural = 'Lineas de investigación'

    def __str__(self):
        return self.nombre

class Trabaja(models.Model):
    grupo_inv = models.ForeignKey(GrupoInvestigacion, on_delete=models.CASCADE, blank=False, null=False, default=1)
    area_con = models.ForeignKey(AreaConocimiento, on_delete=models.CASCADE, blank=False, null=False, default=1)
    estado_estudio = models.BooleanField()

    class Meta:
        verbose_name = 'Trabaja'
        verbose_name_plural = 'Trabaja'

class Maneja(models.Model):
    linea_inv = models.ForeignKey(LineaInvestigacion, on_delete=models.CASCADE, blank=False, null=False, default=1)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=False, null=False, default=1)
    estado_analisis = models.BooleanField()

    class Meta:
        verbose_name = 'Maneja'
        verbose_name_plural = 'Maneja'

class Dirige(models.Model):
    grupo_inv = models.ForeignKey(GrupoInvestigacion, on_delete=models.CASCADE, blank=False, null=False, default=1)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=False, null=False, default=1)
    estado_direccion = models.BooleanField()
    
    class Meta:
        verbose_name = 'Dirige'
        verbose_name_plural = 'Dirige'

