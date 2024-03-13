from django import forms

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