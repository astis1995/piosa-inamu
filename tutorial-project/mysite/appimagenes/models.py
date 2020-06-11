from django.db import models
from django.db.models import Model
from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll
from datetime import date


class ImagenesModel(CMSPlugin):
    nombre = models.CharField(max_length=140)
    cedula = models.CharField(max_length=10)
    foto_de_perfil = models.BooleanField(default=False)
    foto_de_producto =models.BooleanField(default=False)
    imagen = models.ImageField()
    fecha = date.today().strftime("%d/%m/%Y")

    def __str__(self):

        return self.nombre + "_"+ self.fecha


class persona(CMSPlugin):
    nombre = models.CharField(max_length=140)
    cedula = models.CharField(max_length=10)
    resenia = models.CharField(max_length=1400)
    formal = models.BooleanField(default=False)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=140)
    PROVINCIAS = (
        ('sanjose', 'San Jose'),
        ('alajuela', 'Alajuela'),
        ('heredia', 'Heredia'),
        ('cartago', 'Cartago'),
        ('limon', 'Limón'),
        ('puntarenas', 'Puntarenas'),
        ('guanacaste', 'Guanacaste'),
    )
    provincia = models.CharField(max_length=10, choices=PROVINCIAS);
    canton = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    direccion = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre
# Create your models here.
