from django.db import models

# Create your models here. 
# Aqui se crean todos los objetos y datos que se guardan en SQLite

class Contacto(models.Model):
    email = models.EmailField(primary_key = True, blank = False) # Llave primaria -> sera nuestro identificador en la base de datos.

    nombres = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 10)
    comentario = models.CharField(max_length = 500)
