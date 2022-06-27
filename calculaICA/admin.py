from django.contrib import admin
from calculaICA.models import Contacto

# Register your models here.
# Aqui añadimos los modelos para que se puedan visualizar desde 
# el panel administrativo. 

admin.site.register(Contacto)
