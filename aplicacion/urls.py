from django.urls import path, include
from .views import *

urlpatterns = [
      path('', home, name = "home"),
      path('bodegones/', bodegones, name = "bodegones"),
      path('bodegueadores/', bodegueadores, name = "bodegueadores"),
      path('resenas/', resenas, name = "resenas"),
      
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
      
]