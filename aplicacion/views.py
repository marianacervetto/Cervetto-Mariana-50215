from django.shortcuts import render
from aplicacion.models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def bodegones(request):
    contexto = {'bodegones': Bodegon.objects.all()}
    return render(request, "aplicacion/bodegones.html", contexto)

def bodegueadores(request):
    contexto = {'bodegueadores': Bodegueador.objects.all()}
    return render(request, "aplicacion/bodegueadores.html", contexto)

def resenas(request):
    contexto = {'resenas': Resena.objects.all()}
    return render(request, "aplicacion/resenas.html", contexto)

def bodegonForm(request):
    if request.method == "POST":
        miForm = BodegonForm(request.POST)
        if miForm.is_valid():
            bodegon_nombre = miForm.cleaned_data.get("nombre")
            bodegon_direccion = miForm.cleaned_data.get("direccion")
            bodegon_zona = miForm.cleaned_data.get("zona")
            bodegon_telefono = miForm.cleaned_data.get("telefono")
            bodegon = Bodegon(nombre=bodegon_nombre, direccion=bodegon_direccion, zona=bodegon_zona, telefono=bodegon_telefono)
            bodegon.save()
            contexto = {'bodegones': Bodegon.objects.all()}
            return render(request, "aplicacion/bodegones.html", contexto)          
    else:
        miForm = BodegonForm() 
        
    return render(request, "aplicacion/bodegonForm.html", {"form":miForm})

def bodegueadorForm(request):
    if request.method == "POST":
        miForm = BodegueadorForm(request.POST)
        if miForm.is_valid():
            bodegueador_nombre = miForm.cleaned_data.get("nombre")
            bodegueador_apellido = miForm.cleaned_data.get("apellido")
            bodegueador_cantidad_resenas = miForm.cleaned_data.get("cantidad_resenas")
            bodegueador = Bodegueador(nombre=bodegueador_nombre, apellido=bodegueador_apellido, cantidad_resenas=bodegueador_cantidad_resenas)
            bodegueador.save()
            contexto = {'bodegueadores': Bodegueador.objects.all()}
            return render(request, "aplicacion/bodegueadores.html", contexto)          
    else:
        miForm = BodegueadorForm() 
        
    return render(request, "aplicacion/bodegueadorForm.html", {"form":miForm})

def resenaForm(request):
    if request.method == "POST":
        miForm = ResenaForm(request.POST)
        if miForm.is_valid():
            resena_autor = miForm.cleaned_data.get("autor")
            resena_bodegon = miForm.cleaned_data.get("bodegon")
            resena_fecha = miForm.cleaned_data.get("fecha")
            resena_contenido = miForm.cleaned_data.get("contenido")
            resena = Resena(autor=resena_autor, bodegon=resena_bodegon, fecha=resena_fecha, contenido=resena_contenido)
            resena.save()
            contexto = {'resenas': Resena.objects.all()}
            return render(request, "aplicacion/resenas.html", contexto)          
    else:
        miForm = ResenaForm() 
        
    return render(request, "aplicacion/resenaForm.html", {"form":miForm})

#___________Buscar

def buscarBodegon(request):
    return render(request, "aplicacion/buscar.html")

def encontrarBodegones(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        bodegones = Bodegon.objects.filter(nombre__icontains=patron)
        contexto = {"bodegones":bodegones}
        return render(request, "aplicacion/bodegones.html", contexto)
    
    contexto = {'bodegones': Bodegon.objects.all()}
    return render(request, "aplicacion/bodegones.html", contexto)   
        
  
def buscarResenas(request):
    return render(request, "aplicacion/buscar_resenas.html")

def encontrarResenas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        resenas = Resena.objects.filter(bodegon__icontains=patron)
        contexto = {"resenas":resenas}
        return render(request, "aplicacion/resenas.html", contexto)
    
    contexto = {'resenas': Resena.objects.all()}
    return render(request, "aplicacion/resenas.html", contexto)   

def buscarBodegueadores(request):
    return render(request, "aplicacion/buscar_bodegueadores.html")

def encontrarBodegueadores(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        bodegueadores = Bodegueador.objects.filter(nombre__icontains=patron)
        contexto = {"bodegueadores":bodegueadores}
        return render(request, "aplicacion/bodegueadores.html", contexto)
    
    contexto = {'bodegueadores': Bodegueador.objects.all()}
    return render(request, "aplicacion/bodegueadores.html", contexto)   