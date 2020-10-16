from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
# --------------------------------------------------Arias

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
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=False, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.nombre

# -------------------------------------------Jeison
# Clase que contiene la informacion basica de los Grupos de Investigacion
class GrupoInvestigacion(models.Model):
    id= models.AutoField(primary_key=True)
    id_institucion = models.IntegerField()
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
    id_area_con = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Linea de investigación'
        verbose_name_plural = 'Lineas de investigación'

    def __str__(self):
        return self.nombre

class Trabaja(models.Model):
    id_grupo_inv = models.IntegerField()
    id_area_con = models.IntegerField()
    estado_estudio = models.BooleanField()
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = 'Trabaja'
        verbose_name_plural = 'Trabaja'

class Maneja(models.Model):
    id_linea_inv = models.IntegerField()
    id_profesor = models.IntegerField()
    estado_analisis = models.BooleanField()
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = 'Maneja'
        verbose_name_plural = 'Maneja'

class Dirige(models.Model):
    id_grupo_inv = models.IntegerField()
    id_profesor = models.IntegerField()
    estado_direccion = models.BooleanField()
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = 'Dirige'
        verbose_name_plural = 'Dirige'

#Create your models here.
# class User(AbstractUser):
#     personal_id = models.CharField(max_length=14, unique=True)
#     cellphone = models.CharField(max_length=16)

#     def __str__(self):
#         return "{}".format(self.personal_id)

#     class Meta:
#         verbose_name = "Usuario"
#         verbose_name_plural = "Usuarios"