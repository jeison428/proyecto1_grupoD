from django.db import models
from django.contrib.auth.models import User        # TODO: Actualizar usuario a estudiante

# Create your models here.


class actividad(models.Model):
    idActividad=models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    idEstudiante = models.PositiveIntegerField() # models.ForeignKey(User, on_delete=models.CASCADE) #TODO: Actualizar usuario a estudiante
    descripcion = models.CharField(max_length=50)
    justificante = models.FileField(upload_to="b_activities_app/archivos", null=True, blank=True)
    estado = models.CharField(max_length=20)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()


class ponenciaCongreso(actividad):
    entidadOrganizadora=models.CharField(max_length=50)
    #Lugar=     #TODO: Relacionar con ciudad

    class Meta:
        verbose_name='ponencia en congreso'
        verbose_name_plural='ponencias en congresos'
    
    def __str__(self):
        return self.nombre

class publicacion(actividad):
    tipo=models.CharField(max_length=50)
    autores=models.CharField(max_length=50)
    datosGenerales=models.CharField(max_length=50)

    class Meta:
        verbose_name='Publicacion'
        verbose_name_plural='Publicaciones'
    
    def __str__(self):
        return self.nombre

class curso(actividad):
    programa=models.CharField(max_length=50)
    horasAsignadas=models.PositiveIntegerField()

    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
    
    def __str__(self):
        return self.nombre

class estanciaInvestigacion(actividad):
    proposito=models.CharField(max_length=50)
    institucion=models.CharField(max_length=50)
    responsable=models.CharField(max_length=50)
    #TODO: Relacionar con ciudad

    class Meta:
        verbose_name='Estancia  de  investigación'
        verbose_name_plural='Estancias  de  investigación'
    
    def __str__(self):
        return self.nombre

class exposicionResultados(actividad):
    modalidad=models.CharField(max_length=50)
    duracion=models.PositiveIntegerField()
    lugar=models.CharField(max_length=50)
    class Meta:
        verbose_name='Exposición de resultados'
        verbose_name_plural='Exposición de resultados'
    
    def __str__(self):
        return self.nombre

class parcipacionProyecto(actividad):
    nombreInvestigador=models.CharField(max_length=50)
    informacionVRI=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)

    class Meta:
        verbose_name='Participación  en  proyecto'
        verbose_name_plural='Participación  en  proyectos'
    
    def __str__(self):
        return self.nombre