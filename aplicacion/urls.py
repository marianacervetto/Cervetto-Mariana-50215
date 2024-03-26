from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
      path('', home, name = "home"),
      path('bodegones/', bodegones, name = "bodegones"),
      path('bodegueadores/', bodegueadores, name = "bodegueadores"),
      path('resenas/', resenas, name = "resenas"),
      path('acerca/', acerca, name = "acerca"),
      
      #_______________Formularios
      path('bodegon_form/', bodegonForm, name = "bodegon_form"),
      path('bodegueador_form/', bodegueadorForm, name = "bodegueador_form"),
      path('resena_form/', resenaForm, name = "resena_form"),
      
      #______________Busqueda
      path('buscar_bodegones/', buscarBodegon, name="buscar_bodegones"),
      path('encontrar_bodegones/', encontrarBodegones, name = "encontrar_bodegones"),
      path('buscar_resenas/', buscarResenas, name="buscar_resenas"),
      path('encontrar_resenas/', encontrarResenas, name = "encontrar_resenas"),
      path('buscar_bodegueadores/', buscarBodegueadores, name="buscar_bodegueadores"),
      path('encontrar_bodegueadores/', encontrarBodegueadores, name = "encontrar_bodegueadores"),
 
 
      #____________Update
      path('bodegon_update/<id_bodegon>/', bodegonUpdate, name="bodegon_update"),
      path('resena_update/<id_resena>/', resenaUpdate, name="resena_update"),
      path('bodegueador_update/<id_bodegueador>/', bodegueadorUpdate, name="bodegueador_update"),
      
      
      #___________Delete
      path('bodegon_delete/<id_bodegon>/', bodegonDelete, name="bodegon_delete"),
      path('bodegueador_delete/<id_bodegueador>/', bodegueadorDelete, name="bodegueador_delete"),
      path('resena_delete/<id_resena>/', resenaDelete, name="resena_delete"),
      
      #___________Login, Logout, Registration
      path('login/', login_request, name="login"),
      path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
      path('registrar/', register, name="registrar"),
      
      #___________Edición de perfil, Cambio de clave, Avatar
      path('perfil/', editProfile, name="perfil"),
      path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
      path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]


