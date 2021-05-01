from django.http import HttpResponse
from django.template import Context,Template
import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='signin')
def home(request):
    return render(request, 'homeq.html')





def bienvenidaRojo(request):
    return HttpResponse("<p style='color:red;'>bienvenida</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria="Tercera edad"
        else:
            categoria="adultez"
    else:
        if edad <= 10:
            categoria="niñes"
        else:
            categoria="adolecente"
        
    resultado ='<h1>categoria edad  %s </h1>'%categoria
    return HttpResponse(resultado)

def horaActual(request):
    # respuesta="Momento actual {0}".format(datetime.datetime.now())
    respuesta="Momento actual {0}".format(datetime.datetime.now().strftime("%A %d/%m/%y %H:%M:%S"))

    return HttpResponse(respuesta)
def contenidoHTML(request, nombre,edad):
    contenido=""" 
        <html>
        <body>
        <p>
        Nombre : %s / edad: %s
        </p>
        </body>
        </html>
    """%(nombre, edad)
    return HttpResponse(contenido)
    
def miPrimeraPlantilla(request):
    plantillaExterna=open("C:/Users/57310/Desktop/md/TesPro/TesPro/template/miPrimeraPlantilla.html")
    template=Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto=Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
   
def PlantillaParametro(request):
    plantillaExterna=open("C:/Users/57310/Desktop/md/TesPro/TesPro/template/plantillaParametro.html")
    template=Template(plantillaExterna.read())
    plantillaExterna.close()
    nombre="luis"
    fecha=datetime.datetime.now().strftime("%A %d/%m/%y %H:%M:%S")
    contexto=Context({"nombreCanal":nombre,"fecha":fecha})
    documento = template.render(contexto)
    return HttpResponse(documento)
                