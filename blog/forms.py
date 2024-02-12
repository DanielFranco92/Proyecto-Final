from django.forms import ModelForm
from .models import motos
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class MotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MotoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  

    class Meta:
        model = motos
        fields = ['titulo', 'marca', 'modelo', 'cilindrada', 'kilometro', 'color', 'precio', 'telefono', 'email', 'descripcion', 'imagen']
        
class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  

    class Meta:
        model = User
        fields = ['name', 'apellido', 'username', 'email', "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label        

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', "password1", "password2"]
        help_texts = {k:"" for k in fields}

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})        