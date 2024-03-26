from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class BodegonForm (forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    direccion = forms.CharField(max_length=80, required=True)
    zona = forms.CharField(max_length=40, required=True)
    telefono = forms.CharField(max_length=40, required=True)
    
class BodegueadorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    cantidad_resenas = forms.IntegerField()
    
class ResenaForm(forms.Form):
    autor = forms.CharField(max_length=40)
    bodegon = forms.CharField(max_length=40)
    fecha = forms.DateField()
    contenido = forms.CharField(max_length=1500)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)