from django.test import TestCase

# Create your tests here.

#Pruebas JAVIER -> https://www.youtube.com/watch?v=1FqxfnlQPi8

import json
from .models import Pais
from .urls import *
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from .serializers import *

class CrearPaisTestCase(APITestCase):
    def test_crearPais(self):
        data = {"nombre":"Venezuela"}
        response = self.client.post('/api/1.0/crear_pais/',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

