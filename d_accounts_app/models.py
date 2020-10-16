from django.db import models
from django.contrib.auth.models import Permission, AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# MODIFICACIÓN DEL MODELO DE USUARIO POR DEFECTO DE DJANGO, INCLUYE:
    # - username
    # - email
    # - first_name, last_name
    # - password
# POR DEFECTO, EL username ES USADO PARA EL LOGIN

#Create your models here.
class User(AbstractUser):
    personal_id = models.CharField(max_length=14, unique=True)
    cellphone = models.CharField(max_length=16)

    def __str__(self):
        return "{}".format(self.personal_id)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"