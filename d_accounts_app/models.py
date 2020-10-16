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
class User(AbstractUser):
    pass
