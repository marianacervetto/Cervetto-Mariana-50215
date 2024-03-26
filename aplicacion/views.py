from django.shortcuts import render, redirect
from django. urls import reverse_lazy
from aplicacion.models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

#____________________Acerca de mi

def acerca(request):
    return render(request, "aplicacion/acerca.html")


#________________________BODEGON

@login_required
def bodegones(request):
    contexto = {'bodegones': Bodegon.objects.all().order_by("id")}
    return render(request, "aplicacion/bodegones.html", contexto)

@login_required
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

@login_required
def bodegonUpdate(request, id_bodegon):
    bodegon = Bodegon.objects.get(id=id_bodegon)
    if request.method == "POST":
        miForm = BodegonForm(request.POST)
        if miForm.is_valid():
            bodegon.nombre = miForm.cleaned_data.get("nombre")
            bodegon.direccion = miForm.cleaned_data.get("direccion")
            bodegon.zona = miForm.cleaned_data.get("zona")
            bodegon.telefono = miForm.cleaned_data.get("telefono")
            bodegon.save()
            
            contexto = {'bodegones': Bodegon.objects.all().order_by("id")}
            return render(request, "aplicacion/bodegones.html", contexto) 
      
    else:
        miForm = BodegonForm(initial={'nombre':bodegon.nombre, 'direccion': bodegon.direccion, 'zona':bodegon.zona, 'telefono':bodegon.telefono}) 
        
    return render(request, "aplicacion/bodegonForm.html", {"form":miForm})

@login_required
def bodegonDelete(request, id_bodegon):
    bodegon = Bodegon.objects.get(id=id_bodegon)
    bodegon.delete()
    return redirect(reverse_lazy('bodegones'))
    

#_____________________BODEGUEADOR

@login_required
def bodegueadores(request):
    contexto = {'bodegueadores': Bodegueador.objects.all().order_by("id")}
    return render(request, "aplicacion/bodegueadores.html", contexto)

@login_required
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

@login_required
def bodegueadorDelete(request, id_bodegueador):
    bodegueador = Bodegueador.objects.get(id=id_bodegueador)
    bodegueador.delete()
    return redirect(reverse_lazy('bodegueadores'))

@login_required
def bodegueadorUpdate(request, id_bodegueador):
    bodegueador = Bodegueador.objects.get(id=id_bodegueador)
    if request.method == "POST":
        miForm = BodegueadorForm(request.POST)
        if miForm.is_valid():
            bodegueador.nombre = miForm.cleaned_data.get("nombre")
            bodegueador.apellido = miForm.cleaned_data.get("apellido")
            bodegueador.cantidad_resenas= miForm.cleaned_data.get("cantidad_resenas")
            bodegueador.save()
            
            contexto = {'bodegueadores': Bodegueador.objects.all().order_by("id")}
            return render(request, "aplicacion/bodegueadores.html", contexto) 
      
    else:
        miForm = BodegueadorForm(initial={'nombre':bodegueador.nombre,'apellido': bodegueador.apellido, 'cantidad_resenas':bodegueador.cantidad_resenas }) 
        return render(request, "aplicacion/bodegueadorForm.html", {"form":miForm} )
    
    


#______________________RESENA 

@login_required
def resenas(request):
    contexto = {'resenas': Resena.objects.all().order_by("id")}
    return render(request, "aplicacion/resenas.html", contexto)

@login_required
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

@login_required
def resenaUpdate(request, id_resena):
    resena = Resena.objects.get(id=id_resena)
    if request.method == "POST":
        miForm = ResenaForm(request.POST)
        if miForm.is_valid():
            resena.autor = miForm.cleaned_data.get("autor")
            resena.bodegon = miForm.cleaned_data.get("bodegon")
            resena.fecha = miForm.cleaned_data.get("fecha")
            resena.contenido = miForm.cleaned_data.get("contenido")
            resena.save()
            
            contexto = {'resenas': Resena.objects.all().order_by("id")}
            return render(request, "aplicacion/resenas.html", contexto) 
      
    else:
        miForm = ResenaForm(initial={'autor':resena.autor,'bodegon': resena.bodegon, 'fecha':resena.fecha, 'contenido':resena.contenido }) 
        return render(request, "aplicacion/resenaForm.html", {"form":miForm}    )

@login_required
def resenaDelete(request, id_resena):
    resena = Resena.objects.get(id=id_resena)
    resena.delete()
    return redirect(reverse_lazy('resenas'))

#___________Buscar

@login_required
def buscarBodegon(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrarBodegones(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        bodegones = Bodegon.objects.filter(nombre__icontains=patron)
        contexto = {"bodegones":bodegones}
        return render(request, "aplicacion/bodegones.html", contexto)
    
    contexto = {'bodegones': Bodegon.objects.all()}
    return render(request, "aplicacion/bodegones.html", contexto)   
        
@login_required  
def buscarResenas(request):
    return render(request, "aplicacion/buscar_resenas.html")

@login_required
def encontrarResenas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        resenas = Resena.objects.filter(bodegon__icontains=patron)
        contexto = {"resenas":resenas}
        return render(request, "aplicacion/resenas.html", contexto)
    
    contexto = {'resenas': Resena.objects.all()}
    return render(request, "aplicacion/resenas.html", contexto)   

@login_required
def buscarBodegueadores(request):
    return render(request, "aplicacion/buscar_bodegueadores.html")

@login_required
def encontrarBodegueadores(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        bodegueadores = Bodegueador.objects.filter(nombre__icontains=patron)
        contexto = {"bodegueadores":bodegueadores}
        return render(request, "aplicacion/bodegueadores.html", contexto)
    
    contexto = {'bodegueadores': Bodegueador.objects.all()}
    return render(request, "aplicacion/bodegueadores.html", contexto)   


#___________________Login, Logout, Registration y Authentication
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #___________________________________________

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
   
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))   
       
    else:
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )    


#______________________Edición de perfil, Cambio de clave y avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
           
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy('home'))
    else:
    
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )      