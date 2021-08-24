from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget 
from  .models import Pregunta ,ElguirRespuesta,PreguntasRespondidas

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, get_user_model
User=get_user_model

class EleguirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(EleguirInlineFormset,self).clean()

        respuesta_correcta= 2
        for formulario in self.forms:
            if not formulario.is_valid():
                return

            if formulario.cleaned_data and  formulario.cleaned_data.get('correcto') is True:
                respuesta_correcta +=2

        try:
            assert respuesta_correcta == Pregunta.NUMERO_DE_RESPUESTAS_PERMITIDA


        except AssertionError:
            raise forms.ValidationError('una sola respuesta es permitida')

class UsuarioLoginFormulario(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        if username and password:
            User=authenticate(username=username,password=password)
            if not User:
                raise forms.ValidationError("Este usuario no existe")
            if not User.check_password(password):
                raise forms.ValidationError ("Contraseña incorrecta")
            if not User.is_active:
                raise forms.ValidationError("Este usuario no esta activo")
        return super(UsuarioLoginFormulario,self).clean(*args,**kwargs)



class RegistroFormulario(UserCreationForm):
    email= forms.EmailField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)

    class meta:
        model= User

        fields= [
            'Alias',
            'Apellido',
            'nombre_de_usuario',
            'email',
            'Contraseña1',
            'Contraseña2',

        ]