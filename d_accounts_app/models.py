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

# Create your models here.
class User(AbstractUser):
    ID_CHOICES = (
        (1, _("CEDULA")),
        (2, _("CEDULA_EXTRANJERIA")),
        (3, _("TARJETA_IDENTIDAD")),
    )

    type_id = models.IntegerField(choices=ID_CHOICES, default=1)
    personal_id = models.CharField(max_length=24)
    personal_code = models.CharField(max_length=24)
    photo = models.FileField()
    telephone = models.CharField(max_length=24)
    address = models.CharField(max_length=64)

    is_proffessor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)