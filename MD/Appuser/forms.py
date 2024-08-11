from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        #limpiamos de ésta forma. Busqueda sobre diccionario, aplasta la clase Meta
        help_text = {k: "" for k in fields}


class UserEditform(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=30, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

