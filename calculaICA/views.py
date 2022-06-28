import math
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from calculaICA import models

# Create your views here.

def paginaPrincipal(request):
    #usuarios = models.nom.alls
    return  render(request, 'index.html' ,)


def paginaContacto(request):
    return render(request, 'contacto.html')

#####################################################################

def crearContacto(request):

    # Se obtienen los datos desde el formulario
    correo = request.POST['correoElectronico']
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    tel = request.POST['telefono']
    comment = request.POST['message']

    if request.method == 'POST':
        # Se crea el objeto y se guarda en la base de datos.
        newContacto = models.Contacto.objects.create(email=correo, nombres = nombres, apellidos = apellidos, telefono = tel, comentario = comment)
        newContacto.save()

    return JsonResponse({'email':correo, 'nombre':nombres, 'apellidos': apellidos, 'telefono': tel, 'comentario': comment})


def calcularIcomi(request):

    conduct = float(request.POST['conductividad'])
    dureza = float(request.POST['dureza'])
    alcal = float(request.POST['alcalinidad'])


    # CONDUCTIVIDAD
    if conduct > 270:
        conduct = 1
        indice_conductividad = 1
    else:
        logaritmo_conductividad = -3.26 + 1.34 * math.log10(conduct)
        indice_conductividad = math.pow(10, logaritmo_conductividad)

    # DUREZA

    if dureza > 110:
        dureza = 1
        indice_dureza = 1
    elif dureza < 30:
        dureza = 0
        indice_dureza = 0
    else:
        logaritmo_dureza = -9.09 + 4.4 * math.log10(dureza)
        indice_dureza = math.pow(10, logaritmo_dureza)
    

    # ALCALINIDAD

    if alcal > 250:
        alcal = 1
        indice_alcalin = 1
    elif alcal < 50:
        alcal = 0
        indice_alcalin = 0
    else:
        indice_alcalin = -0.25 + 0.005 * alcal
    
    resultado = (1/3) * (indice_conductividad + indice_dureza + indice_alcalin)

    return JsonResponse({'result': resultado, 'conduct': indice_conductividad, 'dureza': indice_dureza, 'alcalinidad': indice_alcalin})


def calcularIcosus(request):

    solid_total = request.POST['solidos_totales']

    resultado = -0.02 + 0.003 * float(solid_total) 

    return HttpResponse(resultado)
