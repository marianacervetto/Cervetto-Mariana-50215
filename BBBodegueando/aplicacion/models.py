from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bodegon(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80)
    zona = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = "Bodegon"
        verbose_name_plural = "Bodegones"
    
    def __str__ (self):
        return f"{self.nombre}"
    
class Bodegueador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cantidad_resenas = models.IntegerField()
    
    class Meta:
        verbose_name = "Bodegueador"
        verbose_name_plural = "Bodegueadores"
    
    def __str__ (self):
        return f"{self.apellido}, {self.nombre}"

class Resena(models.Model):
    autor = models.CharField(max_length=40)
    bodegon = models.CharField(max_length=40)
    fecha = models.DateField()
    contenido = models.CharField(max_length=1500)
    
    def __str__ (self):
        return f"{self.bodegon}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
  
    
