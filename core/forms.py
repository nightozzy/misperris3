from django import forms
from .models import Mascota,Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class FormularioMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields= ["nombreMascota","raza","genero","fecha_ingreso","fecha_nacimientoMascota","imagen","estado"]

class formularioUser(UserCreationForm):

    def clean_email(self):
        correo = self.cleaned_data['correo']
        usuario = User.objects.filter(correo = correo)

        if  usuario:
            raise ValidationError("El correo ya existe")
        
        return correo

    class Meta:
        model= Usuario

        fields = (
            'correo',
            'clave',
            'rut',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'telefono',
            'tipoVivienda',
            'region'
        )

    

    




