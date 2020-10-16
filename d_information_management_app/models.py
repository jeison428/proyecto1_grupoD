from django.db import models

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