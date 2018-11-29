from django.db import models
from .choises import genero

# Create your models here.

#class Marca(models.Model):
    #nombre = models.CharField(max_length=50)
    #descripcion = models.CharField(max_length=200)

    #def __str__(self):
        #return self.nombre

class Region(models.Model):
    descripcionRegion = models.CharField(max_length=90 , verbose_name='Nombre Region')

    def __str__(self):
        return self.descripcionRegion
    
    class Meta:
        verbose_name= "Region"
        verbose_name_plural= "Regiones"

class Raza(models.Model):
    descripcionRaza = models.CharField(max_length=20, verbose_name='Nombre raza')
    def __str__(self):
        return self.descripcionRaza

class Estado(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion

class TipoVivienda(models.Model):
    descripcionVivienda = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcionVivienda

class Usuario(models.Model):
    correo = models.EmailField(max_length=40)
    clave = models.CharField(max_length=25)
    rut = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=8)
    tipoVivienda = models.ForeignKey(TipoVivienda,on_delete=models.CASCADE)
    region= models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.correo

class Genero(models.Model):
    descripcion = models.CharField(max_length = 10)
    def str(self):
        return self.descripcion    

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=20)
    raza = models.CharField (max_length=20)
    genero= models.CharField (max_length=20)
    fecha_ingreso= models.DateField(null=True)
    fecha_nacimientoMascota= models.DateField(null=True)
    estado = models.CharField (max_length=20)
    def __str__(self):
        return self.nombreMascota

class User(models.Model):
	password = models.CharField (max_length = 128)
	last_login = models.DateField
	is_superuser = models.BooleanField
	username = models.CharField (max_length = 150)
	first_name = models.CharField (max_length = 30)
	email = models.CharField (max_length = 254)
	is_staff = models.BooleanField
	is_active = models.BooleanField
	date_joined = models.DateField
	last_name = models.CharField (max_length = 150)
	



    
    