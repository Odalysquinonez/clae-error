from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def Bienvenido (request):
    #mensajes = {'msg1':'valor mensaje 1','msg2':'valor mensaje 2'}
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    #return render(request,)
    #return render(request, "bienvenido.html",{'msg1':'valor mensaje 1','msg2':'valor mensaje 2'})
    return render(request, "Bienvenido.html",{'no_personas':no_personas, 'personas': personas})











#def Contacto (request):
    #return HttpResponse("Mi nombre es Sergio y mi telefono  es 0980634085")
#def despedida (request):
    #return HttpResponse("Adios mundo desde Django")
