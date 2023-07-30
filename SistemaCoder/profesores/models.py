from django.db import models
from django.utils import timezone


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    creacion = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.nombre
    
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=50)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    curso = models.ForeignKey( Curso, on_delete=models.DO_NOTHING )
    
    def __str__(self):
        return ( self.nombre +" " + self.apellido )
    
    